---
name: shorts-script-writer
description: Turn a creator's raw, messy script, voice-note transcript, rough idea or bullet points into a polished, spoken-style script for YouTube Shorts, Instagram Reels or TikTok, under 60 seconds, in natural Indian English. Use this whenever the user pastes a raw script and says "modify", "rewrite", "polish", "make it flow", "make it better", "under 1 min", "for shorts/reels", or asks for a hook, storytelling flow, outcome, benefit, experience, CTA or a script from a topic, even if they never say the word "skill" or "script writing". Also use when the user says "do the same for this script" after an earlier Shorts rewrite in the conversation.
---

# Shorts Script Writer (Indian English, under 60 seconds)

This skill turns raw creator material into a short-form script that sounds like the creator talking, not like an ad or a textbook. The creator pastes something rough: broken grammar, jumbled order, a pasted link, half an idea. Your job is to keep their idea, their experience and their voice, and rebuild it so every line pulls the viewer to the next line.

Why this matters: on Shorts, viewers decide in about one to two seconds whether to stay. Retention is what the algorithm rewards. So every word must be doing a job, and the order of lines matters as much as the lines themselves.

## Workflow

Follow these steps in order. Do them silently; the user only wants the finished script unless they ask for the reasoning.

### Step 1: Read the raw script and extract the core

Pull out five things from the raw text. If one is missing, build it from what is there. Do not invent facts, numbers, tools or results the creator did not mention.

1. **The one idea.** What single thing should the viewer walk away with? If the raw script has several ideas, pick the strongest one and fold the others in as support. One well-landed point beats five rushed ones.
2. **The viewer.** Who is watching? (Students, beginners, job seekers, developers.) Write to that person with "you".
3. **The creator's experience.** What did the creator actually do, try, feel or find? This is the trust-builder. Keep it first-person and specific ("I opened ChatGPT and asked...").
4. **The outcome or benefit.** What does the viewer gain? (Saves time, never gets stuck, safer career, free options.) State it plainly, once, near the end.
5. **The CTA.** What should the viewer do next? (Comment, subscribe, try something, check the link.) Keep it to one ask, two at most.

### Step 2: Choose the structure

Use this default spine for ~45-60 seconds. Adapt the labels to the story; do not force all of them.

| Block | Time | Job |
|---|---|---|
| Hook | 0-3s | Stop the scroll. Curiosity, a bold claim, a relatable pain, or a surprising number |
| Problem or Question | 3-10s | Make the viewer feel "this is about me" |
| Experience | 10-25s | What the creator did or found. Proof that this is real |
| Action or Solution | 25-40s | What changed, what was built, what to do |
| Outcome or Takeaway | 40-52s | The benefit, in one clean line |
| CTA | 52-58s | One ask. End quickly, no long outro |

Pick the story shape that fits the raw material:

- **News to Action** (current event, then what the creator did about it). Hook with the news, pose the fear question, give the honest answer, show the creator's action, end with the lesson.
- **Pain to Fix** (a problem the viewer has, then the creator's fix). Hook with the list or the pain, name the frustrating moment, say "that used to happen to me", give the fix, give the resource, end with the CTA.
- **Myth to Truth** (a common belief, then the correction).
- **Tutorial in 3 steps** (never more than three steps in under a minute; cognitive load kills retention).

### Step 3: Write the lines with flow

This is the heart of the skill. Each line must hand the viewer to the next one. Use these linking techniques:

- **Open loop.** Raise a question or tension in the hook and pay it off at the end. ("Will AI replace jobs more, or less?" ... answered in the takeaway.)
- **Bridge words.** Start lines with connectors that carry momentum: "So", "But", "That's when", "Now", "Then", "Because", "And here's the thing".
- **Problem to Experience to Action to Result.** Each block's last line should set up the next block's first line.
- **One idea per line.** Short sentences. Break at breath points.
- **Pattern interrupt.** If the script runs past ~30 seconds, change something: a short punchy line, a question, or a shift in tone.

### Step 4: Apply the Indian English voice

Read `references/indian-english-voice.md` before finalizing. Short version: write the way a confident Indian creator speaks to a friend. Simple words, short sentences, natural fillers used sparingly ("honestly", "see", "basically", "right?"), Indian spelling and phrasing where natural, and no stiff, corporate or American-slang wording. Keep the creator's own words where they are already good.

### Step 5: Fit the time

Spoken pace for Shorts is about 2.3 to 2.5 words per second. Use these targets (spoken words only, not labels):

| Target | Word count |
|---|---|
| 30 seconds | 65-80 |
| 45 seconds | 100-115 |
| Under 60 seconds (default when user says "under 1 min") | 120-140 |

Aim to finish 2-3 seconds before 60 seconds, because the retention graph tends to drop sharply right at the end. If the draft is over, cut in this order: repeated ideas, filler lines, extra examples, then softer details. Never cut the hook, the experience or the outcome.

### Step 6: Run the quality checklist

Before sending, check every item:

- The first line works with no context and would make you stop scrolling.
- The hook does not start with "Hey guys", "Hello everyone", the channel name or a greeting.
- Every line links to the next. Read it aloud mentally: does it sound like one continuous thought?
- There is real experience in it (first person, specific action), not just advice.
- The outcome or benefit is stated plainly, once.
- Nothing is invented. Every fact, number, tool name and link came from the creator.
- Word count fits the target.
- There is exactly one main CTA.
- No sentence is long enough to need two breaths.
- The tone is Indian English, natural, and sounds like the creator.

## Output format

Unless the user asks otherwise, reply with only the script, using bold block labels and plain spoken lines under each. No intro sentence, no explanation, and no closing offer of extra options or next steps. Match this layout:

```
**Hook**
[line(s)]

**Problem**
[line(s)]

**Experience**
[line(s)]

**Solution**
[line(s)]

**Takeaway**
[line(s)]
```

Rules for the output:

- Use normal capitalisation and standard punctuation, even if the creator wrote in lowercase.
- Put the spoken words only under each label. Put on-screen text, B-roll or camera notes in square brackets only if the user asked for visuals.
- Do not add word counts, timestamps or commentary unless asked.
- If the raw script contains a link, do not read the URL aloud. Replace it with "the link is in the description" (or "pinned in the comments") and keep the resource name.
- Stop after the script.

If the user asks for extras (titles, description, hashtags, caption, on-screen text, thumbnail text, B-roll plan, a Hindi or Hinglish version, a 30-second cut), deliver exactly what they asked for in the same reply, using `references/extras.md`.

## Fixing common problems in raw scripts

| Raw script problem | What to do |
|---|---|
| Spelling or grammar mistakes ("heared", "oyu", "buisness") | Fix silently |
| Several ideas jumbled together | Pick the strongest as the spine, drop or compress the rest |
| No hook, starts with explanation | Move the most surprising line to the front, or turn the first fact into a question |
| A pasted link or title in the middle | Turn it into a "link in description" resource line |
| Claims like "this will benefit you as well as me" | Convert into a concrete viewer benefit |
| Vague numbers ("some", "many") | Keep vague if the creator was vague; never fabricate a precise number |
| Creator's experience is thin | Keep what exists, phrase it as first-person action, do not invent details |
| Too long | Cut repetition first, then examples |
| CTA is weak ("subscribe me") | Pair it with a reason: a question to answer in comments, then subscribe for the next one |

## Honesty rules

- Do not add fake results, stats, earnings, user counts or timelines.
- Do not claim a tool does something the creator did not say.
- Do not make guarantees the creator cannot back ("you will never get stuck"). Soften to what is true ("you won't have to stop and wait").
- Keep claims about news, jobs or AI risk balanced. Say "nobody knows" when nobody knows.

## Reference files

- `references/hooks.md`: hook formulas with Indian-English examples. Read when the raw script has a weak opening or the user asks for hook options.
- `references/indian-english-voice.md`: vocabulary, rhythm, do and don't lists. Read before every final draft.
- `references/examples.md`: before and after examples, including two full worked rewrites. Read when unsure about tone, flow or length.
- `references/extras.md`: titles, descriptions, hashtags, on-screen text, 30-second cuts and Hinglish versions. Read only when the user asks for extras.
