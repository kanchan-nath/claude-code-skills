# Look and personality

Read at Step 3 (the Style Bible). When the user supplies a brand (colours, fonts, logo, footage, tone), the brand wins over every default here, including the hard bans; record it as "brand-supplied" and drop that item from the negatives.

## Contents
1. Personality first (three adjectives)
2. Hard bans
3. Colour
4. Type
5. Layout and framing
6. Surfaces, texture, decoration
7. Showing the product (UI depiction)
8. Tells that make work look generated

## 1. Personality first

Write three adjectives for the brand, then derive the look. Without this step every film drifts to the same cool, light, geometric-sans minimalism, which reads as a template on the second viewing. A calm notes app and a fast CI tool must not share a look.

| Personality | Type (a clean sans, one or two weights) | Stage | Accent family | Shapes | Motion character |
|---|---|---|---|---|---|
| Calm, clear, unhurried (notes, reading) | humanist sans, light-regular (350-450), sentence case | light neutral/cool paper, soft ink | low-chroma ink blue, moss/sage, teal | soft radii, thin strokes | unhurried: 0.5-0.8 s moves, soft settles, no overshoot, long holds |
| Fast, exact, confident (CI, APIs, build tools) | tight grotesk, 600-650, lowercase or sentence; mono for numbers/logs | often dark (near-black ink), neutral/cool | hot signal: signal red, signal green, clean yellow on ink | square or tiny corners, hard edges, visible grid | crisp: 0.2-0.35 s moves, cuts on the beat, no overshoot |
| Bright, friendly, playful (consumer, social, games) | rounded sans, 600-700, sentence | light, or one designed flood of the accent | one saturated primary: red, blue, green, yellow | big radii, pills, soft blobs | lively: quick arrivals, contact squash; overshoot only on <= 2 true landings |
| Precise, quiet, expensive (finance, legal, premium) | neo-grotesk, 400-500, light touch | deep near-black (green-black, navy-black) or bright neutral paper with fine rules | deep jewel tones at restrained chroma: emerald, sapphire, deep red | 2-6 unit corners, hairlines | slow and exact: 0.6-1 s, no overshoot |
| Raw, mechanical, honest (dev tools, hardware) | mono plus grotesk, 500-700, lowercase | concrete grey or dark | safety yellow (on ink/concrete) or signal red | square corners, notches, rules, registration marks | mechanical: detents, steps, hard stops, conveyors |
| Warm, kind, steady (health, care, community) | friendly humanist sans, 500-600 | light neutral with soft greys (warmth from type, shapes, motion - never a beige paper) | from the product's world: leaf/sage green, sky blue, soft red | rounded 12-24 unit corners, organic shapes | soft: gentle settles, no overshoot |

Light or dark is a brand decision: dark fits dev/infra tools, night, focus, security, anything named for fire/heat/energy, premium cinematic; light fits documents, reading, health, consumer, daylight products. Weight carries tone: a calm brand rarely wants a heavy grotesk wordmark; a fast tool rarely wants a hairline one.

Check: put the planned look next to a generic "minimal tech launch" frame. If a stranger could believe they are one brand, the personality has not reached the prompt.

## 2. Hard bans (when you invent the look)

Never in a prompt; add to the negative prompt block.
- **Words:** eyebrow/kicker labels; stacked taglines; "Introducing..."; text walls; filler text (decorative mono captions, fake metrics, version strings, labels nobody needs, lorem ipsum).
- **Type:** serif faces; italic or oblique (including skewed text). One clean modern sans, plus a mono only if the product shows code/numbers. Condensed display faces read as a generated tell too.
- **Colour:** orange, amber, beige, cream, tan, sand (accent, paper or glow); neon (very bright saturated accents, glow, bloom, halo); purple, violet, indigo, and purple-to-blue or any multi-hue gradient; glassmorphism (backdrop blur + 10-20% white fill + 1 px white border).
- **Decoration:** emoji and stock icons; sparkles for "AI", particles, confetti, lens flares, code rain, bokeh, starfields; bouncy overshoot on anything that is not a true landing.

Allowed: ink and paper (light or dark, neutral or cool), ONE accent with a meaning from red / green / teal / blue / yellow, one sans, and eased, weighted, smooth motion. The creativity goes into the idea, the device and the choreography - not into effects.

## 3. Colour

- **Accent: meaning first, hue second.** One word of meaning from the story ("now", "risk", "water", "handled", "set aside", "look here"). One accent only; one meaning only; never both success and error; never decoration. It covers <= 8% of pixels on any frame except one designed flood (usually the turn). New things arrive in the accent and relax to neutral over ~0.2-0.5 s ("just happened").
- **Choose the hue from the product's world** (safety yellow on a builder's level, the red antifouling paint below a hull's waterline). On a light stage the accent is mid-tone (clearly darker than paper); on a dark stage it is lighter but not glowing. Yellow needs a dark stage (or ink text on a flood); on paper it is invisible. Below very low saturation the accent reads as grey, not a signal.
- **Prompt-language colour words:** say "signal red", "deep pine green", "clean safety yellow on charcoal", "lake teal", "ink blue with depth". Avoid "vibrant", "glowing", "neon", "electric", "pastel gradient", "warm", "golden", "terracotta", "peach", "lavender".
- **Ink is not pure black.** Say "near-black charcoal" / "ink with a faint blue-green tint". Pure black reads as a hole and crushes in compression. Raised surfaces step up one tone lighter.
- **Paper is not beige.** "Cool white / off-white with a faint cool cast". Warm light paper = beige = banned unless brand-supplied.
- **Tint the neutrals** toward the brand's world (cool green-grey, blue slate), or keep them neutral. Never warm. Avoid framework blue on flat grey (the default "template" look) and the stock blue-grey dev-tool dark theme; take the stage from the brand's world instead.
- **Palettes with character:** hillside/fjord/forest = pale green-grey paper or pine-black, accent deep pine or lake teal; foundry/forge = true charcoal with no blue in it, accent a deep red used as heat on a lit edge; night/focus/security = ink-navy with body, cold cyan-teal accent; ledger/archive = cool white, graphite hairlines, one ink blue with depth; signal/traffic/energy = near-black, steel, safety yellow on dark only; garden/health/care = cool mint-white, sage greys, leaf green. One colour story: stage, neutrals and accent from the same world.
- **Colour must show up.** At thumbnail size a mid-film frame must show the brand colour carrying the product's action; a colourless film has no identity.
- **In a dev tool, red means error:** if red is the brand, spend it on the brand's own thing (the device, the payoff) and keep UI states quiet.
- **Light/dark changes** (a polarity flip) are the loudest punctuation: carry them on a moving shape from the device (iris, flood, shutter), land on a downbeat, at most one per bar, the accent floods the frame once. Never a crossfade through black (it dips ~25% in brightness).

## 4. Type

- One family, two weights, chosen for personality; mono only if the product needs it. Emphasis from size or motion, not italics.
- Statements are large and short: 88-128 px on a 1080p frame (about 8-12% of frame height), line spacing tight (0.95-1.05); emphasis words 1.5-1.7x the statement size; secondary lines 44-56 px; UI text >= 22 px on screen after any zoom (readable on a phone). Vertical 9:16: statements 110-140 px, UI >= 32 px.
- One tracking value per role. Sentence case; ALL-CAPS micro labels are landing-page grammar. Numbers in tabular figures so they do not jitter.
- Word-level reveals; per-letter motion only for the single hero word. A reveal must never spell a different word partway, nor show half a glyph.
- Blur only while text enters and moves fast, then land sharp. Text being read moves slowly (about 2-3 px/frame at 60 fps) or not at all.
- Prompt wording: "set in a clean modern grotesk sans-serif, semibold, sentence case, tight spacing, no italics, no serif".

## 5. Layout and framing

- Avoid "text left, UI card right on white" and small centred floating cards on an empty field. Prefer the product full-bleed or a window at 70-92% of frame width, ideally overflowing an edge; anchor type to an eye line or the lower third; one focal action per shot.
- In product shots the hero covers ~40-70% of the frame. Outside designed negative space around a single hero (a logo), no region over about a quarter of the frame stays empty.
- Safe margins: >= 5% of width at the sides, >= 6% of height top and bottom for any text or key action.
- Show only the meaningful part of the product. No half-empty grids, no tables cropped at the frame edge, no rows of blank cells.
- Vertical 9:16 is its own composition (see formats.md): mass in the middle of the safe band, not a 16:9 layout in a tall frame.
- No floating-screenshot cards tilted in a void; no device mockup orbiting in space unless hardware is the product.

## 6. Surfaces, texture, decoration

- Shadows on light stages: one soft key shadow, large and low-opacity. On dark stages, shadows vanish: separate surfaces with a slightly lighter tone and a 1 px top hairline of faint white. Never glow, halo, bloom, outer glow on text, gradient borders.
- Stages are flat tonal fields; at most one or two large soft shapes a few tones off the ground. No haze or colour pools behind the hero (reads as a stock gradient backdrop). Gradients, if essential, are single-hue and subtle (banding is a real artifact in AI video and in encoders).
- Grain is either absent or one global, very light layer (1.5-2%). Not per scene.
- Every element must name its job (reveal, route, validate, emphasise) or be cut.

## 7. Showing the product (UI depiction)

- Real-looking product surfaces with named, specific, internally consistent data (plausible invented names, amounts, times). No fake KPIs, up-and-right charts, lorem ipsum, stock icons, generic dashboards.
- Show the smart part: the non-obvious behaviour (itemised not even split; ranked not listed; only the future rescheduled). Restraint applies to decoration, never to the product's intelligence.
- Name the feature once, as a UI label (the tab, menu item, or the button that causes the action), or as the one line, or on the end card; and show enough real app chrome (header, sidebar, window edge) that a stranger knows it is software.
- Counters count on each visible event; the thing that changes state changes on the frame its cause lands; a paused frame still makes sense (right weekday, counts match items, the payer is not shown owing).
- No cursor once the product acts on its own. A cursor, when needed, travels an arc over ~0.6-0.8 s and presses once.
- AI video generators invent UI text and layouts. Describe UI as simple flat shapes with clear hierarchy, ask for "no readable paragraphs", and plan to composite real UI/text in an editor if exact copy matters.

## 8. Tells that make work look generated (use as a review list)

Concept: feature tour (feature, feature, feature, logo); wrong first frame (Introducing/question/logo/blank); borrowed props (rocket, lightbulb, globe, shield, sparkle); a style posing as an idea; a demo without a cause; the device drops out; frames that contradict the promise; a recycled or dead end card; an oversimplified feature; an anonymous product that cannot be named.
Copy: landing-page grammar; stock phrasing; a feature name as a headline; text wall; over budget; microcopy asked to carry meaning.
Type: serif/italic "elegance"; condensed "impact"; near-miss sizes and weights; flat scale (everything 48-64 px); blur-dissolve on every word; letter gimmicks (typewriter headlines, scramble, per-letter bounce); numbers that jitter.
Colour: indigo-violet-blue gradients, mesh blobs, aurora; neon on black; beige + orange; glass and glow; an accent without a meaning; filler decoration; pure black holes; a default palette (framework blue on flat grey); a colourless film; haze behind the hero.
Layout: the SaaS layout; voids and edge bands; no margins; sliced glyphs; cropped social versions; a lockup lost in a void (under ~25% of width); an empty vertical frame.
Motion: the default fade-in/slide-up-30px entrance; uniform timing (every move 0.4-0.5 s on one curve); bounce everywhere; ease-in entrances and ease-out exits; stall-then-lurch; everything moving at once; six objects landing on one frame.
Pacing: soft first second; dead holds; cramming (17 scenes in 32 s); flat energy; sound on every event.
