---
name: cold-email
description: Build a visually styled HTML cold-outreach email (feedback requests, intros, investor/recruiter outreach) with a small vector logo mark, an accent color, light icon use, and a clickable CTA button — not a plain-text paragraph email. Use this whenever the user asks to draft, write, or style a "cold email," "outreach email," "feedback request email," or asks to make an email "more visual," with "icons," "vector images," or "look nicer," especially for StudeQ outreach to founders/investors/recruiters. Produces both an HTML version (for Gmail draft creation) and a plain-text fallback.
---

# Cold Email (visual HTML style)

A reusable visual template for cold outreach emails — used on top of the voice/content rules already defined in Kanchan's Notion "Research Doc" (tone, length, banned words, templates per platform). This skill is about the **visual packaging** of the email once the words are decided, not the wording itself.

## When to use this

Trigger this skill when the user wants a cold/outreach email that should look like a small designed artifact rather than a plain paragraph email — e.g. "make the mailing style more visual," "add icons/vector images," "style this cold email," "make it look like a product email." If the user only wants the words (no mention of visuals/styling), just write plain text per the Research Doc templates and skip this skill.

## Design tokens (reuse across all cold emails for consistency)

- **Accent color:** `#4F46E5` (indigo) — used for the header band, CTA button, link color, and the "ask" card's left border. Keep the rest of the palette neutral: white card (`#FFFFFF`), soft page background (`#F3F4F8`), body text (`#1F2430`), muted footer text (`#8A8F9C`).
- **Typography:** system-safe stack only — `Helvetica, Arial, sans-serif`. Do not use custom web fonts; most email clients strip `@font-face`.
- **Layout:** table-based (not flexbox/grid — many email clients, including older Outlook, don't support them). Outer 100%-width table for the page background, inner fixed-width (560px) table for the actual card, `border-radius: 12px`, subtle `box-shadow`.
- **Icon style:** one small vector mark (SVG) in the header for brand identity, plus sparing single-emoji icons (🔎 🙋 🔗 📚 🙂) inline in copy for warmth. Never more than one emoji per sentence, and never in the subject line.

## Structure (in order)

1. **Header band** — solid accent-color background, the vector logo mark (left) + product name + one-line tagline (right), white/light text.
2. **Opening lines** — 2–3 short paragraphs, plain body text color, no styling beyond normal weight/line-height (1.6).
3. **The "ask" card** — the one thing you want from the recipient, pulled into its own light-tinted box with a left accent border and a 🙋 or similar icon, so it's not buried in prose. Only one ask card per email.
4. **CTA button** — a single centered, pill/rounded button in the accent color linking to the product/profile URL. Label it with what it does ("Try StudeQ"), not "Submit" or "Click here."
5. **Sign-off** — plain paragraph, name in bold.
6. **Footer** — light grey background, small muted text, product name + link only. No legal boilerplate needed for a personal cold email.

## Building the vector logo mark

Generate a small inline SVG (circle + 1–2 simple shapes relevant to the product/subject — e.g. an open book for a study app, a chat bubble for a comms tool). Keep it under ~10 path/shape elements — simple vector icon, not illustration.

Encode it as a URL-encoded data URI (not base64 — base64 bloats the HTML and some clients choke on very long attribute values) and use it directly as an `<img src="data:image/svg+xml,...">`. This renders in Gmail, Apple Mail, and most modern clients without any external request (so no "images are blocked" placeholder).

To generate the encoded string:
```python
import urllib.parse
svg = '<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96">...</svg>'
data_uri = "data:image/svg+xml," + urllib.parse.quote(svg)
```

## Email-client compatibility rules (non-negotiable)

- **Inline CSS only**, on every element that needs styling — no `<style>` blocks (Gmail web strips `<head>` styles unless scoped, and many clients ignore them entirely).
- **Table layout**, `role="presentation"`, explicit `width` attributes — not just CSS width.
- **No external images, fonts, or scripts.** Data-URI SVG is the one exception that reliably renders without a network request.
- **Always provide a plain-text `body`** alongside the `htmlBody` — pass both to `create_draft`/`update_draft` so clients that strip HTML (or show a text preview) still read cleanly.
- Keep total HTML modest (one card, under ~60 lines) — a cold email that looks like a landing page will read as over-produced and work against the "sounds like a real person" rule from the voice guide.

## HTML skeleton to adapt

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#F3F4F8;padding:32px 0;font-family:Helvetica,Arial,sans-serif;">
<tr><td align="center">
<table role="presentation" width="560" cellpadding="0" cellspacing="0" style="background-color:#FFFFFF;border-radius:12px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.08);">

<tr><td style="background-color:#4F46E5;padding:28px 36px;">
  <table role="presentation" cellpadding="0" cellspacing="0"><tr>
    <td style="padding-right:14px;"><img src="data:image/svg+xml,<ENCODED_SVG>" width="44" height="44" alt="<PRODUCT>" style="display:block;"/></td>
    <td><span style="color:#FFFFFF;font-size:20px;font-weight:600;">PRODUCT_NAME</span><br/><span style="color:#D9D7FB;font-size:12.5px;">One-line tagline</span></td>
  </tr></table>
</td></tr>

<tr><td style="padding:32px 36px 8px 36px;">
  <p style="margin:0 0 16px 0;font-size:15.5px;line-height:1.6;color:#1F2430;">Opening lines go here...</p>
</td></tr>

<tr><td style="padding:0 36px 24px 36px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#F6F5FF;border-left:3px solid #4F46E5;border-radius:6px;">
    <tr><td style="padding:16px 20px;">
      <p style="margin:0;font-size:14.5px;line-height:1.6;color:#2A2550;">🙋 <strong>The ask:</strong> ...</p>
    </td></tr>
  </table>
</td></tr>

<tr><td align="center" style="padding:0 36px 28px 36px;">
  <a href="<URL>" style="background-color:#4F46E5;color:#FFFFFF;text-decoration:none;font-size:14.5px;font-weight:600;padding:12px 28px;border-radius:8px;display:inline-block;">🔗 CTA label</a>
</td></tr>

<tr><td style="padding:0 36px 28px 36px;">
  <p style="margin:0;font-size:15.5px;line-height:1.6;color:#1F2430;">Sign-off...<br/>Thanks,<br/><strong>Name</strong></p>
</td></tr>

<tr><td style="background-color:#F9FAFB;padding:18px 36px;border-top:1px solid #EEF0F4;">
  <p style="margin:0;font-size:12px;color:#8A8F9C;">📚 PRODUCT_NAME — <a href="<URL>" style="color:#4F46E5;text-decoration:none;">link</a></p>
</td></tr>

</table>
</td></tr>
</table>
```

## Workflow

1. Get the words first (from the Research Doc cold-email template, or whatever the user supplies) — don't invent new copy here.
2. Swap in the recipient's name, company, and ask.
3. Generate/reuse the vector logo mark for the product being pitched.
4. Fill the HTML skeleton above, keep the plain-text version in sync.
5. Create or update the Gmail draft with both `body` and `htmlBody`.
6. Flag to the user if the visual styling risks undercutting the "sounds like a real person" voice rule — offer a toned-down variant (logo + button only, no tinted card/emoji) as an alternative.
