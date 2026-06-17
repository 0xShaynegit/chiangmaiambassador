# Chiang Mai Ambassador - Development Standards

## TEMPLATE FIRST - The Overriding Principle

**When creating any page: you are NOT building from first principles. You are building FROM A TEMPLATE.**

This applies to:
- Single pages
- 50 SEO pages in a batch
- Blog posts
- New sections
- New features
- Every HTML page

**If you don't know which template to use, ASK. Do not write HTML from scratch.**

### The One Exception

Creating a brand new template for this project for the very first time. That's it. Every other page: from template.

### Why This Rule Exists

- **Speed:** Copy template, adjust paths, update content, ship. 15 minutes. Not 4+ hours of iteration.
- **Consistency:** Template IS the brand. Nav, footer, typography, spacing. They never drift.
- **Quality:** Template ensures the page works. No structural surprises. No contrast issues. No accessibility gaps.
- **Discipline:** When feedback points to surface issues, ask before patching. Structural problems hide under styling symptoms.

---

## Project Structure

```
chiangmaiambassador/
├── CLAUDE.md (this file - development standards)
├── TEMPLATE_STANDARD.md (template reference and rules)
├── template.html (master page template)
├── css/
│   ├── tokens.css (design tokens)
│   ├── base.css (base styles)
│   ├── sections.css (section layouts)
│   ├── components.css (reusable components)
│   └── blog.css (blog-specific styles)
├── fonts/
│   ├── outfit-600.woff2
│   ├── outfit-800.woff2
│   ├── plus-jakarta-400.woff2
│   └── plus-jakarta-500.woff2
├── js/
│   └── main.js (progress bar and interactivity)
├── images/ (all WebP, semantically named)
├── lifestyle/
│   ├── README.md (lifestyle section standards)
│   ├── index.html (living in Chiang Mai overview)
│   ├── moving-checklist.html
│   └── neighborhoods/
│       ├── nimman.html
│       ├── old-city.html
│       └── riverside.html
├── chiang-mai/ (other sections follow same structure)
├── guides/
├── food/
└── pages/ (legal, privacy, terms, etc.)
```

---

## Creating a New Page - Step by Step

### Step 1: Identify the Template
Ask: "Which template should this use?"
- Most blog/guide pages: `template.html`
- Different type? Ask before building.

### Step 2: Copy the Template
```
cp template.html [your-page-name].html
```

### Step 3: Adjust Paths Based on Folder Depth

- **Root or /lifestyle/** (1 level deep): Use `../` prefix
  - `../css/tokens.css`
  - `../fonts/outfit-600.woff2`
  - `../images/...`
  - `../js/main.js`

- **/lifestyle/neighborhoods/** (2 levels deep): Use `../../` prefix
  - `../../css/tokens.css`
  - `../../fonts/outfit-600.woff2`
  - `../../images/...`
  - `../../js/main.js`

- **All nav links adjust by same depth**
  - Root: `../chiang-mai/`, `../lifestyle/`, etc.
  - neighborhoods/: `../../chiang-mai/`, `../../lifestyle/`, etc.

### Step 4: Update Content Only

These sections change. Everything else stays locked:

- **Meta tags (head)**
  - `<meta name="description">`
  - `<title>Page Title | Chiang Mai Ambassador</title>`

- **Blog hero section**
  - `<h1>Your Heading <span class="gold-gradient-text">Highlight</span></h1>`
  - `<p class="blog-excerpt">Brief description...</p>`

- **Blog metadata**
  - Breadcrumb path: `<a href="...">Home</a> / Category / Topic`
  - Read time: `5 min`, `8 min`, etc.
  - Last updated: `May 24, 2026`

- **Article intro**
  - `<h2>Main Opening Question</h2>`
  - `<p class="article-vibe">Explanation paragraph...</p>`

- **TL;DR sidebar** (article-sidebar)
  - `<h4>Title</h4>`
  - `<ul>` bullet points

- **Body content** (blog-body)
  - `<h3>Section Headings</h3>`
  - `<p>Body paragraphs...</p>`
  - `<strong>Bold text</strong>`

- **Key takeaways section**
  - `<h3>Key Takeaways</h3>`
  - `<p>Summary paragraph...</p>`

- **Related blog cards**
  - Card title, description, link only
  - Keep images and layout structure

### Step 5: JSON-LD Schema

Update the schema with correct headline and description:
```json
{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "Your Page Title",
    "description": "Your meta description",
    "datePublished": "2026-05-24",
    "author": { "@type": "Organization", "name": "Chiang Mai Ambassador" }
}
```

### Step 6: Ship

That's it. Done. No customization. No redesign. No new CSS blocks.

---

## What's Locked (Never Changes)

- Navigation structure with logo and SVG
- Navigation dropdowns with all menu items
- Footer structure, layout, and content
- Blog metadata styling and layout
- Blog body typography and spacing
- Key takeaways box styling
- Related posts section layout
- Article sidebar (TL;DR box) styling
- Progress bar and interactivity
- Script tags and references

---

## Operational Rules

- **No custom nav.** The nav is the brand.
- **No footer redesigns.** The footer is the brand.
- **No new CSS blocks.** Template CSS is comprehensive.
- **No inline styles for layout.** Only inline styles already in template (margin-top, padding, etc.)
- **No new fonts.** Use Outfit and Plus Jakarta only.
- **No framework imports.** Zero React, Vue, Tailwind. Pure vanilla.
- **No CDN assets.** All fonts, CSS, JS are local.
- **Images WebP only.** Semantic naming. Under 200KB per page total.

---

## Files Using This Standard

- ✅ template.html (master)
- ✅ lifestyle/index.html
- ✅ lifestyle/moving-checklist.html
- ✅ lifestyle/neighborhoods/nimman.html
- ✅ lifestyle/neighborhoods/old-city.html
- ✅ lifestyle/neighborhoods/riverside.html

All future pages follow this exact pattern.

---

## When Something Feels Off

- **Feedback points to styling issues?** Ask if it's structural before patching.
- **Nav looks wrong?** Don't customize it. Copy the exact template nav.
- **Footer text doesn't align?** Don't change the footer. Copy the exact template footer.
- **Page layout feels cramped?** Don't invent new CSS. Use template structure and spacing.

**Template first. Always. No exceptions beyond that one exception.**

---

## Quick Reference

| Task | Answer |
|------|--------|
| Creating a new page? | Copy template.html |
| Don't know which template? | Ask |
| Need custom nav? | Use template nav |
| Need custom footer? | Use template footer |
| Need custom styling? | Use template CSS only |
| Want to add a new feature? | Does template support it? If not, ask. |

**Template is the law. Follow it exactly.**
