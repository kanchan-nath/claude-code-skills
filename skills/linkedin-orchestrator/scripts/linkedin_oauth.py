#!/usr/bin/env python3
"""
LinkedIn OAuth 2.0 Helper for Antigravity.
Exchanges Client ID & Client Secret for personal Access Token and URN.
"""

import sys
import os
import json
import urllib.parse
import urllib.request
import urllib.error
import http.server
import socketserver
import threading
import time
from pathlib import Path

AUTH_CONFIG = Path.home() / ".gemini" / "config" / "linkedin_auth.json"
REDIRECT_URI = "http://localhost:8080/callback"
PORT = 8080
SCOPES = ["openid", "profile", "w_member_social"]

captured_code = None
server_done = threading.Event()

class OAuthCallbackHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Quiet logs

    def do_GET(self):
        global captured_code
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/callback":
            params = urllib.parse.parse_qs(parsed.query)
            if "code" in params:
                captured_code = params["code"][0]
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                html = """
                <html>
                <body style="font-family: system-ui, sans-serif; display: flex; align-items: center; justify-content: center; height: 90vh; background: #f3f4f6;">
                    <div style="background: white; padding: 2rem 3rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center;">
                        <h2 style="color: #057642; margin-bottom: 0.5rem;">Antigravity Connected to LinkedIn!</h2>
                        <p style="color: #4b5563;">You can close this tab now and return to Antigravity.</p>
                    </div>
                </body>
                </html>
                """
                self.wfile.write(html.encode("utf-8"))
                server_done.set()
                return
            elif "error" in params:
                err = params.get("error_description", ["Unknown error"])[0]
                self.send_response(400)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(f"<h2>Authorization Failed: {err}</h2>".encode("utf-8"))
                server_done.set()
                return

        self.send_response(404)
        self.end_headers()

import ssl

def get_ssl_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def exchange_code(client_id, client_secret, code):
    url = "https://www.linkedin.com/oauth/v2/accessToken"
    data = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": client_id,
        "client_secret": client_secret
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    try:
        with urllib.request.urlopen(req, context=get_ssl_context()) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error exchanging code: {e.read().decode('utf-8')}", file=sys.stderr)
        return None

def fetch_user_info(access_token):
    req = urllib.request.Request(
        "https://api.linkedin.com/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    try:
        with urllib.request.urlopen(req, context=get_ssl_context()) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error fetching userinfo: {e}", file=sys.stderr)
        return None

def save_credentials(client_id, client_secret, token_data, user_info=None):
    AUTH_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    
    person_urn = None
    name = "User"
    if user_info:
        sub = user_info.get("sub")
        if sub:
            person_urn = f"urn:li:person:{sub}"
        name = user_info.get("name", "User")

    creds = {
        "client_id": client_id,
        "client_secret": client_secret,
        "access_token": token_data.get("access_token"),
        "refresh_token": token_data.get("refresh_token"),
        "expires_in": token_data.get("expires_in"),
        "person_urn": person_urn,
        "name": name,
        "updated_at": time.time()
    }

    with open(AUTH_CONFIG, "w", encoding="utf-8") as f:
        json.dump(creds, f, indent=2)

    return creds

def get_auth_url(client_id):
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "state": "antigravity_auth",
        "scope": " ".join(SCOPES)
    }
    return "https://www.linkedin.com/oauth/v2/authorization?" + urllib.parse.urlencode(params)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="LinkedIn OAuth setup")
    parser.add_argument("--client-id", default="YOUR_LINKEDIN_CLIENT_ID", help="LinkedIn App Client ID")
    parser.add_argument("--client-secret", default="YOUR_LINKEDIN_CLIENT_SECRET", help="LinkedIn App Client Secret")
    parser.add_argument("--code", help="Manually provide authorization code or full redirect URL")
    parser.add_argument("--url-only", action="store_true", help="Print authorization URL and exit")
    args = parser.parse_args()

    client_id = args.client_id
    client_secret = args.client_secret

    auth_url = get_auth_url(client_id)

    if args.url_only:
        print(auth_url)
        return

    if args.code:
        code = args.code
        if "code=" in code:
            code = urllib.parse.parse_qs(urllib.parse.urlparse(code).query).get("code", [code])[0]
        token_data = exchange_code(client_id, client_secret, code)
        if token_data:
            user_info = fetch_user_info(token_data["access_token"])
            creds = save_credentials(client_id, client_secret, token_data, user_info)
            print("SUCCESS")
            print(json.dumps(creds, indent=2))
        else:
            sys.exit(1)
        return

    # Start local server to catch callback
    print(f"\n🔗 Open this link in your browser to authorize:")
    print(f"{auth_url}\n")
    print(f"📡 Listening on {REDIRECT_URI} for the authorization response...")

    server = socketserver.TCPServer(("localhost", PORT), OAuthCallbackHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    # Wait up to 180 seconds for user authorization
    server_done.wait(timeout=180)
    server.shutdown()
    server.server_close()

    if captured_code:
        print("\n🔑 Received authorization code from LinkedIn! Exchanging for token...")
        token_data = exchange_code(client_id, client_secret, captured_code)
        if token_data:
            user_info = fetch_user_info(token_data["access_token"])
            creds = save_credentials(client_id, client_secret, token_data, user_info)
            name = creds.get("name", "User")
            urn = creds.get("person_urn", "Detected")
            print(f"🎉 Successfully authenticated as: {name} ({urn})")
            print(f"✅ Credentials securely stored at: {AUTH_CONFIG}")
        else:
            print("❌ Failed to exchange code for token.", file=sys.stderr)
            sys.exit(1)
    else:
        print("⏱️ Timed out waiting for browser authorization callback.")
        print("If you were redirected to a page that failed to load, you can copy the full URL from your browser's address bar and run:")
        print("  python3 ~/.gemini/claude-skills/scripts/linkedin_oauth.py --code \"<pasted URL or code>\"")

if __name__ == "__main__":
    main()
