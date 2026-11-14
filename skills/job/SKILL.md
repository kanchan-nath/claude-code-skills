---
name: job
description: Write outreach messages to recruiters/hiring managers when Kanchan is applying for a job, and answer job application questions, using Kanchan's resume and the job details he provides. Style is simple, respectful, down-to-earth English, no fancy words, no AI-sounding phrases, no exaggeration. Trigger whenever Kanchan shares a job posting/JD along with his resume and asks to write a message to a recruiter, an outreach note for a job, a LinkedIn message about a job opening, a cold email applying for a position, or gives application form questions (like "why this role", "why should we hire you", "tell us about yourself") that need answers. Also trigger on phrases like "write outreach for this job", "message this recruiter", "help me apply for X position", "/job", or when Kanchan gives job details + resume + platform (LinkedIn/email/application questions) and expects a ready-to-send message or answer back.
---

# Job Application Outreach Writer

Writes outreach messages from Kanchan to recruiters/hiring managers when applying for a job, and answers job application form questions — using the job details and resume Kanchan provides.

This is a sister skill to `outreach`, but for job applications specifically (talking to a recruiter about a role), not general cold outreach (asking someone to review StudeQ).

## Before drafting, check you know

- **Job details**: position/title, company, and platform where Kanchan found it or is applying (LinkedIn, email, company site, etc).
- **Resume**: Kanchan's actual background — pull only real facts from what he shares (his resume text/file, or a summary he gives in chat). Never invent job titles, years of experience, skills, or companies.
- **Platform**: LinkedIn (connection note / InMail / DM to recruiter), Email (cold email applying), or Application questions (a set of questions from a job form that need written answers).

If platform is not stated, ask ONE short question. If job details or resume are missing, ask for them — do not draft a job outreach message without knowing what job it's for and who is applying.

## Voice rules — always follow

- Simple, respectful, down-to-earth English. Formal but plain words only.
- No AI-sounding phrases. Banned: "I hope this message finds you well", "I am excited to apply", "I would be a great fit", "passionate about", "dynamic", "synergy", "leverage", "reach out" (say "message" or "contact"), "circle back", "touch base", "team player", "go-getter", "results-driven".
- No exclamation marks. No emojis.
- Short sentences, one idea per sentence.
- Generic over tailored by default: state that Kanchan is applying for the role and is interested, without stretching every resume line to match the job description. Only pull in a specific skill/project if Kanchan explicitly says to highlight it.
- Never exaggerate or invent experience. If resume is thin for the role, keep the message honest and simple — do not oversell.
- Mention resume as attached/linked (do not paste the full resume text into the message body).
- Respectful tone throughout — recruiter is being asked for their time, not doing Kanchan a favor to be guilted into.
- End with a no-pressure, polite close.

## Universal structure for outreach messages (4 parts)

1. Who Kanchan is — 1 line (name, and one-line current context e.g. "solo developer" — only if relevant, do not force it).
2. The role and why messaging — 1 line (which position, where he found it/applying).
3. Resume mention — 1 line (attached/linked, available on request).
4. Polite, no-pressure close — 1 line.

## Platform variants

### LinkedIn — connection request note (to recruiter)
Max ~300 characters. Just enough to state interest in the role and reason to connect. No attachment possible here — mention resume can be shared once connected.

### LinkedIn — InMail / DM (to recruiter, after connecting or via InMail)
4–6 short lines. Slightly more detail than the connection note. Mention resume is attached or linked.

### Email — cold email applying for a role
- Subject line: plain, states the role and purpose. Example: "Application for [Position] — Kanchan Nath"
- Body: short paragraphs (2–4 lines each). Mention resume is attached. Sign-off with name.

### Application form questions
Recruiters/ATS forms often ask questions like "Why do you want to work here", "Why should we hire you", "Tell us about yourself", "What makes you a good fit". For these:
- Answer directly and honestly using only facts Kanchan has given about himself/StudeQ/his background.
- Same plain, non-AI voice — no buzzwords, no forced enthusiasm.
- Length: 2–5 sentences per answer unless the form specifies a word/character limit — ask if unclear and it matters.
- It is fine to mention StudeQ as a real project/proof of work where relevant to the question, but only when Kanchan indicates it's relevant to this role.

## Templates

### LinkedIn connection note
```
Hi [Recruiter Name], I saw the opening for [Position] at [Company] and wanted to connect. I am applying for the role and would like to share my profile with you.
```

### LinkedIn InMail / DM
```
Hi [Recruiter Name],

I am Kanchan. I saw the [Position] opening at [Company] and am applying for it.

[One honest line on relevant background, only if Kanchan gives specifics — otherwise skip.]

I have attached my resume here. Happy to share more details if useful.

Thank you for your time,
Kanchan
```

### Cold email
```
Subject: Application for [Position] — Kanchan Nath

Hi [Recruiter Name],

I am Kanchan, applying for the [Position] role at [Company].

I have attached my resume with this email. [One honest line on background, only if given — otherwise skip.]

Please let me know if you need anything else from my side.

Thank you,
Kanchan
```

### Application question answer (example shape, not fixed text)
```
[Direct answer in 2-5 plain sentences, using only facts Kanchan provided. No buzzwords, no filler opening line, no restating the question back before answering.]
```

## Workflow

1. Confirm you have: job details (position, company), resume/background facts, and platform. Ask ONE question if something key is missing.
2. If platform is "application questions", ask for the exact question text if not already given, and answer each one directly using the voice rules.
3. If platform is LinkedIn/Email, pick the matching template and fill in real details only — leave nothing invented.
4. Keep it generic/short by default. Only tailor to specific job requirements if Kanchan explicitly asks to highlight particular skills.
5. Run the checklist before returning the draft.

## Checklist before returning a draft

- [ ] No banned/AI-sounding phrases or buzzwords
- [ ] No invented experience, skills, or claims
- [ ] Resume mentioned as attached/linked, not pasted in full
- [ ] Length fits the platform
- [ ] Sounds like a real person applying, not AI-generated
- [ ] Respectful, no-pressure close
- [ ] For application-question answers: answers the actual question directly, no restating it first
