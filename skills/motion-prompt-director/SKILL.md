---
name: motion-prompt-director
description: Turns any product, idea or brief into a complete, production-ready prompt pack for AI video and motion-graphics generators (Google Flow / Veo, Runway, Kling, Luma, Sora, Pika), plus key-frame image prompts, a music prompt and edit notes, using the Cinetic cinematic motion-design method (one product-specific idea, a story device, a reusable Style Bible, beat-timed shots, copy discipline, hard bans on generic AI looks). Use this whenever the user wants a prompt, shot list, storyboard, script or treatment for a launch video, product demo, feature animation or loop, logo sting or reveal, kinetic typography, teaser, trailer, intro or promo clip, or says things like "make a video about X", "write a Flow prompt", "animate this feature", "I need a launch clip", "storyboard this", "make this look premium, not AI", or pastes a video prompt to critique or rewrite. Also use it for 9:16 / 1:1 social versions, looping hero animations, and for turning a code-based motion brief into prompts for a generative tool.
license: MIT (derived from Leonxlnx/cinetic, see LICENSE-NOTICE.md)
---

# Motion Prompt Director

You are directing a short film on paper. The deliverable is a set of copy-paste prompts and plans, not code. Picture, copy and sound are one system on one beat grid, and nothing is finished until it has been critiqued against the checklist.

This skill adapts the Cinetic method (a code-driven film pipeline) to generative video tools. Everything about taste, concept, copy, timing, camera, transitions and sound carries over; anything that needs frame-exact rendering (exact text, logos, counters, perfect loops, beat-synced audio) is assigned to the editor and the user is told so.

## The bar

The target is a film people watch twice: one idea the product owns, told in pictures, where every frame looks chosen and nothing is there to fill space.
- **Substance before polish.** Show the specific, clever thing this product does that a simpler product would not. Flawless motion around a generic claim loses to a rough film that makes the viewer think "oh, that's smart".
- **Its own look.** Every brand gets a visual language derived from its name, product and personality, inside the hard bans. Restraint means no decoration; it does not mean one minimal house style for everything.
- **Visual, not narrated.** The idea reads with the sound off; words only confirm what the picture said.
- **Weight and stillness.** Motion has mass, arrives on the beat, then rests, so the fast moments land.
- **Smooth and clean.** Eased, weighted, no jitter, no pops, no effects standing in for ideas.
- **Restraint over decoration.** When in doubt, remove.

## The five laws

1. **One idea, specific to this product.** Say the film in one sentence; the proof shows what this product does that the obvious version would not.
2. **Visual, not narrated.** Must read muted. Fewer than 20-35 words in a 30 s film.
3. **Weight and stillness.** Every move eased, landing on a beat, then holding.
4. **Every word earns its place.** Short lines, viewer's words, no stock phrasing.
5. **Restraint.** Every element names its job (reveal, route, validate, emphasise) or is cut.

## Hard bans (when you invent the look)

Never in a prompt; always in the negative block:
- **Words:** eyebrow/kicker labels, stacked taglines, "Introducing...", text walls, filler text (decorative captions, fake metrics, lorem ipsum).
- **Type:** serif, italic/oblique (including skewed). One clean modern sans (+ a mono only if the product shows code/numbers).
- **Colour:** orange, amber, beige, cream, tan, sand; neon, glow, bloom, halo; purple, violet, indigo, any multi-hue gradient; glassmorphism.
- **Decoration:** emoji, stock icons, sparkles for "AI", particles, confetti, lens flares, code rain, bouncy overshoot (except a true landing, at most twice).

Allowed: ink and paper (light or dark, neutral or cool), ONE accent with a meaning from red / green / teal / blue / yellow, one sans, smooth weighted motion. If the user supplies a brand that includes a banned item (their serif wordmark, their orange), the brand wins: use it, note it as brand-supplied, and remove that item from the negatives.

## Which mode?

- **New prompt pack** (default): run the full workflow below.
- **Quick prompt** (one shot, one image, "just give me a prompt for X"): still apply the five laws, the bans, a mini Style Bible and the shot anatomy; skip the full treatment. Say what you assumed in one line.
- **Critique / rewrite** (user pastes a prompt or describes a generated clip): run `references/review-checklist.md`, diagnose with shot numbers and P0/P1/P2, then give the rewritten prompt, not general advice.
- **Social variants / loop**: re-lay out per aspect ratio (never crop); design loops as cycles (see `references/formats.md`).

## Workflow

### Step 0: Intake (ask only what is missing, in one short message)

Need: (1) product/subject and what it does in one line, (2) target tool (default Google Flow with Veo) and aspect ratio (default 16:9), (3) length (default 20-30 s), (4) brand: colours, fonts, logo, tone, (5) audience and where it plays (feed, landing page, keynote; must it read muted? loop?). If the brief is enough, skip questions and state assumptions in one line. Never ask more than one round of questions.

### Step 1: Pick the format

Read `references/formats.md`. Choose the nearest row (launch film, product video, feature loop, logo sting, UI walkthrough, teaser, vertical). It sets length, beats, word budget and deliverables.

### Step 2: Concept (before any prompt)

Read `references/concept-and-copy.md`.
1. Fill the inventory: name meaning, **non-obvious behaviour** ("Unlike the obvious version, it ..."), value sentence (before/after), the number, pain scene, product objects, category cliches (banned).
2. Generate ideas through three lenses (verb made literal, pain made visible, formal device) and pick one finalist per lens; run the tests (ownership, deletion, muted, feature word, poster, one sentence, retell, specificity, budget, truth).
3. Write the **idea (<= 8 words)**, **device** (one owned object that carries every shot and ends as the mark or resolved unit), **grammar** (the rule the film's form obeys) and a **logline (<= 15 words)**. When the user wants to choose, show three loglines (device + one frame each) with a recommendation in 12 lines or fewer.

### Step 3: Draw techniques, do not choose them

Choosing by hand converges on the same fade-up, push-in and end card in every film. If you can run code, run:

`python3 scripts/pick_techniques.py --format <launch|feature|loop|sting|walkthrough|vertical> --energy <calm|medium|high> --seconds <length>`

It prints about one technique per 2.5 s of film with what/use-when/avoid-when and a ban-safe variant where needed. Without code execution, grep `references/technique-catalog.md` by category and take unfamiliar entries rather than the first familiar one. Build the picks the concept can carry, retold in THIS product's objects; reroll a pick that fights the concept at most twice (`--exclude <id>`), or drop it with a written reason; never add a technique the draw did not give you. A short film carries a few moves done well; a film that crams in every move reads as a showreel.

### Step 4: Personality and the Style Bible

Read `references/look-and-personality.md`. Write three adjectives for the brand, then derive typeface character, weight/case, stage (light/dark, neutral/cool), accent hue and its one-word meaning, shapes and motion character. Take the palette from the world of the name and product, not framework defaults. Write the **Style Bible** (template in `references/prompt-templates.md` section 1): one reusable 40-80 word block that is pasted unchanged at the top of every shot prompt.

### Step 5: Beat sheet, copy and timing

Read `references/motion-camera-sound.md` and `references/concept-and-copy.md` section 9.
- Map the arc (hook > problem > turn > proof > promise > lockup, or the format's arc) onto seconds. Hook inside the problem, moving at frame 0, problem felt by 1 s and stated by 2 s; turn on a downbeat; proof as cause > action > result with the result held; the lockup arrives from the story and the final frame is the poster.
- Pick a tempo (default 120 BPM; 100-120 for product videos) and put section changes on downbeats, cuts on 8ths. Give each bar one motion peak.
- Write the copy: viewer's words, <= 5 words per line, <= 2 lines per shot, callback structure (plant early, pay off later), line test on every line, no stock phrasing. Count the words against the format budget.
- Plan seams: 6-8 transition types, each at most twice, one signature move from the mark used at open/middle/close; the device never blinks out.
- Plan sound by personality row: sparse intro, drop on the turn, loudest moment on the payoff, silence before it, lockup resolved rather than loud.

### Step 6: Shot prompts

Read `references/prompt-templates.md`. Split the beats into clips of about 4-8 s (or the tool's limit), one main action per clip. Each prompt: subject + action, setting, camera, motion timing with a named rest state, the Style Bible (pasted), exact on-screen words in quotes or "no text", negatives. For continuity generate key frames first and use them as start frames / ingredients. Show each prompt in its own code block so the user can copy it.

### Step 7: Key frames, music, edit notes

Write image prompts for the hook frame, the product frame and the end-card/poster frame; a music prompt from the sound table (tempo, key, palette, breakdown time, hit time, ending); and edit notes: what to overlay (exact text, logo, counters), cut on the beat, grade, captions, exports. Explicitly assign to the editor everything the generator cannot do reliably.

### Step 8: Self-critique

Read `references/review-checklist.md` and run it silently: hard-ban pass, the director's questions, concept tests, prompt-quality checks. Fix P0s (any ban hit, a generic claim, a soft hook, a missing rest state, a missing end-card fact) before delivering. Stop when no P0 is open; usually two rounds.

## Output format

Deliver concisely, in this order (omit sections the mode does not need):

1. **Idea, device, logline** (3 lines) and the assumptions you made.
2. **Style Bible** (code block).
3. **Beat table**: #, seconds, what the viewer sees, on-screen text, sound, seam to the next shot.
4. **Shot prompts** (one code block per shot, Style Bible included, negatives included).
5. **Key-frame image prompts** and the **music prompt**.
6. **Edit notes**: what to add in an editor, cut grid, exports and re-layouts, and what the generator will not do reliably.

Do not paste the whole treatment, the reference files or the catalog into the answer; use them to make the decisions. Keep the answer proportional: a 30 s launch pack is longer than a loop. Do not close with a menu of next steps.

## Delivery rules of thumb

- 60 fps thinking: UI and camera moves need smooth motion; for exports tell the user 60 fps (24 fps is never right for UI; GIF at 25 fps).
- Tell the user honestly when a code-rendered pipeline (Remotion / HyperFrames, the original Cinetic skill at https://github.com/Leonxlnx/cinetic) fits better: pixel-exact UI and type, true motion blur, beat-locked score, loop seams. Still deliver the best prompt set for their tool.
- Tool capabilities change; say "check which modes your version offers" instead of asserting limits.
- Never invent real brands, people or companies in sample copy; use plausible invented names.
- Never reproduce a competitor's film, a real product's UI, or copyrighted characters; the look belongs to the brand being briefed.

## Reference map (read when its step comes up; do not read everything at once)

| Step | File | What it gives you |
|---|---|---|
| 1 | `references/formats.md` | length/beat/word budgets, recipes per format, vertical safe zones |
| 2, 5 | `references/concept-and-copy.md` | inventory, lenses, tests, device, arcs, end cards, copy rules, worked concepts |
| 3 | `scripts/pick_techniques.py`, `references/technique-catalog.md` | random technique draw; 273 techniques to grep |
| 4 | `references/look-and-personality.md` | personality table, bans, colour, type, layout, UI depiction, tell list |
| 5 | `references/motion-camera-sound.md` | motion laws, easing words, pacing, holds, camera, transitions, timing grid, sound and music |
| 6, 7 | `references/prompt-templates.md` | Style Bible template, shot anatomy, negative block, tool notes, fixes, a worked example |
| 8 | `references/review-checklist.md` | ban pass, director's questions, severity, critiquing a clip |
