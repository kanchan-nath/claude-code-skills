---
name: linkedin-humanizer
alias: [Linkeidn_Humanizer, linkedin-humanizer]
description: Writes LinkedIn posts that read as human-written, not AI-written, on any topic the user gives, then runs a strict second "boss" reviewer pass (AI-vs-human verdict, hook check, LinkedIn mechanics) and rewrites until it passes. Use this whenever the user asks to write, draft, rewrite, polish, humanize, or check a LinkedIn post, caption, or build-in-public update, or says a post "sounds like AI", even if they never say "humanizer".
---

# LinkedIn Humanizer

Write a LinkedIn post on the user's topic in a believable human voice, then have a separate reviewer agent judge it like a strict editor. If the reviewer says it sounds AI-written or the hook is weak, rewrite and review again.

## Files in this skill

| File | Read it when |
|---|---|
| `references/vaibhav_posts_ai_vs_human.md` | Step 1, every run. 45 real posts already sorted into human-sounding (17) and AI-sounding (28), each with notes on why. This is the training reference. |
| `references/voice_analysis.md` | Step 1, every run. The patterns distilled from those posts, plus what to copy and what never to copy. |
| `references/reviewer_rubric.md` | Step 5, by the reviewer agent only. Scoring, hook checklist, fix menu. |
| `scripts/humanizer_lint.py` | Steps 4 and 5. Run `python scripts/humanizer_lint.py --help` first, then run it on the draft. |

The reference posts are by a different author on different topics. Use them to learn what human writing sounds like versus AI writing. Never reuse their topics, sentences, or signature lines.

## Author voice (edit this block to change who the posts sound like)

- Casual, direct, emotionally authentic.
- Normal capitalization and standard sentence case. Never all-lowercase.
- First person, talks to one reader like a friend, not an audience.
- Background the author may draw on only if relevant: BTech student and entry-level full-stack (MERN) developer, building in public from India.

## Step 0: Intake

Required: the topic. Optional: goal, audience, real facts or a real moment from the author's life, length, tone, whether a CTA is wanted.

- If the user gave only a topic, do not stop. Write from an angle that needs no invented experience (a reaction, an opinion, an observation).
- Ask one short question only when the post would be much better with a real detail the user clearly has (for example "what happened when you tried it?"). Never ask more than one.
- Never invent personal experiences, numbers, quotes, names, or results. Every "I did X" must come from the user. Facts about the world that you are unsure of must be stated as uncertain or left out.

## Step 1: Learn the two voices

Read `references/voice_analysis.md`, then skim the Part 1 (human) and Part 2 (AI) sections of `references/vaibhav_posts_ai_vs_human.md`. Before drafting, state to yourself in two lines: what makes the human bucket sound human, and what makes the AI bucket sound AI. The signals table at the top of the reference file is the short version.

## Step 2: Pick the post shape

| Input from the user | Shape | Length |
|---|---|---|
| A tool, news item, or thing they saw | A. Reaction: one thing, one reaction, one opinion | 20 to 70 words |
| A personal moment or experience | B. Story: concrete moment, a turn, a plain ending | 80 to 200 words |
| A take or lesson | C. Opinion: one concrete example, no moral summary | 60 to 150 words |
| Content that is truly list-shaped | D. Explainer: at most 4 "→" items, each with a specific detail, plus one human aside | 100 to 220 words |

When unsure, pick A. Shorter is safer. Do not pad to hit a length.

## Step 3: Write the draft

Hook (the first line decides everything):
- It must work alone, before "see more". Aim for 15 words or fewer and under 140 characters.
- It needs one concrete anchor: a name, number, place, moment, or a personal stake.
- Good hook types seen in the human posts: a plain reaction ("Guys, ..."), a concrete moment ("Saw X do Y. So I tried Z."), a confession with stakes, a blunt claim with a name or number, or a real-life detail.
- Never open with: "In today's...", "I'm excited to share...", "Have you ever wondered...", a generic question, or an "X isn't Y, it's Z" contrast.
- The body must pay off whatever the hook promises, within the first third.

Voice and rhythm:
- Write like a DM to a friend. Use contractions.
- Mix sentence lengths on purpose: some 2 to 5 word fragments, some medium, one longer run-on. Uniform sentence length is the biggest AI tell.
- Have an actual opinion, said plainly. A little attitude is good.
- At most one casual aside ("Btw", "honestly", "to be fair").
- 0 to 2 emoji, used as a reaction in the hook or the last line, never as decoration.
- Natural looseness is fine. Never fake typos.

Ending:
- End with a plain question the author really wants answered, a blunt line, a thank-you, or just stop.
- No moral, no summary of the post, no "The lesson is...", no "Thoughts?" as filler.

LinkedIn mechanics:
- Plain text only. No markdown, no bold, no headers.
- Short paragraphs, 1 to 2 lines, blank line between.
- No em dashes, no semicolons.
- No links in the body. If a link is needed, write "link in comments".
- 0 to 3 hashtags, only at the very end, usually none.

Never use these AI patterns (the lint script checks them): "Not X. It is Y." contrasts, tidy two-line chiasmus, "The catch is...", "Here is the catch nobody is talking about", "Think about that", "That is the real story", "The lesson is simple", rule-of-three lists used for rhythm, and anaphora fragment runs like "Calls him... Calls itself... Demands...".

## Step 4: Self-lint

Save the draft to a text file and run:

```
python scripts/humanizer_lint.py draft.txt
```

Fix every HARD flag. Read every SOFT flag and fix it unless there is a clear reason not to.

## Step 5: Boss review (separate agent)

Hand the draft to a second agent that did not write it. If Antigravity can start another agent, start one and give it only: the draft, the topic, the author facts the user supplied, `references/reviewer_rubric.md`, and the reference posts file. If a second agent is not available, run a clearly separated second pass: discard the drafting reasoning and review as a stranger who is paid to catch AI writing.

The reviewer must:
1. Do a blind read first and label the draft HUMAN, AI, or UNSURE with one sentence of reasoning, before using the checklist.
2. Run `scripts/humanizer_lint.py` on the draft.
3. Score it and check the hook, voice, mechanics, and truthfulness using the rubric.
4. Return PASS or FAIL. On FAIL, list line-level problems and the exact fix for each.

## Step 6: Rewrite loop

On FAIL, rewrite only what the reviewer flagged, re-lint, and send it back to the reviewer. Maximum 3 rounds. If it still fails after round 3, deliver the best version and state plainly what is still wrong.

## Step 7: Deliver

Output the final post as plain copy-ready text, then a short verdict block:

```
Reviewer verdict: PASS (round N of 3) | Human-ness: X/10 | Hook: PASS | Lint: clean
Reviewer changes: <1 to 3 short items, or "none">
```

Do not end with offers, next-step suggestions, or "want me to...". Do not show the drafting reasoning.

## Illustration (for calibration only, do not reuse)

AI-sounding: "Debugging isn't about finding the bug. It's about understanding the system. The lesson is simple: slow down before you speed up."

Human-sounding: "Spent 3 hours on a bug today. The fix was one missing await. One. I wanted to throw my laptop 😅 Anyone else lose an afternoon to something this small?"
