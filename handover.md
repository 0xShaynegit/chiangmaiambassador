# Chiang Mai Ambassador - Handover

**Last updated:** 14/06/2026
**Session:** New blog post (dying in Thailand) + nav/sitemap/internal linking + bug fixes

---

## Current Position

Site is clean. 112 pages. All pages have nav hamburger button (fixed last session). New blog post live and fully linked.

| Commit | What |
|--------|------|
| `b06a6bb` | Photo credit added to homepage about section (Jonky Dawson). Nav hamburger button batch-added to all 110 non-index pages (fixes site-wide dropdown). |
| `5c864aa` | dying-in-thailand.html created (879 lines). Chiang Mai Guru voice. Full practical guide: death registration, embassy notification, repatriation costs table, local cremation, wills (Ken Brown FC links), insurance (Tawm Rosendal + internal guide link), 24hr checklist, Buddhist cremation context, FAQ. Article schema, OG, canonical, 4 font preloads, analytics. |
| `1a12a0e` | dying-in-thailand added to sitemap.xml. "Dying in Thailand" nav link added under Guides on all 111 pages (batch PowerShell). |
| `e0a17e4` | Inline links to dying-in-thailand added to 5 related pages: embassies-consulates, chiang-mai-insurance, moving-checklist, retirement-visa, living-better-in-thailand. |
| `8d0454d` | Removed btn-primary button at bottom of dying page. Replaced with inline text link. |
| `ab39611` | Fixed hero lanterns stuck at bottom of dying page. Root cause: blog-hero missing position:relative. Float elements are position:absolute and anchored to wrong parent without it. Added position:relative + overflow:hidden to the section. |

---

## New Page: dying-in-thailand.html

- Root-level file, same path depth as cheapest-border-run-chiang-mai.html
- All asset paths: no `../` prefix (fonts/, css/, js/, images/, favicon.svg)
- External links: Ken Brown FC (wills/estate planning), Tawm Rosendal Facebook (insurance)
- Internal links: pages/embassies-consulates.html (x3 inc. nav + inline + closing sentence), guides/chiang-mai-insurance.html
- CTA at bottom: inline text only (no button)

---

## Still NOT Done (carried from previous session)

1. **guides/what-to-do-after-a-vehicle-accident.html** -- different internal layout (no blog-content wrapper, no TL;DR figure). Restructuring needs visual confirmation.
2. **pages/visas.html** -- TL;DR figure sits after article-sidebar. pages/ uses page-template so rule may not apply. Left alone.
3. **Substituted images** needing human eyes: finding-pet-friendly-home cards, internet/TV/mobile-phones related cards use generic fallback images.
4. **Re-run Lighthouse** after Cloudflare propagation to confirm CWV improvements (CLS, INP, LCP fixes from previous session).

---

## Key Technical Notes

- **CSS:** All styles in `css/styles.css`. Original 4 files still exist in `css/` but unlinked. Do not delete until confident no rollback needed.
- **LOCKED TL;DR figure style** (blog template pages only): before `<div class="article-sidebar">`, never inside it
- **PowerShell:** `[System.IO.File]::ReadAllText()/WriteAllText()` only, never Set-Content
- **Two-template system:** pages/ uses page-template.html; all other folders use template.html
- **Blog-hero pages:** must have `position: relative; overflow: hidden` on the section or hero lanterns break
- **No buttons for links:** inline text only. Never btn-primary for related content links.
- **Repo:** `C:\ZZZWebsites\chiangmaiambassador`, GitHub `0xShaynegit/chiangmaiambassador`, live chiangmaiambassador.com

## Next Possible Work

- Internal linking second pass (root-level standalone blogs still thin on links)
- Schema markup audit (Petra)
- FAQ/tips for out-of-scope pages (after design decision)
- Add dying-in-thailand to sitemapv2.xml if that file is being maintained separately
