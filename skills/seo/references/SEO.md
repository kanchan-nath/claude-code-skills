# SEO MASTERCLASS: ZERO → EXPERT
*For SaaS developers. Technical depth. No fluff.*

---

## PART 1: WHAT SEO ACTUALLY IS

### Simple definition
SEO = Search Engine Optimization. Make website appear higher in search results for relevant queries. Higher rank = more free traffic = more users.

### Why search engines exist
People want information fast. Web has billions of pages. Search engines index everything, match queries to best pages, return results in milliseconds. Without them, web is unusable.

### Why Google ranks pages
Google business = ads. Ad revenue only flows if people use Google. People use Google only if results are good. So Google *must* rank best pages to survive commercially. This alignment is what makes SEO honest — Google wants to rank your page if your page is genuinely best.

### How search engines make money
```
User searches → sees organic results + ads above/alongside
→ clicks ad → advertiser pays Google per click
→ more searches = more ad impressions = more revenue
```
Google earned ~$175B in ad revenue (2023). Every dollar depends on search quality. This is why they fight spam hard.

### Why some pages rank, others don't
Pages rank when:
- Relevant to query (semantically, not just keyword match)
- Trusted by Google (backlinks from authoritative sites)
- Technically accessible to bots
- Better than competitors on 200+ ranking signals

Pages fail when:
- Blocked by robots.txt or noindex
- No backlinks → no authority
- Slow → poor page experience
- Thin/duplicate content
- Wrong intent match

### Real purpose of SEO
Not trick Google. Make site genuinely best answer for target queries, then *signal that clearly* to bots. SEO = quality + discoverability.

---

### Three perspectives

**User perspective:**
Types query, wants best answer fast. Clicks result #1–3 (CTR drops sharply after #3). Ignores page 2 almost entirely. Bounces back immediately if page doesn't answer question → Google notes this → page drops.

**Google perspective:**
Must return best result in <200ms. Uses ML models, 200+ signals, real user data to judge quality. Wants user to *not* bounce back — bounce = failed result. Every algorithm update targets pages that rank without deserving to.

**Website owner perspective:**
Organic search = free, compounding traffic. Unlike paid ads, SEO traffic doesn't stop when budget ends. A page ranked #1 for a 10,000/month keyword can drive traffic for years. Building SEO early = compounding advantage.

---

## PART 2: HOW SEARCH ENGINES WORK INTERNALLY

### CRAWLING

#### What is a crawler?
Bot program that visits webpages, reads HTML, follows links, sends content back to Google servers. Runs continuously across billions of URLs.

**Googlebot** = Google's main crawler. Multiple types:
- `Googlebot` — desktop crawler
- `Googlebot-Mobile` — mobile crawler (primary, since 2019 mobile-first indexing)
- `Googlebot-Image` — images
- `AdsBot-Google` — ad landing pages

#### How bots discover websites
1. Start from known seed URLs (large set of known pages)
2. Crawl those pages, extract all `<a href>` links
3. Add discovered URLs to crawl queue
4. Process queue → discover more links → repeat forever

**Other discovery methods:**
- Sitemap.xml submission (most direct)
- Backlinks from already-indexed pages (strongest signal for new sites)
- Google Search Console URL inspection / submit

#### What happens when bot visits page
```
1. Bot picks URL from queue
2. DNS lookup → IP address of server
3. TCP handshake with server
4. HTTP GET /page HTTP/1.1
5. Server responds: 200 OK + HTML
6. Bot parses HTML
7. Extracts: all <a href>, images, text content, metadata
8. Schedules JS rendering (separate Chromium-based rendering queue)
9. Sends raw HTML + rendered DOM to indexing servers
10. Adds extracted URLs to crawl queue
```

**Response codes matter:**
- `200` → crawl + index
- `301` → follow redirect, pass link equity
- `302` → follow redirect, don't pass link equity permanently
- `404` → remove from index eventually
- `503` → retry later (don't remove yet)
- `noindex` header or meta → crawl but don't index

#### Crawl budget
Google won't crawl every page of every site infinitely. Each site gets allocation: how many pages Googlebot crawls per day. Large sites (ecommerce, SaaS with thousands of pages) must manage this.

**Crawl budget wasted by:**
- Infinite pagination generating unique URLs
- Session IDs in URLs (`?session=abc123` → unique URL per visitor)
- Faceted navigation creating millions of URL combinations
- Duplicate pages (www vs non-www, HTTP vs HTTPS)
- URLs with tracking params treated as unique pages
- Blocking CSS/JS → bot can't render → re-crawls trying to

**Small SaaS:** crawl budget not critical. Becomes relevant at ~10,000+ pages.

#### Crawl depth
Pages further from homepage = harder to reach = crawled less frequently.

```
Homepage → 1 click away → crawled daily
Homepage → Category → 2 clicks away → crawled weekly
Homepage → Category → Sub → Sub → 4 clicks away → maybe never
```

Rule: important pages ≤ 3 clicks from homepage.

#### Internal links
Links between your own pages. Bot follows these to:
1. Discover new pages
2. Pass authority (PageRank) between pages

Anchor text of internal links signals what linked page is about.

#### Complete crawling flow
```
Google Crawl Queue
      ↓
Bot picks URL
      ↓
Check robots.txt (cached) → Disallowed? Stop.
      ↓
DNS lookup → IP
      ↓
TCP connection to server
      ↓
HTTP GET /url
      ↓
Server returns HTML (200 OK)
      ↓
Bot parses HTML immediately
  ├── Extract links → add to queue
  ├── Extract text, metadata, images
  └── Send raw HTML to indexing pipeline
      ↓
Rendering queue (Chromium)
  ├── Execute JavaScript
  ├── Wait for DOM to settle
  └── Send rendered HTML to indexing pipeline
      ↓
Both versions (raw + rendered) → Indexing
```

**Key point:** Two-wave indexing. First: raw HTML (fast). Second: JS-rendered (delayed — hours to weeks). If content only visible after JS runs, it gets indexed later. This is why SSR/SSG matters.

---

### INDEXING

#### What indexing means
Storing + organizing crawled content so it can be retrieved in milliseconds during a search. Crawling = collect. Indexing = organize for retrieval.

#### Difference: crawling vs indexing
- **Crawling:** visiting page, downloading content
- **Indexing:** processing, understanding, storing that content in searchable format

A page can be crawled but not indexed (thin content, noindex tag, too many duplicate signals). A page cannot be indexed without being crawled.

#### How search engines store information
Google's index runs on custom infrastructure (Bigtable, Colossus file system, distributed across datacenters globally). At core: inverted index.

#### Inverted index
Standard index: document → words it contains.
Inverted index: word → documents containing it.

```
Standard:
doc_1 → ["flashcard", "study", "spaced", "repetition"]
doc_2 → ["quiz", "test", "study", "prep"]

Inverted:
"flashcard" → [doc_1, doc_47, doc_233]
"study"     → [doc_1, doc_2, doc_15, ...]
"spaced"    → [doc_1, doc_88, doc_412]
"repetition"→ [doc_1, doc_88, doc_99]
```

When user searches "spaced repetition flashcard":
→ Find intersection of all three term lists
→ `doc_1` appears in all → strong candidate

Also stored per entry: position in document, frequency, field (title vs body vs URL), surrounding words. This enables phrase matching, proximity scoring, field-weighted scoring.

#### Keyword extraction
1. Tokenize text ("studying" → "studying")
2. Normalize: lowercase, remove punctuation
3. Stem or lemmatize ("studying" → "study", "studies" → "study")
4. Remove stop words ("the", "a", "is" — optional in modern systems)
5. Index tokens with position + frequency
6. Calculate TF-IDF weight

**TF-IDF:**
```
TF (term frequency) = count("spaced repetition" in doc) / total words in doc
IDF (inverse doc frequency) = log(total docs / docs containing "spaced repetition")
TF-IDF = TF × IDF
```
High TF-IDF = word important to this specific document relative to whole corpus.

#### Semantic indexing
Old: exact keyword match only.
Modern: understand meaning, not just strings.

Google uses:
- **Word2Vec** — word embeddings (similar words have similar vectors)
- **BERT** — bidirectional transformer, understands context
- **MUM** — multimodal, understands across 75 languages + images

"Cheap flights NYC" and "affordable New York airfare" → same semantic meaning → both match flight-related queries even without shared keywords.

#### Entity recognition
Google extracts named entities: people, companies, products, places, concepts. Links them to Knowledge Graph (Google's database of real-world entities + relationships).

Example:
Page mentions: "Anki", "spaced repetition", "SM-2 algorithm", "Hermann Ebbinghaus"
→ Google recognizes entities, understands page is about flashcard learning methodology
→ Assigns topical category: EdTech > Memory Techniques > Spaced Repetition
→ This informs ranking for related queries even without exact keyword

#### Vector search
Content converted to high-dimensional embedding vector via neural network. Similar content = vectors close in vector space. Enables semantic matching.

```
Query: "best note-taking app"
Query vector: [0.23, -0.45, 0.12, ..., 0.89]  ← 768 dimensions

Page A: "top apps for taking notes" 
Page A vector: [0.21, -0.43, 0.14, ..., 0.91]  ← similar vector

Cosine similarity = 0.98 → strong match
Even though no shared keywords.
```

This is why your content doesn't need exact keywords anymore — semantic quality matters more.

#### AI-powered indexing
Google's MUM model reads your page and:
- Understands topic at deep conceptual level
- Identifies gaps in coverage vs other top-ranked pages
- Assesses quality vs competing pages
- Understands images + text together

Your content must be genuinely informative and complete. Keyword density is dead. Topical depth wins.

#### Complete indexing flow
```
Crawled HTML + Rendered HTML arrive at indexing servers
      ↓
Text extraction (strip HTML tags, extract content)
      ↓
Language detection
      ↓
Tokenization + normalization + stemming
      ↓
Entity extraction (NLP — Named Entity Recognition)
      ↓
Embedding generation (BERT/MUM → vector representation)
      ↓
Quality signals calculation:
  - PageRank (backlinks)
  - Content quality score
  - E-E-A-T signals
  - Page experience signals
      ↓
Inverted index update (keyword → document mapping)
      ↓
Vector index update (semantic search index)
      ↓
Knowledge Graph entity association
      ↓
Distributed across Google's global index (Bigtable/Colossus)
      ↓
Available for ranking in queries
```

---

### RANKING

#### What happens after user searches
Query enters ranking pipeline. Multiple ML models fire simultaneously. SERP returned in <200ms. Involves candidate retrieval from billions of documents → progressive filtering → final ranking.

#### Query understanding
Before any ranking, Google processes query:
1. Spell correction ("stuyd" → "study")
2. Query expansion (add synonyms: "cheap" → also "affordable", "low-cost")
3. Identify query type (navigational/informational/transactional)
4. Named entity recognition in query ("Anki" = specific software entity)
5. Language + script detection
6. Geolocation detection (local queries get local results)
7. Personalization (logged-in user's history, device type)
8. Freshness requirement detection (does this query need recent results?)

#### Search intent detection
4 types Google classifies every query into:

| Intent | Query Example | What user wants | Best page type |
|--------|--------------|-----------------|----------------|
| Informational | "what is spaced repetition" | Learn | Blog post, guide |
| Navigational | "Anki login" | Find specific site | Homepage/login page |
| Commercial investigation | "best flashcard apps 2024" | Compare before buying | Listicle, comparison |
| Transactional | "buy Anki subscription" | Purchase now | Pricing/product page |

Google won't rank blog post for transactional query. Won't rank pricing page for informational query. **Match your page type to intent.**

#### Ranking signals (200+)

Core signals:

**Relevance signals:**
- Semantic similarity of content to query
- Keyword presence in title, H1, body, URL
- Topical coverage (how many related subtopics covered)
- Content length + depth
- Recency (for time-sensitive queries)

**Authority signals:**
- PageRank (quality + quantity of backlinks)
- Domain authority
- Backlink anchor text diversity
- Links from topically relevant sites

**Trust signals:**
- HTTPS
- Known brand/entity
- Low spam score
- Privacy policy, contact info present
- Accuracy of information (fact-checking)

**User experience signals:**
- Core Web Vitals (LCP, INP, CLS)
- Mobile-friendliness
- HTTPS
- No intrusive interstitials (popup spam)

**User engagement signals:**
- CTR in search results (high CTR = Google shows result more)
- Dwell time (how long user stays on page)
- Bounce rate back to SERP (quick bounce = bad result signal)
- Pogo-sticking (user tries multiple results before finding good one)

**Structured data signals:**
- Schema markup present
- Rich snippet eligibility

#### Complete ranking pipeline
```
User types query
      ↓
Query understanding (intent, entities, expansion, personalization)
      ↓
Candidate retrieval (L0 ranker)
  - BM25 keyword score on inverted index
  - ~millions of candidates → filtered to ~100,000
      ↓
Fast scoring (L1 ranker)
  - Lightweight ML model
  - Basic relevance + quality signals
  - ~100,000 → ~1,000
      ↓
Deep scoring (L2 ranker)
  - Heavy neural models (LaMDA, BERT-based)
  - Full signal set
  - ~1,000 → ~20-50
      ↓
Reranking + adjustments
  - Freshness boost (if query needs fresh content)
  - Diversity (don't show 10 results from same domain)
  - Personalization (user history)
  - Featured snippet selection
  - Local pack insertion
      ↓
SERP assembly
  - Ads (top + bottom)
  - Featured snippet (position 0)
  - People Also Ask
  - Image pack
  - Local map pack
  - Organic results
  - AI Overview (SGE)
      ↓
Response to user in <200ms
```

---

## PART 3: SEO FUNDAMENTALS

### KEYWORDS

#### What keywords are
Words/phrases users type into search. Target wrong keywords → zero traffic. Target right ones → targeted buyers/users. Keywords are the bridge between what users want and what your page provides.

#### Search intent mapping

| Intent | Query | Who's searching | Page type |
|--------|-------|-----------------|-----------|
| Informational | "how to memorize vocabulary" | Students curious | Blog post |
| Navigational | "Spark.E login" | Existing users | Login/homepage |
| Commercial | "best study app for students" | Shopping around | Comparison/feature |
| Transactional | "Spark.E pricing" | Ready to sign up | Pricing page |

#### How keyword research actually works

1. **Brainstorm seeds:** What would your buyer type at each funnel stage?
   - "how to study better" (awareness)
   - "best flashcard app" (consideration)
   - "Anki alternative" (decision — switching)

2. **Expand with tools:**
   - Google Search Console (what you already rank for)
   - Ahrefs / SEMrush (volume, difficulty, related terms)
   - Google "People Also Ask" (free, excellent intent signals)
   - Google autocomplete (real queries users type)

3. **Evaluate each keyword:**
   - Search volume (searches/month)
   - Keyword difficulty (0-100, higher = harder to rank)
   - Traffic potential (top-ranking page's total traffic, better than volume)
   - Business value (will this traffic convert?)

4. **Map to pages:**
   ```
   "spaced repetition explained" → /blog/spaced-repetition-guide
   "best flashcard app" → /compare/ or homepage
   "Anki alternative" → /alternatives/anki-alternative
   "AI study app" → homepage or /features
   ```

5. **Cluster related keywords:**
   One page can rank for many related keywords. Don't create separate pages for:
   - "flashcard app"
   - "flashcard application"
   - "flashcard software"
   These are same intent → one page.

#### Modern vs old SEO

Old (pre-2012): Stuff keyword 50 times on page.
```
"Best flashcard app. Our flashcard app is the best flashcard app for students. 
Try our flashcard app today. Flashcard app users love our flashcard app."
```
→ Worked until Google Panda (2011) and Penguin (2012) destroyed this.

Modern: Write best, most complete answer for topic. Use keyword naturally. Cover related subtopics. Google's NLP understands context — keyword proximity matters less than topical depth.

```
One natural mention of "flashcard app" in H1.
Cover: what flashcards are, how spaced repetition works, features comparison.
Include related terms: "active recall", "memory retention", "SM-2 algorithm".
→ Ranks for 50+ related queries, not just the primary keyword.
```

---

### CONTENT SEO

#### How Google reads content
Google doesn't scan for keywords. It:
1. Extracts semantic meaning via transformer models
2. Maps content to known entities in Knowledge Graph
3. Compares topical coverage vs competing pages
4. Evaluates E-E-A-T signals
5. Checks structural signals (headings hierarchy)

#### Headings — semantic structure
```html
<h1>Spaced Repetition: The Science of Remembering Anything</h1>
  <!-- Single H1 = page topic. Contains primary keyword. -->

  <h2>What Is Spaced Repetition?</h2>
    <h3>The Forgetting Curve (Ebbinghaus)</h3>
    <h3>How the SM-2 Algorithm Works</h3>
    <h3>Why Spacing Intervals Beat Cramming</h3>

  <h2>Best Apps for Spaced Repetition</h2>
    <h3>Anki</h3>
    <h3>Spark.E</h3>
    <h3>Quizlet</h3>

  <h2>How to Start a Spaced Repetition Practice</h2>
    <h3>Step 1: Choose Your Tool</h3>
    <h3>Step 2: Create Your First Deck</h3>
```

H1 = page topic (one only).
H2 = major sections.
H3 = subsections.

Not decoration. Semantic document structure. Google's parser reads this as outline of what page covers.

#### Topical relevance
Cover full topic, not just one angle. Page about "flashcard apps" should cover:
- What flashcards are (definition)
- How spaced repetition works (mechanism)
- Features to look for (criteria)
- App comparison (options)
- Who should use (audiences)
- How to get started (action)

Shallow coverage → Google prefers competing page that covers all angles. This is "content depth" — not word count, but comprehensive topical coverage.

#### Semantic SEO — related terms
Use related terms naturally throughout content. If writing about "flashcard app":

Required semantic terms:
- "spaced repetition"
- "active recall"
- "memory retention"
- "forgetting curve"
- "SM-2 algorithm"
- "review intervals"
- "anki decks"

These signals topical depth to Google's NLP. Page that covers all related concepts = recognized as authoritative on topic.

#### Entities
Named, distinct things Google has in Knowledge Graph:
- **Anki** = software entity
- **Hermann Ebbinghaus** = person entity
- **SM-2 algorithm** = concept entity
- **spaced repetition** = concept entity

Include entities relevant to your topic. Helps Google understand content category without requiring exact keyword matches.

#### Topic clusters
Structure for building topical authority:

```
PILLAR PAGE: "The Complete Guide to Studying Effectively"
(broad, comprehensive, links to all clusters)
  ↕
CLUSTER: "Spaced Repetition Explained"
CLUSTER: "Active Recall Methods"
CLUSTER: "How to Create Effective Flashcards"
CLUSTER: "The Pomodoro Technique for Students"
CLUSTER: "Memory Palace Method"
```

Every cluster links to pillar. Pillar links to all clusters. Internal linking signals to Google: "this site covers this topic comprehensively." → topical authority.

---

### ON-PAGE SEO

#### Title tag
```html
<title>Best Flashcard App for Students — Spark.E</title>
```
Displayed in SERP browser tabs. Most important on-page ranking signal.

Rules:
- Primary keyword near front (Google weights start of title higher)
- 50–60 characters (longer gets truncated)
- Unique per page (never duplicate)
- Compelling — users must want to click
- Brand name at end after separator

Bad: `<title>Spark.E - We Are An AI Powered Educational Technology Solution</title>`
Good: `<title>AI Flashcard App with Spaced Repetition | Spark.E</title>`

#### Meta description
```html
<meta name="description" content="Spark.E uses AI + spaced repetition to help students remember 3x more. Free trial. No card needed. Join 50,000+ students.">
```
Not a ranking signal. Affects CTR (click-through rate). Google sometimes rewrites it (pulls relevant excerpt from page instead). 150–160 characters.

#### Canonical tag
```html
<link rel="canonical" href="https://sparke.app/flashcards/">
```
Tells Google: "This URL is the authoritative version of this content." Prevents duplicate content issues from query params, tracking codes, pagination variants.

#### H1
```html
<h1>AI-Powered Flashcard App That Helps You Remember Longer</h1>
```
One per page. Contains primary keyword. Can differ from title tag (title = SERP display, H1 = page heading). Bot reads both.

#### Open Graph tags
```html
<meta property="og:title" content="Spark.E — AI Flashcard App">
<meta property="og:description" content="Study smarter with AI-powered spaced repetition.">
<meta property="og:image" content="https://sparke.app/og/homepage.jpg">
<meta property="og:url" content="https://sparke.app/">
<meta property="og:type" content="website">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Spark.E — AI Flashcard App">
<meta name="twitter:image" content="https://sparke.app/og/homepage.jpg">
```
Not ranking signals. Control how page looks when shared on social platforms. Better preview image/title → more clicks → indirect SEO benefit.

OG image standard: 1200×630px.

#### Alt text
```html
<!-- Bad -->
<img src="screen1.png" alt="image">
<img src="screen1.png" alt="">

<!-- Good -->
<img src="review-screen.png" alt="Spark.E flashcard review screen showing spaced repetition countdown timer and answer confidence buttons">
```
Tells Google what image contains. Accessibility (screen readers). Keywords in alt text are minor ranking signal for image search + contextual understanding.

#### Internal links
```html
<!-- Bad anchor text -->
<a href="/features/spaced-repetition">click here</a>
<a href="/features/spaced-repetition">read more</a>

<!-- Good anchor text -->
<a href="/features/spaced-repetition">spaced repetition engine</a>
<a href="/blog/sm2-algorithm">SM-2 algorithm explained</a>
```
Anchor text = signal to Google about linked page's topic. "Click here" tells Google nothing. "spaced repetition engine" tells Google exactly what `/features/spaced-repetition` is about.

#### URL structure
```
Good: sparke.app/blog/spaced-repetition-guide
Good: sparke.app/features/ai-quiz-generator
Good: sparke.app/compare/anki-vs-sparke

Bad: sparke.app/p?id=123&cat=42
Bad: sparke.app/page/entry/2024/01/15/the-ultimate-guide-to
Bad: sparke.app/features/aiQuizGenerator   ← camelCase, no hyphens
```

Rules: short, readable, lowercase, hyphens (not underscores), keyword-rich, no query params for public pages.

#### Breadcrumbs
```
Home > Blog > Study Techniques > Spaced Repetition Guide
```
Navigation trail. Helps users. Enables rich breadcrumb snippet in SERP (shows path below title → more SERP real estate). Signals site hierarchy to Google.

```html
<nav aria-label="breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/blog/">Blog</a></li>
    <li><a href="/blog/study-techniques/">Study Techniques</a></li>
    <li aria-current="page">Spaced Repetition Guide</li>
  </ol>
</nav>
```

---

## PART 4: TECHNICAL SEO

### ROBOTS.TXT

Located at `yourdomain.com/robots.txt`. First thing Googlebot checks before crawling any page.

#### Purpose
Tell bots which pages to crawl, which to skip. Save crawl budget. Protect private areas.

#### Syntax
```
User-agent: *                    ← applies to ALL bots
Disallow: /admin/                ← block admin panel
Disallow: /api/                  ← block API routes
Allow: /api/public/              ← allow specific API path (overrides Disallow above)
Disallow: /dashboard/            ← authenticated area, no SEO value
Disallow: /checkout/             ← no SEO value
Disallow: /*?*sort=*             ← block sorted URL variants (duplicate content)

User-agent: Googlebot            ← only Google
Disallow: /staging/              ← block Google from staging area

Sitemap: https://sparke.app/sitemap.xml   ← required
```

#### Critical mistakes
- `Disallow: /` → blocks entire site (catastrophic)
- `Disallow: /static/` or `Disallow: /_next/` → blocks CSS/JS → Google can't render pages correctly
- Thinking robots.txt = noindex (wrong — it prevents crawling, not indexing. Ironically, disallowed pages can still appear in index from backlinks)
- Not pointing to sitemap URL

**Robots.txt does NOT prevent indexing.** It prevents crawling. Use `<meta name="robots" content="noindex">` to prevent indexing.

---

### SITEMAP.XML

Located at `yourdomain.com/sitemap.xml`. Map of your site for search bots.

#### Why it exists
Large sites have pages bots might never discover through link-following alone. Sitemap = direct list of "please crawl these." Also carries metadata (last modified, priority).

#### Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

  <url>
    <loc>https://sparke.app/</loc>
    <lastmod>2024-01-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>

  <url>
    <loc>https://sparke.app/features/spaced-repetition/</loc>
    <lastmod>2024-01-10</lastmod>
    <priority>0.8</priority>
  </url>

  <url>
    <loc>https://sparke.app/blog/spaced-repetition-guide/</loc>
    <lastmod>2024-01-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>

</urlset>
```

#### Sitemap index (for large sites)
```xml
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://sparke.app/sitemap-pages.xml</loc>
  </sitemap>
  <sitemap>
    <loc>https://sparke.app/sitemap-blog.xml</loc>
  </sitemap>
  <sitemap>
    <loc>https://sparke.app/sitemap-decks.xml</loc>
  </sitemap>
</sitemapindex>
```

#### Best practices
- Include ONLY indexable pages (no noindex, no 404, no redirects)
- Max 50,000 URLs per sitemap file
- Submit to Google Search Console (GSC) — don't just have it, tell Google it exists
- Auto-generate dynamically for SaaS (blog posts, deck pages change)
- Submit sitemap URL in robots.txt as well

---

### CANONICAL URLS

#### Problem
Same content accessible at multiple URLs (common in SaaS):
```
sparke.app/flashcards
sparke.app/flashcards/
sparke.app/flashcards?ref=homepage
sparke.app/flashcards?utm_source=twitter
sparke.app/flashcards?sort=popular
```
Google sees 5 URLs, doesn't know which is "real". May split authority across all 5. May index wrong one.

#### Solution
```html
<link rel="canonical" href="https://sparke.app/flashcards/">
```

Add to every page. Point to the "official" URL for that content.

#### When to use canonical
- UTM parameters (`?utm_source=twitter`)
- Sorting/filtering parameters (`?sort=price`)
- Session IDs
- Pagination (page 2+ canonical → not to page 1, but to self)
- www vs non-www versions
- HTTP vs HTTPS versions
- Same content syndicated to multiple pages

#### Self-referencing canonical
Even if a page has no duplicates, add canonical pointing to itself. Prevents any future URL variation from diluting authority.

---

### STRUCTURED DATA (SCHEMA MARKUP)

Machine-readable metadata embedded in page HTML. Google uses it to display rich results — enhanced SERP listings with extra information (ratings, FAQs, breadcrumbs, prices).

**Format:** JSON-LD, placed in `<script type="application/ld+json">` tag in `<head>` or `<body>`.

#### FAQ Schema
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is spaced repetition?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Spaced repetition is a learning technique that schedules review sessions at increasing intervals based on the Ebbinghaus forgetting curve, optimizing long-term retention."
      }
    },
    {
      "@type": "Question",
      "name": "Is Spark.E free to use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, Spark.E has a free plan with core features. Pro plan adds AI generation, unlimited decks, and advanced analytics."
      }
    }
  ]
}
</script>
```
Enables FAQ rich snippet in SERP → page takes up much more SERP real estate → higher CTR.

#### Organization Schema (homepage)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Spark.E",
  "url": "https://sparke.app",
  "logo": "https://sparke.app/logo.png",
  "description": "AI-powered flashcard app with spaced repetition for students.",
  "foundingDate": "2024",
  "sameAs": [
    "https://twitter.com/sparkeapp",
    "https://linkedin.com/company/sparke",
    "https://github.com/sparke"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer support",
    "email": "support@sparke.app"
  }
}
</script>
```

#### SoftwareApplication Schema
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Spark.E",
  "applicationCategory": "EducationalApplication",
  "operatingSystem": "Web, iOS, Android",
  "url": "https://sparke.app",
  "description": "AI-powered flashcards with spaced repetition for students.",
  "offers": [
    {
      "@type": "Offer",
      "name": "Free",
      "price": "0",
      "priceCurrency": "USD"
    },
    {
      "@type": "Offer",
      "name": "Pro",
      "price": "9.99",
      "priceCurrency": "USD",
      "billingDuration": "P1M"
    }
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "ratingCount": "1240",
    "bestRating": "5"
  }
}
</script>
```

#### Article Schema (blog posts)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Complete Guide to Spaced Repetition",
  "author": {
    "@type": "Person",
    "name": "Jogamaya",
    "url": "https://sparke.app/about"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Spark.E",
    "logo": {
      "@type": "ImageObject",
      "url": "https://sparke.app/logo.png"
    }
  },
  "datePublished": "2024-01-10",
  "dateModified": "2024-01-15",
  "image": "https://sparke.app/blog/og/spaced-repetition.jpg",
  "description": "Learn how spaced repetition works, why it's effective, and how to implement it with tools like Spark.E."
}
</script>
```

#### BreadcrumbList Schema
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://sparke.app/"},
    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://sparke.app/blog/"},
    {"@type": "ListItem", "position": 3, "name": "Spaced Repetition Guide", "item": "https://sparke.app/blog/spaced-repetition-guide/"}
  ]
}
</script>
```

Verify all schema at: https://search.google.com/test/rich-results

---

### WEBSITE ARCHITECTURE

#### Site hierarchy for SaaS
```
Homepage (tier 1) — highest authority, linked everywhere
├── Features/ (tier 2)
│   ├── spaced-repetition/ (tier 3)
│   ├── ai-quiz-generator/ (tier 3)
│   └── flashcard-maker/ (tier 3)
├── For/ (tier 2) — use-case landing pages
│   ├── medical-students/ (tier 3)
│   ├── language-learners/ (tier 3)
│   └── bar-exam-prep/ (tier 3)
├── Compare/ (tier 2)
│   ├── anki-vs-sparke/ (tier 3)
│   └── quizlet-vs-sparke/ (tier 3)
├── Alternatives/ (tier 2)
│   └── anki-alternative/ (tier 3)
├── Blog/ (tier 2)
│   └── [slugs] (tier 3)
├── Pricing/ (tier 2)
└── Docs/ (tier 2)
    └── [doc pages] (tier 3)
```

Important pages = high tier = fewer clicks from homepage = more crawl priority + more PageRank flow.

#### Information architecture rules
- Flat hierarchy preferred. Max 3-4 levels deep.
- Every important page reachable in ≤3 clicks from homepage
- Group related content together (all feature pages share parent, all blog posts share parent)
- Navigation links carry strong internal link weight (bots see nav on every page)

#### Crawl optimization
- Homepage has most PageRank → link from homepage to highest-priority pages
- Footer links help coverage for large sites
- Don't bury important pages in deep, JavaScript-rendered menus (bots may miss them)
- Pagination: use `rel="next"` and `rel="prev"` where applicable

---

### CORE WEB VITALS

Google ranking signal since 2021. Measures actual user experience — not lab metrics, but real Chrome user data.

#### LCP — Largest Contentful Paint
Time from navigation start until largest visible element (image, video, text block) renders.

**Target:** <2.5s good, <4.0s needs improvement, >4.0s poor.

Measured element is usually: hero image, H1 large text, featured image.

**Fixes:**
```html
<!-- Preload hero image — tells browser fetch this first -->
<link rel="preload" as="image" href="/hero.webp" fetchpriority="high">

<!-- Use modern formats -->
<img src="hero.webp" width="1200" height="630" alt="..." loading="eager">

<!-- For Next.js -->
<Image src="/hero.webp" priority={true} width={1200} height={630} alt="..." />
```

Other LCP fixes:
- CDN for images (serve from edge near user)
- Compress images (WebP → 30–40% smaller than JPEG)
- Eliminate render-blocking CSS/JS
- Reduce server response time (TTFB < 800ms)

#### INP — Interaction to Next Paint
Time between user interaction (click, tap, key press) and next visual update. Replaced FID in March 2024.

**Target:** <200ms good, <500ms needs improvement, >500ms poor.

**Fixes:**
- Break up long JavaScript tasks (> 50ms = long task → blocks main thread)
- Use `setTimeout()` or `scheduler.postTask()` to yield control
- Move heavy computation to Web Workers
- Avoid large React re-renders on interaction
- Debounce/throttle expensive event handlers

```tsx
// BAD: Entire component re-renders on every keypress
const [value, setValue] = useState("");
<input onChange={(e) => setValue(e.target.value)} />

// BETTER: Debounce if search triggers expensive operation
const debouncedSearch = useDeferredValue(value);
```

#### CLS — Cumulative Layout Shift
Measures visual instability — how much content shifts during page load.

**Target:** <0.1 good, <0.25 needs improvement, >0.25 poor.

**Common causes:**
- Images without explicit dimensions (browser doesn't know size until loaded → content shifts)
- Late-loading ads (inject into DOM, push content down)
- Web fonts causing FOUT (Flash of Unstyled Text → text reflows)
- Dynamic content injected above existing content

**Fixes:**
```html
<!-- Always specify dimensions so browser reserves space -->
<img src="hero.jpg" width="800" height="450" alt="..." />

<!-- Next.js Image component handles this automatically -->
<Image src="/hero.jpg" width={800} height={450} alt="..." />
```

```css
/* Reserve space for ad containers */
.ad-container {
  min-height: 250px; /* Reserve height before ad loads */
}
```

```css
/* Prevent font swap shift */
@font-face {
  font-display: optional; /* Don't swap if font loads late */
}
```

#### How Google measures
1. **Field data** — Chrome User Experience Report (CrUX). Real measurements from real Chrome users visiting your site. 75th percentile. This is what Google uses for ranking.
2. **Lab data** — Lighthouse / PageSpeed Insights simulated test. Useful for development but not what ranks you.

Field data > Lab data. Site in development has no CrUX data → lab data used temporarily.

Check: https://pagespeed.web.dev/

---

## PART 5: SAAS SEO STRATEGY

### THE FUNNEL
```
AWARENESS (top-of-funnel)
  "how to study more effectively" → Blog posts, guides, tutorials
  
CONSIDERATION (middle-of-funnel)
  "best flashcard apps 2024" → Comparison pages, feature pages
  "Anki alternative with AI" → Alternative pages
  
DECISION (bottom-of-funnel)
  "Spark.E pricing" → Pricing page
  "Spark.E vs Quizlet" → Comparison page
  "Spark.E free trial" → Homepage / signup page
```

Each stage needs different content. Don't write only blog posts (awareness) and wonder why you get traffic but no signups.

---

### PRODUCT-LED SEO

Let the product generate indexable content. Users create public content → bots index it → drives new users.

Examples:
| Product | User creates | Indexed content |
|---------|-------------|-----------------|
| Notion | Public pages | `notion.so/username/page-title` |
| Canva | Public designs | design thumbnail pages |
| Figma | Public prototypes | embed preview pages |
| Loom | Public videos | `loom.com/share/[id]` |

**For Spark.E:** Public flashcard decks on topics:
```
sparke.app/decks/biology-cell-division       ← searches: "biology flashcards cell division"
sparke.app/decks/javascript-closures          ← searches: "javascript closures practice"
sparke.app/decks/spanish-irregular-verbs      ← searches: "spanish irregular verbs flashcards"
```

Each page = unique content (the actual flashcards). Users search topic-specific flashcard queries. They find your page, try the deck, sign up to save progress. **Product-led SEO at its best.**

Requirements:
- Public deck URL must be static/SSG (not behind auth)
- Deck content must be rich enough to be indexed
- Add title, description, card count, subject tags
- Add structured data (`Dataset` or `ItemList` schema)

---

### LANDING PAGES

One per key use case or audience segment:

```
sparke.app/for/medical-students
→ targets: "study app for medical school", "flashcards for USMLE"

sparke.app/for/language-learners
→ targets: "vocabulary learning app", "flashcards for language learning"

sparke.app/for/bar-exam-prep
→ targets: "bar exam study app", "MBE flashcards"

sparke.app/for/teachers
→ targets: "flashcard app for teachers", "classroom quiz tool"
```

Each page:
- Targets audience-specific keywords
- Speaks to their specific pain points
- Shows relevant features/use cases
- Has testimonials from that audience type
- Clear CTA

---

### PROGRAMMATIC SEO

Generate thousands of pages from template + data. Each page targets a specific long-tail keyword.

**Pattern:** `[Topic] Flashcards` for any possible topic:
```
sparke.app/flashcards/anatomy           searches: "anatomy flashcards"
sparke.app/flashcards/organic-chemistry searches: "organic chemistry flashcards"
sparke.app/flashcards/spanish           searches: "spanish flashcards"
sparke.app/flashcards/javascript        searches: "javascript flashcards"
```

**Requirements for success:**
1. Each page has unique content (not just title changed)
2. Include sample cards for that topic (actual value)
3. Target keywords with real search volume
4. Add subject-specific description, stats, related topics
5. Internal links between related topics

**Never:** Generate 10,000 near-identical pages with only title changed. Google calls this thin content / spam. Penalty risk.

---

### DOCUMENTATION SEO

Docs rank for "how to use [feature]" queries. These searchers are in consideration stage — already evaluating your product.

Good docs SEO:
- Each doc page has clear H1 with feature name
- Include canonical URL (docs often accessed from multiple paths)
- Add FAQ schema at bottom of complex docs
- Interlink docs → feature marketing pages
- Add breadcrumb navigation + schema
- Make docs publicly accessible (not behind login)

```
docs.sparke.app/spaced-repetition
→ ranks for: "how to use spaced repetition in Spark.E"
→ user reading this is evaluating or already using product
```

---

### BLOG SEO

Target informational queries. Build awareness. Internal link to product pages.

**Best SaaS blog topics:**

| Content type | Example | Intent |
|-------------|---------|--------|
| How-to guides | "how to memorize vocabulary fast" | Informational |
| Comparisons | "spaced repetition vs cramming" | Informational/commercial |
| Lists | "10 study techniques that actually work" | Informational |
| Studies/data | "why students forget 80% within 24 hours" | Informational |
| Case studies | "how [user] passed USMLE using Spark.E" | Commercial |

Every blog post → internal link to relevant feature.

---

### COMPARISON PAGES

High conversion intent. Users searching "Anki vs Spark.E" have already decided to use one of them.

```
sparke.app/compare/anki-vs-sparke
sparke.app/compare/quizlet-vs-sparke
sparke.app/compare/notion-vs-sparke-for-students
```

Structure:
1. Hero: brief summary of winner
2. Quick comparison table (features, pricing, ease of use)
3. Detailed comparison section per key feature
4. "Who should choose X" section
5. "Who should choose Spark.E" section
6. FAQ with schema
7. CTA: "Try Spark.E free"

Rule: Be honest. Users trust honest comparisons. "Anki is better if you want maximum control and offline use. Spark.E is better if you want AI generation and modern UX."

---

### ALTERNATIVE PAGES

Target: "[Competitor] alternative" queries. Users actively wanting to switch.

```
sparke.app/alternatives/anki-alternative
sparke.app/alternatives/quizlet-alternative
```

These convert extremely well — user is already motivated to switch, just needs to find the right replacement.

Structure:
1. "Why people look for Anki alternatives" (validate their pain)
2. "What to look for in an alternative" (criteria that favor you)
3. Spark.E as primary recommendation (detailed)
4. 3-4 other alternatives (honest — builds trust)
5. Comparison table
6. CTA

---

### FEATURE PAGES

One page per core feature. Ranks for feature-specific queries.

```
sparke.app/features/spaced-repetition
→ "spaced repetition app", "SM-2 algorithm app"

sparke.app/features/ai-quiz-generator
→ "AI quiz maker", "auto-generate quiz from notes"

sparke.app/features/flashcard-maker
→ "flashcard creator app", "digital flashcard maker"

sparke.app/features/study-analytics
→ "study progress tracker", "learning analytics app"
```

Each page includes:
- What feature does (clear explanation)
- How it works (mechanism)
- Who benefits (audiences)
- Screenshots/demo
- FAQ with schema
- CTA

---

### USE-CASE PAGES

One page per use case:

```
sparke.app/use-cases/medical-school-studying
→ "how to study for medical school", "medical flashcard app"

sparke.app/use-cases/language-learning
→ "best app for learning languages", "vocabulary retention app"

sparke.app/use-cases/test-preparation
→ "test prep app", "study app for exams"
```

---

### REAL PATTERNS FROM SUCCESSFUL SAAS

**Notion:**
- Every feature = own landing page + docs
- Templates page = programmatic SEO (10,000+ templates indexed)
- Blog covers productivity broadly → drives awareness from non-Notion users

**Linear:**
- Exceptional docs (every integration has own page)
- Comparison vs Jira, Asana on site
- Changelog = fresh content signal

**Vercel:**
- Docs best-in-class → rank for every Next.js query
- Blog covers Next.js deeply (their audience = Next.js devs)
- Every framework/language has its own "deploy [framework] on Vercel" page (programmatic)

**Ahrefs:**
- Free tools (broken link checker, SERP checker, etc.) → link magnets
- Each free tool = own page targeting "[tool type] tool free"
- Educational content dominates SEO space → makes them authority

---

## PART 6: SEO INSIDE SAAS CODEBASE (NEXT.JS)

### FILES AFFECTING SEO

#### `app/layout.tsx` — Root layout (global SEO defaults)
```tsx
// app/layout.tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: {
    default: "Spark.E — AI Flashcard App",
    template: "%s | Spark.E",   // → "Spaced Repetition | Spark.E"
  },
  description: "AI-powered flashcards with spaced repetition. Study smarter, remember longer.",
  metadataBase: new URL("https://sparke.app"),
  
  openGraph: {
    type: "website",
    siteName: "Spark.E",
    images: [{ url: "/og-default.jpg", width: 1200, height: 630 }],
  },
  
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

**Why `lang="en"` matters:** Language attribute helps Google serve content to correct audience. Omitting it = Google guesses language.

#### `app/sitemap.ts` — Dynamic sitemap generation
```ts
import { MetadataRoute } from "next";
import { getAllBlogPosts, getPublicDecks, getFeaturePages } from "@/lib/content";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const [posts, decks] = await Promise.all([
    getAllBlogPosts(),
    getPublicDecks(),
  ]);

  // Static pages
  const staticPages: MetadataRoute.Sitemap = [
    { url: "https://sparke.app/", priority: 1.0, changeFrequency: "weekly", lastModified: new Date() },
    { url: "https://sparke.app/pricing", priority: 0.9, changeFrequency: "monthly" },
    { url: "https://sparke.app/features/spaced-repetition", priority: 0.8 },
    { url: "https://sparke.app/features/ai-quiz-generator", priority: 0.8 },
    { url: "https://sparke.app/compare/anki-vs-sparke", priority: 0.7 },
    { url: "https://sparke.app/alternatives/anki-alternative", priority: 0.7 },
    { url: "https://sparke.app/blog", priority: 0.7, changeFrequency: "daily" },
  ];

  // Dynamic blog pages
  const blogPages: MetadataRoute.Sitemap = posts.map(post => ({
    url: `https://sparke.app/blog/${post.slug}`,
    lastModified: new Date(post.updatedAt),
    priority: 0.6,
    changeFrequency: "monthly" as const,
  }));

  // Dynamic deck pages (product-led SEO)
  const deckPages: MetadataRoute.Sitemap = decks.map(deck => ({
    url: `https://sparke.app/decks/${deck.slug}`,
    lastModified: new Date(deck.updatedAt),
    priority: 0.5,
    changeFrequency: "weekly" as const,
  }));

  return [...staticPages, ...blogPages, ...deckPages];
}
```

#### `app/robots.ts` — Robots rules
```ts
import { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
        disallow: [
          "/dashboard/",       // Authenticated area
          "/api/",             // API routes
          "/admin/",           // Admin panel
          "/settings/",        // User settings
          "/*?*session*",      // Session ID URLs
          "/*?*sort=*",        // Sorted/filtered duplicates
        ],
      },
    ],
    sitemap: "https://sparke.app/sitemap.xml",
  };
}
```

#### `next.config.js` — Redirects, headers, image config
```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Redirect www to non-www
  async redirects() {
    return [
      {
        source: "/:path*",
        has: [{ type: "host", value: "www.sparke.app" }],
        destination: "https://sparke.app/:path*",
        permanent: true, // 301
      },
    ];
  },

  // Security headers (also trust signals for Google)
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "X-Frame-Options", value: "DENY" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
        ],
      },
    ];
  },

  images: {
    formats: ["image/avif", "image/webp"],  // Modern formats → smaller → better LCP
    domains: ["cdn.sparke.app"],
  },
};

module.exports = nextConfig;
```

---

### METADATA — COMPLETE EXAMPLES

#### Static page (feature page):
```tsx
// app/features/spaced-repetition/page.tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Spaced Repetition Engine",  // Template: "Spaced Repetition Engine | Spark.E"
  description: "Spark.E's SM-2 based spaced repetition schedules reviews at scientifically optimal intervals. Remember 3x more in half the time.",
  
  alternates: {
    canonical: "https://sparke.app/features/spaced-repetition",
  },
  
  openGraph: {
    title: "Spaced Repetition Engine | Spark.E",
    description: "Schedule reviews scientifically. Remember longer.",
    images: [{ url: "/og/spaced-repetition.jpg", width: 1200, height: 630 }],
    url: "https://sparke.app/features/spaced-repetition",
    type: "website",
  },
  
  twitter: {
    card: "summary_large_image",
    title: "Spaced Repetition Engine | Spark.E",
    description: "Schedule reviews scientifically. Remember longer.",
    images: ["/og/spaced-repetition.jpg"],
  },
};

export default function SpacedRepetitionPage() {
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            {
              "@type": "Question",
              "name": "What is spaced repetition?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Spaced repetition is a scientifically proven study technique that schedules review sessions at increasing intervals based on how well you know each item."
              }
            }
          ]
        })}}
      />
      {/* Page JSX */}
      <h1>Spaced Repetition Engine</h1>
      {/* ... */}
    </>
  );
}
```

#### Dynamic page (blog post):
```tsx
// app/blog/[slug]/page.tsx
import type { Metadata } from "next";

interface Props {
  params: { slug: string };
}

export async function generateStaticParams() {
  const posts = await getAllBlogPosts();
  return posts.map(p => ({ slug: p.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const post = await getBlogPost(params.slug);
  
  if (!post) return { title: "Not Found" };

  return {
    title: post.title,
    description: post.excerpt,
    
    alternates: {
      canonical: `https://sparke.app/blog/${post.slug}`,
    },
    
    openGraph: {
      title: post.title,
      description: post.excerpt,
      images: [{ url: post.ogImage || "/og-blog-default.jpg" }],
      type: "article",
      publishedTime: post.publishedAt,
      modifiedTime: post.updatedAt,
      authors: [post.author.url],
      tags: post.tags,
    },
    
    twitter: {
      card: "summary_large_image",
      title: post.title,
      description: post.excerpt,
      images: [post.ogImage || "/og-blog-default.jpg"],
    },
  };
}

export default async function BlogPost({ params }: Props) {
  const post = await getBlogPost(params.slug);
  
  const schema = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": post.title,
    "description": post.excerpt,
    "image": post.ogImage,
    "author": {
      "@type": "Person",
      "name": post.author.name,
      "url": `https://sparke.app/authors/${post.author.slug}`,
    },
    "publisher": {
      "@type": "Organization",
      "name": "Spark.E",
      "logo": { "@type": "ImageObject", "url": "https://sparke.app/logo.png" }
    },
    "datePublished": post.publishedAt,
    "dateModified": post.updatedAt,
    "mainEntityOfPage": { "@type": "WebPage", "@id": `https://sparke.app/blog/${post.slug}` }
  };

  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sparke.app/" },
      { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://sparke.app/blog/" },
      { "@type": "ListItem", "position": 3, "name": post.title, "item": `https://sparke.app/blog/${post.slug}` }
    ]
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />
      <article>
        <h1>{post.title}</h1>
        {/* post content */}
      </article>
    </>
  );
}
```

---

### CSR vs SSR vs SSG vs ISR — SEO IMPACT

#### CSR (Client-Side Rendering)
```
Request → Server returns empty HTML shell → Browser downloads JS → JS executes → Content renders
```
Bot gets at first visit: `<div id="root"></div>` — empty.

Content exists only after JS runs. Googlebot must schedule a second wave to render JS (can take hours to weeks). Unreliable for SEO. Content may be indexed with delay or not at all.

**When to use:** Authenticated dashboards, user-specific content, real-time apps behind login. Never for public marketing/content pages.

#### SSR (Server-Side Rendering)
```
Request → Server fetches data + renders HTML → Returns full HTML → Browser
```
Bot gets: complete HTML with all content. Immediate.

Each request = fresh server render. Slightly slower than static. Better for frequently changing, personalized content.

**When to use:** Personalized public pages, search results pages, feed pages.

#### SSG (Static Site Generation)
```
Build time → Server renders all pages → HTML files → Deployed to CDN → Served instantly
```
Bot gets: pre-rendered HTML from CDN. Fastest possible.

Built once, served forever (until next build). Ideal for content that doesn't change per user.

**When to use:** Homepage, feature pages, pricing, comparison pages, blog posts, documentation.

#### ISR (Incremental Static Regeneration) — Next.js unique
```
Build time → Render → Static HTML → After revalidate seconds → Re-render in background on next request
```
Bot gets: always HTML (same as SSG — pre-rendered).
After revalidation period, stale page served once more → next request triggers fresh render in background.

**When to use:** Blog posts (update when edited), product pages (pricing/feature changes), programmatic pages (user-generated content).

```tsx
// ISR configuration
export const revalidate = 3600; // Re-render every 1 hour

export default async function BlogPost({ params }) {
  const post = await getBlogPost(params.slug);
  return <article>{/* ... */}</article>;
}
```

#### Decision table for Spark.E
| Page | Strategy | Reason |
|------|----------|--------|
| Homepage | SSG | Static, same for all users |
| Feature pages | SSG | Rarely changes |
| Blog posts | SSG + ISR (3600s) | Fresh but mostly static |
| Pricing | SSG + ISR (1800s) | Update when plans change |
| Comparison pages | SSG | Static content |
| Docs | SSG + ISR | Update when docs edited |
| Public deck pages | ISR (300s) | User content changes |
| Dashboard | CSR | Auth-gated, no SEO |
| User profile (public) | SSR or ISR | Dynamic per user |

---

### JAVASCRIPT SEO PITFALLS

#### Problem 1: Content inside useEffect (invisible to bots on first pass)
```tsx
// BAD — content only appears after JS runs
export default function FeaturePage() {
  const [features, setFeatures] = useState([]);
  
  useEffect(() => {
    fetch("/api/features").then(res => res.json()).then(setFeatures);
  }, []);

  return (
    <ul>
      {features.map(f => <li key={f.id}>{f.name}</li>)}  {/* Empty on bot visit */}
    </ul>
  );
}

// GOOD — data fetched server-side, in HTML immediately
export default async function FeaturePage() {
  const features = await getFeatures(); // Server-side

  return (
    <ul>
      {features.map(f => <li key={f.id}>{f.name}</li>)}  {/* In HTML */}
    </ul>
  );
}
```

#### Problem 2: Lazy-loaded critical content
```tsx
// BAD — H1 lazy loads
const HeroSection = dynamic(() => import("./HeroSection"), { ssr: false });
//                                                           ↑ turns off SSR!

// GOOD — hero is server-rendered
const HeroSection = dynamic(() => import("./HeroSection")); // ssr: true by default
// Or better: just import normally if it's above the fold
import HeroSection from "./HeroSection";
```

#### Problem 3: `ssr: false` in dynamic imports for SEO content
```tsx
// BAD — any component with SEO-critical content must NOT use ssr:false
const BlogContent = dynamic(() => import("./BlogContent"), { ssr: false });

// GOOD — only use ssr:false for truly client-only components
const ThreeJSScene = dynamic(() => import("./ThreeJSScene"), { ssr: false }); // OK, not SEO content
```

#### Problem 4: Canonical missing on dynamic routes
```tsx
// Without canonical, ?utm_source=twitter and clean URL = duplicate content
// Always include:
export async function generateMetadata({ params }) {
  return {
    alternates: {
      canonical: `https://sparke.app/blog/${params.slug}`, // Always explicit canonical
    }
  };
}
```

#### Problem 5: Missing metadata on paginated routes
```tsx
// app/blog/page/[page]/page.tsx
export async function generateMetadata({ params }) {
  return {
    title: params.page === "1" ? "Blog | Spark.E" : `Blog — Page ${params.page} | Spark.E`,
    alternates: {
      canonical: params.page === "1" 
        ? "https://sparke.app/blog/" 
        : `https://sparke.app/blog/page/${params.page}/`,
    },
    // Don't index pagination beyond page 1 (debated — but common practice)
    robots: params.page !== "1" ? { index: false } : undefined,
  };
}
```

#### Complete developer mistakes list
1. Content in `useEffect` (invisible to bots)
2. `ssr: false` on SEO-critical components
3. No `<title>` on some pages
4. Duplicate `<title>` across pages
5. Missing meta description
6. Missing canonical tag
7. Canonical pointing to 404
8. No OG image (social previews broken)
9. Images without `width`/`height` (CLS)
10. Images without `alt` text
11. Large uncompressed images (LCP)
12. Missing H1 on page
13. Multiple H1s on one page
14. No internal links from homepage to feature pages
15. Blocking CSS/JS in robots.txt
16. No sitemap.xml
17. Sitemap includes 404/redirect pages
18. No schema markup anywhere
19. CSR for public content pages
20. Session IDs leaking into public URLs

---

## PART 7: ADVANCED SEO

### SEMANTIC SEARCH

Old model: user types exact string → search engine finds pages containing that exact string.

Modern model: user types query → search engine understands *meaning* → finds pages that *answer the question* even without keyword match.

BERT (2019) was transformational. Bidirectional attention mechanism understands full sentence context:

```
"can you suggest a good bank?"
Old: results about financial banks (most common meaning)
BERT: checks context — is this about river banks? Memory banks? Financial banks?
→ Serves correct type based on surrounding words
```

For SEO: Write naturally for humans. Use varied vocabulary. Cover subtopics comprehensively. Dense, jargon-stuffed pages no longer win against genuinely helpful content.

---

### KNOWLEDGE GRAPH

Google's internal database of entities (people, companies, places, things) and their relationships.

```
Entity: "Spark.E"
Properties:
  type: SoftwareApplication
  category: EdTech
  function: Flashcard app + spaced repetition
  platform: Web
  language: English
  competitors: [Anki, Quizlet]
  
Relationships:
  "Spark.E" → USES → "SM-2 algorithm"
  "Spark.E" → IS_A → "Study app"
  "Spark.E" → CATEGORY → "EdTech SaaS"
```

When Google understands your product as an entity, it can better:
- Associate your content with relevant queries
- Show you in entity-based features (Knowledge Panel)
- Understand your competitive landscape

**How to get into Knowledge Graph:**
1. Organization schema on homepage (most direct)
2. Consistent brand name + description across web
3. Wikipedia article (strong but hard for startups)
4. Wikidata entry (more achievable)
5. Press mentions that describe what you are
6. sameAs links in schema (Twitter, LinkedIn, Crunchbase)

---

### ENTITIES IN SEO

Entities = specific, distinct things. Not keywords — real-world concepts.

"spaced repetition" = concept entity (known thing)
"Ebbinghaus" = person entity
"SM-2" = concept entity
"flashcard" = object entity

When your content discusses real entities (not just keywords), Google understands what your page is *about* at a deeper level.

**Entity co-occurrence:** If your page about "study apps" co-occurs with entities "spaced repetition", "active recall", "Ebbinghaus" → Google knows this page is about memory science study methods, not productivity apps or gaming apps.

---

### E-E-A-T

Experience, Expertise, Authoritativeness, Trustworthiness.
Used in Google's Search Quality Evaluator Guidelines (human raters who evaluate Google's algorithm output).

**Experience:** Author has direct, first-hand experience with topic.
→ "I used Anki for 3 years during medical school" > "Studies show Anki helps memory"

**Expertise:** Author demonstrably knows the subject.
→ Medical advice from doctor > advice from random blog
→ For SaaS: technical content from actual developers/experts

**Authoritativeness:** Others recognize you as authority.
→ Other authoritative sites link to you
→ Brand mentioned in industry publications
→ Community recognition (GitHub stars, product reviews)

**Trustworthiness:** Core of E-E-A-T.
→ HTTPS
→ Clear privacy policy, terms of service
→ Real contact information
→ No deceptive content
→ Accurate, fact-checkable claims

**For Spark.E E-E-A-T:**
- Author bios on all blog posts (with real LinkedIn)
- Credentials/experience in bio ("Built X study tools, tested Y methods")
- Accurate claims with sources
- Review profiles (G2, Trustpilot, Capterra)
- Press mentions
- HTTPS, clear privacy policy
- Real company contact details

---

### PAGERANK + LINK EQUITY

PageRank = Google's foundational algorithm (1998, still core signal today).

Core concept: A link from page A to page B = vote of confidence for page B. More votes = more authority. Quality of voter matters (NYT link >> random blog link).

```
Simplified PageRank formula:
PR(B) = (1-d) + d × Σ(PR(Ai) / C(Ai))

Where:
d = damping factor (0.85 — probability user continues clicking links)
PR(Ai) = PageRank of linking page A
C(Ai) = number of outbound links from A (divides authority among all recipients)
```

**What this means practically:**
- Getting linked from page with lots of inbound links = valuable
- Getting linked from page that links to 500 other sites = less valuable (diluted)
- Homepage has highest PageRank → links from homepage go to your most important pages

**Internal PageRank flow:**
```
Homepage (PR: 100)
→ links to: Features (PR: 70), Blog (PR: 60), Pricing (PR: 80)

Features page (PR: 70)
→ links to: Spaced Repetition (PR: 45), AI Quiz (PR: 45)

Spaced Repetition page
→ Has reasonable PR but isn't in homepage footer
→ Add homepage footer link → PR increases significantly
```

**Link quality signals:**
- Domain Rating of linking site (Ahrefs' metric)
- Topical relevance of linking site to your content
- Placement of link (editorial body link >> sidebar >> footer)
- Anchor text
- No-follow vs do-follow attribute

---

### TOPICAL AUTHORITY

Google rewards sites that comprehensively cover a topic. Being the recognized expert in a niche > being a generalist.

**Build topical authority:**
1. Pick your niche narrowly at first ("spaced repetition for students")
2. Write 20-30 pieces covering all aspects of that niche
3. Create topic cluster with pillar page + cluster pages
4. Get backlinks from other educational/EdTech sites
5. Expand niche once authority established

Topical authority = Google trusts you for all queries in that topic area. Even new pages on that topic rank faster because domain already trusted for topic.

---

### INFORMATION RETRIEVAL — MODERN SYSTEM

Modern search is hybrid:

**Stage 1 — Sparse retrieval (BM25):**
Keyword-based inverted index lookup. Fast. Returns millions of candidates.

**Stage 2 — Dense retrieval (neural):**
Query encoded as vector. Approximate nearest-neighbor search in vector space. Finds semantically similar pages. Returns thousands.

**Stage 3 — Cross-encoder reranking:**
Both query and page fed together into neural model. Deeper understanding of relevance. Expensive but precise. Returns 20-50.

**Stage 4 — Learning to Rank:**
ML model incorporating all signals (PageRank, freshness, engagement, E-E-A-T). Final ordering.

**For SEO strategy:** Your content must satisfy all layers:
- Contains relevant keywords (BM25 layer)
- Is semantically rich (dense retrieval layer)
- Directly answers the query (cross-encoder layer)
- Has authority signals (LTR layer)

---

### EMBEDDINGS + VECTOR DATABASES

Every page Google indexes → BERT/MUM generates embedding: high-dimensional vector (768 or 1536 dims) representing semantic meaning.

```
"What is spaced repetition?" → query embedding
"The science of memorization and how review timing affects retention" → page embedding

Cosine similarity: 0.92 → highly relevant
Even without "spaced repetition" in page title
```

**For your Spark.E backend:** You already use Pinecone! Same concept — you embed user notes/content, store in Pinecone, retrieve semantically similar content. This is exactly what Google does at scale.

Your knowledge of Pinecone + vector search directly maps to understanding modern search engines.

**GEO (Generative Engine Optimization):** As LLMs are used to answer queries, being embedded in training data + having clear, structured content matters. LLMs retrieve from training (web content) and real-time search. Your content needs to be:
- Clear and direct (LLMs quote concise passages)
- Factually accurate (LLMs won't cite unreliable sources)
- Structured with clear headings (LLMs parse structure)
- On authoritative domains (LLMs weight source authority)

---

### AI SEARCH — SGE / AI OVERVIEWS

Google AI Overviews (formerly SGE) = AI-generated answer appears above organic results. Sources cited below.

**How to get cited in AI Overviews:**
1. Clear, direct answers to specific questions
2. FAQ schema (Google's AI pulls from FAQ rich results)
3. Concise, quotable paragraphs (1-3 sentences that answer question directly)
4. Authoritative domain (E-E-A-T matters even more here)
5. Structured content (clear H2s make it easy to extract relevant sections)
6. Factual accuracy (AI won't cite disputed/inaccurate content)

**Impact on organic traffic:**
- Zero-click searches increase when AI Overview fully answers question
- Being the cited source in AI Overview > ranking #1 but not cited
- Conversational, specific queries more likely to trigger AI Overview
- "Best [X]" queries often still show traditional results

**LLM-powered search (Perplexity, ChatGPT Search, Claude):**
These crawl web in real-time + have training data. Content strategies:
- Get on sites these LLMs are trained on (Wikipedia, GitHub, authoritative publications)
- Clear structured content → easier for LLMs to extract and cite
- Factual, with specific numbers/data → LLMs favor citable specifics
- Your docs/content must be publicly accessible (not behind login)

---

## PART 8: SEO AUDIT FRAMEWORK (PRE-LAUNCH CHECKLIST)

### TECHNICAL SEO

| Check | Why It Matters | How To Verify |
|-------|---------------|---------------|
| HTTPS enforced everywhere | Trust + ranking signal | SSL Labs (ssllabs.com/ssltest/) |
| www → non-www redirect (or opposite, consistently) | Prevent duplicate homepage | `curl -I http://www.domain.com` |
| HTTP → HTTPS redirect | Consolidate authority | `curl -I http://domain.com` |
| No redirect chains (A→B→C) | Each hop loses authority | Screaming Frog / httpstatus.io |
| robots.txt exists and correct | Bot instructions | yourdomain.com/robots.txt |
| robots.txt NOT blocking site CSS/JS | Bot needs to render page | Check Disallow rules carefully |
| robots.txt NOT blocking important paths | Bots must reach pages | Check against page URLs |
| sitemap.xml exists | Bot discovery | yourdomain.com/sitemap.xml |
| Sitemap contains no 404s/redirects | Wastes crawl budget | Screaming Frog sitemap audit |
| Sitemap submitted to GSC | Google aware of it | GSC → Sitemaps |
| Canonical on every page | Prevent duplicate content | View source, check `<head>` |
| No self-referencing canonical errors | Canonical must match real URL | Crawl with Screaming Frog |
| Clean URL structure (no session IDs, query param mess) | Crawlability | Audit URL patterns |
| No broken internal links | User experience + crawl | Screaming Frog → Response Codes |
| All pages reachable within 3 clicks | Crawl depth | Manual audit + Screaming Frog |

### ON-PAGE SEO

| Check | Target | Common Mistake |
|-------|--------|----------------|
| Unique `<title>` per page | 50-60 chars, keyword first | Duplicate titles across pages |
| Meta description per page | 150-160 chars | Missing on most pages |
| One `<h1>` per page | Contains primary keyword | Multiple H1s or no H1 |
| H2-H6 logical hierarchy | Nested correctly | H3 without H2 parent |
| Canonical present on every page | Matches intended URL | Missing on dynamic pages |
| Alt text on all images | Descriptive, not "image1.jpg" | Empty alt="" on informational images |
| Internal links to key pages | From content, not just nav | All links only in nav/footer |
| Descriptive anchor text | Not "click here" | Generic anchors everywhere |
| OG tags complete | title, description, image, url | Missing og:image (social broken) |
| Twitter card tags | card, title, image | Not set |
| `lang` attribute on `<html>` | Correct language code | Missing |
| No keyword stuffing | Natural language | Exact keyword repeated 20+ times |

### CONTENT SEO

| Check | Notes |
|-------|-------|
| Each page targets specific keyword cluster | No two pages target same primary keyword |
| Content matches search intent | Informational → guide, Transactional → pricing |
| Adequate depth for competitive keywords | 1500+ words for competitive informational topics |
| Related semantic terms present | Not just primary keyword repeated |
| FAQ section on key pages | Enables rich snippets |
| Author bio on blog posts | E-E-A-T signal |
| Published + updated dates visible | Freshness signal |
| Sources/citations for factual claims | Trust signal |
| External links to authoritative sources | Normal pattern; not a penalty |
| Topic cluster structure exists | Pillar → cluster linking |

### PERFORMANCE SEO

| Metric | Target | Tool |
|--------|--------|------|
| LCP | <2.5s | PageSpeed Insights (mobile) |
| INP | <200ms | PageSpeed Insights |
| CLS | <0.1 | PageSpeed Insights |
| TTFB | <800ms | WebPageTest.org |
| Total page weight | <1MB (aim for <500KB) | Chrome DevTools Network tab |
| Image format | WebP or AVIF | Lighthouse audit |
| Images compressed | <200KB per image | Squoosh.app |
| Hero image preloaded | `<link rel="preload">` for hero | View source |
| No render-blocking resources | CSS/JS non-blocking | Lighthouse |
| Mobile friendly | Pass | Google Mobile-Friendly Test |
| All Core Web Vitals green | 75th percentile passes | GSC → Core Web Vitals report |

### SCHEMA SEO

| Schema Type | Pages | Verified By |
|-------------|-------|-------------|
| Organization | Homepage | Rich Results Test |
| WebSite + SearchAction | Homepage | Rich Results Test |
| SoftwareApplication | Homepage + Pricing | Rich Results Test |
| FAQPage | Feature pages, comparison, landing | Rich Results Test |
| Article | All blog posts | Rich Results Test |
| BreadcrumbList | All non-homepage pages | Rich Results Test |
| Person (author) | Author profile pages | Rich Results Test |

Verify all: https://search.google.com/test/rich-results

### SAAS SEO

| Item | Status Check |
|------|-------------|
| Homepage targets primary keyword + clear value prop | "AI flashcard app" in H1/title |
| Feature page per core feature | /features/[feature] |
| Use-case page per audience | /for/[audience] |
| Comparison page vs top 3 competitors | /compare/ |
| Alternative page per top competitor | /alternatives/ |
| Blog exists with 3+ published articles | Pre-launch minimum |
| Public docs indexed | Not behind login |
| Pricing page has schema | SoftwareApplication + Offer |
| Social profiles exist + linked in Organization schema | Twitter, LinkedIn at minimum |
| Brand consistent across: site, GSC, social, schema | Same name everywhere |

### AI SEARCH READINESS

| Check | Why |
|-------|-----|
| Content answers specific questions directly | AI Overviews pull direct answers |
| FAQ schema on all key pages | AI parses FAQ schema heavily |
| Organization schema + sameAs links | AI understands who you are |
| All critical content in HTML (not JS-rendered) | Many AI crawlers don't execute JS |
| Factual, accurate content with sources | AI won't cite inaccurate content |
| Specific numbers and data points | "3x faster retention" > "faster retention" |
| Clear heading structure (H2s answer sub-questions) | AI extracts sections by heading |
| Page renders fully without JavaScript | AI crawlers often non-rendering |

---

## PART 9: SEO ROADMAP

### WEEK 1 — FOUNDATIONS
**Learn:**
- Google Search Console setup (verify domain, submit sitemap)
- Bing Webmaster Tools setup
- GA4 (Google Analytics 4) installation
- Screaming Frog installation (free version sufficient initially)

**Research:**
- Audit top 5 competitors:
  - What pages do they have? (Screaming Frog their site)
  - What keywords do they rank for? (Ahrefs free tools or Ubersuggest)
  - What content types? (blog, comparison, alternative pages)
- Brainstorm 50+ seed keywords across all funnel stages
- Validate with Google autocomplete + People Also Ask
- Map keywords to page types

---

### WEEK 2 — TECHNICAL IMPLEMENTATION
**Implement:**
- `app/layout.tsx` — global metadata template
- `app/sitemap.ts` — dynamic sitemap generation
- `app/robots.ts` — robots rules
- Canonical tags on every page type
- OpenGraph + Twitter card tags on every page
- `next.config.js` — www redirect, security headers
- Verify HTTPS enforced everywhere
- Fix any render-blocking resources (Lighthouse)
- Add `lang` attribute to HTML element
- Set up image optimization (WebP, explicit dimensions)

---

### WEEK 3 — ON-PAGE + SCHEMA
**Implement:**
- Homepage: clear H1, meta description, Organization schema, SoftwareApplication schema
- Feature pages (one per feature): title, description, H1, FAQ schema, canonical
- Pricing page: SoftwareApplication + Offer schema
- 1-2 comparison pages: structured, honest comparison + FAQ schema
- 1-2 alternative pages
- Blog infrastructure: Article schema template, author bio pages
- BreadcrumbList schema on all non-homepage pages
- Internal linking audit: homepage → feature pages → blog posts

---

### WEEK 4 — PRE-LAUNCH AUDIT + SUBMISSION
**Audit:**
- Full Screaming Frog crawl → fix all 404s, redirect chains, missing titles
- PageSpeed Insights on all key pages → fix CWV issues
- Rich Results Test on all schema pages → fix warnings
- Mobile-friendly test → fix any issues
- Manual review: every page has unique title, H1, canonical, meta description

**Submit:**
- Submit sitemap to Google Search Console
- Submit sitemap to Bing Webmaster Tools
- Request indexing for 10 most important pages via GSC URL Inspection

---

### MONTH 2 — CONTENT LAUNCH
**Execute:**
- Publish 2-4 blog posts targeting informational queries
- Each post: proper schema, internal links to relevant features, 1000+ words
- Build first topic cluster: pillar page + 3-4 cluster articles
- Monitor GSC for first indexing signals
- Fix any crawl errors appearing in GSC

---

### MONTH 3 — AUTHORITY BUILDING
**Analyze:**
- Which pages got impressions? Click rate reasonable?
- Which pages indexed? Any indexing issues in GSC?

**Execute:**
- Product Hunt launch → press coverage → backlinks
- Submit to SaaS directories: G2, Capterra, ProductHunt, BetaList, SaaSHub
- HARO (Help A Reporter Out) → expert quotes → media backlinks
- Guest post outreach to EdTech blogs
- Create one "skyscraper" piece targeting your most competitive informational keyword

---

### MONTH 4-6 — OPTIMIZATION CYCLE
**Analyze monthly:**
- GSC Performance: impressions trending up? CTR improving?
- Pages ranking 4-10: these are "almost there" — add content, get 1-2 backlinks → push to top 3
- Pages with high impressions, low CTR: fix title/meta description
- Pages not indexed: diagnose (crawl error? thin content? canonical issue?)
- CWV report in GSC: any pages newly failing?

**Execute:**
- Update + republish old blog posts with new information
- Expand programmatic SEO if applicable (decks, use cases, topics)
- Add more comparison/alternative pages as you identify competitors being searched
- Build content around products/companies adjacent to yours (EdTech ecosystem)

---

### MONTH 7-12 — SCALE + AUTHORITY
**Execute:**
- Systematic link building (identify broken links on other sites that you can replace)
- Video SEO: YouTube content → embed on site → dual ranking opportunity
- Expand topic cluster to adjacent topics
- Implement Content/editorial calendar: consistent publishing velocity
- Monitor AI Overview appearances in GSC
- Optimize featured snippet targets: identify queries where you rank 1-3 but no featured snippet → restructure content as definition, numbered list, or comparison table

**Advanced:**
- Structured content experiments (test different FAQ formats, compare snippets earned)
- Entity building (get mentioned on Wikidata, industry publications)
- International SEO if expanding to non-English markets (hreflang setup)

---

## PART 10: SAAS PROJECT REVIEW LENS

When you share Spark.E codebase, I'll audit it like a senior SEO engineer.

### FILES I'LL EXAMINE

**SEO-critical files (check these first):**
```
app/layout.tsx                    → Global metadata, fonts
app/page.tsx                      → Homepage content + metadata
app/sitemap.ts (or sitemap.xml)   → Exists? Correct?
app/robots.ts (or robots.txt)     → Rules correct?
next.config.js                    → Redirects, headers

app/blog/[slug]/page.tsx          → Dynamic metadata?
app/features/*/page.tsx           → Per-feature metadata?
app/pricing/page.tsx              → Schema? Metadata?
app/compare/*/page.tsx            → If exists

public/                           → OG images present?
components/
  Header/                         → Nav link structure
  Footer/                         → Important links present?
```

---

### WHAT I'LL REPORT

#### MISSING
- No `generateMetadata` on dynamic routes (every `[slug]` page)
- Missing `app/sitemap.ts`
- Missing `app/robots.ts`
- No canonical tags
- No OG images
- No schema anywhere
- Missing meta descriptions
- No breadcrumb navigation

#### WRONG
- Title template not consistent (`%s | Spark.E` missing)
- Canonical pointing to http:// instead of https://
- Canonical with trailing slash inconsistency
- H1 not on page, or multiple H1s
- Images without alt text or dimensions
- CSR (`"use client"` + `useEffect` fetch) for public content pages
- Robots.txt blocking important paths
- Sitemap including auth-only pages

#### HARMFUL
- `noindex` on pages that should rank
- `robots.txt` accidentally blocking entire site or critical CSS/JS
- Redirect chains (A → B → C → page)
- Duplicate page content without canonical (e.g., `/flashcards` and `/flashcards/` both exist without canonical)
- Session or user IDs leaking into public URLs
- Dynamic `import(..., { ssr: false })` on components containing SEO content

#### SHOULD IMPROVE
- Title tags not including primary keyword near front
- Meta descriptions too short/long or not compelling
- No FAQ schema on feature/landing pages
- Blog posts missing Article schema
- No BreadcrumbList schema on any pages
- Homepage not linking to feature pages internally
- Blog posts not internally linking to relevant features
- Pricing page not using SoftwareApplication + Offer schema
- No programmatic SEO strategy (decks, topics pages)
- Public docs hidden behind authentication

#### ALREADY GOOD
- Whatever I find implemented correctly (I'll acknowledge it)

---

### HOW TO SHARE CODEBASE FOR AUDIT

Paste these files directly:
1. `app/layout.tsx`
2. `app/page.tsx`
3. `app/sitemap.ts`
4. `app/robots.ts`
5. `next.config.js`
6. One example of `app/[dynamic-route]/page.tsx`
7. `app/blog/[slug]/page.tsx`

I'll provide line-by-line audit with specific fixes.

---

*Build SEO in from day one. Every public page needs: title, description, canonical, OG tags. Every route group needs sitemap coverage. Every content page needs schema. This is not optional for a SaaS competing in search.*
