# Chiang Mai Ambassador - Product Requirements Document

**Status:** Live (June 2026)  
**Version:** 1.0  
**Last Updated:** June 4, 2026  
**Author:** Reverse engineered from production build

---

## Executive Summary

Chiang Mai Ambassador is an authoritative, SEO-optimized lifestyle guide for English-speaking expats considering or living in Chiang Mai, Thailand. The site serves 89+ pages of content spanning visas, cost of living, neighborhoods, food, culture, and practical logistics. Built on vanilla HTML/CSS/JS, hosted on Cloudflare Pages, with a focus on portability, performance, and human-centric content.

---

## Product Definition

### What This Product Is
- **Content Hub:** Comprehensive guide to living as an expat in Chiang Mai
- **Authority Site:** 16+ years of lived experience packaged as searchable knowledge
- **SEO-First:** Designed to rank for high-intent keywords (visas, cost of living, neighborhoods)
- **Community Platform:** Connects expats with resources, recommendations, and each other

### What This Product Is NOT
- Not a booking platform (no transactional functionality)
- Not a social network (no user accounts or comments)
- Not a course or membership site (all content is free)
- Not a directory or database (manually curated content only)

### Core Value Proposition
**For Expats:** Get reliable, experienced guidance on moving to and living in Chiang Mai from someone who's actually lived there 16+ years.

**For Search Engines:** Comprehensive, original, well-structured content on visa types, cost of living, neighborhoods, and lifestyle topics. Schema-rich, mobile-optimized, fast-loading.

---

## Target User Personas

### Primary Persona: The Visa Seeker
- **Age:** 40-70, retired or semi-retired
- **Income:** $2k-$5k/month (independent, pension, rental income)
- **Goal:** Find the right Thai visa type and understand the process
- **Pain Point:** Overwhelmed by visa options, conflicting information online, legal complexity
- **Behavior:** Searches "retirement visa Thailand," "LTR visa requirements," "DTV visa"
- **Content Needed:** Detailed guides, step-by-step processes, cost breakdowns, legal requirements
- **Success:** Understands which visa fits, knows what documents to prepare

### Secondary Persona: The Digital Nomad
- **Age:** 25-40, remote work income
- **Income:** $3k-$10k/month from online business/employment
- **Goal:** Find an affordable, livable city; understand visa options
- **Pain Point:** Too short to stay anywhere; seeking longer-term stability
- **Behavior:** Searches "cost of living Chiang Mai," "DTV visa," "where to stay"
- **Content Needed:** Practical guides, lifestyle content, cost comparisons, neighborhood reviews
- **Success:** Feels confident moving to CM and settling in

### Tertiary Persona: The Lifestyle Explorer
- **Age:** 30-55, considering major life change
- **Income:** Variable (savings, side projects, part-time work)
- **Goal:** Improve quality of life, explore new culture, reduce expenses
- **Pain Point:** Not sure if Chiang Mai is right; needs reassurance
- **Behavior:** Searches "best neighborhoods Chiang Mai," "eating in Chiang Mai," "expat community"
- **Content Needed:** Lifestyle guides, cultural guides, community resources, food recommendations
- **Success:** Feels excited about moving; understands daily life realities

---

## Feature & Content Requirements

### Core Features (Minimum Viable)
1. ✅ **Homepage** - Credibility, CTAs, overview
2. ✅ **Blog/Article Pages** - Rich text, images, metadata, schema
3. ✅ **Navigation** - Clear IA, easy discovery
4. ✅ **Search** - Pagefind local search index
5. ✅ **Mobile Responsive** - Works on phone/tablet/desktop
6. ✅ **SEO Foundation** - Meta tags, schema, sitemaps
7. ✅ **Performance** - <3s load time, 90+ Lighthouse

### Content Pillars (89 Pages)

**Visa Guides (14 pages)**
- Hub/Overview
- Tourist Visa (30 days, renewal process)
- Retirement Visa (O-A, O-X, medical requirements)
- LTR Visa (Long Term Resident, application, requirements)
- Volunteer Visa (eligibility, organizations)
- ED Visa (3 types: Thai Language, Muay Thai, Combat Training)
- DTV Visa (Digital Traveler, eligibility, validity)
- Marriage Visa (requirements, processing)
- Business Visa (requirements, paperwork)
- Border Run Strategy (cheapest options, timing)
- Visa Exempt vs VOA comparison

**Lifestyle Content (25+ pages)**
- Where to Stay in Chiang Mai (guide)
- Neighborhoods Deep Dive (Nimman, Old City, Riverside, etc.)
- Moving Checklist (practical steps)
- Understanding Thai Culture (customs, etiquette, taboos)
- Thai Eating Etiquette (how to eat respectfully)

**Food & Culture (15+ pages)**
- Restaurant Recommendations (by cuisine, price, location)
- Markets Guide (Warorot, Walking Street, Sunday Market, Yunnan Farmers Market)
- Specific Restaurant Reviews (Khun Joe School, Chef Fuji, Meela Peanut Butter, Punspace, etc.)
- Thai Food Overview (dishes, spices, regional variations)
- Food Sourcing (where to buy Western food, Thai ingredients, specialties)

**Practical Guides (20+ pages)**
- Cheapest Border Run Comparison (Mae Sai vs Ranong vs Sadao vs Laos, cost breakdown)
- Modern Transport Guide (buses, songthaews, taxis, motorbikes, aviation)
- Motorbike Registration in Chiang Mai (requirements, costs, legal)
- Mobile/Internet Setup (SIM cards, providers, costs)
- Banking & Money Transfer (Thai accounts, international transfers)
- Healthcare in Chiang Mai (hospitals, insurance, costs)
- Community Resources (blood banks, schools, social groups, volunteering)

**Chiang Mai Exploration (10+ pages)**
- Best Things to Do (activities, attractions, seasonal)
- Temple Guide & Etiquette (respect, dress code, customs)
- Markets & Shopping (where to buy what, prices)
- Events & Festivals (annual events, calendar)
- Day Trips from Chiang Mai (nearby attractions, itineraries)

**Legal & Meta (5 pages)**
- Privacy Policy (Australia + Thailand compliant)
- Terms of Service (usage, liability)
- About Page (founder story, experience, credibility)
- Contact Page (inquiry form, contact info)
- Search Page (Pagefind results)

---

## User Journey & Experience

### Typical User Flows

**Flow 1: Visa Decision-Making (Primary)**
```
Search "retirement visa Thailand" 
  → Land on Retirement Visa guide
    → Read detailed requirements & costs
      → Check related visa guides (LTR, ED, DTV)
        → Check border run guide for long-term strategy
          → Email inquiry or schedule consultation
```

**Flow 2: Lifestyle Research (Secondary)**
```
Search "cost of living Chiang Mai"
  → Land on Cost of Living guide
    → Browse neighborhood guides
      → Read food & restaurant recommendations
        → Check moving checklist
          → Join community forum or newsletter
```

**Flow 3: Discovery (Tertiary)**
```
Visit homepage
  → Browse featured content
    → Click "Neighborhoods" CTA
      → Read Nimman, Old City, Riverside guides
        → Click "Food" section
          → Read restaurant recommendations
            → Share with friend / bookmark site
```

### Key Interactions
- Navigation: Top nav with dropdowns (Visas, Lifestyle, Food, Guides, Pages)
- Breadcrumbs: Home > Category > Topic (helps users orient)
- Related Posts: At bottom of each article (encourages deeper exploration)
- CTAs: Email signup, consultation request, community links
- Search: Pagefind local search (typing, filtering, results)
- Progress Bar: Indicates scroll position (subtle engagement indicator)

---

## Content Standards & Guidelines

### Blog/Article Structure
Every blog post follows this locked structure:

```
<head>
  - Meta title (page | Chiang Mai Ambassador)
  - Meta description (compelling, <160 chars)
  - Canonical URL (chiangmaiambassador.com)
  - Open Graph (title, description, image, type)
  - Twitter Card (same as OG)
  - JSON-LD Article schema
  - Favicon
  - Font preloads
</head>

<body>
  <nav> (locked) </nav>
  
  <main>
    <article class="blog-content">
      <div class="blog-hero">
        <h1>Main Heading <span class="gold-gradient-text">Optional Highlight</span></h1>
        <p class="blog-excerpt">Brief description</p>
      </div>
      
      <div class="blog-metadata">
        <div>Breadcrumb Path</div>
        <div>Read Time: 5 min</div>
        <div>Last Updated: May 24, 2026</div>
      </div>
      
      <div class="blog-sidebar">
        <h4>TL;DR: Title</h4>
        <ul>
          <li>Key point 1</li>
          <li>Key point 2</li>
          <li>Key point 3</li>
        </ul>
      </div>
      
      <div class="article-intro">
        <h2>Opening Question or Context</h2>
        <p class="article-vibe">Explanation paragraph...</p>
      </div>
      
      <div class="blog-body">
        <h3>Section 1</h3>
        <p>Content...</p>
        
        [Image: float-right, float-left, or full-width]
        
        <h3>Section 2</h3>
        <p>Content...</p>
      </div>
      
      <div class="key-takeaways">
        <h3>Key Takeaways</h3>
        <p>Summary paragraph...</p>
      </div>
      
      <div class="blog-related">
        <h2>Related Articles</h2>
        [3-4 related post cards]
      </div>
    </article>
  </main>
  
  <footer> (locked) </footer>
</body>
```

### Writing Guidelines
- **Tone:** Direct, conversational, evidence-based. No corporate fluff.
- **Length:** 2,000-4,000 words (deep but scannable)
- **Structure:** Short sentences for impact. Vary sentence length. Use bold for emphasis.
- **Voice:** First person where appropriate ("I've lived here 16 years..."). Personal anecdotes build trust.
- **Specificity:** Use concrete numbers, names, dates. Vague claims lose credibility.
- **No em-dashes:** Use periods, commas, colons for flow.

### SEO Requirements per Page
- Unique meta title (under 60 chars, includes primary keyword)
- Unique meta description (120-160 chars, compelling, includes keyword)
- Canonical URL (self-referential on canonical page)
- Internal links (3-5 links to related content, inline text only)
- H1 (page title, once per page)
- H2/H3 (section hierarchy, logical nesting)
- Image alt text (descriptive, not keyword-stuffed)
- Schema markup (Article or specific type)
- Keyword coverage (primary keyword 2-3x in content, related keywords 1-2x)

---

## Design System & Visual Language

### Color Usage
- **Gold (#EAB308):** Primary CTA, links, accents, highlights
- **Purple (#7E22CE):** Secondary accents, hover states, emphasis
- **Emerald (#10B981):** Buttons, success states, positive actions
- **Dark (#0F172A):** Main background, high-contrast text
- **Slate (#1E293B):** Surface elements, card backgrounds, subtle sections
- **White (#F1F5F9):** Body text on dark, high contrast

### Typography System
- **Headlines:** Outfit 800 (hero), 600 (subheadlines)
- **Body:** Plus Jakarta Sans 400 (regular), 500 (emphasis)
- **Sizes:** 
  - H1: 3rem
  - H2: 2rem
  - H3: 1.25rem
  - Body: 1rem
  - Small: 0.875rem

### Component Patterns
- **Links:** Gold (#EAB308), underline on hover
- **Buttons:** Gold background, dark text, emerald on hover
- **Cards:** Dark surface (#1E293B), 1px border, hover lift
- **Sidebars:** Gold background (#f0d080), 4px left border accent
- **Lists:** No bullets, 0.75rem gap, indented
- **Quotes:** Left border accent, italic body

---

## Technical Requirements

### Performance Targets
- First Contentful Paint: <1.5s
- Largest Contentful Paint: <2.5s
- Cumulative Layout Shift: <0.1
- Total Page Size: <500KB (with images)
- Lighthouse Score: 90+ on all metrics

### Mobile Responsiveness
- Mobile: 1 column (320px+)
- Tablet: 2 columns (640px+)
- Desktop: 3 columns (1024px+)
- No horizontal scrolling at any breakpoint
- Touch targets: 44x44px minimum

### Browser Support
- Chrome/Edge 90+ (latest)
- Firefox 88+ (latest)
- Safari 14+ (latest)
- Mobile browsers (iOS Safari, Chrome Android, Firefox Android)

### Accessibility Standards
- WCAG 2.1 Level AA
- Semantic HTML (proper heading hierarchy)
- Color contrast: 4.5:1 (body), 3:1 (large text)
- Keyboard navigation: All interactive elements
- Alt text on all images
- Skip to content link (visible on focus)
- No flashing content (≤3 flashes/second)

### Security Requirements
- HTTPS only (Cloudflare Pages provides)
- No inline scripts for sensitive operations
- CSP headers configured (Cloudflare manages)
- No hardcoded API keys or secrets
- Form submissions to verified endpoints only

---

## Success Metrics & KPIs

### Traffic Metrics
- **Target:** 5,000+ organic sessions/month (month 6)
- **Tracked via:** Google Analytics 4, Search Console
- **Top Keywords:** Visa types, cost of living, neighborhoods
- **Referral Sources:** Google (80%+), direct, social, other

### Engagement Metrics
- **Avg Session Duration:** 2+ minutes
- **Pages per Session:** 2.5+
- **Bounce Rate:** <50%
- **Scroll Depth:** 75%+ (median)

### Conversion Metrics
- **Email Signups:** 100+ per month (target)
- **Consultation Requests:** 10+ per month (target)
- **Community Joins:** Track via external links
- **Repeat Visitors:** 30%+ of traffic

### Technical Metrics
- **Core Web Vitals:** All green (90+)
- **Page Speed:** <3s load time globally
- **Uptime:** 99.9%+
- **CDN Cache Hit Ratio:** 85%+

---

## Maintenance & Updates

### Content Updates
- **Visa Information:** Quarterly (law changes)
- **Cost of Living:** Semi-annually (inflation updates)
- **Neighborhood Guides:** Annually (development changes)
- **Restaurant Reviews:** As needed (closures, new opens)
- **All Pages:** "Last Updated" date visible

### Technical Maintenance
- **Dependencies:** None (vanilla JS, no npm packages)
- **Font Updates:** As needed (if adding new weights/languages)
- **Image Optimization:** Ongoing (audit old images for compression)
- **Schema Validation:** Quarterly (check rich snippets in Search Console)

### SEO Monitoring
- **Keyword Rankings:** Monthly report (top 20 keywords)
- **Search Console:** Weekly review (indexing issues, query performance)
- **Google Analytics:** Weekly review (traffic, behavior, conversions)
- **Backlinks:** Quarterly (new referring domains, link quality)

### Version Control
- **Git Workflow:** Atomic commits (one feature = one commit)
- **Branches:** Main (production), develop (staging if needed)
- **Deploy:** Push to main → Cloudflare Pages auto-deploys
- **Rollback:** Git revert if needed; ~5 min downtime worst-case

---

## Constraints & Non-Negotiables

### Technical Constraints
- **No frameworks:** Vanilla HTML/CSS/JS only. No React, Vue, Svelte, Astro.
- **No build step:** Static site, no compile/bundling required.
- **No dependencies:** Zero npm packages, zero external JS libraries (except Pagefind).
- **All local:** Fonts, CSS, JS, images all served from project folder.
- **Portable:** Every file relative to project root. Moveability guaranteed.

### Design Constraints
- **Template locked:** Nav, footer, blog structure never change.
- **No custom CSS per page:** Use template CSS only.
- **No inline styles:** Exception: image floats, margin tweaks (use template patterns).
- **No new fonts:** Outfit + Plus Jakarta Sans only.
- **Color palette locked:** 6 colors, no gradients beyond logo.

### Content Constraints
- **No AI-generated content:** All original, human-written.
- **No excessive self-promotion:** Focus on helping users, not selling.
- **No paid partnerships:** No sponsored content or affiliate links (unless clearly disclosed).
- **No user-generated content:** Curated content only, no comments or user submissions.
- **No external embeds:** No YouTube, Twitter, Instagram embeds (privacy, performance).

---

## Success Criteria

### Phase 1: Foundation (Months 1-2)
- ✅ All 89 pages built and deployed
- ✅ Homepage optimized for conversions
- ✅ All visa guides complete and detailed
- ✅ SEO foundation in place (schema, meta tags)
- ✅ Mobile responsive, <3s load time
- ✅ Pagefind search working

### Phase 2: Growth (Months 3-6)
- ✅ Ranking on first page for 10+ primary keywords
- ✅ 2,000+ organic sessions/month
- ✅ 50+ email signups
- ✅ 5+ consultation requests
- ✅ 85%+ Core Web Vitals (green)
- ✅ Repeat visitor rate 25%+

### Phase 3: Optimization (Months 6+)
- ✅ 5,000+ organic sessions/month
- ✅ First-page ranking for 20+ keywords
- ✅ 100+ email signups/month
- ✅ 10+ consultation requests/month
- ✅ Avg session duration 2.5+ minutes
- ✅ Pages per session 3+

---

## Appendix: File Structure

```
chiangmaiambassador/
├── index.html (homepage)
├── template.html (master blog template)
├── favicon.svg
├── robots.txt
├── sitemap.xml
├── _redirects (Cloudflare routing)
├── wrangler.jsonc (Cloudflare config)
│
├── css/
│   ├── tokens.css (design tokens)
│   ├── base.css (element resets)
│   ├── sections.css (layout patterns)
│   ├── components.css (reusable components)
│   └── blog.css (blog-specific styles)
│
├── fonts/
│   ├── outfit-600.woff2
│   ├── outfit-800.woff2
│   ├── plus-jakarta-400.woff2
│   └── plus-jakarta-500.woff2
│
├── js/
│   └── main.js (progress bar, interactions)
│
├── images/
│   └── [WebP images, semantically named]
│
├── visa/ (14 pages)
│   ├── index.html
│   ├── tourist-visa.html
│   ├── retirement-visa.html
│   ├── ltr-visa.html
│   ├── volunteer-visa.html
│   ├── ed-visa.html
│   ├── ed-visa-thai-language.html
│   ├── ed-visa-muay-thai.html
│   ├── ed-visa-combat-training.html
│   ├── dtv-visa.html
│   ├── marriage-visa.html
│   ├── business-visa.html
│   ├── border-run-strategy.html
│   └── visa-exempt-vs-voa.html
│
├── lifestyle/
│   ├── index.html
│   ├── moving-checklist.html
│   ├── where-to-stay.html
│   └── neighborhoods/
│       ├── nimman.html
│       ├── old-city.html
│       └── riverside.html
│
├── food/
│   ├── index.html
│   ├── restaurants.html
│   ├── markets.html
│   ├── thai-eating-etiquette.html
│   └── [other pages]
│
├── guides/
│   ├── index.html
│   ├── cheapest-border-run.html
│   ├── transport-guide.html
│   ├── motorbike-registration.html
│   └── [other pages]
│
├── chiang-mai/
│   ├── index.html
│   ├── culture.html
│   ├── temples.html
│   └── [other pages]
│
├── pages/
│   ├── about.html
│   ├── contact.html
│   ├── privacy-policy.html
│   ├── terms.html
│   └── search.html
│
├── MD/ (markdown documentation)
│   ├── INITIAL_PROMPT.md (this document)
│   ├── PRD.md (this file)
│   └── images/ (WebP images for documentation)
│
├── .claude/
│   └── settings.json (Claude Code configuration)
│
└── docs/
    ├── CODEMAPS.md (file structure)
    └── README.md (quick start)
```

---

## Questions & Contact

For questions about this PRD or reverse engineering, refer to memory system or reach out to Shayne (slrclaude@proton.me).

**Last Generated:** June 4, 2026  
**Purpose:** Document how CMA was built so future sites follow the same pattern
