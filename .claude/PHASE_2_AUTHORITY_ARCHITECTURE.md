# Phase 2: Authority Architecture for Chiang Mai Living

**Status**: Phase 2 Planning  
**Date Created**: 2026-05-24  
**Project**: chiangmaiambassador.com  
**Focus**: Guides + Lifestyle + Cost of Living (NOT visa authority)

---

## Executive Summary

This document outlines the topical authority architecture for chiangmaiambassador.com, with focus on Chiang Mai as a living destination. The site's core value is helping people understand what it's like to relocate to or visit Chiang Mai, with practical guides, lifestyle information, cost data, and community resources. Visa information is explicitly repositioned as an addon that links to cmlocals, not a primary authority silo.

**Core Objective**: Establish chiangmaiambassador as the go-to authority source for people researching what it's like to live in Chiang Mai, with top-3 rankings for lifestyle and guides queries.

**Key Shift from Original Plan**: Visa authority mapping is abandoned. The real topical authority is built around living, guides, cost of living, neighborhoods, and local experience.

---

## Master Topic Map

### Core Entity
**Chiang Mai as a living destination** for expats, digital nomads, retirees, and long-stay visitors.

### Primary Intent Layers

| Layer | User Question | Page Type | Depth |
|-------|--------------|-----------|-------|
| **Awareness** | "What's Chiang Mai like to live in?" | Hub pages | Broad overview |
| **Consideration** | "How much does it cost?" "Where should I live?" "What do I need to know?" | Cluster pages | Practical details |
| **Decision** | "How do I move there?" "What are visa requirements?" | Addon links OUT to cmlocals | Not authority focus |
| **Retention** | "Best places to eat/visit" "How do I make friends?" "Getting around" | Detail + community pages | Local expertise |

### Revenue Model
- **Primary**: Informational authority (builds credibility, attracts audience)
- **Secondary**: Addon links to cmlocals for visa/ED program details (referral partnership)
- **Tertiary**: Food/experience content (local recommendations)

---

## Hub and Cluster Blueprint

```
LEVEL 1: CORE GEOGRAPHIC HUB
└─ /chiang-mai/index.html 
   Status: ✅ EXISTS (recently created)
   Purpose: Geographic hub connecting all silos
   Links to: /lifestyle/, /guides/, /food/, /pages/

LEVEL 2: PRIMARY TOPICAL CLUSTERS
├─ /lifestyle/ 
│  Status: ❌ NEEDS CREATION (hub page)
│  Purpose: Living authority hub
│  Sub-clusters:
│  ├─ Cost of Living [cluster page]
│  ├─ Neighborhoods [cluster page]
│  ├─ Expat Life & Culture [cluster page]
│  └─ Daily Living Guide [cluster page - NEW]
│
├─ /guides/ 
│  Status: ✅ EXISTS (hub created May 2026)
│  Purpose: Practical logistics authority
│  Organized by: Transport, Health, Permits, Activities, Festivals, Resources
│  Note: 23 guides in 7 categories, well-structured
│
├─ /food/ 
│  Status: ⚠️ PARTIAL (individual pages exist, no hub)
│  Purpose: Food & restaurant authority
│  Sub-clusters:
│  ├─ Restaurant Reviews [by neighborhood]
│  ├─ Local Food Culture [Thai food guide]
│  └─ Budget Eating Guide [cheap eats, markets]
│
├─ /pages/experiences/ 
│  Status: ⚠️ SCATTERED (individual pages exist)
│  Purpose: Community & experiences
│  Pages:
│  ├─ getting-social-in-chiang-mai.html
│  ├─ best-chiang-mai.html
│  └─ [activities, events, sports - scattered]
│
└─ /visa/ 
   Status: ⚠️ NEEDS RESTRUCTURING (currently mixed addon)
   Purpose: ADDON ONLY - links OUT to cmlocals
   Note: Basic info only, not authority focus
```

---

## Intent Segmentation Map

### Awareness Layer (Top of Funnel)
These queries bring people into the funnel. Pages here are broad, inspirational, and informational.

| Intent | Target Keywords | Current Coverage | Page Type | Target |
|--------|-----------------|------------------|-----------|--------|
| Living in CM generally | "living in chiang mai" "moving to chiang mai" "chiang mai expat" "what's chiang mai like" | Partial (/chiang-mai/ hub exists) | Hub page | /chiang-mai/ + /lifestyle/ hub |
| Cost overview | "cost of living chiang mai" "how much money needed" "chiang mai budget" | Partial (page exists but orphaned) | Cluster page | /lifestyle/cost-of-living |
| Neighborhood overview | "best areas chiang mai" "where to live chiang mai" "neighborhoods in chiang mai" | Partial (page exists but orphaned) | Cluster page | /lifestyle/neighborhoods |

### Consideration Layer (Middle of Funnel)
Specific questions from people seriously researching. Pages provide detailed, comparable information.

| Intent | Target Keywords | Current Coverage | Page Type | Target |
|--------|-----------------|------------------|-----------|--------|
| Neighborhood specifics | "nimman chiang mai" "old city chiang mai" "riverside chiang mai" "where should i live" | ❌ Missing (no deep-dives) | Detail pages | /lifestyle/neighborhoods/[neighborhood]/ |
| Cost comparisons | "chiang mai vs bangkok cost" "chiang mai expensive" "cost breakdown chiang mai" | ❌ Missing | Cluster page | /lifestyle/chiang-mai-vs-bangkok |
| Expat life | "expat life chiang mai" "dating in chiang mai" "making friends chiang mai" | Partial (only tax guide) | Cluster page | /lifestyle/expat-life-guide |
| Daily logistics | "banking in chiang mai" "utilities chiang mai" "internet thailand" "housing rental" | ⚠️ Scattered in /guides/ | Cluster page | /lifestyle/daily-living-guide |
| Transport | "driving chiang mai" "motorbike rental" "getting around" | ✅ Complete in /guides/ | Cluster hub | /guides/ |
| Health | "hospitals chiang mai" "dentists" "insurance" | ✅ Complete in /guides/ | Cluster hub | /guides/ |
| Food & restaurants | "best restaurants chiang mai" "local food chiang mai" "cheap eats" | ⚠️ Individual reviews, no hub | Cluster hub | /food/ |

### Decision Layer (Bottom of Funnel)
Actionable information. These pages convert consideration into action (moving, visiting).

| Intent | Target Keywords | Current Coverage | Page Type | Target |
|--------|-----------------|------------------|-----------|--------|
| Moving checklist | "how to move to chiang mai" "moving checklist" "steps to relocate" | ❌ Missing | Convergence page | /lifestyle/moving-checklist OR /guides/moving-here-checklist |
| Visa requirements | "chiang mai visa" "retirement visa" "ED visa" | ✅ Exists (but addon) | Link OUT to cmlocals | /visa/ → cmlocals |
| Practical guides | "license plates" "registration" "getting a work permit" | ✅ Exists in /guides/ | Cluster | /guides/ |

### Retention Layer (Post-Conversion)
Ongoing value for people already in Chiang Mai.

| Intent | Target Keywords | Current Coverage | Page Type | Target |
|--------|-----------------|------------------|-----------|--------|
| Social groups | "expat groups chiang mai" "meetups chiang mai" "dating apps" | ✅ Exists | Detail page | /pages/getting-social-in-chiang-mai |
| Activities & events | "things to do chiang mai" "festivals" "events" | ⚠️ Scattered | Cluster/Detail | /guides/ + /pages/ |
| Local recommendations | "best cafes" "best bars" "best shops" | ⚠️ Scattered | Detail pages | /pages/best-chiang-mai + /food/ |

---

## URL Silo Structure

### Hierarchy and Relationships

```
ROOT
│
├─ /chiang-mai/index.html [CORE HUB - Level 1]
│  │  Links to: /lifestyle/, /guides/, /food/, /pages/
│  │  Anchor pattern: "Living Guide" / "Practical Tips" / "Food & Dining"
│  │
│  │
│  ├─ /lifestyle/ [PRIMARY CLUSTER HUB - Level 2] ❌ NEEDS CREATION
│  │  Purpose: Living authority hub
│  │  Meta description: "Complete guide to cost of living, neighborhoods, and daily life in Chiang Mai for expats and long-stay visitors"
│  │  Word count target: 2500-3500
│  │  Links to:
│  │  ├─ /lifestyle/cost-of-living.html [CLUSTER PAGE - Level 3]
│  │  │  Exists: Yes (page exists but orphaned)
│  │  │  Word count: 1500-2000
│  │  │  Links to:
│  │  │  ├─ /lifestyle/cost-of-living-by-neighborhood.html ❌ NEW
│  │  │  ├─ /lifestyle/chiang-mai-vs-bangkok.html ❌ NEW
│  │  │  ├─ /lifestyle/neighborhoods.html [sibling cluster]
│  │  │  └─ /guides/daily-living/ [support cluster]
│  │  │
│  │  ├─ /lifestyle/neighborhoods.html [CLUSTER PAGE - Level 3]
│  │  │  Exists: Yes (basic page)
│  │  │  Status: Needs expansion + hub structure
│  │  │  Word count: 1800-2200
│  │  │  Links to detail pages:
│  │  │  ├─ /lifestyle/neighborhoods/nimman.html ❌ NEW [DETAIL - Level 4]
│  │  │  ├─ /lifestyle/neighborhoods/old-city.html ❌ NEW [DETAIL - Level 4]
│  │  │  ├─ /lifestyle/neighborhoods/riverside.html ❌ NEW [DETAIL - Level 4]
│  │  │  ├─ /lifestyle/neighborhoods/chiang-mai-land.html ❌ NEW [DETAIL - Level 4]
│  │  │  └─ [more neighborhoods as variants]
│  │  │  Word count per detail: 1200-1600
│  │  │
│  │  ├─ /lifestyle/expat-life-guide.html ❌ NEW [CLUSTER PAGE - Level 3]
│  │  │  Purpose: Expat culture, social, relationships, integration
│  │  │  Word count: 1500-2000
│  │  │  Links to:
│  │  │  ├─ /pages/getting-social-in-chiang-mai.html [sibling]
│  │  │  ├─ /lifestyle/us-expat-tax-guide.html [existing detail]
│  │  │  └─ /guides/resources/ [support]
│  │  │
│  │  ├─ /lifestyle/daily-living-guide.html ❌ NEW [CLUSTER PAGE - Level 3]
│  │  │  Purpose: Utilities, internet, banking, phone, housing rental, bureaucracy
│  │  │  Word count: 1500-2000
│  │  │  Links to:
│  │  │  ├─ /guides/permits/ [support - deeper logistics]
│  │  │  ├─ /guides/transport/ [support - local transport]
│  │  │  └─ /lifestyle/cost-of-living.html [cost context]
│  │  │
│  │  └─ /lifestyle/moving-checklist.html ❌ NEW [CONVERGENCE PAGE - Level 3]
│  │     Purpose: Funnel convergence - connects all lifestyle info
│  │     Word count: 1800-2200
│  │     Links to:
│  │     ├─ /visa/ (links OUT to cmlocals) [addon reference]
│  │     ├─ /lifestyle/neighborhoods.html [where to live]
│  │     ├─ /lifestyle/cost-of-living.html [budget]
│  │     ├─ /guides/permits/ [visa/logistics]
│  │     └─ /lifestyle/daily-living-guide.html [setup]
│  │
│  ├─ /guides/ [PRIMARY CLUSTER HUB - Level 2] ✅ EXISTS
│  │  Status: Well-structured (23 guides in 7 categories)
│  │  Links to: Transport, Health, Permits, Activities, Festivals, Resources, etc.
│  │  New addition:
│  │  └─ /guides/moving-here-checklist.html ❌ NEW [Level 3]
│  │     Purpose: Logistics checklist (visa, registration, permits)
│  │     Links to: /visa/ (OUT to cmlocals), /permits/, /lifestyle/
│  │
│  ├─ /food/ [PRIMARY CLUSTER HUB - Level 2] ⚠️ NEEDS HUB
│  │  Status: Individual pages exist, no hub structure
│  │  To create: /food/index.html [HUB PAGE]
│  │  Word count target: 2000-2500
│  │  Links to:
│  │  ├─ /food/restaurants-by-neighborhood/ [CLUSTER]
│  │  ├─ /food/local-food-guide.html [CLUSTER]
│  │  └─ /food/budget-eating-guide.html [CLUSTER]
│  │
│  └─ /pages/ [EXPERIENCES & COMMUNITY - Level 2] ⚠️ SCATTERED
│     ├─ /pages/getting-social-in-chiang-mai.html [DETAIL]
│     ├─ /pages/best-chiang-mai.html [DETAIL]
│     └─ [activities, events, sports pages - to be consolidated]
│
│
├─ /visa/ [ADDON ONLY - Level 2] ⚠️ NEEDS RESTRUCTURING
│  Status: Currently mixed with general info
│  New approach: Minimal info hub + links OUT to cmlocals
│  Links:
│  ├─ OUT to cmlocals [main referral]
│  ├─ Back to /lifestyle/moving-checklist.html [context]
│  └─ Back to /guides/permits/ [logistics]
│
└─ [Other sections: existing pages, not authority focus]
```

---

## Content Depth Plan (Word Count Tiers)

### Tier 1: Pillar Pages (Hub Pages)

These are the foundation of topical authority. Each pillar serves as a comprehensive entry point and links to all major clusters.

| Page | URL | Status | Word Count | Purpose |
|------|-----|--------|-----------|---------|
| Chiang Mai Hub | /chiang-mai/ | ✅ Exists | 2500-3000 | Geographic entry point, links all silos |
| Lifestyle Hub | /lifestyle/ | ❌ New | 2500-3500 | Living authority hub, links cost/neighborhoods/expat/daily |
| Guides Hub | /guides/ | ✅ Exists | 2000-2500 | Practical logistics hub, links all guide categories |

**Pillar Page Requirements**:
- Clear definition of scope in opening paragraph
- Entity reinforcement (Chiang Mai, expat, cost of living)
- Links to all major clusters (3-5 links minimum)
- FAQ schema block addressing primary questions
- Article + BreadcrumbList schema
- Last updated date visible
- Author/expert attribution (credibility)

---

### Tier 2: Cluster Pages

Specific topic clusters within each pillar. These pages rank for mid-level intent queries and link to detail pages.

| Page | URL | Status | Word Count | Parent | Purpose |
|------|-----|--------|-----------|--------|---------|
| Cost of Living | /lifestyle/cost-of-living.html | ✅ Exists | 1500-2000 | /lifestyle/ | Budget breakdown by category |
| Neighborhoods | /lifestyle/neighborhoods.html | ✅ Exists | 1800-2200 | /lifestyle/ | Overview of living areas, intro to detail pages |
| Expat Life Guide | /lifestyle/expat-life-guide.html | ❌ New | 1500-2000 | /lifestyle/ | Culture, social, relationships, integration |
| Daily Living | /lifestyle/daily-living-guide.html | ❌ New | 1500-2000 | /lifestyle/ | Utilities, banking, internet, housing, permits |
| Cost of Living by Neighborhood | /lifestyle/cost-of-living-by-neighborhood.html | ❌ New | 1600-2000 | /lifestyle/ | Rent, food, transport by specific areas |
| Chiang Mai vs Bangkok | /lifestyle/chiang-mai-vs-bangkok.html | ❌ New | 1400-1800 | /lifestyle/ | Cost and lifestyle comparison |
| Food Guide (Hub) | /food/index.html | ❌ New | 2000-2500 | /chiang-mai/ | Restaurant authority, links categories |
| Transport Guide | /guides/transport/ | ✅ Exists | 1500-2000 | /guides/ | Driving, motorbikes, public transport |
| Health Guide | /guides/health/ | ✅ Exists | 1500-2000 | /guides/ | Hospitals, dentists, insurance, blood donation |

**Cluster Page Requirements**:
- Target specific keyword (e.g., "cost of living chiang mai")
- 2-4 outgoing links to parent hub
- 1-3 links to sibling clusters
- 2-3 links to related detail pages
- FAQ schema block
- Article schema
- Comparison tables where applicable (cost data, neighborhoods)
- Statistics with sources

---

### Tier 3: Detail Pages

Deep-dive pages that rank for long-tail intent queries. Detailed, actionable information.

| Page | URL | Status | Word Count | Parent | Purpose |
|------|-----|--------|-----------|--------|---------|
| Nimman Guide | /lifestyle/neighborhoods/nimman.html | ❌ New | 1200-1600 | /lifestyle/neighborhoods/ | Neighborhood profile: vibe, cost, transport, restaurants |
| Old City Guide | /lifestyle/neighborhoods/old-city.html | ❌ New | 1200-1600 | /lifestyle/neighborhoods/ | Historic area profile |
| Riverside Guide | /lifestyle/neighborhoods/riverside.html | ❌ New | 1200-1600 | /lifestyle/neighborhoods/ | Suburban area profile |
| Chiang Mai Land | /lifestyle/neighborhoods/chiang-mai-land.html | ❌ New | 1200-1600 | /lifestyle/neighborhoods/ | Residential area profile |
| Moving Checklist | /lifestyle/moving-checklist.html | ❌ New | 1800-2200 | /lifestyle/ | End-to-end funnel convergence |
| Moving Here Checklist (Guides) | /guides/moving-here-checklist.html | ❌ New | 1500-2000 | /guides/ | Logistics-focused (visa, registration, permits) |
| Restaurant Reviews | /food/[neighborhood]/[restaurant].html | ⚠️ Scattered | 800-1200 | /food/ | Specific reviews by neighborhood |

**Detail Page Requirements**:
- Target specific long-tail keyword ("cost of living in Nimman")
- Link up to parent cluster page
- 1-2 links to sibling detail pages
- 2-3 links to related clusters
- FAQ schema block
- Hero image with alt text
- Statistics/pricing where applicable
- "Last updated" date

---

### Tier 4: Long-Tail Pages

Comparison and breakdown pages. Semi-programmatic variants.

| Page | URL | Status | Word Count | Purpose |
|------|-----|--------|-----------|---------|
| Cost of Living Breakdown | /lifestyle/cost-of-living-breakdown.html | ❌ New | 800-1000 | Expense categories (rent, food, transport, utilities) |
| Chiang Mai vs SE Asia | /lifestyle/chiang-mai-vs-se-asia.html | ❌ New | 900-1200 | Regional cost comparison |
| Budget by Lifestyle | /lifestyle/budget-by-lifestyle.html | ❌ New | 800-1000 | Budget for backpacker/digital nomad/expat/family |
| Restaurant Reviews by District | /food/restaurants-[district].html | ❌ New | 600-900 | Sorted by neighborhood/type |

---

### Tier 5: Programmatic Variants

Template-based long-tail expansion. High volume, controlled quality.

| Template | Examples | Word Count | Purpose |
|----------|----------|-----------|---------|
| "Cost of living in [Neighborhood]" | Nimman, Old City, etc. | 400-700 | SEO long-tail, feed from main cluster |
| "Budget [Activity] in Chiang Mai" | Dating, fitness, dining, etc. | 400-700 | Activity-based budget guides |
| "[Neighborhood] restaurant guide" | Nimman restaurants, etc. | 500-800 | Locality-specific food guides |
| "Best [Activity] in Chiang Mai" | Waterfalls, motorbike rental, etc. | 400-600 | Activity rankings |

---

## Crawl Depth Optimization

### Current State Analysis

**Average crawl depth**: 2-3 clicks from home for priority pages

| Page | Current Depth | Ideal Depth | Notes |
|------|---------------|------------|-------|
| /chiang-mai/ | 1 click | 1 click | ✅ Good (homepage link) |
| /lifestyle/ [new] | 2 clicks | 2 clicks | ✅ Will be good (nav accessible) |
| /guides/ | 2 clicks | 2 clicks | ✅ Good (nav accessible) |
| /lifestyle/neighborhoods/ | 3 clicks | 3 clicks | ✅ Acceptable |
| /lifestyle/neighborhoods/nimman/ | 4 clicks | 3-4 clicks | ⚠️ Watch depth |
| /food/ [new] | 2 clicks | 2 clicks | ✅ Will be good (nav accessible) |

### Optimization Strategy

**Tier 1 Pages (≤2 clicks from home)**:
- /chiang-mai/ — Link from nav or homepage
- /lifestyle/ — Add to main nav
- /guides/ — Link from main nav (already in place)
- /food/ — Add to main nav or footer

**Tier 2 Pages (≤3 clicks)**:
- /lifestyle/neighborhoods/ — Link from /lifestyle/ hub + main navigation dropdown
- /lifestyle/cost-of-living/ — Link from /lifestyle/ hub
- /guides/transport/ — Link from /guides/ hub + nav

**Tier 3 Pages (≤4 clicks)**:
- /lifestyle/neighborhoods/nimman/ — Link from /lifestyle/neighborhoods/ + /chiang-mai/ card
- /guides/moving-here-checklist/ — Link from /guides/ hub + /lifestyle/moving-checklist/

### Navigation Changes Needed

1. **Main Navigation**: Add /lifestyle/ as top-level item
2. **Breadcrumb**: Implement on all pages (Home > Lifestyle > Neighborhoods > Nimman)
3. **Sidebar**: Add related links to priority pages
4. **Footer**: Link to major hubs (/lifestyle/, /guides/, /food/)
5. **Homepage Cards**: Create cards for /lifestyle/, /guides/, /food/ hubs

---

## Authority Flow Model

### Link Distribution Rules

```
PILLAR HUBS (receive and distribute authority)
│
├─ /chiang-mai/ [geographic hub]
│  Receives: Homepage, nav
│  Distributes: 5-7 links to major clusters (/lifestyle/, /guides/, /food/, /pages/)
│  Link density: 1 link per 300-400 words
│
├─ /lifestyle/ [living authority hub] NEW
│  Receives: /chiang-mai/, nav, homepage
│  Distributes: 5-6 links to clusters and detail pages
│  Internal structure: cost → neighborhoods → expat → daily → checklist
│
├─ /guides/ [practical authority hub] EXISTING
│  Receives: /chiang-mai/, nav, homepage
│  Distributes: Links to all guide categories (transport, health, permits, etc.)
│
└─ /food/ [food authority hub] NEW
   Receives: /chiang-mai/, nav, footer
   Distributes: Links to restaurant guides, local food guides

CLUSTER PAGES (receive from hub, distribute to detail)
│
├─ /lifestyle/neighborhoods/
│  Receives: /lifestyle/ hub, /chiang-mai/ nav
│  Distributes: Links to detail pages (Nimman, Old City, Riverside, etc.)
│  Lateral: Links to cost-of-living, neighborhoods-overview [2-3 max]
│
├─ /lifestyle/cost-of-living/
│  Receives: /lifestyle/ hub
│  Distributes: Links to cost-by-neighborhood, chiang-mai-vs-bangkok
│  Lateral: Links to neighborhoods, daily-living [2-3 max]
│
└─ /guides/transport/
   Receives: /guides/ hub, /chiang-mai/ nav
   Distributes: Links to specific guides (driving, motorbike, taxis)
   Lateral: Links to health, permits [2-3 max]

DETAIL PAGES (receive from cluster, light lateral linking)
│
├─ /lifestyle/neighborhoods/nimman.html
│  Receives: /lifestyle/neighborhoods/, /chiang-mai/ card
│  Links to: Parent (neighborhoods), 1-2 siblings (Old City, Riverside), related cluster (restaurants in Nimman via /food/)
│  Outbound: 3-5 total links
│
└─ /food/restaurants-nimman.html
   Receives: /food/ hub
   Links to: Parent (/food/), neighborhood profile (/lifestyle/neighborhoods/nimman/)
   Outbound: 3-4 total links
```

### Authority Boosting Strategy

**High-performing pages** (based on future GSC data) distribute links to:
1. Underperforming strategic pages (e.g., if "cost of living" gets traffic but "neighborhoods" doesn't, cost-of-living links to neighborhoods)
2. Newly published clusters (ensure crawlability and initial PageRank)
3. Money pages needing reinforcement (moving-checklist, expat-life-guide)

**Isolated addon**: /visa/ receives minimal internal links. Instead, lifestyle and guides pages link OUT to /visa/ only when contextually relevant (e.g., moving-checklist → "visa requirements" → links to cmlocals).

---

## Critical Content Gaps (Expansion Opportunities)

### High Priority (Blocks other work)

**1. Lifestyle Hub Page** — /lifestyle/index.html
- Status: ❌ MISSING
- Purpose: Connects cost of living, neighborhoods, expat life, daily logistics
- Currently: Only individual pages exist (orphaned, no topical structure)
- Word count: 2500-3500
- Should link to: cost-of-living, neighborhoods, expat-life-guide, daily-living-guide, moving-checklist
- Schema: Article, BreadcrumbList, FAQPage
- Timeline: Week 1 of Phase 2

**2. Neighborhood Deep-Dives** — /lifestyle/neighborhoods/[neighborhood].html
- Status: ❌ MISSING (only overview exists at /pages/neighborhoods.html)
- Purpose: Rank for "where to live" and neighborhood-specific queries
- Pages needed:
  - /lifestyle/neighborhoods/nimman.html (tech hub, expat area)
  - /lifestyle/neighborhoods/old-city.html (historic, culture)
  - /lifestyle/neighborhoods/riverside.html (suburban, quiet)
  - /lifestyle/neighborhoods/chiang-mai-land.html (residential)
  - [Additional neighborhoods based on search volume]
- Word count per page: 1200-1600
- Each page includes: Vibe, cost breakdown, transport, restaurants, photos
- Schema: Article, LocalBusiness (references), FAQPage
- Timeline: Weeks 1-2 of Phase 2

**3. Cost of Living Comparisons** — Missing pages
- /lifestyle/chiang-mai-vs-bangkok.html (1400-1800 words)
  - Monthly budget comparison, quality of life, expat community size
- /lifestyle/cost-of-living-by-neighborhood.html (1600-2000 words)
  - Table: Nimman, Old City, Riverside, etc. with rent, food, transport costs
- /lifestyle/cost-of-living-breakdown.html (800-1000 words)
  - Categories: Housing, food, transport, utilities, entertainment, healthcare
- Timeline: Weeks 1-3 of Phase 2

**4. Expat Life Pillar** — /lifestyle/expat-life-guide.html
- Status: ❌ MISSING (only /lifestyle/us-expat-tax-guide.html exists)
- Purpose: Rank for "expat life chiang mai" queries
- Content: Dating, relationships, making friends, cultural adaptation, integration
- Word count: 1500-2000
- Schema: Article, FAQPage
- Links to: /pages/getting-social-in-chiang-mai.html, /lifestyle/us-expat-tax-guide.html
- Timeline: Week 2 of Phase 2

**5. Daily Living Guide** — /lifestyle/daily-living-guide.html
- Status: ❌ MISSING (partially scattered in /guides/)
- Purpose: Comprehensive "how to live" guide for new arrivals
- Content: Utilities, internet, phone, banking, housing rental, healthcare basics, transport
- Word count: 1500-2000
- Links to: /guides/ for deeper logistics
- Schema: Article, HowTo, FAQPage
- Timeline: Week 2 of Phase 2

**6. Moving Checklist Convergence Pages** — 2 variants
- /lifestyle/moving-checklist.html (funnel view — lifestyle focus)
  - Sections: Before you go, choosing where to live, budgeting, packing
  - Links to: neighborhoods, cost of living, expat guide, moving-here-checklist
  - Word count: 1800-2200
- /guides/moving-here-checklist.html (logistics view)
  - Sections: Visa, registration, permits, housing setup, banking, utilities
  - Links to: /guides/, /visa/ (OUT to cmlocals), /lifestyle/
  - Word count: 1500-2000
- Timeline: Weeks 2-3 of Phase 2

---

### Medium Priority (Strengthens structure)

**7. Food Section Hub** — /food/index.html
- Status: ❌ MISSING (individual reviews exist, no hub)
- Purpose: Establish food authority, link to restaurant guides
- Content: Food culture overview, restaurants by neighborhood/type, local food guide, budget eating
- Word count: 2000-2500
- Links to: /food/restaurants-by-neighborhood/, /food/local-food-guide.html, /food/budget-eating.html
- Timeline: Week 3 of Phase 2

**8. Activities & Experiences Hub** — Consolidate existing content
- Status: ⚠️ SCATTERED (waterfalls in /guides/, social in /pages/, activities mixed)
- Purpose: Provide organized navigation for activities and experiences
- Current pages: Bua Tong Waterfalls, running, driving tours, getting social, best-chiang-mai
- Consolidation: Create /pages/activities/ or /experiences/ index page linking all
- Timeline: Week 3 of Phase 2

**9. Visa Addon Restructuring** — /visa/index.html
- Status: ⚠️ NEEDS RESTRUCTURING (currently mixed with general info)
- New approach: Clear landing page with links OUT to cmlocals
- Content: Brief overview, "see detailed visa info at cmlocals.com", contextual internal links
- Links to: cmlocals (main), /lifestyle/moving-checklist/, /guides/permits/
- Purpose: Clear signal that visa is addon, not primary authority
- Timeline: Week 1 of Phase 2

---

### Low Priority (Long-tail expansion)

**10. Cost Breakdown by Lifestyle Type** — /lifestyle/budget-by-lifestyle.html
- Variants: Backpacker budget, digital nomad budget, expat family budget, retirement budget
- Word count: 800-1200
- Template-based programmatic variants
- Timeline: Phase 4 (scaling)

**11. Neighborhood Cost Pages** — Programmatic
- Template: "Cost of living in [Neighborhood], Chiang Mai"
- Examples: "Cost of living in Nimman", "Cost of living in Old City"
- Word count: 400-700 per variant
- Links from: /lifestyle/cost-of-living-by-neighborhood/, /lifestyle/neighborhoods/
- Quantity: 8-12 variants based on search volume
- Timeline: Phase 4 (scaling)

**12. Budget Activity Guides** — Programmatic
- Template: "Budget [Activity] in Chiang Mai"
- Examples: "Budget dating in Chiang Mai", "Budget fitness in Chiang Mai", "Budget nightlife"
- Word count: 400-700 per variant
- Links from: /lifestyle/daily-living-guide/, /pages/best-chiang-mai/
- Quantity: 10-15 variants
- Timeline: Phase 4 (scaling)

**13. Restaurant Guides by District** — Programmatic
- Template: "[Neighborhood] restaurants guide"
- Examples: "Nimman restaurants", "Old City restaurants", "Riverside restaurants"
- Word count: 600-900 per variant
- Links from: /food/ hub, /lifestyle/neighborhoods/[neighborhood]/
- Quantity: 8-10 variants
- Timeline: Phase 4 (scaling)

---

## Cannibalization Risk Assessment

### Potential Conflicts and Resolutions

| Conflict | Risk Level | Resolution |
|----------|-----------|-----------|
| /lifestyle/cost-of-living.html + /lifestyle/cost-of-living-by-neighborhood.html | Low | Cost-by-neighborhood is detail page (parent clusters cost), links back to parent. Different intent (general vs neighborhood-specific). |
| /lifestyle/neighborhoods.html + /lifestyle/neighborhoods/[neighborhood].html | Low | Neighborhoods is overview + table. Individual pages are deep-dives. Different intent, clear parent-child relationship. |
| /pages/neighborhoods.html (old) + /lifestyle/neighborhoods.html (new) | Medium | Consolidate: Keep lifestyle version as primary, update /pages/neighborhoods to redirect or link to /lifestyle/neighborhoods.html. Clear content hierarchy. |
| /guides/transport/ + /guides/driving/ | Low | Transport is hub, driving is detail. No conflict. |
| /lifestyle/cost-of-living.html + /chiang-mai/index.html | Low | Hub has brief mention + link. CbyL has detailed breakdown. Different depth, no duplication. |
| /guides/moving-here-checklist.html + /lifestyle/moving-checklist.html | Low | Guides version is logistics-focused (visa, permits, registration). Lifestyle version is lifestyle-focused (where to live, cost, expat life). Complementary, clear distinction. |
| /pages/getting-social.html + /lifestyle/expat-life-guide.html | Low | Social is specific (community groups, dating), expat-life is broader (culture, relationships, integration). Complementary. Expat-life links to getting-social. |
| /food/budget-eating.html + /lifestyle/cost-of-living.html | Low | Food focuses on restaurants. Cost of living is broader (housing, transport, etc.). Different intent. |

**Cannibalization Prevention Actions**:
1. Clear internal link hierarchy (parent → child only)
2. Anchor text differentiation (avoid exact match anchors across competing pages)
3. URL structure clarity (silo paths match topical relationship)
4. Schema markup (Article on all, BreadcrumbList on nested pages)
5. Regular monitoring (quarterly review of Google Search Console for ranking conflicts)

---

## Authority Distribution Plan

### Link Flow Architecture

```
HOME
│
├─ NAV: /chiang-mai/ [primary hub]
├─ NAV: /lifestyle/ [new primary cluster] NEW
├─ NAV: /guides/ [existing primary cluster]
├─ NAV: /food/ [new primary cluster] NEW
└─ NAV: /pages/ [secondary, experiences]

FROM /chiang-mai/ [distributes authority]
├─→ /lifestyle/ [Anchor: "Living Guide" or "Lifestyle"]
├─→ /guides/ [Anchor: "Practical Guides"]
├─→ /food/ [Anchor: "Food & Dining"]
├─→ /pages/getting-social-in-chiang-mai.html [Anchor: "Social & Community"]
└─→ /pages/best-chiang-mai.html [Anchor: "Local Recommendations"]

FROM /lifestyle/ [distributes to clusters and details]
├─→ /lifestyle/cost-of-living.html [Anchor: "Cost of Living"]
├─→ /lifestyle/neighborhoods.html [Anchor: "Best Neighborhoods"]
├─→ /lifestyle/expat-life-guide.html [Anchor: "Expat Life"]
├─→ /lifestyle/daily-living-guide.html [Anchor: "Daily Living"]
└─→ /lifestyle/moving-checklist.html [Anchor: "Moving Checklist"]

FROM /lifestyle/neighborhoods/ [distributes to detail pages]
├─→ /lifestyle/neighborhoods/nimman.html [Anchor: "Nimman"]
├─→ /lifestyle/neighborhoods/old-city.html [Anchor: "Old City"]
├─→ /lifestyle/neighborhoods/riverside.html [Anchor: "Riverside"]
└─→ /lifestyle/neighborhoods/chiang-mai-land.html [Anchor: "Chiang Mai Land"]

FROM /lifestyle/cost-of-living/ [distributes to variants]
├─→ /lifestyle/cost-of-living-by-neighborhood.html [Anchor: "By Neighborhood"]
├─→ /lifestyle/chiang-mai-vs-bangkok.html [Anchor: "vs Bangkok"]
└─→ /lifestyle/cost-of-living-breakdown.html [Anchor: "Expense Breakdown"]

FROM /guides/ [distributes to guide categories]
├─→ /guides/transport/ [Anchor: "Transport"]
├─→ /guides/health/ [Anchor: "Health & Medical"]
├─→ /guides/permits/ [Anchor: "Permits & Registration"]
├─→ /guides/activities/ [Anchor: "Activities & Recreation"]
├─→ /guides/festivals/ [Anchor: "Festivals & Events"]
├─→ /guides/resources/ [Anchor: "Resources & Support"]
└─→ /guides/moving-here-checklist.html [Anchor: "Moving Checklist"]

FROM /food/ [new hub distributes to guides]
├─→ /food/restaurants-by-neighborhood/ [Anchor: "Restaurants"]
├─→ /food/local-food-guide.html [Anchor: "Local Food"]
└─→ /food/budget-eating-guide.html [Anchor: "Budget Eating"]

LATERAL LINKING (same-level clusters)
├─ /lifestyle/cost-of-living/ ↔ /lifestyle/neighborhoods/ [Anchor: "neighborhoods" / "cost breakdown"]
├─ /lifestyle/expat-life-guide/ ↔ /pages/getting-social.html [Anchor: "meeting people" / "expat culture"]
└─ /guides/transport/ ↔ /guides/permits/ [Anchor: "registration" / "motorbike rental"]

CONVERGENCE POINTS
├─ /lifestyle/moving-checklist.html
│  Links to: neighborhoods, cost-of-living, expat-life, daily-living, /guides/moving-here-checklist, /visa/ → cmlocals
│
└─ /guides/moving-here-checklist.html
   Links to: /guides/permits/, /guides/transport/, /visa/ → cmlocals, /lifestyle/moving-checklist
```

### Pages That Receive Most Authority (Tier 1)

1. **Pillar Hubs**:
   - /chiang-mai/ [geographic hub]
   - /lifestyle/ [living authority hub]
   - /guides/ [practical authority hub]

2. **High-Priority Clusters**:
   - /lifestyle/neighborhoods.html [top query volume]
   - /lifestyle/cost-of-living.html [top query volume]
   - /guides/transport/ [popular guide]

3. **Money Pages** (conversion focus):
   - /lifestyle/moving-checklist.html [funnel convergence]
   - /guides/moving-here-checklist.html [logistics focus]

### Pages That Distribute Authority (Link Sources)

1. **Hub pages** — distribute to all clusters
2. **Pillar pages** — distribute to detail pages
3. **High-traffic pages** — distribute to underperforming strategic pages (identified via GSC quarterly)

### Isolated Content (Minimal Internal Linking)

- **Addon pages**: /visa/ [no internal links except in context, links OUT to cmlocals]
- **Secondary experiences**: /pages/getting-social.html, /pages/best-chiang-mai.html [receive links from hubs, minimal outbound]

---

## Implementation Timeline (Phase 2)

### Week 1: Foundation
- [ ] Create /lifestyle/index.html hub page
- [ ] Restructure /visa/index.html as addon landing page
- [ ] Start neighborhood deep-dives (Nimman, Old City, Riverside, CMland)
- [ ] Create /lifestyle/moving-checklist.html convergence page

**Output**: 4 new pages, core structure established

### Week 2: Expansion
- [ ] Complete neighborhood deep-dives (finish 4+ pages)
- [ ] Create /lifestyle/expat-life-guide.html
- [ ] Create /lifestyle/daily-living-guide.html
- [ ] Create /guides/moving-here-checklist.html
- [ ] Create /lifestyle/chiang-mai-vs-bangkok.html

**Output**: 5-6 new pages, lifestyle pillar fully formed

### Week 3: Food & Refinement
- [ ] Create /food/index.html hub page
- [ ] Create cost of living comparison pages (by neighborhood, vs SE Asia)
- [ ] Implement internal linking architecture (update nav, add breadcrumbs)
- [ ] Add schema markup to all new pages
- [ ] Update template.html breadcrumb & nav links

**Output**: 3-4 new pages, full internal linking deployed, schema complete

### Week 4: QA & Documentation
- [ ] Crawl audit (verify crawl depth ≤3 for Tier 2 pages)
- [ ] Cannibalization check (Search Console simulate)
- [ ] Link validation (all anchors work, no orphans)
- [ ] Update documentation (site map, silo reference)
- [ ] Prepare for Phase 3 (content optimization)

**Output**: QA complete, ready for content optimization

---

## Success Metrics (Phase 2 Completion)

### Structure Completeness

- [ ] All pillar hubs exist and link to clusters (3/3 complete)
- [ ] All Tier 2 clusters exist and link to details (8/8 complete)
- [ ] All Tier 3 details exist and link up (8+/8 complete)
- [ ] No orphaned pages (all have ≥2 incoming links)
- [ ] Crawl depth: 90% of priority pages ≤3 clicks from home

### Content Quality

- [ ] All new pages have Article + BreadcrumbList schema
- [ ] All hub pages have FAQPage schema
- [ ] All pages have "last updated" date visible
- [ ] All pages have meta descriptions (160 chars)
- [ ] All pages have H1 + clear structure

### Authority Signals

- [ ] All pillar hubs link to 5+ clusters
- [ ] All clusters link to 3+ details
- [ ] Lateral linking: 2-3 sibling links per cluster page
- [ ] No page exceeds 1 internal link per 150 words
- [ ] Anchor text diversity (avoid exact match overuse)

### SEO Readiness

- [ ] URL structure follows silo (no orphaned paths)
- [ ] Breadcrumb navigation implemented site-wide
- [ ] Footer links major hubs
- [ ] Homepage cards link to major clusters
- [ ] Sitemap updated

---

## Notes & Assumptions

### Key Assumptions

1. **Visa is addon, not authority focus**: User clarified visa content redirects to cmlocals. Authority focuses on lifestyle/guides/living information.

2. **Guides already well-structured**: /guides/index.html exists with 23 organized guides. Guides provide support layer to lifestyle content, not competing topics.

3. **Food & community exist but scattered**: Individual pages exist (/food/, /pages/), but lack hub structure and internal linking. Will organize these into proper clusters.

4. **Geographic hub as entry point**: /chiang-mai/ is the true core hub (not a specific silo). It connects all topics because they're all about Chiang Mai as a living destination.

5. **Search intent primary driver**: Content organization follows search intent (awareness → consideration → decision → retention) rather than strict category buckets.

6. **No local search component (yet)**: This plan focuses on organic SEO. Local SEO optimization (/food/ with schema, local business listings) can be Phase 5 addition.

---

## Related Documents

- **Phase 1 Work**: Hub pages created (/chiang-mai/, /guides/), schema added to retirement-visa.html, color contrast fixed
- **Phase 3 Plan**: Content optimization (add statistics + sources, expert attribution, content depth expansion)
- **Phase 4 Plan**: Programmatic scaling (long-tail variants for cost of living, neighborhoods, budget activities)
- **Phase 5 Plan**: Pre-deployment QA (AI search audit, crawlability, Core Web Vitals, GSC validation)

---

## Document Metadata

**Document**: PHASE_2_AUTHORITY_ARCHITECTURE.md  
**Created**: 2026-05-24  
**Status**: Ready for implementation  
**Owner**: Shayne  
**Last Updated**: 2026-05-24  
**Superpowers Framework**: TACE Module 1 (Authority Architecture Layer)
