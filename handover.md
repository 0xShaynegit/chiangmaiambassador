# Chiang Mai Ambassador - Handover

**Last updated:** 15/06/2026 (end of session)
**Session:** Nav restructure, dying-in-thailand improvements, broken image fix, content research

---

## Current Position

Site is clean. Last commit `4eda329`. Nav fully restructured on index.html only   other pages retain old nav until next session approves rollout.

| Commit | What |
|--------|------|
| `4eda329` | Nav restructured to journey model (1.Planning / 2.Arriving / 3.Living Here / Explore / Visas). dying-in-thailand executor/POA section rewritten, two location-based death process sections added. live-in-chiang-mai broken Women's Prison Massage image fixed. |
| `33acdeb` | Fixed TL;DR image float on dying-in-thailand.html. |
| `25ab57d` | Site-wide hero standardisation: eyebrow + gold-gradient-text on all blog pages. |
| `971067b` | Rebuilt lifestyle/traveling-alone.html. |
| `c12df47` | Fixed double footer on 16 pages. |
| `a68ca16` | Full audit fixes: placeholder footer nav replaced on 17 pages. |
| `0eab3ee` | Button links fixed. |
| `69e9fcd` | Orphaned content links fixed. |

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
5. **Nav rollout** - new journey-based nav is on index.html only. Needs approval before rolling to all other pages.

---

## Content Research Tasks (investigate before writing)

1. **Bangkok Bank 4-month seasoning** - Verify current policy. Is KBank/SCB/Krungsri now the correct recommendation for new arrivals on 90-day Non-O? Update retirement visa and banking pages.
2. **CoR originals vs copies** - Confirm each use requires a separate original. Update residency certificate guide.
3. **Driving licence** - Car and moto are separate licences with separate CoR. Verify current DLT process for foreign licence + IDP holders. Update guide.
4. **Pet travel guide** - Add: microchipping mandatory, AQS off-airport collection, 3-month prep timeline, morning arrival for heat, cage bedding welfare, agent vs DIY section.
5. **Smoky season** - Add warning inline on planning and moving checklist pages. Flag lease timing risk.
6. **Wise transfer timing** - Now 2-3 days, not instant. Update retirement visa and banking content. Add cash backup advice.
7. **TM.30 framing** - Filed BY the landlord, not obtained by the foreigner. Audit all pages mentioning TM.30.

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
