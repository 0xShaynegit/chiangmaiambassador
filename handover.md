# Chiang Mai Ambassador - Handover

**Last updated:** 14/06/2026 (end of session)
**Session:** Structural audit, rebuilds, PDF compression, TL;DR image work

---

## Current Position

Site is clean. 112 pages. Full structural audit completed and all issues resolved. Zero placeholder links, zero double footers, consistent hero treatment across all blog pages.

| `33acdeb` | Fixed TL;DR image float on dying-in-thailand.html - float:right inline on figure. |
| Commit | What |
|--------|------|
| `25ab57d` | Site-wide hero standardisation: eyebrow + gold-gradient-text on all blog pages. |
| `971067b` | Rebuilt lifestyle/traveling-alone.html - removed double footer, structured content, proper FAQ + Guru Tip. |
| `c12df47` | Fixed double footer (stray footer mid-content) on 16 pages: best-chiang-mai, motorbike-registration, thai-eating-etiquette, understanding-thai-culture, womens-prison-massage, butter-is-better, siripanna-lunch, flat-tire, work-permit-medical-certificate, alcohol-observations, currency-in-and-out, learning-languages, life-budget, songkran, traveling-with-friends, vientiane-visa-run. |
| `a68ca16` | Full audit fixes: placeholder footer nav (Guides/Tools/Community) replaced with correct Explore/Visas/About on 17 pages. Analytics added to traveling-alone. |
| `0eab3ee` | Button links fixed: planning-a-move -> just-arriving, just-arriving -> living-better. |
| `69e9fcd` | Orphaned content links fixed: nomad groups -> getting-social, Digital Nomads -> facebook.com/groups/chiangmainomads. |

---

## Audit: Current Clean State

Run this PowerShell scan at start of any session to check structural health:

```powershell
$base = "C:\ZZZWebsites\chiangmaiambassador"
$files = Get-ChildItem -Path $base -Recurse -Filter "*.html" | Where-Object { $_.FullName -notlike "*_archive*" -and $_.FullName -notlike "*\.md*" -and $_.FullName -notlike "*_scripts*" -and $_.Name -ne "404.html" }
$issues = @()
foreach ($f in $files) {
    $c = [System.IO.File]::ReadAllText($f.FullName)
    $rel = $f.FullName.Replace("$base\", "")
    if ($c -match 'meta http-equiv="refresh"') { continue }
    if ($rel -eq "search.html") { continue }
    if (([regex]::Matches($c, '<footer class="site-footer"')).Count -gt 1) { $issues += "DOUBLE_FOOTER | $rel" }
    if (-not ($c -match '38ebf6cb1000449b961756de0ca25576')) { $issues += "NO_ANALYTICS | $rel" }
    if ($c -match 'href="#tools"') { $issues += "PLACEHOLDER_LINKS | $rel" }
    if ($c -match 'class="blog-hero"' -and -not ($c -match 'class="eyebrow"')) { $issues += "NO_EYEBROW | $rel" }
}
$issues | Group-Object { $_.Split(' | ')[0] } | ForEach-Object { Write-Host "=== $($_.Name) ($($_.Count)) ==="; $_.Group | ForEach-Object { Write-Host "  $($_.Split(' | ')[1])" } }
```

Known acceptable non-issues: pages/about.html (no eyebrow, uses page-template), chiang-mai/index.html and guides/index.html (no TL;DR, hub pages), pages/neighbourhoods.html (href="#nimman" etc. are valid anchors).

---

## Blog Backlog

Full content gap list at: `blog-backlog.md` in site root.
Top 10 missing topics: dental care, cafes/coffee, vegan dining, buying property, temples/Buddhism, scams/fraud, northern Thailand travel, street food guide, tattoos, Sak Yant.
Work from this list when there is nothing else pressing.

---

## Still NOT Done (carried)

1. **guides/what-to-do-after-a-vehicle-accident.html** - different internal layout (no blog-content wrapper, no TL;DR). Needs visual confirmation before touching.
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
- **Old migration pages** (traveling-alone, traveling-with-friends, etc.) had raw div content blobs with unclosed article tags. Check structure if editing these.
- **Footer nav standard:** Explore / Visas / About (3 groups). Any page showing Guides / Tools / Community is using the old wrong footer.
- **Cloudflare analytics token:** `38ebf6cb1000449b961756de0ca25576`
- **Repo:** `C:\ZZZWebsites\chiangmaiambassador`, GitHub `0xShaynegit/chiangmaiambassador`, live chiangmaiambassador.com
- **handover.md is in .gitignore:** use `git add -f handover.md` to commit it.
