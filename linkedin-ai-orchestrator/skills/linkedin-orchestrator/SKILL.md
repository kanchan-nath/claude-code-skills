---
name: linkedin-orchestrator
description: "End-to-end LinkedIn AI Orchestrator: converts raw ideas or transcripts into humanized, algorithm-optimized LinkedIn posts, audits against AI slop, previews for user review, and publishes directly to personal LinkedIn profiles with media attachments."
---

# LinkedIn AI Orchestrator Skill

Autonomous workflow for researching, drafting, humanizing, and publishing high-engagement LinkedIn posts directly to a personal profile.

---

## Operating Workflow

```mermaid
flowchart TD
    UserQuery["Raw User Input / Transcript / Idea"] --> PromptEng["1. Automatic Prompt Engineering<br>• Extract core outcome<br>• Inject practitioner voice<br>• Enforce 140-char mobile fold hook"]
    PromptEng --> Humanize["2. Content Humanizer Audit<br>• humanizer_scorer.py check<br>• Strip AI buzzwords (delve, tapestry, leverage)<br>• Ensure natural sentence rhythm"]
    Humanize --> Lint["3. Algorithm & Format Linter<br>• post_linter.py check<br>• 100/100 SHIP score standard<br>• 3 focused hashtags, no external body links"]
    Lint --> DraftGate["4. Draft-First Guardrail (Mandatory)<br>• Present full draft to user<br>• Await explicit confirmation"]
    DraftGate --> Publish["5. LinkedIn API Publishing<br>• linkedin-post --file draft.txt<br>• Attach certificate/media if provided<br>• Output live Post ID & URL"]
```

---

## Guardrails & Non-Negotiable Rules

1. **Draft-First Policy**:
   - **Never auto-publish without user approval.**
   - Always present the draft, the humanizer score, and the linter score to the user first.
   - Wait for explicit user confirmation ("Yes, post it") before calling the publishing tool.

2. **Personal Profile Targeting**:
   - Always verify the author URN targets `urn:li:person:<id>` to ensure posts go to the member's personal feed, never a corporate or showcase page.

3. **Human Voice Standards**:
   - Banned words: *delve, tapestry, crucial, multifaceted, leverage, testament, beacon, realm, vital*.
   - No robotic hedging (*"In today's fast-paced world...", "It is important to remember..."*).
   - Varied sentence lengths with concrete details and metrics.

4. **Media Handling**:
   - Single-page PDFs (like certificates) are rendered as crisp PNG assets (1989x1294px) and registered through LinkedIn's `feedshare-image` recipe for rich, full-card display on feeds.

---

## Tool Reference

### 1. Publishing & Media
```bash
# Preview post without sending
linkedin-post --dry-run "Post text..."

# Publish text post (after user approval)
linkedin-post "Post text..."

# Publish post with certificate / image attached
linkedin-post --file draft.txt --media /path/to/certificate.png
```

### 2. Quality & Humanizer Audits
```bash
# Score draft for AI patterns (0-100)
python3 scripts/humanizer_scorer.py draft.txt

# Lint draft for LinkedIn algorithm reach (0-100)
python3 scripts/post_linter.py --input draft.txt --output human
```

### 3. Account Connection
```bash
# Run one-time OAuth setup
linkedin-post --setup
# Or run the local OAuth listener
python3 scripts/linkedin_oauth.py
```
