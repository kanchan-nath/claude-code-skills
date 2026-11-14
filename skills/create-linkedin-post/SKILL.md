---
name: create-linkedin-post
alias: [Create_Linkedin_Post, create-linkedin-post]
description: "End-to-end LinkedIn post creation: takes a raw topic, writes a humanized post that passes AI-detection review, generates an image/carousel prompt in parallel, waits for user-supplied image, then schedules the post with media via LinkedIn API. Combines the Humanizer writing skill, the Image Prompting skill, and the LinkedIn Orchestrator publishing skill into one unified workflow. Use when the user says 'create a LinkedIn post', 'write a post for LinkedIn', 'LinkedIn post about...', or any variant of writing + publishing a LinkedIn post."
---

# Create LinkedIn Post

One skill to go from raw topic to scheduled LinkedIn post with image.

## Workflow Overview

```
Topic from user
    │
    ▼
┌──────────────────────────────────┐
│  PHASE 1: HUMANIZED POST WRITING │  (Main Agent)
│  • Learn human vs AI voice       │
│  • Draft post                    │
│  • Self-lint                     │
│  • Boss review (subagent)        │
│  • Rewrite loop (max 3 rounds)   │
│  • Deliver PASS'd post to user   │
└──────────────────────────────────┘
    │ post is PASS'd
    │
    ├──────────────────────────────────────────┐
    ▼                                          ▼
┌──────────────────────────┐   ┌────────────────────────────────┐
│  PHASE 2a: IMAGE PROMPT  │   │  PHASE 2b: USER REVIEWS POST   │
│  (Parallel Subagent)     │   │  (Main Agent waits for edits)  │
│  • Read style-presets.md │   │                                │
│  • Generate image prompt │   │                                │
│  • Deliver prompt to user│   │                                │
└──────────────────────────┘   └────────────────────────────────┘
    │
    ▼
  User creates/attaches image
    │
    ▼
┌──────────────────────────────────┐
│  PHASE 3: SCHEDULE & PUBLISH     │  (Main Agent)
│  • Draft-first guardrail         │
│  • User confirms                 │
│  • linkedin-post with --media    │
│  • Output post URL               │
└──────────────────────────────────┘
```

## Files in this skill

| File | Used by | When |
|---|---|---|
| `references/voice_analysis.md` | Phase 1 writer | Every run, before drafting |
| `references/vaibhav_posts_ai_vs_human.md` | Phase 1 writer | Every run, learn human vs AI voice |
| `references/reviewer_rubric.md` | Phase 1 reviewer subagent | During boss review |
| `references/style-presets.md` | Phase 2a image subagent | When generating image prompt |
| `scripts/humanizer_lint.py` | Phase 1 writer + reviewer | Lint the draft |
| `scripts/render.js` | Phase 2a (if building HTML slides) | Render slides to PNG |
| `scripts/package.json` | Phase 2a | npm dependencies for render |
| `assets/template.html` | Phase 2a | Base HTML template for slides |

---

## PHASE 1: Write the Humanized Post

### Author voice (edit this block per user)

- Casual, direct, emotionally authentic.
- Normal capitalization and standard sentence case. Never all-lowercase.
- First person, talks to one reader like a friend, not an audience.
- Background the author may draw on only if relevant: BTech student and entry-level full-stack (MERN) developer, building in public from India.

### Step 0: Intake

Required: topic. Optional: goal, audience, real facts or moment, length, tone, CTA preference.

- If user gave only a topic, do not stop. Write from an angle needing no invented experience (reaction, opinion, observation).
- Ask one short question only when the post would be much better with a real detail the user clearly has.
- Never invent personal experiences, numbers, quotes, names, or results.

### Step 1: Learn the two voices

Read `references/voice_analysis.md`, then skim Part 1 (human) and Part 2 (AI) of `references/vaibhav_posts_ai_vs_human.md`. Before drafting, state to yourself in two lines: what makes the human bucket sound human, and what makes the AI bucket sound AI.

### Step 2: Pick the post shape

| Input | Shape | Length |
|---|---|---|
| A tool, news item, something they saw | A. Reaction: one thing, one reaction, one opinion | 20–70 words |
| A personal moment or experience | B. Story: concrete moment, a turn, a plain ending | 80–200 words |
| A take or lesson | C. Opinion: one concrete example, no moral summary | 60–150 words |
| Truly list-shaped content | D. Explainer: max 4 "→" items with specific detail, plus one human aside | 100–220 words |

When unsure, pick A. Shorter is safer. Do not pad.

### Step 3: Write the draft

**Hook** (first line):
- Must work alone before "see more". Aim for ≤15 words and <140 characters.
- Needs one concrete anchor: name, number, place, moment, or personal stake.
- Good hook types: plain reaction ("Guys, ..."), concrete moment, confession with stakes, blunt claim with name/number, real-life detail.
- Never open with: "In today's...", "I'm excited to share...", "Have you ever wondered...", generic question, or "X isn't Y, it's Z".
- Body must pay off the hook promise within the first third.

**Voice and rhythm:**
- Write like a DM to a friend. Use contractions.
- Mix sentence lengths: some 2–5 word fragments, some medium, one longer run-on. Uniform sentence length is the biggest AI tell.
- Have an actual opinion, said plainly. A little attitude is good.
- At most one casual aside ("Btw", "honestly", "to be fair").
- 0–2 emoji as reaction, never decoration.
- Natural looseness fine. Never fake typos.

**Ending:**
- Plain question the author really wants answered, a blunt line, a thank-you, or just stop.
- No moral, no summary, no "The lesson is...", no filler "Thoughts?".

**LinkedIn mechanics:**
- Plain text only. No markdown, bold, headers.
- Short paragraphs (1–2 lines), blank line between.
- No em dashes, no semicolons.
- No links in body. "link in comments" if needed.
- 0–3 hashtags at the very end, usually none.

**Never use these AI patterns** (lint checks them): "Not X. It is Y." contrasts, tidy chiasmus, "The catch is...", "Here is the catch nobody is talking about", "Think about that", "That is the real story", "The lesson is simple", rule-of-three lists for rhythm, anaphora fragment runs.

### Step 4: Self-lint

Save draft to text file and run:

```bash
python scripts/humanizer_lint.py draft.txt
```

Fix every HARD flag. Review every SOFT flag and fix unless clear reason not to.

### Step 5: Boss review (separate subagent)

Launch a reviewer subagent. Give it only: the draft, the topic, author facts the user supplied, `references/reviewer_rubric.md`, and the reference posts file.

The reviewer must:
1. Blind read → label HUMAN / AI / UNSURE with one sentence reasoning, before checklist.
2. Run `scripts/humanizer_lint.py` on the draft.
3. Score using rubric: hook, voice, mechanics, truthfulness.
4. Return PASS or FAIL. On FAIL, list line-level problems and exact fix for each.

### Step 6: Rewrite loop

On FAIL, rewrite only what reviewer flagged, re-lint, send back. Max 3 rounds. If still fails after round 3, deliver best version and state what's still wrong.

### Step 7: Deliver post

Output final post as plain copy-ready text plus verdict block:

```
Reviewer verdict: PASS (round N of 3) | Human-ness: X/10 | Hook: PASS | Lint: clean
Reviewer changes: <1–3 short items, or "none">
```

---

## PHASE 2a: Image Prompt Generation (Parallel Subagent)

**Trigger:** Launch this subagent immediately after Phase 1 produces a PASS'd post.

The image subagent receives: the final post text, topic, and author context.

### Image Subagent Instructions

1. **Read** `references/style-presets.md` to understand available visual styles.
2. **Analyze** the post to extract:
   - Core message / hook
   - Key phrase or stat worth visualizing
   - Emotional tone (bold, minimal, dark, playful, etc.)
3. **Select** the best style preset (1–7) for the post.
4. **Generate a detailed image prompt** containing:
   - Recommended format: single image or carousel (with slide count)
   - Chosen style preset name and why
   - Canvas size (default 1080×1350)
   - Exact text to appear on each slide
   - Color scheme, font suggestions, layout description
   - Any icons, shapes, or visual elements (CSS/SVG only, no stock photos of people)
   - Footer: author handle/name
5. **Deliver the prompt** to the user for image creation.

### Image Prompt Output Format

```
IMAGE PROMPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Format: [single image / carousel (N slides)]
Style Preset: [name from style-presets.md]
Canvas: 1080×1350

SLIDE 1 (Hook):
  Headline: "..."
  Subtext: "..."
  Visual: [description of shapes, gradients, icons]
  Colors: bg #xxx, text #xxx, accent #xxx

[SLIDE 2, 3... if carousel]

Footer: @handle
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

If the user wants to build the image themselves (e.g., in Canva, Figma, or an AI image tool), this prompt gives them everything needed.

If the user wants the agent to build HTML slides and render PNGs:
- Create slides at `output/<post-name>/slides/slide-01.html` etc., starting from `assets/template.html`
- Render with: `cd scripts && npm install && npx playwright install chromium` (first time), then `node scripts/render.js output/<post-name>`
- Verify 2–3 exported PNGs: no clipped text, high contrast, fonts loaded, footer inside margin. Fix and re-render up to 3 times.

---

## PHASE 2b: User Review (concurrent)

While the image subagent works, present the post to the user. Accept any edits. If edits change the post substantially, re-run lint.

---

## PHASE 3: Schedule & Publish

**Trigger:** User provides the image and confirms the post.

### Step 1: Draft-First Guardrail (Mandatory)

Present the complete package to the user:
- Final post text (plain, copy-ready)
- Image file path(s)
- Reviewer verdict
- Proposed schedule (if user requested a time; otherwise "post now")

**Never auto-publish. Wait for explicit "Yes, post it" or "Schedule it".**

### Step 2: Publish

```bash
# Preview (dry run)
linkedin-post --dry-run "Post text..."

# Publish with image
linkedin-post --file draft.txt --media /path/to/image.png

# Or schedule (if user gave a time)
linkedin-post --file draft.txt --media /path/to/image.png --schedule "2024-01-15T09:00:00"
```

### Step 3: Confirm

Output:
```
✅ Post published/scheduled
Post ID: <id>
URL: <url>
Media: <attached file>
```

---

## Guardrails

1. **Draft-First Policy**: Never publish without explicit user approval.
2. **Personal Profile**: Verify author URN targets `urn:li:person:<id>` (personal feed, not company page).
3. **Human Voice Standards**: Banned words: *delve, tapestry, crucial, multifaceted, leverage, testament, beacon, realm, vital*. No robotic hedging.
4. **No Fabrication**: Every "I did X" must come from user. No invented stats, quotes, names, or results.
5. **Media Rules**: No logos, photos or names of real people/brands unless user supplied them. One accent color per design. Max two typefaces.

---

## Quick Reference

| Command | Purpose |
|---|---|
| `python scripts/humanizer_lint.py draft.txt` | Lint post for AI patterns |
| `python scripts/humanizer_lint.py draft.txt --json` | JSON lint output |
| `node scripts/render.js output/<name>` | Render HTML slides to PNG |
| `node scripts/render.js output/<name> --pdf` | Also build carousel PDF |
| `node scripts/render.js output/<name> --size 1080x1080` | Square format |
| `linkedin-post --file draft.txt --media img.png` | Publish with image |
| `linkedin-post --dry-run "text"` | Preview without posting |

---

## Illustration (calibration only, never reuse)

AI-sounding: "Debugging isn't about finding the bug. It's about understanding the system. The lesson is simple: slow down before you speed up."

Human-sounding: "Spent 3 hours on a bug today. The fix was one missing await. One. I wanted to throw my laptop 😅 Anyone else lose an afternoon to something this small?"
