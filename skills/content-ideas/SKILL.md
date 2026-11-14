---
name: content-ideas
description: Turn a YouTube video (usually a research/informational video Kanchan watched) into individual, trackable content-idea rows inside his Notion "Content Ideas" database, instead of one row holding the whole transcript. Trigger this skill whenever Kanchan sends a YouTube link and asks to log it, pull content ideas from it, add it to his content ideas database, or invokes "/content-ideas". Also trigger if he says things like "I watched this video, there's stuff I want to make videos on later" or pastes a transcript/captions and asks for it to be broken into ideas. Covers: getting the transcript (with on-screen text/visual context, not just spoken audio), splitting it into distinct, usable content chunks, and writing each chunk as its own database row with title, source video, URL, timestamp, date added, status (Pending / Done / Already Made Video), a Content Potential rating (High/Medium/Low — how likely the topic is to attract views), category, summary, and why it could work. Target database: "Content Ideas" inside Kanchan's "The Rover Kanchan" Notion page (collection://4184ee2e-9d6c-81eb-ae84-000b94df91cd).
---

# Content Ideas — YouTube → Notion pipeline

## Why this exists
Kanchan watches informational YouTube videos for research. He often can't make a
video on what he learned right away (timing, backlog, etc.), and a month later
he's forgotten the specific points. This skill makes sure every useful point from
a watched video becomes its own durable, filterable row — not one row with a wall
of transcript text dumped in it.

## The database
Notion data source: `collection://4184ee2e-9d6c-81eb-ae84-000b94df91cd`
(page "Content Ideas", inside "The Rover Kanchan" page: `3ee4ee2e9d6c8099b128e20f41c79e51`)

Columns:
- **Idea Title** (title) — short, specific name for this ONE chunk/point (not the video title)
- **Source Video** (text) — the YouTube video's actual title
- **YouTube URL** (url) — the video link (keep the same link on every row from that video)
- **Timestamp** (text) — rough mm:ss or range where this point is made, if knowable
- **Date Added** (date) — today's date
- **Status** (status) — "Pending" (default), "Done" (he made the video), "Already Made Video" (he's already covered this topic before, so deprioritize/skip)
- **Content Potential** (select) — High / Medium / Low: your honest read of how likely this specific chunk is to attract viewers/engagement as its own video, not a rating of the source video
- **Category** (select) — pick the closest fit from his existing content pillars: AI & AI Tools · Making Money & Side Hustles · Business & Entrepreneurship · Career Development · College Life & Student Advice · Communication & Personality · Productivity & Self-Improvement · Tech & Gadgets Reviews · Lifestyle & Vlogging · Personal Finance · Grooming & Fashion · Trending Topics & News
- **Summary** (text) — 2-4 sentences: what this point actually says/teaches, in enough detail that Kanchan can remember it a month later without rewatching
- **Why It Could Work** (text) — 1-2 sentences: the hook/angle — why this specific point, not just the general topic, would make people watch

## Workflow

### Step 1 — Get the transcript AND on-screen context
Don't rely on spoken-word captions alone — informational videos often show text,
labels, numbers, tool names, or UI on screen that is never said out loud, and
auto-captions mangle names/jargon. So:

1. Try to pull the actual transcript/captions for the video.
2. Separately account for visually-shown information: tool names, website URLs,
   on-screen bullet points, numbers/stats shown in graphics, code/UI shown, etc.
   If you have no way to inspect video frames directly, say so plainly and ask
   Kanchan to paste anything important that's only shown on screen (e.g. a tool
   list, a slide of steps) rather than guessing at it.
3. If no transcript tool is available in this session (no connector that fetches
   YouTube captions/audio, and the URL isn't fetchable), don't fabricate a
   transcript. Tell Kanchan plainly, and ask him to paste the transcript text
   (YouTube → ⋯ → "Show transcript" → copy) and flag anything shown on-screen
   that he wants captured. Proceed once he provides it.

### Step 2 — Find the video's real title
Confirm the actual video title (from the page/search result, or ask) — this goes
in "Source Video" on every row, not the raw URL.

### Step 3 — Chunk it, don't dump it
Read through the transcript and split it into the distinct, separable points/
sections a viewer would actually come away with — the things Kanchan could make
a standalone Short or video on. Rules of thumb:
- One row per *idea*, not per sentence and not per video. A 15-minute video
  might yield 4-10 rows.
- Merge sentences that are really one point; split sentences that smuggle in
  two different ideas.
- Skip filler (intros, sponsor reads, "like and subscribe", repeated recaps)
  unless the filler itself contains a usable point.
- Write the Idea Title and Summary in Kanchan's own words (paraphrase), not
  quoted/copied transcript text.

### Step 4 — Rate each chunk
For each chunk, decide:
- **Category** — best-fit pillar from the list above.
- **Content Potential** — High/Medium/Low, based on how fresh/specific/
  actionable the point is and whether it's the kind of thing that performs
  well in his niche (practical, surprising, or money/career-relevant beats
  generic advice).
- **Status** — default "Pending" unless Kanchan says he's already made a video
  covering that exact point (then "Already Made Video").

### Step 5 — Write the rows
Create one Notion page per chunk in the data source above via
`notion-create-pages`, with `parent: {"type":"data_source_id","data_source_id":"collection://4184ee2e-9d6c-81eb-ae84-000b94df91cd"}`.
Set Date Added to today via `"date:Date Added:start"`.
Batch all chunks from one video into a single `notion-create-pages` call
(multiple entries in `pages`).

### Step 6 — Report back
After writing, give Kanchan a short list of the chunk titles you created (not
the full summaries again) and the Notion link, so he can see at a glance what
got captured from that video.

## Notes
- If Kanchan sends multiple video links in one message, process them one video
  at a time, still batching each video's rows into one create call.
- If a chunk clearly duplicates a topic he's covered before (he's mentioned it
  in conversation or it's an obvious repeat), still log it but set Status to
  "Already Made Video" and say why.
