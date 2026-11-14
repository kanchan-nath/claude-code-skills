# Formats

Pick the row first. It sets length, density, on-screen words and what you deliver. Budgets scale with LENGTH, not ambition: a 15 s launch is half the beats and words of a 30 s one, not the same film squeezed.

| Format | Length | Tempo | Story beats | On-screen words | Sound | Deliverables (what to tell the user to produce) |
|---|---|---|---|---|---|---|
| Launch film / teaser | 20-45 s | 120 BPM | 8-10 per 30 s | 15-25, cap 35 | full score + SFX | 16:9 master, 9:16 and 1:1 re-layouts, poster frame, brand kit if invented |
| Product / feature video | 8-30 s | 100-120 | 1 capability per 8-10 s | <= 15 | light bed + UI SFX | master, poster |
| Feature loop | 4-15 s, whole bars | any, whole bars | 3-5 | <= 8, reads muted | optional | MP4, WebM, GIF (25 fps), seamless seam |
| Logo sting | 3-8 s | 120 | 2-4 | name + <= 4 | one tuned hit + tail | MP4, alpha versions, poster, brand kit if invented |
| UI walkthrough | 20-90 s | 90-110 | 1 chapter per 2-4 bars | <= 6 per caption | bed + UI SFX | master, caption file |

Use 60 fps whenever UI, text or camera moves (24 fps is never right for UI; 30 fps makes slow drifts step). A GIF is the exception: export at 25 or 50 fps.

The destination decides three things: whether it must read muted (feeds and landing pages autoplay without sound), whether it loops, and which aspect ratios you owe. Ask or assume, and state it.

## Launch film (20-45 s) and teaser

Purpose: make a viewer feel a problem, see the product answer it, remember the name. 30 s template (15 bars + 1 s tail):

| Time | Beat | What happens | Sound |
|---|---|---|---|
| 0-6 s | hook > problem | Frame 0 already moving, device on screen; problem felt by 1 s, stated by 2 s, then piles up visibly; ends in an implosion or a gather into the device | signature motif alone, then intro chords; a "suck" to true silence before the turn |
| 6-10 s | turn | Drop 1 on a downbeat: the device meets or becomes the mark; lockup <= 1.5 s or visibly building; the mark opens into the product (container morph) | drop 1, motif keeps time |
| 10-18 s | proof 1 | One capability as cause > action > result; the human's one input first, then the product acts; drop 2 where the product takes over | riser into drop 2; landings on chord tones |
| 18-24 s | proof 2 / consequences | One line per bar, each paying off earlier copy; one consequence per line on the beat | whips peak on the kick; payoff on the clap |
| 24-30 s | promise | Pull back to show scale; the refrain resolves; device becomes the mark | breakdown, then the resolution chord on the promise word |
| 30-33 s | lockup / end card | Name, URL (readable >= 1.7 s), bookend, tail to silence | motif bookends; tail to zero |

Two drops, not five. The signature move appears three times (open, middle, close). Teaser (15-20 s): keep hook, turn and lockup, cut proof to a glimpse or nothing, 6-10 words; still never open on the logo.

## Product / feature video (8-30 s)

Show one capability so clearly the viewer could explain it afterwards. Structure (16 s example): 0-4 s inside the product in the "before" state with the pain visible and the device/accent marking what is wrong; ~6 s the cause (one human input, the only cursor moment); 8-12 s the product acts (state changes, counters count on each event, camera anchors on the region doing the work); ~12-14 s the result holds with the one line naming the value in the viewer's words; last ~2 s a small lockup (mark, name, feature name if needed). Keep the device (an accent-marked item, a selection, a moving total). No cursor after the cause. Name the feature once and show enough app chrome to read as software.

## Feature loop (4-15 s)

A landing-page hero or social post that autoplays muted and repeats without a visible restart. The first 2 s already show the product and the action starting (a row arriving, a reading dropping, a card dragged); a quiet setup beat is not a hook. Design a CYCLE, not enter > hold > exit: conveyor (items flow through, last arrives where the first started), relay (the device exits one side and re-enters with a new input on the other), or state round-trip (A > the product acts > B > B becomes the next A). A loop that fades out and back in is a slideshow. Frame 0 is also the poster, so compose it with the product's name or chrome visible. Prompt it: "the last frame is identical to the first frame; seamless loop". With generative tools, generate from a key frame used as BOTH first and last frame (Flow: frames-to-video with the same image as start and end) and check the seam in the edit. Copy: <= 8 words, readable muted, e.g. "18%. Water now." > "42%. Leave it."

## Logo sting (3-8 s)

The mark arrives with intent, makes one sound, and holds long enough to be read. The lockup at resolved size spans ~28-45% of frame width (smaller = a small object in a void). Anatomy (6 s): 0-2 s gather (frame 0 already moving; one primitive of the mark builds tension with anticipation: a pull back before the push, or a rising tick); 2.0 s assembly hit (primitives accelerate into contact, squash, one tuned hit on the contact frame; if the accent floods the frame this is its one moment); 2.5-3.5 s the wordmark reveals from behind the mark's live edge, words lock without overshoot; 4-6 s lockup holds and builds (10-20% push, tiny beat punch), tail decays to silence. Assemble the mark from its own 2-4 primitives (a fade or scale-up of a flat logo teaches nothing). End on the lockup, held and building; never a slow fade to blank. Mark rules: build from the name's meaning, a letterform, the product's object or a pure geometric construction; reject anything that could belong to ten other startups or misreads at 64 px as a common symbol (minus/plus, emoticon, menu, padlock, play button). Generative tools cannot be trusted with exact logos: generate the motion/feeling and composite the real logo in an editor.

## UI walkthrough (20-90 s)

Teaches a flow; calmer than a launch film but never static. Chapter template (repeat per feature, chapter changes on downbeats): establish (wide on the product, chapter caption in the lower third) > push (camera moves to the feature's anchor) > cause (one cursor arc over ~0.6-0.8 s and one click, or typing) > action > result (holds >= 0.6 s + 0.1 s per word while the caption is readable) > hand-off (whip or pull-back to the next anchor). One caption per chapter, <= 6 words, burned in for muted viewing, >= 28 px, lower third. Cold open on the end result for 2-4 s. One anchor camera for the whole walkthrough; UI drifts during holds. Over 60 s, generate chapter by chapter.

## Social re-layouts (9:16, 1:1, 4:5)

Re-lay out; never crop a 16:9 master. Timing stays identical; positions, sizes, line breaks and camera anchors change. Write separate prompts per aspect ratio from the same beat sheet.

Vertical 9:16 (1080x1920): a tall frame is not a wide frame with bars. Safe band for text and key action: from ~14% down to ~78% of the height (top ~270 px, bottom ~420 px, right ~120 px; stricter for long captions/paid posts: bottom ~35%). Content mass sits in the middle of the safe band (~y 885), no empty bottom 40%, the product fills or bleeds past the band; type and UI about 1.3-1.5x their 16:9 sizes (statements 110-140 px, at most two lines of <= 3 words; UI >= 32 px). The header and caption zones carry the stage or the product's edge as texture, never anything to read. Burn captions into every feed variant.

| Aspect | Keep text/key action inside | Type minimums |
|---|---|---|
| 16:9 | 5% at sides, 6% top/bottom | statement 8-12% of height, UI >= 2% of height |
| 9:16 feed | top 14%, right 6%, bottom 22%, left 3% | statement 110-140 px at 1080 wide, UI >= 32 px |
| 1:1 | 6% on every side | statement >= 72 px, UI >= 28 px |
| 4:5 | 6% at sides, 7% top/bottom | statement >= 80 px, UI >= 30 px |

## Other short forms

| Request | Recipe |
|---|---|
| Teaser or trailer | launch teaser variant: hook > turn > lockup, 15-20 s, 6-10 words |
| Intro / outro for other videos | sting recipe, 3-5 s; the outro reverses the intro's entrance; ask for a transparent-background version |
| Kinetic type piece | launch structure with words as the device; one line at a time; a statement per bar |
| App demo | product video if one capability, walkthrough if a flow |
| Promo clip with footage | product video structure; the brand's footage and grade win; add type and sound on the grid |
| Social cut-down of a finished film | trim at bar boundaries, never mid-bar; re-lay out |
