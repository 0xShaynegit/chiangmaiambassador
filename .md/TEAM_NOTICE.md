# TEAM NOTICE: Content Standards Enforcement (Effective Immediately)

## Current Status
**295 rule violations detected** across 101 pages. 

The project is currently **REJECTED** for deployment until these are fixed.

---

## Three Critical Failures

### 1. INLINE STYLES IN HEAD (96+ pages)
**Your code:**
```html
<head>
    <!-- ... meta tags -->
    <style>
        .blog-content { background-color: white !important; }
        .img-right-small { float: right; width: 30%; }
        <!-- More styles here -->
    </style>
</head>
```

**WHAT IT SHOULD BE:**
```html
<head>
    <!-- ... meta tags, NO <style> tags -->
    <link rel="stylesheet" href="../css/tokens.css">
    <link rel="stylesheet" href="../css/base.css">
    <link rel="stylesheet" href="../css/sections.css">
    <link rel="stylesheet" href="../css/components.css">
    <link rel="stylesheet" href="../css/blog.css">
</head>
```

**FIX:**
1. Copy all CSS from `<style>` block
2. Add it to `css/blog.css` or `css/components.css`
3. Delete the `<style>` block from head
4. Verify page still looks identical

**Why:** CSS in `<head>` breaks the template lock and makes the codebase unmaintainable. All styling must be external.

---

### 2. MULTIPLE H1 TAGS (38+ pages)
**Your code:**
```html
<h1>Page Title</h1>
<article>
    <h1>Article Title</h1>  <!-- WRONG: second H1 -->
</article>
```

**WHAT IT SHOULD BE:**
```html
<h1>Page Title</h1>
<article>
    <h2>Article Section</h2>  <!-- Should be H2 -->
    <h3>Subsection</h3>        <!-- Should be H3 -->
</article>
```

**FIX:**
1. Search for `<h1>` on each page
2. Keep only ONE h1 (should be the main page title)
3. Change all other h1s to h2 or h3 as appropriate
4. Maintain proper hierarchy: H1 → H2 → H3 → H4

**Why:** Google penalizes multiple H1s. Screen readers depend on proper hierarchy. SEO ranking drops.

---

### 3. MISSING OPEN GRAPH TAGS (8+ pages)
**Your code:**
```html
<meta property="og:title" content="Page Title">
<!-- missing og:site_name -->
<!-- missing og:image -->
```

**WHAT IT SHOULD BE:**
```html
<meta property="og:title" content="Page Title | Chiang Mai Ambassador">
<meta property="og:description" content="Description...">
<meta property="og:type" content="article">
<meta property="og:url" content="https://chiangmaiambassador.com/food/butter-is-better/">
<meta property="og:site_name" content="Chiang Mai Ambassador">
<meta property="og:image" content="https://chiangmaiambassador.com/images/og-image.webp">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

**FIX:** Add missing og:site_name and og:image to every page that doesn't have them.

---

## How to Fix (Step-by-Step)

### For Each Page You Create:

1. **Start with a template**
   - Copy `cheapest-border-run-chiang-mai.html` (reference template)
   - Replace content only. Don't touch nav, footer, structure

2. **Remove inline styles**
   - Search for `<style>` in head
   - Move CSS to external file
   - Delete the `<style>` block

3. **Fix heading hierarchy**
   - One H1 only (the page title)
   - Use H2 for main sections
   - Use H3 for subsections
   - Never skip levels (H1 → H3 is wrong)

4. **Add all OG tags**
   - Copy the template from above
   - Fill in your actual title, description, URL

5. **Run the audit**
   - Command: `python audit_pages.py`
   - Zero failures before you submit

---

## Enforcement Rules (Non-Negotiable)

**YOU DO NOT SUBMIT UNTIL:**
- [ ] Rule 1: No inline styles in head
- [ ] Rule 2: TEMPLATE LOCK (nav/footer locked)
- [ ] Rule 3: File in correct directory (guides/, food/, pages/, or root)
- [ ] Rule 4: Font preloads at correct depth
- [ ] Rule 5: All images have alt text, width/height, semantic names
- [ ] Rule 6: Canonical URL present and correct
- [ ] Rule 7: All OG tags present
- [ ] Rule 8: One H1 only, proper H1→H2→H3 hierarchy
- [ ] Rule 9: Breadcrumbs inside article, above H1
- [ ] Rule 10: Zero framework imports

**Checklist location:** `ENFORCEMENT_CHECKLIST.md` (this directory)

---

## Tools

**Automated audit script:**
```bash
python audit_pages.py
```

Run this before you submit any page. It checks all 10 rules automatically.

Output:
- `[PASS]` = rule passes
- `[FAIL]` = rule fails (fix required)
- `[WARN]` = rule warning (check it)

**Zero failures = page is ready to merge**

---

## What Happens If You Don't Fix

- Page gets rejected automatically
- You redo the work
- Everyone waits
- Deployment delayed
- Team wasted time

**Cost of enforcement:** 5 minutes per page (fixing before submission)
**Cost of no enforcement:** 50 hours of rework + delays

---

## Questions?

Read `ENFORCEMENT_CHECKLIST.md` for detailed rules.

Read individual rule sections above for specific fixes.

Run `python audit_pages.py` to see exactly what's broken on your page.

---

## Summary

**Old way:** Submit pages, get rejected, redo work, resubmit.
**New way:** Check locally with audit script, fix before submitting, instant approval.

The 10 rules are simple. Follow them. Test with the script. You're done.

This is not negotiable. Every page follows all 10 rules or it doesn't ship.

Let's move.
