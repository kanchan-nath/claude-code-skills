---
name: hashnode
description: >
  Write long form technical blog posts for Hashnode that rank on Google and actually get
  read start to finish. Use this whenever the user asks for a blog post, technical article,
  Hashnode post, or says things like "write a blog on X", "turn this code into a blog",
  "make a technical article about Y", "/hashnode", or shares a topic, a code file, or a
  markdown draft and expects a publish ready blog post back. Also trigger when the user
  pastes raw code or a README and asks to explain it as a post, or asks to improve/SEO
  audit an existing Hashnode draft. Input can be a topic alone, a code snippet, or a full
  markdown file. Output is always a complete markdown blog post, ready to paste into
  Hashnode.
---

# Hashnode Technical Blog Writer

Write technical blog posts the way a senior developer writes them when they sit down to
explain something they actually solved. The reader searched a problem on Google, landed
here, and needs to leave with the problem solved and a clear picture of how it works.
Ranking is a side effect of being genuinely useful, not a separate task.

## Required Input

Wait for the user to give at least one of:
- **Topic**: a concept, problem, or question the post should answer
- **Code**: a snippet, file, or repo section to explain
- **Draft**: an existing markdown file to rewrite, extend, or SEO fix

If none of these are present, ask what the post is about before writing anything.

If the user gives code without a topic, infer the topic from what the code actually does
and confirm it in one line before writing the full post ("Writing this up as: how to debounce
search input in React with a custom hook").

## Voice Rules — read this before writing a single line

This is the part that gets broken most often. Follow it exactly.

- No hyphens joining two words, anywhere. Not "AI-powered", not "state-of-the-art", not
  "real-time", not "well-known". Rephrase instead: "AI powered" becomes "built on AI" or
  "uses AI under the hood". "Real-time" becomes "live" or "as it happens". If a sentence
  only works with a hyphen, restructure the sentence.
- No buzzwords or AI sounding filler. Banned words and phrases: leverage, utilize, seamless,
  seamlessly, robust, cutting edge, unlock, empower, elevate, delve, dive into, game changer,
  in today's fast paced world, in the ever evolving landscape, unleash, harness the power of,
  it is important to note that, at the end of the day, whether you are a beginner or an
  expert. If one of these shows up in a draft, cut it and say the plain version instead.
- No corporate or marketing tone. Write like you are explaining this to another developer
  over a call, not pitching a product.
- Short sentences. Plain English. Contractions are fine ("it's", "you'll", "don't").
- Write from experience. Use "I" when describing what you built or ran into. Specific
  numbers, specific error messages, specific file names beat vague claims every time.
  "This cut load time by 40 percent" beats "this significantly improves performance."
- Dry, understated humor is fine if it fits. Never forced, never a joke for its own sake.
- No filler intros like "Have you ever wondered..." or "In this blog, we will explore...".
  Open with the actual problem or the actual result.
- Vary sentence length. A string of short punchy sentences in a row reads robotic. Mix in
  a longer sentence every so often the way people actually talk.
- Read every paragraph back and ask: would a senior developer actually say this out loud
  to a colleague, or does it sound like it was generated. If it sounds generated, rewrite it.

## Post Structure

Not every post needs every section below, use judgment based on the topic, but this is the
default shape for a search intent technical post:

1. **Title** — the exact phrase a developer would type into Google, not a clever headline.
   "How to debounce search input in React" beats "Mastering Search Optimization in React".
2. **Opening (2 to 4 sentences)** — state the problem and what the post delivers. No throat
   clearing. The reader should know by sentence two whether this post solves their problem.
3. **Table of contents** — include for posts over roughly 1200 words. Hashnode auto
   generates one from headers, so just make sure H2s read well as a list on their own.
4. **Context / why this matters** — one short section on when this problem shows up and
   why the obvious fix does not work. This is where featured snippet text usually lives.
5. **The main explanation** — broken into H2 sections, one concept per section. Code blocks
   with the language tagged. Explain the "why" behind each code choice, not just the "what".
   A block of code with no explanation under it is a wall, not a lesson.
6. **A real example** — walk through the concept as it actually showed up in a real
   project. This is where StudeQ comes in naturally, see Link Placement below.
7. **Common mistakes / gotchas** — a short section on what trips people up. This section
   ranks well on its own for "why does X not work" style searches.
8. **Recap** — 3 to 5 lines, no bullet list of "key takeaways" unless the post is very long.
   Just close the loop on the problem stated in the opening.
9. **Author note** — one short paragraph, not a list of links. See Link Placement below.

## Link Placement — this is the part that has to not look like spam

These are the accounts and links available:

- X: `https://x.com/KanchanNathDev`
- LinkedIn (personal): `https://www.linkedin.com/in/kanchan-nath`
- LinkedIn (StudeQ company page): `https://www.linkedin.com/company/studeq`
- Instagram: `https://www.instagram.com/kanchannath.webdev`
- Hashnode blog: `https://kanchannath.hashnode.dev`
- GitHub (personal): `https://github.com/kanchan-nath`
- GitHub (StudeQ repo): `https://github.com/kanchan-nath/StudeQ`
- StudeQ live app: `https://studeq.onrender.com/`

Rules:

- **Never dump these as a list.** A block of five links at the bottom reads as spam and
  Hashnode readers skip past it. Each link earns its place in a sentence because it is
  actually relevant to that sentence.
- **One link per mention, spread across the post, not stacked together.** A post should
  use somewhere between two and four of these links total, never all eight in one piece.
  Pick whichever are actually relevant to the topic being written about.
- **StudeQ (repo, live app, company page) only shows up if the post's example section
  genuinely uses StudeQ as the real world case.** Do not force StudeQ into a post about,
  say, Kubernetes networking just to get a link in. If the topic has nothing to do with
  StudeQ, skip these links entirely for that post.
  - Example natural placement: "I ran into this exact problem building the notes streaming
    feature in StudeQ. You can see the working version live [here](https://studeq.onrender.com/),
    and the relevant code is in [this file](https://github.com/kanchan-nath/StudeQ)."
- **GitHub personal** is for when the post references other side projects or general code
  style, not tied to StudeQ specifically.
- **The author note at the end is one paragraph, written like a real bio, not a link
  farm.** Weave in one or two links max, in sentence form. Example shape (rewrite the
  specifics each time, do not reuse this verbatim):
  "I'm Kanchan, building StudeQ, an AI study platform, mostly solo. I write about what
  breaks along the way. More of this on [my blog](https://kanchannath.hashnode.dev) or
  find me on [X](https://x.com/KanchanNathDev) if you want to talk shop."
- **LinkedIn personal vs company**: link personal profile when the sentence is about
  Kanchan as a developer, link the company page when the sentence is specifically about
  StudeQ as a product.
- **Instagram** is the lowest priority link, only include it if the post has a visual
  or behind the scenes angle (design decisions, UI screenshots, build in public content).
  Skip it on purely technical deep dives.
- If the user provides a different set of links for a specific post, use those instead
  and apply the same placement rules.

## SEO Rules

Apply all of these. If the user also has the `/seo` skill available and shares frontend
code alongside the blog request, that skill covers code level SEO — this skill covers the
content itself.

**Keyword and search intent**
- Identify the primary keyword: the exact phrase someone would type into Google to find
  this post. Work it into the title, the first 100 words, at least one H2, and the meta
  description.
- Identify 2 to 3 related (LSI) terms and use them naturally through the body. Never force
  a keyword into a sentence where it does not fit grammatically.
- Match search intent. If the phrase implies "how to", the post needs clear numbered or
  sequential steps somewhere. If it implies "why", lead with the explanation, not the fix.

**Title and meta**
- Title: 50 to 60 characters, primary keyword near the front, no clickbait.
- Meta description: 140 to 160 characters, includes the primary keyword, states the
  concrete outcome the reader gets. Write this as the actual last line before the post
  body, labeled `Meta description:` so the user can paste it into Hashnode's SEO field.
- Suggested slug: lowercase, hyphenless is not required here since slugs use hyphens by
  convention and that is a URL, not prose — keep the slug short and keyword matching, e.g.
  `debounce-search-input-react`.

**Structure for ranking**
- One H1 (the title). Everything else H2/H3, properly nested, no skipped levels.
- Every H2 should be a phrase someone might search on its own, this is what wins featured
  snippets.
- Short paragraphs, 2 to 4 sentences. Big walls of text hurt both readability and dwell time.
- Code blocks always tagged with the language for proper syntax highlighting.
- Add a short FAQ section (2 to 4 questions) near the end if the topic has common follow up
  questions people search separately, this is a strong snippet target on Hashnode/Google.

**Tags and metadata for Hashnode**
- Suggest 3 to 5 Hashnode tags at the very end of the output, most specific first
  (e.g. `react`, `javascript`, `webdev`, `performance`, `hooks`).
- Suggest a cover image alt text line if the post would benefit from one.
- If this post is a cross post from `kanchannath.hashnode.dev` or vice versa, remind the
  user in one line to set the canonical URL in Hashnode settings, do not fake a canonical
  tag in the markdown itself.

**Things that hurt SEO, avoid these**
- Keyword stuffing, repeating the exact phrase unnaturally.
- Duplicate content, near identical paragraphs reworded from the same post.
- Thin content, a post under about 800 words rarely ranks against dedicated competitors
  unless the query is extremely narrow.
- Walls of code with zero surrounding explanation, this reads as thin content even when
  it's technically long.

## Handling Different Inputs

**Topic only** — write the full post from scratch following the structure above. Pick a
sensible primary keyword yourself and state it in one line before the post if it's not
obvious from the topic.

**Code or a code file** — read the code, understand what it actually does and why it's
structured that way, then write the post explaining the concept the code demonstrates.
Do not just paste the code with a caption. Explain the reasoning: what breaks without this,
what tradeoff was made, what the alternative approaches looked like.

**Markdown draft** — treat it as a first pass. Rewrite for voice (see Voice Rules), restructure
for SEO if headers are missing or misordered, tighten anything that reads like filler,
and flag in one line at the top what was changed and why, then give the full rewritten post.

## Output Format

- Output only the final markdown blog post. No preamble like "here's your blog post".
- Structure: Title as H1, full post body, then `Meta description:` line, then `Suggested
  tags:` line, then `Suggested slug:` line if relevant.
- Do not include an actual `<!-- canonical -->` HTML comment or frontmatter block, Hashnode
  handles that through its own settings UI, not through markdown.
- If code is included, always use fenced code blocks with the correct language identifier.
