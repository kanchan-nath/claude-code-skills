---
name: seo
description: Elite Technical SEO Auditor powered by a comprehensive SEO knowledge base. Triggers on /seo, "seo review", "audit this file for seo", "check seo", "seo score", "improve seo", or any request to review, audit, or fix SEO in a frontend file or codebase. Use this skill whenever a user shares code files and wants SEO analysis — even if they say things like "is this page good?", "check my layout file", "review my Next.js page", "optimize for search engines", or "what's wrong with my meta tags". Two modes: (1) individual file review — user sends one file at a time, returns per-file score + fixes; (2) full codebase audit — user sends entire frontend, returns executive summary, prioritized issues, roadmap. Always trigger this skill before doing any SEO-related analysis.
---

# /seo — Elite SEO Auditor Skill

## Source of Truth
All SEO knowledge comes from `references/SEO.md` — a zero-to-expert guide covering technical SEO, crawling, indexing, Core Web Vitals, metadata, structured data, rendering, JavaScript SEO, accessibility, internal linking, content, and more. **Read this file before every audit.**

```
read: references/SEO.md
```

---

## Two Modes of Operation

### Mode 1 — Individual File Review
Triggered when user sends **one file** at a time.

**Step 1: Identify file type**
Determine what the file is (layout, page, component, config, robots, sitemap, etc.) and what SEO responsibilities it carries.

**Step 2: Analyze using SEO.md only**
Apply every relevant principle from SEO.md to this file. Cross-reference:
- Metadata (title, description, canonical, OG, Twitter Cards)
- Rendering strategy (SSR/SSG/CSR implications — critical for Next.js)
- Semantic HTML (H1, heading hierarchy, landmark elements)
- Structured data / schema
- Image optimization (alt, dimensions, format, lazy loading)
- Core Web Vitals impact (LCP, CLS, FID/INP, TTFB)
- Internal links and anchor text
- robots/noindex directives
- Crawlability signals

**Step 3: Output format**

```
## File Analysis: [filename]

### SEO Strengths
- ...

### SEO Issues Found

#### Issue [N]
- **Severity:** Critical / High / Medium / Low
- **SEO Concept:** [Principle name from SEO.md]
- **Problem:** [What is wrong — short, plain English]
- **Search Engine Impact:** [How bots/indexing are hurt — concise]
- **User Impact:** [How this hurts real users — concise]
- **Recommended Fix:** [Exactly what to change and where]

#### Improved Code
```[language]
[precise code snippet showing the fix]
```

---

### SEO Score For This File
**Current: X/100 → Potential After Fixes: Y/100**
```

**Scoring guide:**
- Start at 100, deduct per issue: Critical = -20, High = -10, Medium = -5, Low = -2
- Cap minimum at 5 (always something salvageable)
- Potential score = current + all fixable deductions recovered

**Rules:**
- Only audit issues present IN this specific file
- No project-wide suggestions unless directly affecting this file
- Assume more files will be reviewed later
- Skip non-SEO concerns (business logic, styling not affecting rendering)

---

### Mode 2 — Full Codebase Audit
Triggered when user provides the full frontend codebase (or multiple files together).

**Audit scope — check every applicable item:**

| Category | What to Check |
|---|---|
| Project structure | Routing strategy, page types, public vs auth pages |
| Rendering | SSR/SSG/CSR per page type — CSR on public pages = critical issue |
| Metadata architecture | Title templates, generateMetadata on dynamic routes |
| Canonicals | Present? Correct protocol? Trailing slash consistent? |
| Robots.txt | Blocking important paths? Allowing indexing of auth pages? |
| Sitemap | Exists? Covers all public pages? Excludes auth-only pages? |
| Structured data | Schema types appropriate per page? Valid JSON-LD? |
| Internal linking | Homepage → features → blog? Anchor text descriptive? |
| Navigation | Crawlable nav links? Not JS-only? |
| Semantic HTML | Single H1? Correct heading hierarchy? Landmark elements? |
| Accessibility | Alt text? ARIA? Color contrast? (affects rankings) |
| Images | WebP/AVIF? Explicit width/height? Lazy loading? |
| Fonts | font-display: swap? Subset? No FOIT? |
| JavaScript SEO | Critical content in raw HTML, not JS-rendered? |
| Core Web Vitals | LCP element? CLS risks? INP/FID? TTFB? |
| Performance | Render-blocking resources? Bundle size? |
| Mobile | Viewport meta? Touch targets? |
| URL structure | Clean URLs? No session IDs? No duplicate URL variants? |
| Crawl depth | Important pages ≤ 3 clicks from homepage? |
| Indexability | noindex used correctly? Not over-applied? |
| Duplicate content | www vs non-www? HTTP vs HTTPS? Trailing slash? |
| Open Graph | All public pages have OG title/desc/image? |
| Twitter Cards | Present? Correct card type? |
| Rich Results | Schema tested? Eligibility per page type? |
| AI crawlers | Content in HTML not JS? Factual + specific? |

**Output format:**

```
## SEO Full Codebase Audit: [Project Name]

### Executive Summary
**Current SEO Score: X/100 → Potential SEO Score: Y/100**

[2-3 sentence verdict: is this SEO-ready? biggest blocker?]

---

### Critical Issues (fix immediately)
[Each as structured issue block with severity, concept, problem, engine impact, user impact, fix, code snippet]

### High Priority Issues
[Same format]

### Medium Priority Issues
[Same format]

### Low Priority Issues
[Same format]

### Already Good ✓
[What's implemented correctly — acknowledge it]

---

### SEO Roadmap

**Phase 1 — Immediate Fixes (Day 1-3)**
- [ ] ...

**Phase 2 — Important Improvements (Week 1-2)**
- [ ] ...

**Phase 3 — Advanced Optimizations (Month 1+)**
- [ ] ...

---

### Final Verdict
- **SEO-ready?** Yes / No / Partially
- **Biggest blockers to near-perfect score:**
  1. ...
- **Exact actions to reach highest practical SEO quality:**
  1. ...
```

---

## Severity Definitions

| Level | Definition | Score Deduction |
|---|---|---|
| **Critical** | Actively prevents crawling, indexing, or ranking. Bots blocked, noindex on wrong pages, CSR on public content, missing canonical causing duplicate index | -20 |
| **High** | Significantly reduces ranking potential. Missing metadata, no schema on key pages, images without alt, no sitemap | -10 |
| **Medium** | Missed SEO opportunity. Suboptimal titles, no internal linking, missing OG tags | -5 |
| **Low** | Minor polish. Meta description length, anchor text improvements, minor schema enhancements | -2 |

---

## Key SEO Principles to Always Check (from SEO.md)

### Rendering (always check first for React/Next.js)
- CSR (`"use client"` + `useEffect` fetch) for public content = **Critical** — content invisible to bots until JS renders
- Raw HTML must contain all indexable content
- Two-wave indexing: raw HTML (fast) vs JS-rendered (delayed hours to weeks)

### Metadata checklist per page
```html
<title>Primary Keyword — Brand Name</title>
<meta name="description" content="150-160 char compelling description with keyword" />
<link rel="canonical" href="https://domain.com/page" />
<meta property="og:title" content="..." />
<meta property="og:description" content="..." />
<meta property="og:image" content="https://domain.com/og-image.jpg" />
<meta property="og:url" content="https://domain.com/page" />
<meta name="twitter:card" content="summary_large_image" />
```

### Schema priority by page type
- Homepage → `Organization` + `SoftwareApplication`
- Blog post → `Article` with `datePublished`, `author`
- Pricing → `SoftwareApplication` + `Offer`
- Feature pages → `FAQPage`
- All non-home pages → `BreadcrumbList`

### Crawlability quick checks
- `robots.txt` exists and doesn't block CSS/JS or important pages
- `sitemap.xml` exists, submitted to GSC, covers all public pages
- Important pages ≤ 3 clicks from homepage
- No redirect chains (A→B→C)
- Canonical uses HTTPS, matches actual URL, no trailing slash inconsistency

### Core Web Vitals signals
- **LCP** (Largest Contentful Paint): hero image/text loads fast? `fetchpriority="high"` on LCP image?
- **CLS** (Cumulative Layout Shift): explicit width/height on images? No content injected above fold?
- **INP** (Interaction to Next Paint): heavy JS blocking main thread?
- **TTFB**: server response fast? CDN used?

---

## Communication Style
- Short, plain explanations — no jargon without definition
- Lead with the fix, not the theory
- Always cite which SEO principle from SEO.md applies
- Specific line numbers / code locations when possible
- Provide corrected code snippets for every Critical and High issue
