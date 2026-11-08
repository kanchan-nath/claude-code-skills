---
name: linkedin-post-image
description: Designs and exports LinkedIn post images (single-image posts, quote cards, stat cards, and multi-slide carousels) as 1080x1350 or 1080x1080 PNGs, plus an optional PDF for document-style carousels. Use when the user asks for a LinkedIn post image, carousel, quote card, cheat sheet, or any visual to attach to a LinkedIn post.
---

# LinkedIn Post Image

Builds LinkedIn visuals as HTML/CSS slides, then screenshots them to PNG with Playwright. Adapted from the popular `create-html-carousel` skill (gooseworks-ai/goose-skills), rewritten for Google Antigravity: no Claude-specific question widgets, plain chat questions, and workspace-relative paths.

## Use this skill when
- The user wants an image, carousel, quote card, stat card, or cheat sheet for a LinkedIn post.
- The user shares reference designs and wants something in that style.

## Do not use this skill when
- The user only wants post copy (no visual).
- The user wants video, GIF, or a full slide presentation.

## Specs (LinkedIn)
- Default canvas: **1080x1350** (4:5 portrait, takes the most feed space on mobile). Alternative: **1080x1080** (1:1).
- PNG, under 10 MB each. Max 20 images for a multi-image post; 5-8 slides performs best.
- For a swipeable "document" carousel, also export one PDF (every page 1080x1350).
- Keep all text inside a 80px safe margin. Minimum body text 28px, headline 64px+.

## Instructions

### 1. Gather inputs (ask in one short message, skip anything already given)
1. Topic or the exact text for the image(s).
2. Format: single image or carousel (slide count).
3. Style: pick from `references/style-presets.md` (or "match my reference images").
4. Brand handle / name to show in the footer (optional).
5. Photo or logo files to use (optional). If none are supplied, use CSS shapes, gradients or icons. Never download or embed photos of real people from the web.

If the user pasted content, do not rewrite it. Only trim to fit density rules.

### 2. Plan
- One idea per slide. Slide 1 = hook, last slide = CTA (follow / repost / comment).
- Density limits: headline max 2-3 lines, body max 3 lines, max 4 list items per slide. Must be readable in 2-3 seconds on a phone.
- If the image contains a quote with a person's name, only use quotes the user supplied and tell the user to verify the attribution before posting.

### 3. Build HTML
- Create `output/<post-name>/slides/slide-01.html`, `slide-02.html`, ... Start from `assets/template.html`.
- Copy the chosen preset's CSS variables, fonts and layout rules from `references/style-presets.md`.
- Each file is a fixed-size page (`html, body { width:1080px; height:1350px; overflow:hidden }`). No scrolling, no responsive units, no animations.
- Load fonts from Google Fonts with `<link>`; always add a fallback stack.
- Use inline SVG or CSS for icons, shapes and charts. Use local files from the user for images, referenced by relative path.

### 4. Render
From the skill folder (first time only: `cd scripts && npm install && npx playwright install chromium`):

```
node scripts/render.js output/<post-name>            # PNGs at 1080x1350, 2x sharpness
node scripts/render.js output/<post-name> --size 1080x1080
node scripts/render.js output/<post-name> --pdf      # also builds carousel.pdf
```

PNGs are written to `output/<post-name>/exports/`.

### 5. Verify (required)
Open 2-3 of the exported PNGs (use the browser or image viewer tool) and check: no clipped or overflowing text, contrast is high, fonts loaded (not default serif), footer and slide counter are inside the margin. Fix the HTML and re-render until clean. Retry at most 3 times.

### 6. Deliver
Report the folder path, file list, and the upload order. Do not add extra suggestions.

## Rules
- Do not invent statistics, quotes or testimonials. Use only what the user provided.
- Do not use logos, photos or names of real people or brands unless the user supplied them.
- One accent color per design. Max two typefaces.
- Keep the same layout, margins and footer position on every slide of a carousel.

## Troubleshooting
- Default fonts in PNG: increase `--wait` (`--wait 1500`) or switch to a web-safe fallback.
- Blurry text: `render.js` already uses deviceScaleFactor 2; pass `--scale 1` only if file size exceeds 10 MB.
- Overflow: shorten copy or split the slide; never shrink body text below 28px.
