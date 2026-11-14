# Prompt templates, tool notes and a worked example

## Contents
1. The Style Bible template
2. The shot prompt anatomy
3. The negative block
4. Tool notes (Google Flow / Veo, Runway, Kling, Luma, Sora, Pika; key-frame image tools; music tools)
5. Text, logos and UI: what generators get wrong
6. Continuity workflow
7. Fixing a generator that ignores the rules
8. Worked example (20 s product video)

## 1. The Style Bible (paste at the top of EVERY shot prompt, unchanged)

40-80 words. Fill every slot; this is what makes separate clips look like one film.

```
STYLE: [stage: e.g. cool off-white paper surface, faint cool cast, not beige] with [ink: soft near-black graphite text and UI]. One accent, [colour name], meaning "[one word]", used sparingly (under 8% of the frame). Type: [one clean modern sans, weight, sentence case, tight spacing, upright, no serif, no italic]. Shapes: [corner radius character]. Surfaces: [soft low shadow / thin top hairline], flat tonal fields, no gradients, no glow. Motion: [easing character in words], weighted, smooth, no jitter, settles and then holds still. Camera: [locked-off with slow 2-3% per second push / slow dolly], shallow depth of field only when specified. Light: [flat even soft daylight / controlled studio], no bloom, no lens flare. Grain: none.
```

Build it from the personality table (look-and-personality.md) and the motion words (motion-camera-sound.md). Name the accent in plain colour words ("signal red", "deep pine green"), never hex codes (generators ignore hex).

## 2. The shot prompt anatomy

One shot = one beat = one main action = one rest state. Write plain flowing prose in this order (generators weight the beginning most):

1. **Subject + action** - "A phone-sized app screen fills the frame; the list of 23 groceries reorders, and one row lifts to the top."
2. **Setting / surface** - what it sits on, what is behind it, how much of the frame the hero covers (40-70% for product; full-bleed or 70-92% of width for a window).
3. **Camera** - shot size, movement, speed ("slow push-in about 3% per second, locked horizon, no handheld shake").
4. **Motion timing** - what moves first, easing words, when it rests ("eases in over about half a second, settles with no bounce, then holds perfectly still for the last second"). Name the rest state: it gives a clean cut point.
5. **Look** - the Style Bible, pasted.
6. **Text on screen** - exact words in quotes (<= 5 words/line, <= 2 lines), or "no text".
7. **Negatives** - the negative block (or the tool's negative field).

Also give for each shot: the beat's seconds, the sound note (one line), and the seam to the next shot (what carries across: the device, a colour, a direction).

Length rules: do not ask one prompt for a whole film. Aim for clips of roughly 4-8 s (or whatever the tool's limit is); one idea per clip; trim in the edit.

## 3. The negative block

Paste into the tool's negative-prompt field, or append as "Avoid: ...".

```
serif fonts, italic or slanted text, handwriting fonts, orange, amber, gold, beige, cream, tan, sand, purple, violet, indigo, neon, glow, bloom, halo, lens flare, light leak, glassmorphism, frosted glass, gradients, rainbow, mesh gradient, sparkles, particles, confetti, emoji, stock icons, code rain, bokeh, film grain, lorem ipsum, random small text, watermarks, logos other than the one specified, tilted floating screenshot cards, handheld shake, bouncy overshoot, glitch, RGB split, flash to white, fade through black
```

Remove an item only when the user's brand supplies it (e.g. a serif wordmark), and note it as brand-supplied. If the tool has no negative field, convert to positive phrasing as well ("matte, flat, even, quiet, no effects").

## 4. Tool notes

Capabilities and limits change; tell the user to check what their version offers. These are patterns that hold across tools.

**Google Flow (Veo).** Work shot by shot. Typical modes: text-to-video, frames-to-video (start frame, and where offered an end frame), ingredients-to-video (reference images for subject/style consistency), and a scene builder / timeline to sequence and extend clips. Clips are short (often around 8 s), so plan beats of 4-8 s. Veo-class models can generate sound; if you want to control audio, say "no music, no voiceover, only quiet UI sounds" and add the real score in the edit. Write fluent prose, not keyword soup. Put camera language and timing in the prompt. For a consistent film: generate a key frame image first (a still of the stage + device + type style), reuse it as the start frame or an ingredient for every shot.

**Runway / Kling / Luma / Pika / Sora.** Same anatomy. Use image-to-video from your key frames for consistency; give camera moves explicitly ("slow push-in", "locked-off"); keep a single action per clip; prefer short durations. Where a motion/camera control panel exists, set it to match the prompt rather than relying on text alone.

**Key-frame image tools (Imagen / Midjourney / Nano Banana / DALL-E etc.).** Prompt composition, surface, palette and hierarchy: "flat, clean, minimal product frame, [stage], [hero covering ~60% of the frame], one [accent] element, no text" - then add text in an editor. Generate 3-4 candidates of the SAME frame, pick one, reuse it. Make the end-card/poster frame too. Ask for the aspect ratio you need; for 9:16 describe the vertical composition explicitly (mass in the middle band, bottom 40% filled with the stage).

**Music tools (Suno / Udio / Lyria / stock search).** Use the music template at the end of motion-camera-sound.md; give tempo, key, palette from the personality row, the breakdown timestamp, the hit timestamp and the ending. Instrumental only.

**Editor (CapCut / DaVinci / Premiere / After Effects).** Needed for: exact text and logo, cuts on the beat, speed ramps, consistent grade, the score, caption files, aspect-ratio re-layouts. Say so in the output rather than pretending the generator will do it.

If the user needs pixel-exact UI, readable text, a precise logo, perfect loops or a beat-locked score, say that a code-rendered pipeline (e.g. Remotion or HyperFrames, as in the original Cinetic method) fits better, and still deliver the best prompt set for their chosen tool.

## 5. Text, logos and UI: what generators get wrong

- Generated on-screen text is often garbled or changes between frames. Strategy: (a) ask for the shot with NO text ("clean empty space in the lower third for a one-line caption") and add the real text in the editor; or (b) allow 1-3 short words in quotes and verify every frame.
- Logos and wordmarks: never trust them. Generate the motion (a mark assembling from simple shapes) and composite the real logo.
- UI: describe flat, simple components with clear hierarchy; ask for "abstract list rows with a short title and a small chip, no readable paragraphs"; plan to overlay real UI screenshots/recordings only as texture or in a composited layer; the hero shot should not be a static screenshot - the state change is the point.
- Numbers: counters will not count correctly. Generate the surrounding motion and animate numbers in the editor, or show the result state with a short exact number in quotes.
- Hands, faces and people: avoid unless essential; if used, keep one person, simple, in-world (not stock-style), no stock handshake or smiling-at-phone shots.

## 6. Continuity workflow

1. Key frame(s) first (hook frame, product frame, end-card frame) in the exact palette and type style.
2. Same Style Bible pasted into every video prompt.
3. Start each shot from the previous shot's last frame (frames-to-video / extend) when the device carries across; give the device a visible identity (shape + colour + state).
4. Re-use the same seed or reference images where the tool allows.
5. Generate 2-3 takes per shot and pick the best; discard any take with a banned item, garbled text, a jump cut inside the shot, or motion that never settles.
6. Edit: cut on the beat; keep each clip's best 3-5 s; consistent colour grade over everything; add text, logo, music and SFX last.

## 7. Fixing a generator that ignores the rules

| Symptom | Fix |
|---|---|
| Glow / bloom / lens flare appears | add "matte, flat, even lighting, no bloom, no glow, no lens flare"; lower the contrast of the brightest element; avoid the words "light", "radiant", "shining" |
| Purple/blue gradients or orange tint | name the exact colours in words, add the negative block, say "single flat colour fields"; regenerate from a key frame in the right palette |
| Serif or italic text | "upright geometric sans, no serifs, no italics"; or generate with no text |
| Everything bounces / wobbles | "no bounce, no overshoot, critically damped, ends exactly at rest"; shorten the clip |
| Too many things move | "only X moves; everything else is perfectly still" |
| Camera drifts randomly | "locked-off tripod, no handheld, no camera shake"; specify the one intended move |
| Shot never rests | "after the move, holds perfectly still for the final second" |
| Generic stock look | name the owned device, remove cliche props, add the product's specific objects; rerun the ownership test |
| Inconsistent across shots | key frame as start frame; identical Style Bible; ingredients/reference images; same seed if offered |
| Fake UI text is garbled | "no readable text", composite real UI later |

## 8. Worked example (invented product; pattern only)

**Brief:** "Shelf", a fridge app. 20 s product video for a feed, 16:9 master, muted-first. Smart part: it does not list everything; it ranks by days left and surfaces the one thing that expires tonight, with a "cook this" plan.

**Idea (<= 8 words):** Shelf finds what to cook first.
**Logline (<= 15 words):** A "1 d" chip rises out of 23 identical rows and becomes tonight's dinner.
**Device:** the days-left chip (a small pill with a number). **Grammar:** only vertical moves; after the turn everything gets quieter.
**Personality:** warm, kind, steady. **Accent:** signal red, meaning "cook first".
**Tests:** ownership pass (the chip is the product's object); deletion pass; specificity pass (a plain list would show 23 equal rows - the film shows the ranking); muted pass. Copy: 9 words of a 15 budget.

**Style Bible**
```
STYLE: cool off-white paper surface with a faint cool cast (not beige), soft graphite near-black text and UI. One accent, signal red, meaning "cook first", under 8% of the frame. Type: one friendly humanist sans, medium weight, sentence case, upright, no serifs, no italics. Rounded 16-24 unit corners, soft low shadow, flat tonal fields, no gradients, no glow. Motion: unhurried, eased, weighted, no bounce, settles and then holds still. Camera: locked-off with a slow 2-3% per second push. Light: flat even soft daylight, no bloom, no lens flare. No film grain.
```

**Beat list**
| # | Time | What the viewer sees | On-screen text | Sound |
|---|---|---|---|---|
| 1 | 0-4 s | Full-bleed app list, 23 identical rows each with a quiet grey chip, scrolling slowly; one chip near the middle reads "1 d" | "23 things." | soft mallet ostinato, one tick per row |
| 2 | 4-8 s | Slow push to the "1 d" chip; the scroll stops; everything above and below dims | "One expires tonight." | music thins to a held note, a half-second silence |
| 3 | 8-13 s | The chip rises to the top and turns red, reading "Tonight"; the other 22 rows drop to quiet grey; a counter reads 23 then 1 | - | one warm chord on the landing, quiet bed |
| 4 | 13-17 s | The chip unfolds into a recipe card for what to cook with it; holds still | "Cook this first." | gentle resolve |
| 5 | 17-20 s | The card shrinks back into the chip, which becomes the dot in the wordmark; name and one line under it; slow 10% push; tail | "shelf" | two-note chime, tail to silence |

**Shot 1 prompt**
```
A phone-sized app screen fills the entire frame edge to edge. A list of 23 grocery rows, each with a short item name and a small grey rounded chip showing days left, scrolls upward slowly and steadily; one row near the middle has a chip reading "1 d" that looks identical to the others. Camera locked-off with a very slow 2% per second push. The scroll never speeds up. At the end of the shot the scroll slows to a gentle stop and holds perfectly still for the last half second. On-screen text, lower third, exact words: "23 things." [STYLE block pasted here]. Avoid: [negative block].
```
**Shot 3 prompt**
```
The same app screen, scroll stopped. The chip reading "1 d" lifts straight up out of the list to the top row over about 0.6 seconds, easing in and landing softly with a tiny contact squash and no bounce, and as it lands it turns signal red and its text changes to "Tonight". At the same time the other 22 rows ease down to quiet low-contrast grey. Only these elements move; everything else is perfectly still. A small counter in the corner reads 23 and settles on 1. Camera locked-off, slow 2% per second push. Holds still for the final second. No text overlay. [STYLE block pasted here]. Avoid: [negative block].
```
(Shots 2, 4, 5 follow the same pattern: one action, rest state, exact words, Style Bible, negatives.)

**Key frames to generate first:** the hook frame (full-bleed list, one "1 d" chip), the "Tonight" frame (red chip at top, others grey), the end card (cool off-white stage, wordmark "shelf" with the chip as its dot, one line beneath).
**Music prompt:** "100 BPM, major key, soft mallets and felt piano, warm pad, instrumental; sparse intro for 2 seconds, a quiet held note with half a second of silence at 0:07, one warm chord at 0:08, resolves into a gentle two-note chime ending at 0:18 with a 2 second tail."
**Edit notes:** overlay exact text in the editor in one friendly sans; keep each clip's best 4 s; cut on the 100 BPM beat (every 0.6 s); animate the 23 > 1 counter in the editor; export 16:9 master, then separately re-prompt a 9:16 layout (mass in the middle band, captions inside the safe band).
