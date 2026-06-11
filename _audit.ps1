$root = 'C:\ZZZWebsites\chiangmaiambassador'
$files = Get-ChildItem $root -Recurse -Filter *.html | Where-Object { $_.FullName -notmatch '_archive|node_modules|\\MD\\' }
$results = @()
foreach ($f in $files) {
    $rel = $f.FullName.Replace("$root\", '')
    $t = [System.IO.File]::ReadAllText($f.FullName)
    $dir = Split-Path $f.FullName -Parent

    # word count of visible-ish text (strip tags/scripts/styles)
    $body = $t -replace '(?s)<script.*?</script>', '' -replace '(?s)<style.*?</style>', '' -replace '<[^>]+>', ' '
    $wc = ($body -split '\s+' | Where-Object { $_ }).Count

    # images without alt
    $imgs = [regex]::Matches($t, '<img\b[^>]*>')
    $noAlt = ($imgs | Where-Object { $_.Value -notmatch 'alt\s*=' }).Count
    $noDim = ($imgs | Where-Object { $_.Value -notmatch 'width\s*=' -or $_.Value -notmatch 'height\s*=' }).Count

    # broken internal links (href/src to local files)
    $broken = @()
    foreach ($m in [regex]::Matches($t, '(?:href|src)\s*=\s*"([^"#?]+?)(?:[#?][^"]*)?"')) {
        $u = $m.Groups[1].Value
        if ($u -match '^(https?:|mailto:|tel:|javascript:|data:|//)' -or $u -eq '' -or $u -eq '/') { continue }
        if ($u.StartsWith('/')) { $p = Join-Path $root $u.TrimStart('/') } else { $p = Join-Path $dir $u }
        try { $p = [System.IO.Path]::GetFullPath($p) } catch { continue }
        if (-not (Test-Path $p)) { $broken += $u }
    }
    $broken = $broken | Select-Object -Unique

    # external CDN/script refs
    $cdn = [regex]::Matches($t, '(?:src|href)\s*=\s*"(https?://[^"]+\.(?:js|css)[^"]*)"') | ForEach-Object { $_.Groups[1].Value } | Where-Object { $_ -notmatch 'cloudflareinsights' } | Select-Object -Unique

    # em/en dashes
    $dashes = ([regex]::Matches($t, "[" + [char]0x2013 + [char]0x2014 + "]")).Count

    # TLDR figure check
    $figIdx = $t.IndexOf('img-right-small')
    $sbIdx = $t.IndexOf('article-sidebar')
    $tldrOrder = if ($figIdx -lt 0) { 'no-figure' } elseif ($sbIdx -lt 0) { 'no-sidebar' } elseif ($figIdx -lt $sbIdx) { 'ok' } else { 'AFTER-sidebar' }

    $results += [pscustomobject]@{
        Page       = $rel
        Words      = $wc
        Title      = if ($t -match '<title>') { 'y' } else { 'MISSING' }
        Desc       = if ($t -match 'name="description"') { 'y' } else { 'MISSING' }
        Canonical  = if ($t -match 'rel="canonical"') { 'y' } else { 'MISSING' }
        OG         = if ($t -match 'property="og:title"') { 'y' } else { 'MISSING' }
        Schema     = if ($t -match 'application/ld\+json') { 'y' } else { 'MISSING' }
        Analytics  = if ($t -match 'cloudflareinsights|beacon\.min\.js') { 'y' } else { 'MISSING' }
        Preloads   = ([regex]::Matches($t, 'rel="preload"')).Count
        BlogArt    = if ($t -match '<article class="blog-content"') { 'y' } elseif ($t -match 'class="blog-content"') { 'section' } else { '-' }
        TLDR       = $tldrOrder
        FAQ        = ([regex]::Matches($t, 'class="faq-item"')).Count
        Tips       = if ($t -match 'tips-box') { 'y' } else { '-' }
        Related    = if ($t -match 'blog-related') { 'y' } else { '-' }
        NoAlt      = $noAlt
        NoDim      = $noDim
        Dashes     = $dashes
        WP         = if ($t -match 'wp-content|wp-includes') { 'WP!' } else { '' }
        CDN        = ($cdn -join '; ')
        Broken     = ($broken -join '; ')
    }
}
$results | Export-Csv "$root\_audit_results.csv" -NoTypeInformation -Encoding UTF8
Write-Host "Done: $($results.Count) pages"
