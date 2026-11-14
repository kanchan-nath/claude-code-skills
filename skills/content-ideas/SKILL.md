---
name: content-ideas
description: Turn a video transcript (pasted text or an uploaded .txt file — with or without timestamps, no YouTube URL required) into individual, trackable content-idea rows inside Kanchan's Notion "Content Ideas" database, instead of one row holding the whole transcript. Trigger this skill whenever Kanchan pastes or uploads a transcript and asks to log it, pull content ideas from it, add it to his content ideas database, or invokes "/content-ideas". Also trigger if he sends a YouTube link alone (then ask him to paste/upload the transcript, since no transcript tool is assumed connected). Covers: splitting the transcript into distinct, usable content chunks and writing each as its own database row with title, source video, YouTube URL (if known), timestamp (if present in the transcript), date added, status (Pending / Done / Already Made Video), a Content Potential rating (High/Medium/Low), category, summary, and why it could work. Target database: "Content Ideas" inside Kanchan's "The Rover Kanchan" Notion page (collection://4184ee2e-9d6c-81eb-ae84-000b94df91cd).
---

# Content Ideas — Transcript → Notion pipeline

## Why this exists
Kanchan watches informational YouTube videos for research. He often can't make a
video on what he learned right away, and a month later he's forgotten the
specific points. This skill makes sure every useful point from a watched video
becomes its own durable, filterable row — not one row with a wall of transcript
text dumped in it.

## How input arrives (read this first)
Kanchan sends the **transcript itself** — pasted as text, or as an uploaded
`.txt` (or similar) file. He is not expected to provide a YouTube URL, and no
YouTube-transcript tool is assumed to be connected in this session.

- If only a YouTube link shows up with no transcript attached or pasted, ask
  him to paste the transcript or upload the `.txt` file. Don't try to fetch the
  video yourself unless a transcript/caption tool is actually available and
  connected in this session — check your tool list before assuming one isn't.
- Timestamps may or may not be present in what he sends:
  - If timestamps ARE in the transcript, use them for the **Timestamp** column
    on each row (rough mm:ss or a range is fine).
  - If timestamps are NOT present, leave **Timestamp** blank — don't guess or
    estimate one.
- The transcript is spoken-word only. It won't capture on-screen-only text
  (tool names, slide bullet points, numbers shown in a graphic, UI shown, etc.).
  If the content clearly depends on something that was likely shown on screen
  but isn't in the words (e.g. "as you can see right here", "look at this"),
  note that gap in the Summary rather than guessing what was shown, and you can
  ask Kanchan to fill it in if it matters for a given chunk.

## Getting the video title and URL
These aren't always available from a transcript alone:
- **Source Video** (the title): if Kanchan names it, use that. If not, and a
  filename or pasted header gives a clear title, use that. Otherwise, make
  your best reasonable label from the content and say plainly that you're
  guessing the title since none was given — don't present a guess as fact.
- **YouTube URL**: only fill this in if Kanchan actually gives you the link.
  Leave it blank rather than inventing or guessing one. It's fine to log ideas
  with no URL at all.

## The database
Notion data source: `collection://4184ee2e-9d6c-81eb-ae84-000b94df91cd`
(page "Content Ideas", inside "The Rover Kanchan" page: `3ee4ee2e9d6c8099b128e20f41c79e51`)

Columns:
- **Idea Title** (title) — short, specific name for this ONE chunk/point (not the video title)
- **Source Video** (text) — the video's title (see above)
- **YouTube URL** (url) — only if given; otherwise leave blank
- **Timestamp** (text) — only if present in the transcript; otherwise blank
- **Date Added** (date) — today's date
- **Status** (status) — "Pending" (default), "Done" (he made the video), "Already Made Video" (he's already covered this exact point before, so deprioritize)
- **Content Potential** (select) — High / Medium / Low: your honest read of how likely this specific chunk is to attract viewers/engagement as its own video — not a rating of the source video as a whole
- **Category** (select) — pick the closest fit from his existing content pillars: AI & AI Tools · Making Money & Side Hustles · Business & Entrepreneurship · Career Development · College Life & Student Advice · Communication & Personality · Productivity & Self-Improvement · Tech & Gadgets Reviews · Lifestyle & Vlogging · Personal Finance · Grooming & Fashion · Trending Topics & News
- **Summary** (text) — 2-4 sentences: what this point actually says/teaches, in enough detail that Kanchan can remember it a month later without rewatching
- **Why It Could Work** (text) — 1-2 sentences: the hook/angle — why this specific point, not just the general topic, would make people watch

## Workflow

### Step 1 — Read the transcript
Read the whole thing before chunking (don't work section-by-section from the
start) so you understand the full arc and don't split a point that gets
finished later, or miss a callback.

### Step 2 — Chunk it, don't dump it
Split into the distinct, separable points/sections a viewer would actually
come away with — the things Kanchan could make a standalone Short or video on.
- One row per *idea*, not per sentence and not per video. A 10-20 minute video
  typically yields somewhere around 5-25 rows depending on density — let the
  content decide the count, don't force a round number.
- Merge sentences that are really one point; split sentences that smuggle in
  two different ideas.
- Skip filler (intros, sponsor/ad reads, "like and subscribe", repeated
  recaps) unless the filler itself contains a usable point.
- Write the Idea Title and Summary in Kanchan's own words (paraphrase the
  transcript — never copy sentences verbatim into the database).

### Step 3 — Rate each chunk
For each chunk, decide:
- **Category** — best-fit pillar from the list above.
- **Content Potential** — High/Medium/Low, based on how fresh/specific/
  actionable the point is and whether it's the kind of thing that performs
  well in his niche (practical, surprising, or money/career-relevant beats
  generic advice).
- **Status** — default "Pending" unless Kanchan says he's already made a video
  covering that exact point (then "Already Made Video").

### Step 4 — Write the rows
Create one Notion page per chunk in the data source above via
`notion-create-pages`, with
`parent: {"type":"data_source_id","data_source_id":"collection://4184ee2e-9d6c-81eb-ae84-000b94df91cd"}`.
Set Date Added to today via `"date:Date Added:start"`.
Batch all chunks from one transcript into a single `notion-create-pages` call
(multiple entries in `pages`). Omit YouTube URL and Timestamp properties
entirely for rows where that info isn't available, rather than writing an
empty placeholder string.

### Step 5 — Report back
After writing, give Kanchan a short list of the chunk titles you created (not
the full summaries again) and the Notion link, so he can see at a glance what
got captured.

## Notes
- If Kanchan sends multiple transcripts in one message, process them one at a
  time, still batching each one's rows into its own create call.
- If a chunk clearly duplicates a topic he's covered before (he's mentioned it
  in conversation, or it's an obvious repeat of something already in the
  database), still log it but set Status to "Already Made Video" and say why.
- Never reproduce long verbatim passages from the source transcript, in the
  database or in chat — always paraphrase into Kanchan's own working notes.
