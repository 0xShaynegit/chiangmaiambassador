# Chiang Mai Ambassador - Handover

**Last updated:** 11/06/2026
**Session:** Full-site audit + cleanup pass (links, images, OG tags, dashes, internal linking)

---

## Current Position

Full 111-page audit run, then "action all" cleanup. Two commits:

| Commit | What |
|--------|------|
| `e0748ec` | Site-wide broken links and image paths fixed |
| `a78f782` | OG tags, dash cleanup, 207 internal links across 81 pages |

### Done this session
- **Nav search link** was one level too deep on 78 pages (root used `../search.html`, subdirs `../../search.html`). All corrected. NOTE: old handover note saying `../search.html` is correct for subdirs was WRONG. Correct: root = `search.html`, one-level subdirs = `../search.html`, neighborhoods = `../../search.html`.
- **41 image refs** repointed to correct `/images` depth; ~20 genuinely missing image files substituted with existing semantic matches (some are generic fallbacks, see "needs human review").
- **Broken page links** fixed: motorbike-registration tag links, about.html, vets (mobile-languages typo), smoky-season (cost-of-living path), festivals (modern-transport path).
- **Neighborhoods favicon** fixed (7 pages, now `../../favicon.svg`).
- **Canonical + OG + Twitter** added: nimman, old-city, riverside, chiang-mai-vs-da-nang.
- **All em/en dashes removed** site-wide (8 pages had them; contextual replacement, numeric ranges use "to").
- **Internal linking pass:** 207 inline text links added across 81 pages via keyword wrapping (no copy rewritten). Visa silo now fully cross-linked.
- Audit scripts in `_archive/` (`_audit.ps1`, `_linkpass.ps1`).

### INCIDENT: h-to-r file corruption
During the session, 3 files (chiang-mai-festivals, vets-pet-care, smoky-season) had EVERY letter "h" replaced with "r" on disk ("Chiang" became "Criang", "<html>" became "<rtml>") after PowerShell writes. Cause not identified (not the em-dash hook, which only fires on Write/Edit tools). Files were restored from git HEAD and fixes reapplied cleanly. ALWAYS run a corruption check (`grep 'Criang|<rtml'`) after batch writes in this repo.

## NOT done (needs Shayne decision)
1. **Cloudflare Analytics:** entire site has NO analytics snippet except search.html which has placeholder token "your-token-here". Need the real CF beacon token to roll out site-wide.
2. **FAQ/tips additions** to root-level standalone blogs (8), neighborhoods (7), food-delivery-apps, late-night-eating: these were deliberately excluded from the June 8 standardisation pass (possibly dark-background templates). Adding FAQ blocks = visual format change; needs authorisation + visual check.
3. **guides/what-to-do-after-a-vehicle-accident.html**: different internal layout (callout-boxes, no blog-content wrapper, no TL;DR figure). Restructuring risks breakage without visual confirmation.
4. **pages/visas.html**: img-right-small figure sits after article-sidebar; pages/ uses page-template so the locked TL;DR ordering rule may not apply. Left alone.
5. **Substituted images needing human eyes:** finding-pet-friendly-home cards (bicycle/lantern images), internet/television/mobile-phones related cards (TDAC/lantern images), vets cards. They render but are semantically generic.

## Key Technical Notes (carried forward)
- LOCKED TL;DR figure style, before article-sidebar (blog template pages only)
- PowerShell: `[System.IO.File]::ReadAllText()/WriteAllText()` only
- FAQ/tips CSS goes in `<style>` block in head
- Two-template system: pages/ = page-template.html, other folders = template.html
- Repo: `C:\ZZZWebsites\chiangmaiambassador`, GitHub `0xShaynegit/chiangmaiambassador`, live chiangmaiambassador.com

## Next Possible Work
- Analytics token rollout (one script once token provided)
- FAQ/tips for out-of-scope pages (after design decision)
- Push to GitHub (commits are local only)
- Schema markup audit (Petra)
