# Phase 2: Content Requirements Guide

**Purpose**: Template requirements, schema rules, and best practices for creating Phase 2 pages.

---

## Page Type Templates

### Hub Page Template (Pillar Pages)

**Examples**: /lifestyle/, /guides/, /food/, /chiang-mai/

**Structure**:

```
1. H1 Title (e.g., "Living in Chiang Mai: Complete Lifestyle Guide")

2. Meta Description (150-160 chars)
   "Complete guide to cost of living, neighborhoods, expat life, and daily logistics in Chiang Mai. Find your perfect area to relocate."

3. Introduction Paragraph (100-150 words)
   - What is this page about?
   - Who is it for?
   - What will they learn?
   - Teaser of main sections

4. Quick Navigation Cards or Table of Contents
   - Linked list to all major clusters
   - Visual card layout (optional but recommended)

5. Body Sections (4-6 main sections)
   - Section 1: Overview or context
   - Section 2-5: Major topics (cost, neighborhoods, expat life, etc.)
   - Each section: 300-400 words, links to related cluster page
   - Use H2 for section headers

6. CTA Section (optional)
   - "Start your moving checklist" or "Explore neighborhoods"
   - Link to convergence page (/lifestyle/moving-checklist/)

7. FAQ Section (minimum 5 Q&A pairs)
   - Natural questions people ask
   - 2-3 sentence answers
   - Schema: FAQPage markup required

8. Related Resources Sidebar
   - 3-4 links to other major pages
   - Anchor text: descriptive ("Cost breakdown" not "click here")

9. Author/Updated Info
   - By: [Author Name]
   - Last Updated: [Date]
   - Position/credentials

**Word Count**: 2500-3500 words

**Required Schema**:
- Article (author, datePublished, dateModified, image)
- BreadcrumbList
- FAQPage (minimum 5 Q&A blocks)
- Organization (optional, on homepage)

**Links Required**:
- Outgoing: 5-7 links to major clusters or detail pages
- Sidebar: 2-3 related page links
- Footer: Link back to parent hub (if applicable)
- Anchor text: Varied, descriptive, keyword-relevant

**Images**:
- Hero image: 1200x600px or larger, optimized WebP
- Section images: 2-3 additional images throughout
- All images: Descriptive alt text (not filename)
- Format: WebP preferred, JPG fallback

**Meta Tags**:
- Title (60 chars max): "[Topic] in Chiang Mai: Complete Guide"
- Description (150-160 chars): Key topics + benefit + CTA
- Keywords (optional): 3-5 primary + secondary keywords

---

### Cluster Page Template (Topic Clusters)

**Examples**: /lifestyle/cost-of-living.html, /lifestyle/neighborhoods.html, /guides/transport/

**Structure**:

```
1. H1 Title (e.g., "Cost of Living in Chiang Mai: 2026 Breakdown")

2. Meta Description (150-160 chars)
   "Detailed breakdown of monthly costs in Chiang Mai including rent, food, transport, utilities, and entertainment. Real expat budgets."

3. Introduction (50-100 words)
   - What this page covers
   - Key takeaway (e.g., "Average monthly cost: $800-1200")
   - Who should read

4. Quick Stats Block (optional)
   - Visual callout: Average rent, food cost, budget needed
   - Format: Table or highlighted box
   - Data must be current (2026)

5. Body Sections (4-5 main sections)
   - Section 1: Overview or context (200-300 words)
   - Section 2-4: Detailed breakdowns (300-400 words each)
   - Section 5: Conclusion or comparison (200-300 words)
   - Use H2 for sections, H3 for subsections

6. Comparison Table (if applicable)
   - Table format for cost breakdowns
   - Columns: Category, Cost, Notes
   - Example row: "1-Bedroom Apartment (Nimman): 8,000-12,000 THB"

7. Internal Links Section (minimum 3)
   - Links to detail pages or related clusters
   - Embedded naturally in body
   - Sidebar: 2-3 related links

8. FAQ Section (minimum 3-5 Q&A pairs)
   - Common questions about this topic
   - Schema: FAQPage markup required

9. Updated Info
   - Last Updated: [Date]
   - Sources: [List of sources]
   - Author: [Optional]

**Word Count**: 1500-2000 words

**Required Schema**:
- Article (author, datePublished, dateModified)
- BreadcrumbList (essential for nested pages)
- FAQPage (minimum 3-5 Q&A blocks)

**Links Required**:
- Outgoing: 3-5 links (2-3 to parent/siblings, 1-2 to detail pages)
- Sidebar: 2-3 related page links
- Back link: Parent hub page

**Anchor Text Examples**:
- "Cost breakdown by neighborhood" (descriptive)
- "See Nimman neighborhood profile" (specific)
- "More on daily living costs" (contextual)
- AVOID: "Click here", "Read more", "Learn more"

**Images**:
- Hero: 1200x600px, optimized
- Inline: 1-2 relevant images (e.g., neighborhood photo for cost-by-area page)
- All: Descriptive alt text

---

### Detail Page Template (Neighborhood & Deep-Dive Pages)

**Examples**: /lifestyle/neighborhoods/nimman.html, /lifestyle/neighborhoods/old-city.html

**Structure**:

```
1. H1 Title (e.g., "Living in Nimman, Chiang Mai: Expat Guide & Cost Breakdown")

2. Meta Description (150-160 chars)
   "Complete guide to Nimman neighborhood in Chiang Mai: cost of living, expat community, nightlife, restaurants, and lifestyle tips."

3. Quick Facts Callout (optional)
   - Box with: Population, Primary residents (expats?), Vibe, Best for, Cost level
   - Format: Visual box or 2-column layout

4. Introduction (75-100 words)
   - What is this neighborhood?
   - Who lives there?
   - Why might someone choose it?

5. Body Sections (6-8 main sections)
   - Section 1: Neighborhood Overview (200-300 words) — Vibe, history, character
   - Section 2: Cost of Living (250-350 words) — Rent, food, transport breakdown
   - Section 3: Accommodation & Housing (200-300 words) — Rental market, prices, neighborhoods within
   - Section 4: Food & Dining (200-300 words) — Restaurants, cafes, street food, budget options
   - Section 5: Activities & Nightlife (150-250 words) — Bars, clubs, activities, shopping
   - Section 6: Transport & Accessibility (150-200 words) — How to get around, proximity to city
   - Section 7: Expat Community (150-200 words) — Size, hangout spots, expat density
   - Section 8: Pros & Cons (150-200 words) — Who should live here, trade-offs

6. Comparison Table (optional)
   - Compare to other neighborhoods in site
   - Columns: Neighborhood, Rent (1BR), Food Cost, Expat Presence

7. Photo Gallery (optional but recommended)
   - 3-4 neighborhood photos
   - All with descriptive alt text
   - Examples: "Nimman district Chiang Mai street scene", "Expat cafe in Nimman"

8. Related Neighborhoods Links
   - 2-3 links to sibling neighborhood pages
   - Anchor: Neighborhood names (e.g., "Old City neighborhood", "Riverside area")

9. Related Information Links
   - Link to /lifestyle/cost-of-living-by-neighborhood/ (cost context)
   - Link to /food/restaurants-nimman.html (dining guide, if exists)

10. FAQ Section (minimum 3 Q&A pairs)
    - "Is Nimman good for expats?"
    - "How much rent in Nimman?"
    - "Best cafes in Nimman?"

**Word Count**: 1200-1600 words

**Required Schema**:
- Article (author, datePublished, dateModified)
- BreadcrumbList (critical: Home > Lifestyle > Neighborhoods > Nimman)
- FAQPage (minimum 3 Q&A blocks)
- LocalBusiness (optional: reference restaurants/landmarks in area)

**Links Required**:
- Parent: /lifestyle/neighborhoods/ (back link essential)
- Siblings: 2-3 other neighborhood pages (Nimman → Old City, Riverside, etc.)
- Related clusters: /food/restaurants-[neighborhood], /lifestyle/cost-of-living/
- Total outbound: 4-6 links maximum

**Anchor Text Examples**:
- "Back to neighborhoods overview"
- "Explore Old City" (linking to sibling)
- "Restaurants in Nimman" (linking to food guide)
- "Cost of living comparison"

**Images**:
- Hero: 1200x600px neighborhood photo
- Inline: 2-3 additional images (cafe, street scene, apartment)
- All: Descriptive alt text (location/context, not generic)
- Format: WebP or JPG, optimized for web

---

### Long-Tail & Comparison Page Template

**Examples**: /lifestyle/chiang-mai-vs-bangkok.html, /lifestyle/cost-of-living-breakdown.html

**Structure**:

```
1. H1 Title (e.g., "Chiang Mai vs Bangkok: Cost of Living & Lifestyle Comparison")

2. Meta Description (150-160 chars)
   "Compare living in Chiang Mai vs Bangkok: costs, lifestyle, expat community, and pros/cons. Which city is right for you?"

3. Introduction (50-75 words)
   - What are you comparing?
   - Key finding (e.g., "Chiang Mai is 30% cheaper than Bangkok")

4. Comparison Table (essential)
   - Columns: Category, Chiang Mai, Bangkok, Difference/Notes
   - Rows: Rent, Food, Transport, Entertainment, Cost of Living Index
   - Format: Clear, visual, scannable

5. Body Sections (4-5)
   - Section 1: Cost Comparison (300-400 words)
   - Section 2: Lifestyle Comparison (250-350 words)
   - Section 3: Expat Community (200-300 words)
   - Section 4: Pros & Cons (250-350 words)
   - Section 5: Conclusion (100-150 words)

6. Related Pages
   - Links to related pages in both cities
   - Example: Link to /lifestyle/cost-of-living/ (Chiang Mai cost overview)

7. FAQ Section (minimum 3-5 Q&A pairs)
   - "Is Chiang Mai cheaper than Bangkok?"
   - "Which city is better for expats?"
   - "Can I live on $800 in Chiang Mai?"

**Word Count**: 1000-1500 words (can be shorter than cluster pages)

**Required Schema**:
- Article
- BreadcrumbList
- FAQPage

**Links**: 3-4 outgoing links (to related cluster pages)

---

## Schema Markup Requirements

### Article Schema (Required on ALL pages)

Every page must have Article schema with these fields:

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "H1 title of the page",
  "description": "Meta description (160 chars)",
  "image": "https://...image-url",
  "datePublished": "2026-05-24",
  "dateModified": "2026-05-24",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://chiangmaiambassador.com/about"
  }
}
```

**Fields**:
- `headline`: Your H1 title (max 110 chars)
- `description`: Meta description (120-160 chars)
- `image`: Hero image URL (1200x600px minimum)
- `datePublished`: Original publish date
- `dateModified`: Last update date (CRITICAL for freshness signals)
- `author`: Name of content author (credibility)

---

### BreadcrumbList Schema (Required on nested pages)

Required on ALL pages except homepage and top-level sections.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://chiangmaiambassador.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Chiang Mai",
      "item": "https://chiangmaiambassador.com/chiang-mai/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Lifestyle",
      "item": "https://chiangmaiambassador.com/lifestyle/"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "Neighborhoods",
      "item": "https://chiangmaiambassador.com/lifestyle/neighborhoods/"
    },
    {
      "@type": "ListItem",
      "position": 5,
      "name": "Nimman",
      "item": "https://chiangmaiambassador.com/lifestyle/neighborhoods/nimman.html"
    }
  ]
}
```

**Rules**:
- Position 1: Always "Home"
- Position N: Current page (last item)
- Each item: "name" (display text) + "item" (URL)
- Order: Must match actual site structure/navigation

---

### FAQPage Schema (Required on hub & cluster pages)

All hub and cluster pages must have minimum 3-5 Q&A blocks.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does it cost to live in Chiang Mai?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Average monthly budget for a comfortable lifestyle is $800-1200, including rent ($300-600), food ($200-300), transport ($50-100), and entertainment ($150-300)."
      }
    },
    {
      "@type": "Question",
      "name": "Is Chiang Mai good for expats?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, Chiang Mai has a large expat community, low cost of living, excellent food scene, and a vibrant local culture. It's popular with digital nomads, retirees, and relocating families."
      }
    }
  ]
}
```

**Requirements**:
- Minimum 3 Q&A pairs for detail pages
- Minimum 5 Q&A pairs for hub/cluster pages
- Question: Natural language question (how people actually ask)
- Answer: 1-3 sentence response (concise, extractable)
- Schema must be JSON-LD format (in <script> tag)

**Questions to include**:
- Hub pages: General topic overview questions
- Cluster pages: Specific sub-topic questions
- Detail pages: Location/area-specific questions

---

## Internal Linking Requirements

### Link Rules by Page Type

| Page Type | Links TO (Up) | Links TO (Sideways) | Links TO (Down) | Total Links | Link Density |
|-----------|---------------|-------------------|-----------------|------------|--------------|
| Hub | — | Other hubs (optional) | 5-7 cluster pages | 5-7 | 1 per 400-500 words |
| Cluster | Parent hub | 2-3 sibling clusters | 3-4 detail pages | 5-8 | 1 per 300-400 words |
| Detail | Parent cluster | 1-3 sibling details | — | 3-5 | 1 per 250-350 words |

### Anchor Text Guidelines

**DO**:
- Use descriptive anchor text
- Match keyword intent (but naturally)
- Vary anchors throughout page
- Use brand/neighborhood names when appropriate
- Use question-based anchors: "How much does rent cost in Nimman?"

**Example anchors for /lifestyle/cost-of-living/ page**:

| Target | Anchor Text |
|--------|------------|
| /lifestyle/neighborhoods/ | "See neighborhood cost comparison" |
| /lifestyle/cost-of-living-by-neighborhood.html | "Cost of living by neighborhood" |
| /lifestyle/chiang-mai-vs-bangkok.html | "Chiang Mai vs Bangkok comparison" |
| /guides/daily-living-guide.html | "More on daily living costs" |
| /guides/transport/ | "Transport costs and options" |

**AVOID**:
- "Click here" or "Read more" (3+ uses)
- Exact match anchors (excessive)
- Branded terms on every link
- Keyword stuffing in anchors

### Link Placement Priority

**Best placement** (highest value):
1. First paragraph (if contextually relevant)
2. Body copy (within relevant section)
3. Related resources sidebar (alternative)
4. End of page (least valuable)

**AVOID placement**:
- Footer (unless major hub)
- Sidebar only (should be in body)
- Excessive clustering (all links in one paragraph)

---

## Content Best Practices

### Content Depth

**Hub pages**:
- Comprehensive overview of entire topic
- Scan-friendly (use H2/H3, short paragraphs, tables)
- Multiple entry points (links to related pages)

**Cluster pages**:
- Specific topic breakdown
- 4-5 main sections with clear structure
- Comparison tables where applicable

**Detail pages**:
- Depth in ONE specific area (Nimman neighborhood)
- Practical, actionable information
- Use photos/images to enhance

### Extractability (Important for AI Search)

Pages must be **extractable** — individual paragraphs should work standalone.

**Good extractability**:
> "Average rent in Nimman is 10,000-15,000 THB per month for a 1-bedroom apartment. Studio apartments range from 8,000-12,000 THB. Prices have increased 10-15% since 2024."

**Poor extractability**:
> "Rent here is very reasonable compared to other areas."

### Statistics & Data

**Requirements**:
- Include specific numbers (not "affordable" or "cheap")
- Cite sources (e.g., "As of May 2026...")
- Use current data (2026)
- Format: Currency, exact amounts, date context

**Example**:
> "As of May 2026, monthly rent in Nimman ranges from 10,000-15,000 THB ($270-$410 USD) for 1-bedroom apartments, according to local landlord surveys."

### Fresh Content Signals

**Every page must have**:
- `datePublished`: Original publication date (e.g., 2026-05-24)
- `dateModified`: Last update date (visible in HTML: "Last updated: May 24, 2026")
- Author name (credibility signal)
- Sources cited (where applicable)

---

## Common Pitfalls to Avoid

| Pitfall | Problem | Solution |
|---------|---------|----------|
| No outbound links | Looks thin, limits authority flow | Add 4-6 relevant links per page |
| Too many outbound links | Dilutes authority | Limit to 1 link per 150-200 words |
| Identical anchor text repeated | Looks over-optimized | Rotate anchors (cost vs cost of living vs expenses) |
| No freshness signals | Old content, lower AI priority | Add "Last updated: Date" visible on page |
| Missing schema | AI systems can't understand structure | Validate with Google Rich Results Test |
| Poor heading structure | Hard to scan, impacts SEO | Use H1 once, then H2/H3 for sections |
| Orphaned pages | No incoming links, won't rank | Ensure every page has ≥2 incoming links |
| No FAQ section | Low AI search visibility | Add minimum 3-5 Q&A blocks with FAQPage schema |
| Keywords not in subheadings | Miss ranking opportunity | Include target keyword in H2 or H3 |
| External links only | Doesn't distribute internal authority | Add 3-5 internal links per page |
| Generic "Read more" links | Wasted SEO opportunity | Use descriptive anchors with keywords |
| Outdated cost data | Loss of credibility | Verify all numbers are current (2026) |

---

## Quality Checklist (Before Publishing)

**Content**:
- [ ] Word count meets tier requirement (hub 2500+, cluster 1500+, detail 1200+)
- [ ] H1 tag is present and descriptive (not generic)
- [ ] Meta description is 150-160 characters
- [ ] Introduction paragraph explains scope and audience
- [ ] Body sections are 4-6 major sections (H2 headers)
- [ ] All numbers/statistics are current (2026) and cited
- [ ] Conclusion or summary at end

**Links**:
- [ ] 4-7 outbound internal links (matching page type)
- [ ] All anchors are descriptive (not "click here")
- [ ] Link targets match intent (not random)
- [ ] 1-2 links in first paragraph, rest distributed
- [ ] Sidebar has 2-3 related links
- [ ] No more than 1 link per 150-200 words

**Schema**:
- [ ] Article schema present (headline, author, dateModified)
- [ ] BreadcrumbList schema present (if nested page)
- [ ] FAQPage schema with 3+ Q&A blocks
- [ ] Validate in Google Rich Results Test
- [ ] All dates in ISO format (YYYY-MM-DD)

**Images**:
- [ ] Hero image present (1200x600px minimum)
- [ ] All images have descriptive alt text
- [ ] Images are optimized (JPG or WebP, <200KB)
- [ ] At least 2-3 additional images for detail pages

**SEO**:
- [ ] No spelling/grammar errors
- [ ] Mobile-friendly formatting
- [ ] Paragraphs 2-4 sentences max
- [ ] Lists used for multiple items (not prose)
- [ ] No keyword stuffing or over-optimization

**Freshness**:
- [ ] "Last updated: [Date]" visible on page
- [ ] Author name and credentials visible
- [ ] Current data/statistics (not dated information)
- [ ] Sources cited (links to references)

---

**Document**: PHASE_2_CONTENT_REQUIREMENTS.md  
**Created**: 2026-05-24  
**Status**: Ready for reference during implementation  
**Last Updated**: 2026-05-24
