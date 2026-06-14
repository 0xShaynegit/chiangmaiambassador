# Chiang Mai Ambassador - Handover

**Last updated:** 14/06/2026
**Session:** Hero standardisation site-wide + blog backlog logged

---

## Current Position

Site is clean. 112 pages. All blog pages now have consistent hero treatment: eyebrow label + gold-gradient-text on h1 key phrase. Blog backlog documented for future content work.

| Commit | What |
|--------|------|
| `b06a6bb` | Photo credit (Jonky Dawson) on homepage. Nav hamburger batch-added to all 110 pages. |
| `5c864aa` | dying-in-thailand.html created (879 lines). Full practical guide. |
| `1a12a0e` | dying-in-thailand added to sitemap + nav under Guides on all 111 pages. |
| `e0a17e4` | Inline links to dying-in-thailand from 5 related pages. |
| `8d0454d` | Removed btn-primary button from dying page. Inline text only. |
| `ab39611` | Fixed 3 hero lanterns stuck at bottom of index.html. Removed float-6/7/8 (no CSS keyframes for them). |
| `14001e1` | TL;DR image on planning-a-move-to-thailand.html fixed to standard size (280px). PDF link added to TL;DR. |
| `25ab57d` | Site-wide hero standardisation: `<span class="eyebrow">Category</span>` added to 95 blog pages. `<span class="gold-gradient-text">...</span>` added to h1 on 5 pages that were missing it (internet, mobile-phones, television, chiang-mai-festivals, thailand-media). |

---

## Blog Backlog

Full content gap list at: `blog-backlog.md` in site root.
Top 10 missing topics: dental care, cafes/coffee, vegan dining, buying property, temples/Buddhism, scams/fraud, northern Thailand travel, street food guide, tattoos, Sak Yant.
Work from this list when there is nothing else pressing.

---

## Still NOT Done (carried)

1. **guides/what-to-do-after-a-vehicle-accident.html** - different internal layout (no blog-content wrapper, no TL;DR figure). Needs visual confirmation before touching.
2. **pages/visas.html** - TL;DR figure sits after article-sidebar. pages/ uses page-template so rule may not apply. Left alone.
3. **Substituted images** needing human eyes: finding-pet-friendly-home cards, internet/TV/mobile-phones cards use generic fallback images.
4. **Re-run Lighthouse** after Cloudflare propagation.

---

## Key Technical Notes

- **CSS:** All styles in `css/styles.css`. Original 4 files still in `css/` but unlinked.
- **Blog hero standard:** `<span class="eyebrow">Category</span>` before h1, key phrase in `<span class="gold-gradient-text">...</span>` inside h1.
- **LOCKED TL;DR figure style** (blog template pages): before `<div class="article-sidebar">`, never inside it. Width: `calc(100% - 400px); max-width: 280px;` with `margin-top: -30px`.
- **PowerShell:** `[System.IO.File]::ReadAllText()/WriteAllText()` only, never Set-Content.
- **Two-template system:** pages/ uses page-template.html; all other folders use template.html.
- **No buttons for links:** inline text only. Never btn-primary for related content links.
- **Repo:** `C:\ZZZWebsites\chiangmaiambassador`, GitHub `0xShaynegit/chiangmaiambassador`, live chiangmaiambassador.com
- **handover.md is in .gitignore:** use `git add -f handover.md` to commit it.
