# Motion, camera, transitions, timing and sound (in prompt language)

Read at Steps 4-6. The source numbers were measured at 60 fps; here they are in seconds so you can write them into prompts. Generative video tools will not obey exact timings, so use these as direction words plus a rest state, and fix the exact timing in the edit.

## Contents
1. Motion laws, as words
2. Easing vocabulary
3. Pacing and energy curve
4. Holds and stillness
5. Camera
6. Transitions
7. Timing grid (BPM, bars, reading time)
8. Sound and music

## 1. Motion laws, as words

- Entrances decay (fast start, long gentle settle); exits accelerate (slow start, fast end). Only the camera eases both ways. Fades take ~0.17-0.23 s on a smooth sine-like curve; never an abrupt fade.
- Linear motion is for constant drift only (a slow background creep, a clock hand). Anything that starts or stops uses a curve.
- Duration scales with distance: roughly 0.35 s + 1.35 ms per pixel on a 1080p frame (150 px = 0.55 s, 350 px = 0.8 s); camera moves clamp to 0.6-2.4 s. The longest move in a film lasts at least 3x the shortest, or everything feels the same speed.
- Consecutive moves overlap: a second move begins at ~55-75% of the first (about 0.33 s into a 1 s move) so there is no stall-then-lurch.
- One hero motion plus at most two supporting motions at any moment. Pair fast with real stillness (a 0.4 s whip next to a calm hold).
- Everything is eased or critically damped (settles without bouncing). Overshoot of 1-7% only on a true landing (an object arriving at a surface or a lock), at most twice per film. A contact squash (width +8%, height -10%, back to normal over ~0.13 s, anchored at the contact edge) makes landings feel weighted.
- Shape settles slightly before position. State changes (counter, check, total) change on the frame their cause lands, not a beat later.
- Batch landings: stagger 0-3 frames (~0-0.05 s) within a group, first item on the beat. Never six objects hitting on the same frame.
- Smoothness is a ship gate: no jitter, no single-frame pops, no stepped stairs on slow moves.
- Speed ceiling: nothing crosses the frame faster than about the frame width in ~0.5 s without a designed blur or a cut; faster than that, redesign as a cut on the beat, a match cut, a mask wipe, or a shorter distance.

## 2. Easing vocabulary (token > words to use)

| Token | Prompt words | Use for |
|---|---|---|
| out | "snaps in fast and settles softly" | arrivals, reveals, word entrances |
| outSoft | "arrives and settles gently" | secondary arrivals |
| in | "accelerates away", "implodes" | hard exits, implosions |
| exit | "speeds up as it leaves, cut on the fastest moment" | exits into a cut |
| inOut | "smooth S-curve", "whip" | whips, lockup slides, morphs |
| smooth | "gentle sine drift" | fades, drifts, breathing holds |
| ui | "small crisp state change" | toggles, chips, rows |
| cam | "slow start, early peak, long settle" | camera pushes |
| glide | "glides and lands softly" | 150-350 px element moves |
| rest | "ends perfectly at rest" | anything chained after another move |
| contact | "accelerates into impact, arrives with velocity" | landings |
| whip | "fast feature-to-feature whip, ~0.4-0.5 s" | big camera handoffs |

A film uses about three easing characters. State them in the Style Bible and repeat them.

## 3. Pacing and energy curve (measured on top-tier launch films)

- First visible change within ~0.1-0.4 s; first readable word by ~0.4 s; the problem felt by 1 s and stated by 2 s; premise clear by ~2 s.
- The picture changes about every 0.7 s (a new visual beat), even in films whose median shot is 2.7 s. Median shot 1.1-1.6 s for cut-driven films; 2.3-2.8 s for continuous-take films with beats inside each take. Shots under ~0.45 s carry no text.
- The product appears early (median ~2.8 s) unless a 10-19 s problem act earns the wait; then the product or name appears at ~23-26% of runtime.
- Energy curve: an early peak at 10-25% (hook/reveal); one designed lull of 1-4 s at 55-85% (usually a music breakdown); the last and biggest peak at ~75-90%; a calm outro of 8-20%. Every film whose last peak came before 60% sags. Stretches of 5-10 s with only small typing/static rows read as a sag.
- First 6 s are about twice as dense as the middle. About 45-60 discrete events per 30 s; one motion peak per bar (2 s at 120 BPM) with ~0.5-1.2 s of calm between peaks.
- Calm premium films are mostly near-still frames with sharp spikes on transitions; high-energy films are dense. Spend spikes on transitions and hero moves, never on idle motion.
- Cramming is the most common failure: 3 features in 5 s reads as none; 17 scenes in 32 s reads as a showreel.

## 4. Holds and stillness

- A locked-off frame reads as a stalled player in a muted feed. Every hold has slow life: UI hold = slow drift plus a 2-3% per second push; statement = slow grow (3-5% through the hold); lockup = a creep of under 6% if the still hold is 1.3 s or less, or a 10-20% dolly over ~2 s if longer; reading/typing = background parallax under a sharp foreground.
- Once text resolves it stays at least 0.6 s + 0.1 s per word (1 word 0.7 s, 3 words 0.9 s, 5 words 1.1 s). A URL stays readable at least 1.7 s. Text that has not resolved never exits.
- Nothing is static for more than ~0.8 s, except a designed freeze of 0.25 s exactly on a silence, and one designed near-still hold of 1.0-1.6 s on the key claim or success state under a music dropout, followed by a big move.
- End card: assemble ~1-1.3 s, hold 0.6-1.3 s still or building, then tail. Never a complete card sitting static, never more than ~2.5 s.

## 5. Camera

- Describe the framing like a director: this point of the product sits there on screen, this big. Move between framings with the subject travelling a straight screen path at an even zoom rate (zoom in log space: equal perceived speed).
- Per-hold modifiers: **breath** (about +2.5% push inside a hold, released by the next move), **dip** (a slight pull-back, up to ~18%, during a whip between close framings), **punch** (about +1.2% on a payoff or lock-in; one per payoff, never every beat), **dolly** (1 to 1.2x over a logo/statement hold).
- Push 2-5% per second inside a hold (faster than ~9% per second reads as a move). Interaction moments push in 2-5x so UI reads on a phone; a wide shot of readable UI holds at most ~1.7 s.
- Parallax planes move at ~0.3x (background), 1.0x (subject), 1.6x (foreground); two planes usually enough, three maximum.
- 3D: perspective equivalent to a moderate lens (not wide-angle distortion); each act gets its own axis (vertical hinge, tabletop, roll/pull-back); same tilted-card angle three times in 15 s is a template tell. Keep total visible shear small (text must never lean like faux italics). Real 3D on the live product with its own shadow on its own ground; never tilted screenshot cards floating in space.
- Pull-back to reveal scale: log-space zoom with a slow tilt and a constant drift easing in from the seam. Rack focus: sharp to soft by crossfading a sharp copy with a constant-blur copy; behind a payoff line veil the defocused background at 80-85%.
- Keep the product covering the frame: no accidental void bands or window edges; 5-8% overscan on moving layers.
- Calm films: sine-like camera, long holds. Fast films: cut on the beat, whips with a velocity handoff.

## 6. Transitions

A seam is a designed match, not a cut between unrelated pictures: something carries across (the story device, a shape held within a few percent of the same screen point, a colour, a direction of motion, a velocity).

- 6-8 transition types per film, each at most twice (velocity-matched cuts exempt), plus ONE signature move derived from the mark used three times (open, middle, close).
- Both sides of a cut are at rest, or the incoming shot starts at the outgoing velocity. Accelerate out (speed grows ~13-20% per frame over the last 0.17-0.4 s), cut on the fastest frame, decay in (slows ~6-11% per frame, resting in 0.75-1.5 s).
- Match every property across a cut (position, size, radius, colour, shadow, opacity). The rest pose appears once (no stop-hold-go). Never cross-fade two copies of one object; morph one object, swap content at the arc apex.
- Energy: calm = 0.5-0.8 s (container morph, rack focus, slow iris, pull-back); medium = 0.3-0.5 s (whip, split on a seam, partial slide); high = 0.15-0.3 s (zoom-through, velocity-matched cut, implosion, flood).
- Catalogue of designed seams: relay handoff (device crosses untouched while the world changes); shared-element container morph (mark pieces become product containers); iris or flood from the device (the accent fills the frame once, usually the turn); implosion into the device then silence then the drop; shutter collapse; split on a seam; velocity-matched cut; zoom-through; partial slide cut; word waterfall; an exit that reverses its entrance; words become the mark. Search `technique-catalog.md` (category `transition`) for more.
- Polarity flips (mean brightness jumping from dark to light) are the loudest punctuation: on downbeats, once or twice per film, carried by a moving shape.
- **Banned:** crossfade as default; dissolving two layers through black (a ~25% brightness dip); glitch / RGB split, light leak, film burn, swirl, ripple, dreamy zoom, flash through white, page burn; the same iris or wipe three times; any whip above the speed ceiling; two copies of one object cross-fading.

## 7. Timing grid

Choose a tempo so a beat is a whole number of frames at 60 fps: 90 BPM = 40 f (0.667 s), 100 = 36 f (0.6 s), 120 = 30 f (0.5 s), 144 = 25 f, 150 = 24 f. A bar = 4 beats (2.0 s at 120 BPM).
- Section changes land on downbeats; cuts inside a section land on 8th notes; batches of landings snap to 16ths with 0-3 frame spread, first item on the beat. A micro-rhythm is welcome: the payoff on the clap, its consequence on the next kick.
- Map beats to bars: a 30 s launch at 120 BPM is 15 bars + a 1 s tail. Give each bar one motion peak.
- Hit frames: start a picture change one frame before the cue; pulses peak ~2 frames after their sound.
- Loops: whole bars; the (unrendered) frame after the last equals frame 0; both sides of the seam at rest or at the same velocity.

## 8. Sound and music (write the music prompt from this)

Sound is part of the system: picture and score share one grid, and every hit is caused by something visible. Match the score's energy to the brand's three adjectives; a calm brand under a trailer drop reads as noise.

| Personality | Palette | Dynamics | Signature hit |
|---|---|---|---|
| Calm, literary, unhurried | soft mallets, felt keys, a warm pad, a single bell | narrow, gentle; no sucks, booms, risers | one soft chord or mallet note with a long tail |
| Fast, exact, confident | tight kick, plucks, clicks, a short saw lead | wide; drops on true silence, a sub on the payoff | a tuned snap + kick |
| Bright, friendly | marimba, claps, pops in a major key | bouncy; small risers | a rising two-note motif |
| Precise, expensive | sparse piano-like tones, low strings pad | slow swells, lots of air | one low, warm chord |
| Raw, mechanical | ticks, detents, metallic hits, noise | stepped, rhythmic, dry | a hard mechanical latch |
| Warm, kind | plucked tones, soft pads | gentle rise and fall | a gentle two-note chime |

Shape of a 20-45 s score:
- Sound enters with intent on frame 0 (a drone or a 150-450 ms entry), no fade-in over the first bar; the first ~2 s are sparse (about 12-14 dB under the body, no sub).
- A tuned motif follows the story's progress (for example one note per step climbing a scale).
- Two drops, not five: the first on the turn; the loudest moment on the hero reveal / payoff (30-60% in) and the promise, not on a mid-film drop. A designed breakdown or stop about 40-80% in; true silence (0.25-0.5 s) immediately before the biggest drop.
- The lockup is the most RESOLVED moment, not the loudest: music stops or filters down as the logo forms, 0.2-0.7 s of near-silence, one soft resolved element on the frame the wordmark becomes readable, then a 0.5-2.5 s tail decaying to silence. A sting is the exception: all lockup, one tuned hit is its loudest moment.
- Designed effects only on discrete state changes (about 5 per 10 s), clustered where the music is sparse. Continuous motion, scrolls, progress bars, rolling counters and most cuts get no effect; the music carries them. About two whooshes per film, only on camera-scale moves and logo zooms, onset 0.1-0.45 s ahead, apex on the visual peak. Once a class of action is sounded, every instance is sounded at one level.
- Typing: a dark per-key tock up to ~25 characters per second with the music ducked; one blip per word if faster.
- Tune every pitched effect to the key's root. Impacts land on the contact frame, not the settle. Audio must not lead picture by more than ~45 ms; move the picture, not the sound.
- Loudness: about -14 LUFS integrated for social/feed (a sting that plays ahead of other videos may sit at -16), true peak below -1.5 dBTP; a 20 s+ film wants contrast (payoff ~2-3 LU above the median).
- Avoid: stock whoosh on every cut, meme effects, riser into crash on everything, drops and sub booms under a calm brand, a flat mix, a soft fade-in hook.

**Music prompt template (Suno / Udio / Lyria / a library search):**
`[tempo] BPM, [key/mode], [personality palette from the table], instrumental, no vocals; sparse intro for ~2 s then [rhythm]; a [N]-second breakdown at [timestamp] ending in silence; one big hit at [timestamp]; ends with a resolved [chord/chime] ringing out for 2 s, no fade-out clipping.`
