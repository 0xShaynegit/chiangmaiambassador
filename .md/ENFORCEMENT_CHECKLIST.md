# Chiang Mai Ambassador: Enforcement Checklist
**All 10 rules are NON-NEGOTIABLE. Zero exceptions.**

---

## Rule 1: No Inline Styles in `<head>`
**VIOLATION:** Inline `<style>` blocks in HEAD
**CORRECT:** All CSS in external files (tokens.css, base.css, sections.css, components.css, blog.css)

**Check:** Grep for `<style>` in any page. If found, move to external CSS file.
```bash
grep -n "<style>" *.html guides/*.html food/*.html pages/*.html chiang-mai/*.html
```

---

## Rule 2: TEMPLATE LOCK Protocol
**LOCKED SECTIONS (Never touch after first approval):**
- Navigation (`<nav class="nav-wrapper">`)
- Footer (`<footer>`)
- Breadcrumb structure
- Hero section structure
- Page progress bar

**LOCKED FILES (Read-only):**
- cheapest-border-run-chiang-mai.html (BLOG TEMPLATE)
- pages/cost-of-living.html (REFERENCE PAGE)
- index.html (HOMEPAGE)

**EDITABLE SECTIONS ONLY:**
- Main article content (between `<article>` tags)
- Meta tags (title, description, og tags)
- Heading text
- Body copy
- Images (filename, alt text, placement)

---

## Rule 3: Consistent Path Structure
**APPROVED DIRECTORIES:**
- Root level: Homepage, main articles (best-chiang-mai.html, cheapest-border-run-chiang-mai.html)
- `/guides/` = Guides (chiang-mai-driving.html, blood-donation-procedure.html)
- `/food/` = Food reviews (butter-is-better.html, real-thai-restaurant.html)
- `/pages/` = Landing pages (cost-of-living.html, neighbourhoods.html)
- `/chiang-mai/` = Index pages only (index.html)

**VIOLATION:** Pages created in wrong directories or mixed structure
**RULE:** New page goes in correct directory based on TYPE, not author preference

---

## Rule 4: Font Preloads by Directory Depth
**ROOT LEVEL (e.g., index.html):**
```html
<link rel="preload" href="fonts/outfit-600.woff2" as="font" type="font/woff2" crossorigin>
```

**SUBDIRECTORY 1 LEVEL DEEP (e.g., guides/page.html, food/page.html, pages/page.html):**
```html
<link rel="preload" href="../fonts/outfit-600.woff2" as="font" type="font/woff2" crossorigin>
```

**SUBDIRECTORY 2 LEVELS DEEP (e.g., chiang-mai/subdir/page.html):**
```html
<link rel="preload" href="../../fonts/outfit-600.woff2" as="font" type="font/woff2" crossorigin>
```

**REQUIRED FONTS (all 4, every page):**
- outfit-600.woff2
- outfit-800.woff2
- plus-jakarta-400.woff2
- plus-jakarta-500.woff2

---

## Rule 5: Image Standards
**SEMANTIC NAMING:**
```
chiang-mai-ambassador-[page-slug]-[SEMANTIC].webp
```

Examples:
- `chiang-mai-ambassador-butter-is-better-brunch-platter.webp`
- `chiang-mai-ambassador-blood-donation-red-cross-entrance.webp`
- `chiang-mai-ambassador-cost-of-living-coffee-shop.webp`

**REQUIRED ATTRIBUTES ON EVERY `<img>` TAG:**
```html
<img src="image.webp" alt="Descriptive alt text" width="XXX" height="YYY">
```

**IMAGE FORMAT:** WebP only. No PNG, JPG, JPEG.
**IMAGE SIZE:** 50-150KB per image (total page images under 500KB)
**ALT TEXT:** Must describe image in 8-15 words. No generic "image" or "photo".

---

## Rule 6: Canonical URL (Every Page)
**RULE:** Must match actual URL structure
```html
<link rel="canonical" href="https://chiangmaiambassador.com/food/butter-is-better/">
```

**ROOT PAGES:**
- `https://chiangmaiambassador.com/index/`

**SUBDIRECTORY PAGES:**
- `https://chiangmaiambassador.com/food/butter-is-better/`
- `https://chiangmaiambassador.com/guides/blood-donation-procedure/`
- `https://chiangmaiambassador.com/pages/cost-of-living/`

---

## Rule 7: Open Graph Tags (Every Page)
**REQUIRED TAGS:**
```html
<meta property="og:title" content="Page Title | Chiang Mai Ambassador">
<meta property="og:description" content="Meta description text">
<meta property="og:type" content="article">
<meta property="og:url" content="https://chiangmaiambassador.com/path/">
<meta property="og:site_name" content="Chiang Mai Ambassador">
<meta property="og:image" content="https://chiangmaiambassador.com/images/og-image.webp">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

**TWITTER TAGS (if available):**
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Page Title">
<meta name="twitter:description" content="Meta description text">
<meta name="twitter:image" content="https://chiangmaiambassador.com/images/og-image.webp">
```

---

## Rule 8: Heading Hierarchy (H1 → H2 → H3)
**RULE:** One H1 per page, always first heading
```html
<h1>Main page title</h1>
<h2>First major section</h2>
<h3>Subsection within H2</h3>
```

**VIOLATION:** 
- Multiple H1s on same page
- H2 before H1
- Skipping heading levels (H1 → H3)
- Using H1 for non-title text

---

## Rule 9: Breadcrumb Position & Structure
**POSITION:** Inside article container, above main heading
```html
<article class="article-content">
    <nav class="breadcrumbs">
        <a href="/">Home</a>
        <span>/</span>
        <a href="/food/">Food</a>
        <span>/</span>
        <span>Butter is Better</span>
    </nav>
    <h1>Butter is Better | American Diner in Chiang Mai</h1>
    <!-- Content follows -->
</article>
```

**RULE:** Breadcrumbs never full-width strip. Always aligned with text column.

---

## Rule 10: No External Framework Imports
**VIOLATIONS (will be rejected):**
- React, Vue, Svelte imports
- Tailwind CSS (`@tailwind`)
- Bootstrap, Foundation
- UI component libraries
- JavaScript frameworks

**ALLOWED ONLY:**
- Plain CSS (external files)
- Plain HTML (semantic tags)
- Vanilla JavaScript (no framework)
- Local assets (fonts, images)

---

## Audit Steps (For Each New Page)

### Before Deploy:
1. **Path Check:** Is it in the right directory? (guides/, food/, pages/, or root?)
2. **No Inline Styles:** Grep for `<style>` tag. Must be zero results.
3. **Template Copied:** Does it match cheapest-border-run.html structure? (Nav locked, footer locked?)
4. **Font Preloads:** All 4 fonts present with correct path depth?
5. **Images:** All WebP, semantic names, width/height attributes, alt text?
6. **Canonical URL:** Correct and matches actual URL?
7. **OG Tags:** All required tags present?
8. **Heading Hierarchy:** One H1, proper H1→H2→H3 flow?
9. **Breadcrumbs:** Positioned inside article, above H1?
10. **No Frameworks:** Zero external library imports?

---

## Automation Script
```bash
# Audit script to run on entire project
# See AUDIT_SCRIPT.sh (separate file)
```

---

## Enforcement Gates

**BEFORE MERGE/DEPLOY:**
1. **Dev passes 10-point check** (self-audit)
2. **You run audit script** (automated check)
3. **Page renders in browser** (visual check)
4. **No inline styles visible** (manual grep)

**IF ANY RULE VIOLATED:**
- Page rejected. Return to author.
- Author must fix and resubmit.
- No exceptions. No negotiation.

---

## Summary
These 10 rules are **THE ENTIRE STANDARD**. No ambiguity. No discretion.

Train the team. Audit on merge. Enforce consistently.

**Cost of enforcement:** 5 minutes per page.
**Cost of no enforcement:** 50 hours of broken builds, cascading errors, and team rework.
