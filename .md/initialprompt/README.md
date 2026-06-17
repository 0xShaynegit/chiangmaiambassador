# Chiang Mai Ambassador - Initial Prompt & PRD

This folder contains the reverse-engineered initial prompt and Product Requirements Document for the Chiang Mai Ambassador website project, built June 2026.

## Files

### INITIAL_PROMPT.md
The comprehensive initial brief that describes what was built, how it was built, and why. Covers:
- Project overview & vision
- Technical stack & architecture
- Design system & color palette
- Information architecture (89 pages across 6 main sections)
- Content strategy & SEO framework
- Template architecture & standards
- Development workflows & best practices
- Analytics, deployment, and maintenance

**Use this for:** Understanding the project scope, recreating similar sites, understanding the design decisions.

### PRD.md
The complete Product Requirements Document defining success criteria, user personas, features, and specifications. Covers:
- Executive summary & product definition
- Target user personas (3 primary types)
- Content requirements (89+ pages breakdown)
- User journey & experience flows
- Content standards & writing guidelines
- Design system & visual language
- Technical requirements & performance targets
- Success metrics & KPIs
- Maintenance & update schedule
- Constraints & non-negotiables

**Use this for:** Evaluating if features meet requirements, understanding what makes the site successful, replicating the structure for future projects.

## Quick Reference

### Project Stats
- **Pages:** 89 total (14 visa, 25+ lifestyle, 15+ food, 20+ guides, 10+ exploration, 5+ legal/meta)
- **Stack:** Vanilla HTML/CSS/JS on Cloudflare Pages
- **Audience:** English-speaking expats, digital nomads, retirees considering/living in Chiang Mai
- **Goal:** Authority + organic search traffic for visa/lifestyle keywords

### Core Files
- **Homepage:** `index.html` (founder credibility, CTAs, overview)
- **Blog Template:** `template.html` (master structure for all content pages)
- **CSS System:** `css/tokens.css`, `base.css`, `sections.css`, `components.css`, `blog.css`
- **Fonts:** Local WOFF2 (Outfit 600/800, Plus Jakarta Sans 400/500)
- **Images:** WebP only, semantically named, <200KB per page total

### Design System
**Colors:** Gold (#EAB308), Purple (#7E22CE), Emerald (#10B981), Dark (#0F172A), Slate (#1E293B)
**Typography:** Outfit (headings), Plus Jakarta Sans (body)
**Layout:** 1280px max container, mobile-first responsive

### Golden Rules
1. Template first copy, adjust paths, update content, ship
2. No frameworks (React, Vue, Tailwind)
3. No external dependencies (all local assets)
4. No custom CSS per page (use template only)
5. All images WebP, semantically named
6. Relative paths (portability guaranteed)

## How to Use These Docs

### For Replicating the Project
1. Read INITIAL_PROMPT.md section "Technical Architecture" for the design system
2. Read PRD.md section "Content Standards & Guidelines" for writing/structure rules
3. Reference INITIAL_PROMPT.md "Template Architecture" for page structure
4. Check CLAUDE.md in project root for operational rules

### For Building Similar Sites
1. Use the user persona framework from PRD.md
2. Reference the content pillar strategy (PRD: Content Requirements)
3. Copy the design tokens from tokens.css
4. Use template.html as the starting point
5. Follow the Template-First Workflow (INITIAL_PROMPT.md)

### For Understanding Success
- Check PRD.md "Success Metrics & KPIs" section
- Review "Phase 1-3" success criteria
- Monitor Search Console for keyword rankings
- Track Google Analytics for traffic & engagement

## Key Learnings

### What Worked
- **Template-first approach:** Consistency + speed. No structural surprises.
- **Vanilla stack:** Fast, portable, zero dependency management.
- **Semantic naming:** WebP images named by content improve SEO & clarity.
- **Locked brand elements:** Nav, footer, typography never drift.
- **Schema + meta:** Rich snippets + SEO foundation = rankings.
- **Content depth:** 2000-4000 word guides rank better than short posts.

### What to Avoid
- Adding frameworks mid-project (kills portability)
- Custom CSS per page (breaks consistency)
- CDN assets (reduces portability)
- AI-generated content (lacks credibility)
- Scattered naming conventions (confuses file management)
- Skipping accessibility early (costly to retrofit)

## Related Documents

- **md/INITIAL_PROMPT.md**   Full version in /md folder (same as this one)
- **md/PRD.md**   Full version in /md folder (same as this one)
- **CLAUDE.md**   Project-specific development standards (in project root)
- **Memory system**   At ~/.claude/projects/C--1myguy/memory/ (context across sessions)

---

**Generated:** June 4, 2026  
**Purpose:** Document how CMA was built to enable replication for future projects  
**Status:** Complete & ready for reference
