# Chiang Mai Ambassador - Reverse Engineered Initial Prompt

## Project Overview

Build a comprehensive, SEO-optimized website for an expat lifestyle guide focused on living in Chiang Mai, Thailand. The site serves as a trusted resource for expats, providing practical guidance on visas, cost of living, neighborhoods, food, culture, and community.

**Core Purpose:** Position the founder as a 16+ year Chiang Mai expert advisor. Deliver authoritative, personalized guidance across 89 pages covering practical and lifestyle topics for expats.

**Target Audience:** English-speaking expats (US, UK, Australia, Canada) considering or actively living in Chiang Mai; digital nomads; retirees; remote workers.

**Tone & Voice:** Direct, evidence-based, human-centric. Avoid corporate jargon. Short sentences for impact. No AI fluff. Credibility through specificity and lived experience.

---

## Technical Architecture

### Stack
- **Hosting:** Cloudflare Pages (global CDN, edge caching, email routing)
- **Code:** Vanilla HTML/CSS/JavaScript (no frameworks: React, Vue, Tailwind, Bootstrap)
- **Fonts:** Local WOFF2 (Outfit 600/800, Plus Jakarta Sans 400/500)
- **Images:** WebP only, semantically named, under 200KB total per page
- **Assets:** All local to project. No CDN dependencies. Portable folder structure.
- **Search:** Pagefind (local site search index)

### Design System

**Color Palette:**
- Primary: `#EAB308` (Vibrant Marigold/Gold) - city energy, CTAs
- Secondary: `#7E22CE` (Royal Purple) - twilight mountain haze, accents
- Accent: `#10B981` (Emerald) - tropical life & growth
- Background: `#0F172A` (Deep Midnight) - main dark background
- Surface: `#1E293B` (Slate Grey) - subtle sectioning
- Text: `#F1F5F9` (Light Grey) on dark; `#0F172A` on light

**Typography:**
- Headings: Outfit (600 for nav, 800 for hero)
- Body: Plus Jakarta Sans (400 for body, 500 for emphasis)

**Spacing & Layout:**
- Container max-width: 1280px
- Mobile-first responsive grid (1col mobile, 2col tablet, 3col desktop)
- 4px gold left-border accent for content hierarchy
- Consistent section spacing: 4rem major sections, 1-1.75rem list items

### Portability Requirements
- Every project folder is "a ship in a bottle"   standalone and independent
- No paths pointing outside the specific project directory
- Relative paths for all assets (../css/, ../fonts/, etc.)
- Adjustable depth paths for subdirectories (../ for root level, ../../ for 2 levels deep)

---

## Information Architecture

### Homepage
- Hero with founder credibility (16+ years in Chiang Mai)
- Mission statement: Connector, Helper, Guru
- Primary CTA sections: Arriving in Thailand, Visa guides, Cost of living, Neighborhoods
- Recent blog highlights
- Trust signals: community endorsements

### Main Sections
1. **Visas (14 pages)** - Most critical section
   - Overview/hub page
   - Tourist Visa
   - Retirement Visa (most popular)
   - LTR Visa (Long Term Resident)
   - Volunteer Visa
   - ED Visa (3 variants: Thai Language, Muay Thai, Combat Training)
   - DTV Visa (Digital Traveler Visa)
   - Marriage Visa
   - Business Visa
   - Border Run Strategy
   - Visa Exempt vs VOA comparison

2. **Food (6+ pages)**
   - Restaurant recommendations
   - Markets guide
   - Thai eating etiquette
   - Food-related lifestyle content

3. **Lifestyle (5+ pages)**
   - Neighborhoods (Nimman, Old City, Riverside, etc.)
   - Moving checklist
   - Where to stay guide
   - Neighborhoods overview

4. **Guides (multiple pages)**
   - Cheapest border run comparison
   - Modern transport guide
   - Motorbike registration
   - Khun Joe School
   - Thai culture understanding

5. **Chiang Mai (multiple pages)**
   - Events and activities
   - Community resources
   - Cultural guides

6. **Pages (legal/meta)**
   - Privacy policy
   - Terms of service
   - About page
   - Contact

---

## Content Strategy

### Page Categories

**Blog/Article Pages:**
- TL;DR section at top (golden sidebar) with key bullets
- Blog metadata (breadcrumb, read time, last updated)
- Article intro with context-setting question
- Scannable body content with H2/H3 hierarchy
- Key Takeaways section (golden box)
- Related blog cards at bottom
- Optimal length: 2000-4000 words (skimable, deep enough for SEO)

**Topic Targeting:**
- Visa guides (transactional/informational) - high search intent
- Lifestyle content (informational) - community & belonging angle
- Cost of living & housing (transactional) - practical concerns
- Border runs & logistics (transactional) - regular necessity
- Food & culture (informational/entertainment) - quality of life

**Content Differentiation:**
- Homepage: Emotional sweep, founder credibility
- About: Community/belonging angle, human story
- Visa guides: Comprehensive legal/practical info, step-by-step
- Lifestyle: Neighborhood deep dives, personal recommendations
- Food & Culture: Local authority, insider knowledge

### SEO Framework

**Meta Requirements:**
- Unique meta title and description per page
- Canonical URLs pointing to chiangmaiambassador.com
- Open Graph tags (title, description, image, type)
- Twitter Card tags (same as OG)
- JSON-LD schema (WebSite on homepage, Article on blogs, BreadcrumbList)

**Schema Implementation:**
- WebSite schema on homepage
- Article schema on all blog posts (headline, description, datePublished, author)
- BreadcrumbList for navigation hierarchy
- Organization schema for footer/contact info

**Keywords & Structure:**
- Primary: Visa types, cost of living, neighborhoods, border runs
- Secondary: Thai culture, expat lifestyle, community, logistics
- Internal linking: Footer links for visa hub, related posts at bottom
- Breadcrumbs: Navigation clarity + SEO signals

**Image Metadata:**
- All images WebP format, semantically named
- Naming formula: `chiang-mai-ambassador-chiangmaiambassador-[PAGE]-[SEMANTIC].webp`
- Width/height attributes to prevent CLS
- Alt text: Brief, descriptive (no keyword stuffing)

---

## Template Architecture

### Master Template (template.html)
The foundation for all article/blog pages. Locked structure ensures consistency:

**Locked Sections:**
- Navigation (SVG logo, nav links, dropdowns)
- Footer (content, styling, layout)
- Blog metadata display
- TL;DR sidebar styling
- Progress bar
- Script references

**Customizable Sections:**
- Meta tags (title, description, canonical, OG, Twitter)
- Page heading and excerpt
- Article intro (h2 + explanation)
- Sidebar bullets (TL;DR)
- Body content (h3, p, strong, images)
- Key Takeaways section
- Related blog cards
- JSON-LD schema

### Image Placement Patterns
- **TL;DR Image:** Float right, 30% width
- **Breakout Left:** 55% width, -15% negative margin
- **Full Width Break:** 100%, centered
- **Float Right:** 45% width with text wrapping
- **Side-by-Side:** Multiple images, responsive grid
- **Centered:** Hero or statement images

### CSS Organization
- `tokens.css` - Design tokens, colors, typography, spacing variables
- `base.css` - HTML element resets, typography defaults
- `sections.css` - Layout patterns, containers, grids
- `components.css` - Reusable components (buttons, cards, navigation)
- `blog.css` - Blog-specific styles (metadata, sidebar, body)
- Inline styles in templates: image floats, layout tweaks (rare)

---

## Development Standards

### Template-First Workflow
**Golden Rule:** Do not build from first principles. Copy template, adjust, ship.

1. **Identify Template** → Ask if unclear
2. **Copy Template Entirely** → `cp template.html [page-name].html`
3. **Adjust Paths** → Based on folder depth (../ vs ../../)
4. **Update Content Only** → Meta tags, headings, body, schema
5. **Ship** → No customization beyond content

**Why This Works:**
- Speed: Template to ship in 15 minutes
- Consistency: Brand never drifts
- Quality: Structure, accessibility, contrast already validated
- Discipline: Separates content from structural problems

### Rules That Never Break
- No custom navigation
- No footer redesigns
- No new CSS blocks for individual pages
- No inline layout styles (floats/spacing exceptions allowed)
- No framework imports (React, Vue, Tailwind, Bootstrap)
- No CDN assets (all fonts, CSS, JS are local)
- No framework dependencies or build tools
- All images WebP, semantically named, under 200KB total per page

### When Feedback Appears
- **Styling issue?** Ask if it's structural before patching
- **Nav looks wrong?** Copy exact template nav
- **Layout feels cramped?** Use template structure, not new CSS
- **Contrast issue?** Don't adjust   template CSS is pre-validated

---

## Analytics & Tracking

**Cloudflare Web Analytics** (built into every page):
- Privacy-focused, no cookies required
- Tracks: Unique visitors, page views, bounce rate, referrers
- Integrated into `<head>` of every page (standard for all pages)

---

## Deployment & Maintenance

**Git Workflow:**
- Single Git repository for entire site
- Atomic commits per task (one feature = one commit)
- Pre-commit hooks for linting (if configured)
- No force pushes to main
- Clean history maintained

**Cloudflare Pages Integration:**
- Auto-deploys on git push to main branch
- No build step required (static site)
- CDN caching automatically enabled
- Email routing configured for contact forms

**Search Engine Index:**
- Sitemap.xml auto-generated, included in robots.txt
- All pages set to `index, follow` in meta robots
- Structured data (JSON-LD) on every page type
- No noindex pages (all are public)

---

## Project Goals & Success Metrics

### Primary Goals
1. **Authority**: Establish founder as trusted Chiang Mai expert for English-speaking expats
2. **Traffic**: Rank on first page Google for visa, cost of living, neighborhood keywords
3. **Conversion**: Capture email, consultations, community sign-ups
4. **Depth**: Comprehensive coverage of expat topics (89 pages)

### Success Metrics
- Organic search traffic (Google Analytics)
- Keyword rankings (top 10 for primary keywords)
- Page speed & Core Web Vitals (Lighthouse 90+)
- User engagement (time on page, scroll depth)
- Conversion rate (newsletter sign-ups, contact forms)

### Content Calendar
- Launch with core visa guides + lifestyle content (month 1)
- Expand food/culture section (month 2)
- Add community/events content (month 3)
- Ongoing: Border run updates, visa law changes, seasonal guides

---

## Accessibility & Compliance

### WCAG AA Standards
- Semantic HTML structure (proper heading hierarchy H1-H3)
- Color contrast: 4.5:1 for body text, 3:1 for large text
- Keyboard navigation: Tab through all interactive elements
- Alt text on all images (descriptive, not keyword-stuffed)
- No flashing content (animations max 3 flashes/second)

### Privacy & Legal
- Privacy Policy page (Australian Privacy Act + Thailand PDPA compliant)
- Terms of Service page (usage rights, liability)
- Cookie disclosure (if applicable)
- GDPR compliance (if tracking EU users)

---

## Continuation & Updates

This PRD captures how the site was built as of June 2026. Future pages follow the exact same template-first workflow. Any structural changes require alignment with these standards before implementation.

**No custom layouts. No framework creep. No new CSS blocks. Template is law.**
