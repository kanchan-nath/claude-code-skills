---
name: referral
description: Generates click-worthy referral promotion content - a LinkedIn post (hook, story, hashtags, and a follow-me CTA) plus a matching WhatsApp forward message that links to that post. Use this any time the user wants to promote a referral link, invite code, referral program, waitlist link, or any link they want people to click and share. Trigger on words like "referral", "refer a friend", "invite link", "referral code", or "write a post to promote this link" - even if the user only pastes a bare link with no other context, still use this skill to build the full package around it.
---

# Referral Content Skill

Turns raw referral information into a ready-to-post LinkedIn post and a companion WhatsApp forward message, both built to get clicks.

## What this produces, every time

1. A LinkedIn post
2. A WhatsApp forward message that links to that post
3. Baked into the LinkedIn post: a follow-me CTA line and hashtags

## Step 1: Gather the referral details

Pull from what the user gave you:

- **What's being referred** - product/platform/course/job/program name
- **The link** - use it exactly as given; if it's not ready yet, insert `[YOUR LINK]` as a placeholder and flag that it needs to be dropped in before posting
- **The hook for the reader** - what's in it for someone who clicks: discount, free credits, cash bonus, early access, a job opening, etc.
- **Why the user is personally sharing it** - their real experience, result, or reason. This is the single most important ingredient - without it the post reads like an ad and gets scrolled past
- **Urgency or deadline** (optional) - gives people a reason to act now instead of scrolling on

If "what's being referred" or "why they're sharing it" is missing, ask ONE direct question to fill the biggest gap. For everything else, make a sensible assumption and note it in a single line rather than stalling on more questions.

## Step 2: Write the LinkedIn post

Build it in this order:

1. **Hook - first 2 lines.** LinkedIn truncates posts after ~3 lines on mobile behind a "...more" tap, so these two lines have one job: earn the tap. Use a specific number/result, a bold claim, or a direct question. Skip generic openers like "Excited to share..." - they get scrolled past instantly.
2. **The story, in short lines.** 3-5 short lines (1-2 sentences each), with real line breaks between them - LinkedIn's feed rewards white space over dense paragraphs. This is the "why I'm sharing this" from Step 1, told specifically, not like ad copy.
3. **The offer, as 3-5 bullets.** Plain and scannable: what it is, who it's for, what they get out of clicking.
4. **The click mechanism - never paste the raw link in the post body.** LinkedIn's algorithm suppresses reach on posts with outbound links sitting in the body text. Use one of:
   - "Link's in the first comment" - then the user posts the link as their own first comment the moment they publish
   - "Comment '[keyword]' and I'll send you the link" - trades a click for a comment, which feeds the algorithm more signal than a link click would anyway
   Default to the first option unless the user says they'd rather do the comment-bait version.
5. **Follow-me CTA - one line, right before the hashtags.** Something like: "Following me means you won't miss the next one - I post about [their content topic] regularly." Tie it to what the user actually posts about when that's known; otherwise keep it general to "opportunities/updates like this."
6. **Hashtags - 5 to 8, on their own line at the very end.** Mix broad tags (e.g. #OpenSource, #WebDevelopment) with ones specific to the referral's actual topic. Don't reuse an identical hashtag set across every post - pull from what this particular referral is about.

Write the post in normal sentence case with standard capitalization and punctuation, even if the user's own everyday texting style is casual/lowercase - LinkedIn is the one channel where that polish reads as credible.

## Step 3: Write the WhatsApp forward message

This is not the LinkedIn post copy-pasted - a wall of text feels spammy on WhatsApp and gets skipped. Instead:

- 3-4 short lines, max
- Opens like a message to a friend, not a broadcast
- States what it is and why it's worth 30 seconds, in one line
- Includes the LinkedIn post URL - use `[LINKEDIN POST URL]` as a placeholder if the post isn't live yet
- Closes with a small, specific ask: check it out, and - if they're willing - like or comment on the post itself. Early engagement like that is what pushes a LinkedIn post into more feeds during its first hour
- Emojis are fine, used sparingly. Skip hashtags entirely - nobody uses them on WhatsApp

## Worked example

Given: referring people to a beta waitlist for acadiq.ai, an AI study platform. Hook: early access, and a shoutout for the first 50 sign-ups. Personal reason: built it themselves as a BTech student who needed it.

**LinkedIn post:**

I built the thing I wish existed during my last 3 semesters.

Every exam season I'd lose hours just organizing scattered notes before I could even start studying. So over the last few months I built acadiq.ai - an AI study platform that handles that part for you.

Beta's opening up now, and I'm looking for the first batch of students to try it and break it before the public launch.

What you get:
- Early access before public launch
- A direct line to me for feature requests - I'm actively building this
- First 50 sign-ups get a shoutout in the launch post

Link's in the first comment - jump in if you want a study tool built by someone who's actually been in your shoes.

Following me means you won't miss when it opens up wider - I post about building this in public every week.

#buildinpublic #EdTech #AIforEducation #StudentLife #OpenSource #MERNstack #IndieHackers

**WhatsApp message:**

hey! i built an AI study tool (acadiq.ai) and just opened up early access on linkedin - first 50 people get a shoutout too
[LINKEDIN POST URL]
would mean a lot if you could check it out, and a like/comment there helps more than you'd think

## Notes

- Never fabricate stats, testimonials, or urgency that wasn't given (e.g. "only 3 spots left!") - it undermines trust and is the fastest way to make a referral post feel fake.
- If the user gives a genuinely different context each time (a job referral vs. a product waitlist vs. an open-source contribution call), reuse the structure above but let the specific details change the tone - a job referral leans more formal, a product waitlist can be more personal/story-driven.
