# Chiang Mai Ambassador - Handover

**Last updated:** 08/06/2026
**Session:** Light-background blog page standardisation (all major content folders)

---

## Current Position

The full site-wide blog standardisation pass is COMPLETE across all four target folders.

### What Was Done This Session

**Reference standard:** `modern-transport-guide.html` (root level)

Every light-background blog/guide/lifestyle page now has:
- 1200+ words of clean content (WordPress blobs replaced)
- TL;DR figure with LOCKED inline style BEFORE article-sidebar (never inside it)
- `<article class="blog-content">` (not section)
- `article-sidebar` with real quick facts
- `key-takeaways` box where applicable
- FAQ section (5 items using `.faq-item` divs)
- Guru Tip in `.tips-box`
- `<section class="blog-related container">` with 3 blog-card articles
- `.faq-item` and `.tips-box` CSS in page `<style>` block
- Standard site footer and nav

### Commits This Session

| Commit | Folder | What |
|--------|--------|------|
| `5ecc64a` | guides/ | batch CSS + FAQ/tips fixes |
| `b1d9d35` | guides/ | 5 blob rewrites |
| `415dfca` | guides/ | 6 blob rewrites |
| `cae2ed9` | guides/ | blog-related sections; guides/ COMPLETE |
| `0d970fc` | lifestyle/ | 4 blob rewrites |
| `b1de627` | lifestyle/ | FAQ/tips all pages; lifestyle/ COMPLETE |
| `1ec94f7` | food/ | 4 blob rewrites + FAQ/tips all 9 pages; food/ COMPLETE |
| `821188f` | visa/ | FAQ/tips all 13 pages; visa/ COMPLETE |

### Folder Status

| Folder | Pages | Blobs | FAQ | Tips | Related | Status |
|--------|-------|-------|-----|------|---------|--------|
| guides/ | 27 | 0 | all | all | all | DONE |
| lifestyle/ | 21 | 0 | all | all | all | DONE |
| food/ | 9 | 0 | all | all | all | DONE |
| visa/ | 13 | 0 | all | all | all | DONE |

---

## What is NOT Done

- Dark-background pages were intentionally left untouched (by design)
- `blogs/` folder: has its own workflow (CMA Blog Copy-Template Pattern) - separate system, not part of this pass
- Root-level standalone pages (e.g. `where-to-stay-in-chiang-mai.html`) were not in scope for this pass
- No visual confirmation done - pages look structurally correct but no browser check this session

---

## Key Technical Notes

### LOCKED TL;DR figure style (never change)
```html
<figure class="img-right-small" style="margin-top: -30px; margin-bottom: 1rem; width: calc(100% - 400px); max-width: 280px;">
```
Figure goes BEFORE `<div class="article-sidebar">`, never inside it.

### Nav search path in subdirectories
`../search.html` (one level up only - not `../../search.html`)

### FAQ/tips CSS block location
Added inside `<style>` block in `<head>`, before `</style>`.

### PowerShell file ops
Always use `[System.IO.File]::ReadAllText()` and `WriteAllText()` - never Set-Content or Out-File (line ending corruption).

### Insertion marker for FAQ/tips
`        </article>` - insert FAQ/tips HTML before this marker.

---

## Site Reference

- **Repo:** `C:\ZZZWebsites\chiangmaiambassador`
- **GitHub:** `0xShaynegit/chiangmaiambassador`
- **Live:** chiangmaiambassador.com
- **89 pages total** (blogs + guides + lifestyle + food + visa + root pages)
- **Two-template system:** `pages/` uses `page-template.html`; all other folders use `template.html`
- **Images:** `../images/` from subdirectory pages
- **Fonts:** `../fonts/` from subdirectory pages

---

## Next Possible Work

- Visual spot-check any pages flagged as needing human image review (le-meridien, siripanna had placeholder TL;DR figures - replaced with ChefFuji images as fallback)
- blogs/ folder: ongoing blog creation uses copy-template pattern from `cheapest-border-run.html`
- Internal linking pass across visa/ and guides/ (cross-linking related topics)
- Schema markup audit (Petra)
