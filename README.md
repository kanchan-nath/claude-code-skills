# Claude Code & Agent Skills 🧠⚡

[![Skills Count](https://img.shields.io/badge/Skills-14%20Available-blue.svg)](skills.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Compatible](https://img.shields.io/badge/Compatible-Claude%20Code%20%7C%20Antigravity%20%7C%20Cursor%20%7C%20OpenHands-orange.svg)](#)
[![Validation](https://github.com/kanchan-nath/claude-code-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/kanchan-nath/claude-code-skills/actions)

A curated, production-ready repository of modular AI agent skills for **Claude Code**, **Google Antigravity**, **Cursor**, **OpenHands**, and other agentic developer tools.

Each skill is self-contained with standardized YAML frontmatter, execution workflows, references, and helper scripts.

---

## 🤖 How to Install Skills with Any AI Agent

Whenever you want an AI agent (Claude Code, Antigravity, Cursor, etc.) to install a skill from this repository, simply paste this prompt:

```text
Please read the repository at https://github.com/kanchan-nath/claude-code-skills
and install the '<skill-name>' skill into my agent skills directory.
```

The agent will read [`skills.json`](skills.json) or [`skills/<skill-name>/SKILL.md`](skills/) directly and install it into your local environment.

---

## ⚡ Quick 1-Command CLI Install

Run directly from your terminal:

```bash
# Install a single skill for Claude Code (~/.claude/skills/)
curl -fsSL https://raw.githubusercontent.com/kanchan-nath/claude-code-skills/main/install.sh | bash -s <skill-name>

# Install a skill for Google Antigravity (~/.gemini/config/skills/)
curl -fsSL https://raw.githubusercontent.com/kanchan-nath/claude-code-skills/main/install.sh | bash -s <skill-name> --target antigravity

# Install all skills at once
curl -fsSL https://raw.githubusercontent.com/kanchan-nath/claude-code-skills/main/install.sh | bash -s -- --all

# List available skills
curl -fsSL https://raw.githubusercontent.com/kanchan-nath/claude-code-skills/main/install.sh | bash -s -- --list
```

---

## 📦 Skills Directory

| Skill Name | Category | Primary Triggers & Commands | Description |
|---|---|---|---|
| [`cold-email`](skills/cold-email/SKILL.md) | Outreach | `"cold email"`, `"outreach email"`, `"style this email"` | Builds visually styled HTML cold-outreach emails with vector branding, CTA buttons, and plain-text fallback. |
| [`content-ideas`](skills/content-ideas/SKILL.md) | Content & Media | `/content-ideas`, `"pull content ideas"`, YouTube links | Extracts distinct, actionable content ideas from YouTube videos and formats them for a Notion tracking database. |
| [`create-linkedin-post`](skills/create-linkedin-post/SKILL.md) | Social Publishing | `"create a LinkedIn post"`, `"write a post for LinkedIn"` | End-to-end LinkedIn post workflow: humanized draft, AI vs human review, image/carousel generation, and scheduling. |
| [`dsa`](skills/dsa/SKILL.md) | Software Development | `/dsa`, LeetCode links, `"help me solve this dsa"` | DSA & LeetCode micro-step coach that guides you through problem-solving step by step without spoiling the solution. |
| [`hashnode`](skills/hashnode/SKILL.md) | Technical Writing | `/hashnode`, `"write a blog on X"`, `"turn this code into a blog"` | Long-form technical blog posts for Hashnode optimized for search rankings, retention, and readability. |
| [`job`](skills/job/SKILL.md) | Career & Jobs | `/job`, `"write outreach for this job"`, application questions | Recruiter outreach messages and tailored job application answers in down-to-earth, natural English. |
| [`linkedin-humanizer`](skills/linkedin-humanizer/SKILL.md) | Content & Review | `"humanize"`, `"sounds like AI"`, `"remove AI slop"` | De-slops LinkedIn drafts against a 5-check detection panel and runs a strict editor review loop. |
| [`linkedin-orchestrator`](skills/linkedin-orchestrator/SKILL.md) | Social Publishing | `"post to linkedin"`, `"linkedin orchestrator"` | Automates LinkedIn API authentication, draft verification, linter scoring (100/100 SHIP), and publishing. |
| [`linkedin-post-image`](skills/linkedin-post-image/SKILL.md) | Media Design | `"post image"`, `"carousel design"`, `"visual asset"` | Generates styled image templates and visual assets for high-performing LinkedIn posts and carousels. |
| [`motion-prompt-director`](skills/motion-prompt-director/SKILL.md) | AI Video & Motion | `"write a Flow prompt"`, `"storyboard this"`, `"motion prompt"` | Production-ready prompt pack for AI video and motion graphics (Google Flow, Runway, Kling, Sora, Luma, Pika). |
| [`referral`](skills/referral/SKILL.md) | Career & Outreach | `"referral"`, `"refer a friend"`, `"invite link"` | Click-worthy referral promotion packages: LinkedIn post + companion WhatsApp forward message. |
| [`seo`](skills/seo/SKILL.md) | Web Development | `/seo`, `"seo review"`, `"audit this file for seo"` | Technical SEO auditor for frontend files (Next.js, HTML) and full repository audits with prioritized fixes. |
| [`shorts-script-writer`](skills/shorts-script-writer/SKILL.md) | Video & Scriptwriting | `"shorts script"`, `"reels script"`, `"under 60s"` | Transforms rough notes and bullet points into high-hook, natural spoken scripts for YouTube Shorts & Reels (<60s). |
| [`sparke-codestyle`](skills/sparke-codestyle/SKILL.md) | Backend Architecture | `"sparke codestyle"`, backend code reviews | Backend codestyle and architectural standard enforcement (Express, Zod, BullMQ, Mongoose, Prisma). |

---

## 📂 Repository Layout

```text
claude-code-skills/
├── .github/
│   └── workflows/
│       └── validate-skills.yml    # CI frontmatter & schema validator
├── skills/
│   ├── cold-email/
│   │   └── SKILL.md
│   ├── content-ideas/
│   │   └── SKILL.md
│   ├── create-linkedin-post/
│   │   ├── SKILL.md
│   │   ├── assets/
│   │   ├── references/
│   │   └── scripts/
│   ├── ... (each skill in its own directory)
│   └── sparke-codestyle/
│       └── SKILL.md
├── install.sh                     # Posix CLI installer
├── skills.json                    # Machine-readable registry for agents
├── LICENSE                        # MIT License
└── README.md                      # Documentation & Catalog
```

---

## 🛠 Manual Installation Paths

You can also install any skill manually by copying its directory from `skills/<skill-name>`:

| Tool | Installation Directory |
|---|---|
| **Claude Code** (Global) | `~/.claude/skills/<skill-name>/` |
| **Claude Code** (Project) | `./.claude/skills/<skill-name>/` |
| **Google Antigravity** (Global) | `~/.gemini/config/skills/<skill-name>/` |
| **Google Antigravity** (Workspace) | `./.gemini/skills/<skill-name>/` |
| **Cursor / Windsurf / Codex** | `./.skills/<skill-name>/` |

---

## ➕ Adding a New Skill

1. Create a folder in `skills/<new-skill-name>/`.
2. Add a `SKILL.md` with valid YAML frontmatter:
   ```yaml
   ---
   name: new-skill-name
   description: Clear trigger conditions and instructions for the agent.
   ---

   # Skill Title
   Instructions go here...
   ```
3. Run `python3 -c "import json; ..."` or update [`skills.json`](skills.json).
4. Commit and push to GitHub.

---

## 📄 License

[MIT](LICENSE) © [Kanchan Nath](https://github.com/kanchan-nath)
