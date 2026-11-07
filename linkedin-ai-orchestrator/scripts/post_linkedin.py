#!/usr/bin/env python3
"""
LinkedIn CLI Publisher for Antigravity.
Allows Antigravity and the user to publish directly to LinkedIn or via webhook.
"""

import sys
import os
import json
import urllib.request
import urllib.error
from pathlib import Path

AUTH_CONFIG = Path.home() / ".gemini" / "config" / "linkedin_auth.json"

import ssl

def get_ssl_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def load_auth():
    if not AUTH_CONFIG.exists():
        return {}
    try:
        with open(AUTH_CONFIG, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading auth config: {e}", file=sys.stderr)
        return {}

def save_auth(data):
    AUTH_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    with open(AUTH_CONFIG, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved LinkedIn credentials to {AUTH_CONFIG}")

def get_person_urn(access_token):
    # Try OpenID userinfo endpoint
    req = urllib.request.Request(
        "https://api.linkedin.com/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    try:
        with urllib.request.urlopen(req, context=get_ssl_context()) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            sub = data.get("sub")
            if sub:
                return f"urn:li:person:{sub}"
    except Exception:
        pass

    # Try legacy /v2/me endpoint
    req = urllib.request.Request(
        "https://api.linkedin.com/v2/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    try:
        with urllib.request.urlopen(req, context=get_ssl_context()) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            person_id = data.get("id")
            if person_id:
                return f"urn:li:person:{person_id}"
    except Exception as e:
        print(f"Could not automatically detect person URN: {e}", file=sys.stderr)
    return None

def upload_image_asset(image_path, access_token, person_urn):
    reg_body = {
        "registerUploadRequest": {
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
            "owner": person_urn,
            "supportedUploadMechanism": ["SYNCHRONOUS_UPLOAD"]
        }
    }
    req = urllib.request.Request(
        "https://api.linkedin.com/v2/assets?action=registerUpload",
        data=json.dumps(reg_body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }
    )
    with urllib.request.urlopen(req, context=get_ssl_context()) as resp:
        reg_data = json.loads(resp.read().decode("utf-8"))
        asset_urn = reg_data["value"]["asset"]
        upload_url = reg_data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]

    with open(image_path, "rb") as f:
        img_bytes = f.read()

    up_req = urllib.request.Request(
        upload_url,
        data=img_bytes,
        headers={"Authorization": f"Bearer {access_token}", "Content-Type": "image/png"},
        method="PUT"
    )
    with urllib.request.urlopen(up_req, context=get_ssl_context()) as up_resp:
        pass

    return asset_urn

def publish_post(text, access_token=None, person_urn=None, webhook_url=None, media_path=None):
    # Mode 1: Webhook (Zapier/Make/Buffer)
    if webhook_url:
        req = urllib.request.Request(
            webhook_url,
            data=json.dumps({"text": text, "content": text}).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, context=get_ssl_context()) as resp:
                print("✅ Successfully dispatched post via Webhook!")
                return True
        except Exception as e:
            print(f"❌ Webhook dispatch failed: {e}", file=sys.stderr)
            return False

    # Mode 2: Direct LinkedIn API
    if not access_token:
        print("❌ Error: No LinkedIn Access Token provided.", file=sys.stderr)
        print("Run 'linkedin-post --setup' or set LINKEDIN_ACCESS_TOKEN in env / ~/.gemini/config/linkedin_auth.json", file=sys.stderr)
        return False

    if not person_urn:
        person_urn = get_person_urn(access_token)
        if not person_urn:
            print("❌ Error: Could not determine LinkedIn Person URN.", file=sys.stderr)
            return False

    share_content = {
        "shareCommentary": {
            "text": text
        },
        "shareMediaCategory": "NONE"
    }

    if media_path and os.path.exists(media_path):
        asset_urn = upload_image_asset(media_path, access_token, person_urn)
        share_content["shareMediaCategory"] = "IMAGE"
        share_content["media"] = [
            {
                "status": "READY",
                "description": {
                    "text": "Media Attachment"
                },
                "media": asset_urn,
                "title": {
                    "text": "Attachment"
                }
            }
        ]

    payload = {
        "author": person_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": share_content
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    req = urllib.request.Request(
        "https://api.linkedin.com/v2/ugcPosts",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }
    )

    try:
        with urllib.request.urlopen(req, context=get_ssl_context()) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            post_id = data.get("id")
            print(f"🎉 Successfully posted to LinkedIn! Post ID: {post_id}")
            return True
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"❌ LinkedIn API Error ({e.code}): {error_body}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"❌ Connection error: {e}", file=sys.stderr)
        return False

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Publish posts to LinkedIn from Antigravity")
    parser.add_argument("text", nargs="*", help="The post text to publish")
    parser.add_argument("--file", "-f", help="Read post text from a file")
    parser.add_argument("--media", "-m", help="Path to image or certificate file to attach")
    parser.add_argument("--setup", action="store_true", help="Configure LinkedIn credentials or webhook")
    parser.add_argument("--dry-run", action="store_true", help="Preview post without publishing")
    args = parser.parse_args()

    auth = load_auth()

    if args.setup:
        print("\n🔧 LinkedIn Connection Setup")
        print("Choose your preferred method:")
        print("  1. Direct LinkedIn Developer Access Token")
        print("  2. Automation Webhook (Make.com, Zapier, or Buffer)")
        choice = input("Select [1 or 2]: ").strip()
        if choice == "2":
            webhook = input("Enter Webhook URL: ").strip()
            auth["webhook_url"] = webhook
            save_auth(auth)
        else:
            token = input("Enter LinkedIn OAuth Access Token: ").strip()
            urn = input("Enter Person URN (optional, leave empty to auto-detect): ").strip()
            auth["access_token"] = token
            if urn:
                auth["person_urn"] = urn
            else:
                detected = get_person_urn(token)
                if detected:
                    print(f"Found URN: {detected}")
                    auth["person_urn"] = detected
            save_auth(auth)
        return

    post_text = ""
    if args.file:
        post_text = Path(args.file).read_text(encoding="utf-8")
    elif args.text:
        post_text = " ".join(args.text)
    else:
        # Check stdin
        if not sys.stdin.isatty():
            post_text = sys.stdin.read()

    if not post_text.strip():
        print("Usage: linkedin-post \"Your post text here...\" or linkedin-post -f post.md")
        print("Run 'linkedin-post --setup' to connect your account.")
        sys.exit(1)

    if args.dry_run:
        print("\n📄 [DRY RUN PREVIEW]")
        print("-" * 50)
        print(post_text)
        print("-" * 50)
        print(f"Character count: {len(post_text)} / 3000")
        return

    token = os.environ.get("LINKEDIN_ACCESS_TOKEN", auth.get("access_token"))
    urn = os.environ.get("LINKEDIN_PERSON_URN", auth.get("person_urn"))
    webhook = os.environ.get("LINKEDIN_WEBHOOK_URL", auth.get("webhook_url"))

    if not token and not webhook:
        print("\n⚠️ LinkedIn is not connected yet!")
        print("Run 'linkedin-post --setup' in terminal or provide credentials in ~/.gemini/config/linkedin_auth.json")
        print("\nPreview of what would be posted:")
        print("-" * 50)
        print(post_text)
        print("-" * 50)
        sys.exit(1)

    publish_post(post_text, access_token=token, person_urn=urn, webhook_url=webhook, media_path=args.media)

if __name__ == "__main__":
    main()
