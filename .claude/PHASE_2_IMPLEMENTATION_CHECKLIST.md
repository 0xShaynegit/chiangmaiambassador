# Phase 2: Implementation Checklist

**Phase**: Phase 2 — Authority Architecture  
**Status**: Ready for implementation  
**Date**: 2026-05-24  
**Target Completion**: 2026-06-14 (4 weeks)

---

## Quick Summary

**What we're building**: Topical authority for "Chiang Mai living" by creating a silo structure around lifestyle, guides, food, and community. Visa content becomes an addon that links OUT to cmlocals.

**Key focus areas**:
1. Create missing hub pages (/lifestyle/, /food/)
2. Create neighborhood deep-dives
3. Create comparison content (cost of living variants)
4. Create convergence pages (moving checklists)
5. Implement internal linking architecture

**Total new pages needed**: ~20-25 pages (high priority) + programmatic variants (Phase 4)

---

## Phase 2 Week-by-Week Breakdown

### WEEK 1: FOUNDATION (May 27 - Jun 2)

#### New Pages to Create

- [ ] `/lifestyle/index.html` — Lifestyle hub page
  - Status: NEW
  - Word count: 2500-3500
  - Links to: cost-of-living, neighborhoods, expat-life-guide, daily-living-guide, moving-checklist
  - Schema: Article, BreadcrumbList, FAQPage
  - Priority: CRITICAL (blocks other work)

- [ ] `/lifestyle/moving-checklist.html` — Funnel convergence page (lifestyle view)
  - Status: NEW
  - Word count: 1800-2200
  - Sections: Before you go, choosing where to live, budgeting, packing, initial setup
  - Links to: neighborhoods, cost-of-living, expat-guide, daily-living, /guides/moving-here-checklist, /visa/
  - Schema: Article, HowTo, FAQPage
  - Priority: HIGH

- [ ] `/lifestyle/neighborhoods/nimman.html` — Nimman neighborhood deep-dive
  - Status: NEW (detail page)
  - Word count: 1200-1600
  - Content: Vibe, cost breakdown, transport, restaurants, expat presence, nightlife, pros/cons
  - Links: Parent (/lifestyle/neighborhoods/), siblings (Old City, Riverside), /food/restaurants-nimman
  - Schema: Article, LocalBusiness (reference), FAQPage
  - Priority: HIGH

- [ ] `/lifestyle/neighborhoods/old-city.html` — Old City neighborhood deep-dive
  - Status: NEW (detail page)
  - Word count: 1200-1600
  - Content: Historic vibe, temples, cost, culture, transport, dining, expat numbers
  - Links: Parent (/lifestyle/neighborhoods/), siblings, /food/restaurants-old-city
  - Schema: Article, LocalBusiness, FAQPage
  - Priority: HIGH

- [ ] `/lifestyle/neighborhoods/riverside.html` — Riverside neighborhood deep-dive
  - Status: NEW (detail page)
  - Word count: 1200-1600
  - Content: Suburban vibe, cost, garden houses, families, quietness, transport, proximity
  - Links: Parent, siblings, /food/restaurants-riverside
  - Schema: Article, LocalBusiness, FAQPage
  - Priority: HIGH

#### Updates to Existing Pages

- [ ] Update `/visa/index.html` — Restructure as addon
  - Status: RESTRUCTURE
  - New direction: Brief overview, "See detailed visa info at cmlocals", contextual links OUT
  - Links to: cmlocals (main), /lifestyle/moving-checklist/, /guides/permits/
  - Remove: Detailed visa content (keep links to cmlocals instead)
  - Priority: HIGH

- [ ] Update template.html navigation
  - Add: `/lifestyle/` to main nav
  - Add: `/food/` to main nav or dropdown
  - Update breadcrumb navigation support
  - Priority: MEDIUM

**Week 1 Completion Criteria**:
- 5 new pages created and published
- /visa/ restructured
- Navigation updated in template
- All 5 pages have schema markup

---

### WEEK 2: EXPANSION (Jun 3 - Jun 9)

#### New Pages to Create

- [ ] `/lifestyle/neighborhoods/chiang-mai-land.html` — Chiang Mai Land neighborhood deep-dive
  - Status: NEW (detail page)
  - Word count: 1200-1600
  - Content: Residential area, expat community, cost, family-friendly, schools
  - Links: Parent, siblings
  - Schema: Article, LocalBusiness, FAQPage
  - Priority: HIGH

- [ ] `/lifestyle/expat-life-guide.html` — Expat life comprehensive guide
  - Status: NEW (cluster page)
  - Word count: 1500-2000
  - Content: Dating, relationships, making friends, cultural adaptation, integrating with locals, community
  - Links to: /pages/getting-social-in-chiang-mai, /lifestyle/us-expat-tax-guide, /guides/resources/
  - Links from: /lifestyle/ hub, /chiang-mai/
  - Schema: Article, FAQPage
  - Priority: HIGH

- [ ] `/lifestyle/daily-living-guide.html` — Daily living practical guide
  - Status: NEW (cluster page)
  - Word count: 1500-2000
  - Content: Utilities (water, electricity), internet/phone, banking, housing rental process, healthcare basics, transport basics
  - Links to: /guides/permits/, /guides/transport/, /guides/health/, /lifestyle/cost-of-living/
  - Links from: /lifestyle/ hub
  - Schema: Article, HowTo, FAQPage
  - Priority: HIGH

- [ ] `/guides/moving-here-checklist.html` — Moving checklist (logistics view)
  - Status: NEW (cluster page)
  - Word count: 1500-2000
  - Content: Pre-arrival (visa, planning), on-arrival (accommodation, registration, permits), setup (banking, utilities, insurance)
  - Links to: /guides/permits/, /guides/transport/, /guides/health/, /visa/ → cmlocals, /lifestyle/moving-checklist
  - Links from: /guides/ hub
  - Schema: Article, HowTo, FAQPage
  - Priority: HIGH

- [ ] `/lifestyle/chiang-mai-vs-bangkok.html` — Chiang Mai vs Bangkok comparison
  - Status: NEW (long-tail page)
  - Word count: 1400-1800
  - Content: Cost comparison (rent, food, transport, entertainment), lifestyle differences, expat community size, weather
  - Links to: /lifestyle/cost-of-living/, /lifestyle/neighborhoods/
  - Links from: /lifestyle/cost-of-living/ hub
  - Schema: Article, FAQPage
  - Priority: MEDIUM

#### Updates to Existing Pages

- [ ] Update `/lifestyle/neighborhoods.html` — Expand cluster page
  - Status: UPDATE (add structure and links)
  - Add: Introduction text (2-3 paragraphs)
  - Add: Table of neighborhoods with quick stats (Nimman, Old City, Riverside, CMland, etc.)
  - Add: Links to new detail pages
  - Add: Navigation cards linking to each neighborhood
  - Links to: All detail pages, cost-of-living sidebar
  - Schema: Add BreadcrumbList
  - Priority: MEDIUM

- [ ] Update `/lifestyle/cost-of-living.html` — Optimize cluster page
  - Status: UPDATE (improve structure and links)
  - Add: Link to new cost-of-living-by-neighborhood page
  - Add: Link to chiang-mai-vs-bangkok page
  - Add: Navigation sidebar with other lifestyle topics
  - Schema: Verify Article, BreadcrumbList present
  - Priority: MEDIUM

**Week 2 Completion Criteria**:
- 5 new pages created and published
- 2 existing pages updated with links and structure
- All new pages have schema markup
- Total 10 pages now have proper internal linking

---

### WEEK 3: INTEGRATION & FOOD HUB (Jun 10 - Jun 16)

#### New Pages to Create

- [ ] `/food/index.html` — Food & dining hub page
  - Status: NEW (hub page)
  - Word count: 2000-2500
  - Content: Food culture overview, restaurant guide intro, local food guide, budget eating, by neighborhood
  - Links to: /food/restaurants-by-neighborhood/, /food/local-food-guide.html, /food/budget-eating.html
  - Links from: /chiang-mai/, nav
  - Schema: Article, BreadcrumbList, FAQPage
  - Priority: MEDIUM

- [ ] `/lifestyle/cost-of-living-by-neighborhood.html` — Cost of living breakdown by area
  - Status: NEW (long-tail page)
  - Word count: 1600-2000
  - Content: Table with Nimman, Old City, Riverside, CMland, Nimmanhaemin, Chiang Mai Land costs (rent, food, transport)
  - Links to: Individual neighborhood pages
  - Links from: /lifestyle/cost-of-living/, /lifestyle/neighborhoods/
  - Schema: Article, FAQPage
  - Priority: MEDIUM

- [ ] `/lifestyle/chiang-mai-vs-se-asia.html` — Regional cost comparison
  - Status: NEW (long-tail page)
  - Word count: 900-1200
  - Content: Chiang Mai vs Bangkok, Chiang Mai vs Ho Chi Minh City, Chiang Mai vs Hanoi, Chiang Mai vs Phuket
  - Links to: /lifestyle/cost-of-living/, /lifestyle/chiang-mai-vs-bangkok/
  - Links from: /lifestyle/ hub, /lifestyle/cost-of-living/
  - Schema: Article, FAQPage
  - Priority: LOW

#### Updates to Existing Pages

- [ ] Implement internal linking architecture across all pages
  - Status: UPDATE (all pages created in weeks 1-2)
  - Action: Update all cluster pages with lateral links (2-3 sibling links each)
  - Action: Add related sidebar/suggestion blocks to detail pages
  - Action: Verify all links use descriptive anchor text (not "click here")
  - Priority: HIGH

- [ ] Add breadcrumb navigation to template.html
  - Status: UPDATE (template-level)
  - Add: Breadcrumb logic to article template
  - Test on: /lifestyle/neighborhoods/nimman.html, /guides/transport/, /food/restaurants-nimman
  - Display: Home > Category > Page
  - Schema: Implement BreadcrumbList on all nested pages
  - Priority: HIGH

- [ ] Update homepage and navigation
  - Status: UPDATE
  - Add: /lifestyle/ to main nav
  - Add: /food/ to main nav or footer
  - Add: Cards linking to /lifestyle/, /guides/, /food/, /pages/
  - Update: Any stale links or old structure references
  - Priority: MEDIUM

#### Schema Markup Audit

- [ ] Verify all new pages have:
  - [ ] Article schema (name, author, datePublished, dateModified, description)
  - [ ] BreadcrumbList schema (for nested pages)
  - [ ] FAQPage schema (at least 3 Q&A blocks)
  - [ ] Organization schema on hub pages
  - Checklist per page to ensure compliance
  - Priority: HIGH

**Week 3 Completion Criteria**:
- 3 new pages created
- Internal linking architecture deployed across all ~16 pages
- Breadcrumb navigation implemented
- Schema markup complete and validated
- Homepage/nav updated with new silos

---

### WEEK 4: QA & DOCUMENTATION (Jun 17 - Jun 23)

#### Crawl Depth Audit

- [ ] Verify all Tier 1 pages ≤2 clicks from home
  - /chiang-mai/ — should be 1 click (nav)
  - /lifestyle/ — should be 1-2 clicks (nav)
  - /guides/ — should be 1-2 clicks (nav)
  - /food/ — should be 1-2 clicks (nav)

- [ ] Verify all Tier 2 pages ≤3 clicks from home
  - /lifestyle/neighborhoods/ — 2-3 clicks
  - /lifestyle/cost-of-living/ — 2-3 clicks
  - /guides/moving-here-checklist/ — 3 clicks
  - /food/restaurants-by-neighborhood/ — 3 clicks

- [ ] Check for orphaned pages (no incoming links)
  - Run: Internal link analysis
  - Action: Add links to any orphaned pages
  - Target: 100% of pages have ≥2 incoming links

- [ ] Validate no excessive crawl depth
  - Deepest page: ≤4 clicks from home (acceptable for detail pages)
  - Example: /lifestyle/neighborhoods/nimman — 4 clicks (home > chiang-mai > lifestyle > neighborhoods > nimman)

#### Content Quality Checks

- [ ] Word count validation
  - Hub pages: 2500-3500 ✓
  - Cluster pages: 1500-2000 ✓
  - Detail pages: 1200-1600 ✓
  - Long-tail pages: 800-1200 ✓

- [ ] Schema validation
  - Use: Google Rich Results Test
  - Check: All Article, BreadcrumbList, FAQPage valid
  - Check: No schema warnings/errors

- [ ] Meta description check
  - All pages: 150-160 characters
  - Format: Keyword + benefit + call-to-action
  - Example: "Discover neighborhood profiles, costs, and lifestyle in Chiang Mai. Find the best area for your relocation."

- [ ] H1 tag validation
  - All pages: Exactly 1 H1
  - Content: Matches page title (usually)
  - Example: "Moving Checklist: Your Complete Guide to Relocating to Chiang Mai"

- [ ] Image alt text audit
  - All images: Descriptive alt text (not filename)
  - Example: "Nimman district Chiang Mai with expat cafes and restaurants"

#### Link Validation

- [ ] Anchor text diversity audit
  - Check: No anchor text used more than 2-3 times across entire site
  - Action: Rotate synonyms and variations
  - Examples of safe anchors: "neighborhood guide", "cost of living", "Nimman profile", "see more"
  - Avoid: Exact match over-optimization

- [ ] Broken link check
  - Tool: Internal link validator or manual check
  - Action: Fix any 404s or broken links
  - Check: All /visa/ links point to correct cmlocals URLs

- [ ] Outbound link validation
  - Check: /visa/ pages link OUT to cmlocals (not internally)
  - Check: All external links open in new tab (if intended)
  - Action: Test URLs work

#### Documentation & Handoff

- [ ] Update sitemap.xml
  - Add: All new pages
  - Format: Standard XML sitemap
  - Include: Lastmod dates

- [ ] Update robots.txt
  - Verify: No unwanted Disallow rules
  - Verify: AI bots (GPTBot, PerplexityBot, ClaudeBot, Google-Extended) allowed

- [ ] Create Phase 2 completion report
  - Summary: Pages created, links added, schema deployed
  - Metrics: Crawl depth optimization, link density, orphan pages
  - Next steps: Phase 3 content optimization

- [ ] Prepare Phase 3 brief
  - Focus: Content depth (add statistics, sources, expert attribution)
  - Focus: AI search optimization (citations, extractability)
  - Focus: Refresh existing content (add "last updated", expand thin sections)

**Week 4 Completion Criteria**:
- Crawl depth audit: ✓ All priority pages ≤3 clicks
- Content quality: ✓ All pages meet word count, schema, metadata standards
- Link validation: ✓ No broken links, proper anchor text diversity
- Documentation: ✓ Sitemap updated, robots.txt verified, Phase 3 brief ready

---

## Page Status Tracker

### New Pages Required (20-25 pages)

| Page | URL | Word Count | Week | Status | Notes |
|------|-----|-----------|------|--------|-------|
| Lifestyle Hub | /lifestyle/ | 2500-3500 | 1 | TODO | Critical path |
| Moving Checklist (Lifestyle) | /lifestyle/moving-checklist.html | 1800-2200 | 1 | TODO | Funnel convergence |
| Nimman Guide | /lifestyle/neighborhoods/nimman.html | 1200-1600 | 1 | TODO | High search volume |
| Old City Guide | /lifestyle/neighborhoods/old-city.html | 1200-1600 | 1 | TODO | High search volume |
| Riverside Guide | /lifestyle/neighborhoods/riverside.html | 1200-1600 | 1 | TODO | Medium volume |
| Chiang Mai Land Guide | /lifestyle/neighborhoods/chiang-mai-land.html | 1200-1600 | 2 | TODO | Residential area |
| Expat Life Guide | /lifestyle/expat-life-guide.html | 1500-2000 | 2 | TODO | Cluster page |
| Daily Living Guide | /lifestyle/daily-living-guide.html | 1500-2000 | 2 | TODO | Practical logistics |
| Moving Checklist (Guides) | /guides/moving-here-checklist.html | 1500-2000 | 2 | TODO | Logistics focus |
| Chiang Mai vs Bangkok | /lifestyle/chiang-mai-vs-bangkok.html | 1400-1800 | 2 | TODO | Comparison page |
| Food Hub | /food/index.html | 2000-2500 | 3 | TODO | New hub page |
| Cost of Living by Neighborhood | /lifestyle/cost-of-living-by-neighborhood.html | 1600-2000 | 3 | TODO | Breakdown page |
| Chiang Mai vs SE Asia | /lifestyle/chiang-mai-vs-se-asia.html | 900-1200 | 3 | TODO | Comparison page |
| [Additional neighborhood guides] | /lifestyle/neighborhoods/[area].html | 1200-1600 | Phase 4 | TODO | Nimmanhaemin, etc. |
| [Programmatic variants] | /lifestyle/cost-living-[neighborhood].html | 400-700 | Phase 4 | TODO | Long-tail expansion |

### Pages to Update

| Page | URL | Update Type | Priority | Status | Notes |
|------|-----|-------------|----------|--------|-------|
| Neighborhoods | /lifestyle/neighborhoods.html | Expand structure | MEDIUM | TODO | Add table, detail links |
| Cost of Living | /lifestyle/cost-of-living.html | Improve links | MEDIUM | TODO | Add comparison links |
| Visa | /visa/index.html | Restructure | HIGH | TODO | Addon-only approach |
| Template | template.html | Nav update | HIGH | TODO | Add /lifestyle/, /food/ |
| Template | template.html | Breadcrumb | HIGH | TODO | Add BreadcrumbList support |
| Homepage | index.html | Add cards | MEDIUM | TODO | Link major hubs |

---

## Resource Requirements

### Content Assets Needed

- [ ] Neighborhood photos (Nimman, Old City, Riverside, CMland)
  - Count: 4-6 images per neighborhood
  - Format: JPG/WebP, optimized for web
  - Alt text: Descriptive (e.g., "Nimman district with expat cafes")
  - Priority: MEDIUM (not blocking, can be placeholders initially)

- [ ] Cost of living data
  - Source: Research or user experience
  - Format: Spreadsheet or documented data
  - Verification: Latest 2026 data
  - Priority: HIGH (critical for accuracy)

- [ ] Expat testimonials/quotes (optional)
  - Count: 2-3 per lifestyle page (optional for schema)
  - Format: Text quotes with attribution
  - Purpose: Expert attribution / social proof
  - Priority: LOW (Phase 3+)

### Tools & Validation

- [ ] Google Rich Results Test (schema validation)
- [ ] Screaming Frog (crawl depth, link audit)
- [ ] Internal link validator (broken link check)
- [ ] Meta description checker (word count, quality)

---

## Success Criteria (Phase 2 Complete)

**Structural**:
- [ ] 20+ new pages created with proper schema
- [ ] 100% of pages have ≥2 incoming links (no orphans)
- [ ] All Tier 1 pages ≤2 clicks from home
- [ ] All Tier 2 pages ≤3 clicks from home
- [ ] Breadcrumb navigation implemented across site

**Content**:
- [ ] All hub pages 2500+ words
- [ ] All cluster pages 1500+ words
- [ ] All detail pages 1200+ words
- [ ] All pages have Article + BreadcrumbList schema
- [ ] All FAQ-worthy pages have FAQPage schema

**Authority**:
- [ ] Hub pages link to 5+ clusters/detail pages
- [ ] Cluster pages link to 3+ detail pages
- [ ] Lateral linking: 2-3 sibling links per cluster page
- [ ] No page exceeds 1 internal link per 150 words
- [ ] Anchor text diversity validated (no over-optimization)

**SEO**:
- [ ] All pages have compelling meta descriptions
- [ ] All pages have single, descriptive H1 tag
- [ ] All images have descriptive alt text
- [ ] All external links functional
- [ ] All /visa/ links point to cmlocals (not internal)

**Ready for Phase 3**:
- [ ] Content audit complete
- [ ] Thin content identified (for expansion in Phase 3)
- [ ] Statistics/sources research needed documented
- [ ] Expert attribution opportunities identified
- [ ] Phase 3 brief prepared

---

## Notes

**If stuck on any page**:
- Reference PHASE_2_AUTHORITY_ARCHITECTURE.md for intent segmentation and content requirements
- Check schema requirements in same document
- Verify crawl depth and link targets before publishing

**If adding new pages not in this list**:
- Check for cannibalization risk (PHASE_2_AUTHORITY_ARCHITECTURE.md, section 9)
- Ensure proper parent-child relationship (URL silo structure)
- Add to this tracker before publishing

**Phase 3 handoff**:
- All Phase 2 pages must be published and linked before starting Phase 3
- Phase 3 focuses on content depth, statistics, and AI search optimization
- No new pages created in Phase 3 (only updates to existing Phase 2 pages)

---

**Document**: PHASE_2_IMPLEMENTATION_CHECKLIST.md  
**Created**: 2026-05-24  
**Status**: Ready for execution  
**Last Updated**: 2026-05-24
