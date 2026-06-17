# CHIANG MAI AMBASSADOR - TEMPLATE FIRST PRINCIPLE

## OVERRIDING RULE: All Pages From Templates

**When creating any page for Chiang Mai Ambassador: you are NOT building from first principles. You are building FROM A TEMPLATE.**

This applies to:
- Single pages
- 50 SEO pages in a batch
- Blog posts
- New sections
- New features
- Every HTML page in this project

**If you don't know which template to use, ASK. Do not write HTML from scratch.**

### The One Exception

Creating a brand new template for this project for the very first time. That's it. Every other page: from template.

### Why This Rule Exists

- **Speed:** Copy template, adjust paths, update content, ship. 15 minutes. Not 4+ hours of iteration.
- **Consistency:** Template IS the brand. Nav, footer, typography, spacing. They never drift.
- **Quality:** Template ensures the page works. No structural surprises. No contrast issues. No accessibility gaps.
- **Discipline:** When feedback points to surface issues, ask before patching. Structural problems hide under styling symptoms.

---

# CHIANG MAI AMBASSADOR - TEMPLATE STANDARD (TWO-TEMPLATE SYSTEM)

**Every page uses ONE of two templates. No custom structures. No nav redesigns. No footer changes.**

---

## Template Selection (REQUIRED)

When creating content, you MUST specify which template to use:

### 1. page-template.html
**Location:** pages/ folder only
**Purpose:** Long-form, permanent reference content
**Use for:** Pages, guides, landing pages, definitive reference material
**Features:** Hero section, NO TL;DR, solid long-term structure
**Example content:** Cost of living, neighbourhoods

### 2. template.html
**Location:** Any other folder (root, lifestyle/, guides/, etc.)
**Purpose:** Blog-style informational content
**Use for:** Blog posts, news, timely articles, educational pieces
**Features:** Blog metadata, TL;DR sidebar, FAQ sections, blog styling
**Example content:** Blog articles, guides with frequent updates

---

## How to Use

**In your prompt:** Always specify which template
- "Create a page using page-template.html for..."
- "Build a blog post using template.html for..."

**If not specified:** I will ask which template you need

---

## For Creating Pages (page-template.html)

1. **Copy page-template.html from pages/ folder**
2. **Save with your page name** in pages/ directory
3. **Update only these sections:**
   - Meta description and title
   - Canonical URL and OG tags
   - Hero eyebrow, heading, paragraph
   - Hero CTA links
   - Hero image (560x700)
   - TL;DR sidebar bullets (if needed)
   - Main section headings and content
   - Callout boxes
   - JSON-LD schema

4. **Adjust paths:** All pages in pages/ use `../` prefix

5. **Never change:**
   - Nav structure or dropdowns
   - Footer structure or content
   - Hero split layout
   - Article sidebar styling
   - Callout box styling
   - Any CSS classes or structure

---

## For Creating Blog Posts (template.html)

1. **Copy template.html from project root**
2. **Save with your blog name** in correct folder
3. **Update only these sections:**
   - Meta description and title
   - H1 and excerpt
   - Breadcrumb path
   - Read time
   - Last updated date
   - Article intro heading and paragraph
   - TL;DR sidebar content
   - Body content (h3 sections and paragraphs)
   - Key takeaways text
   - Related cards (title, description, link)

4. **Adjust paths based on folder depth:**
   - In root or lifestyle/: Use `../` prefix
   - In lifestyle/neighborhoods/: Use `../../` prefix

5. **Never change:**
   - Nav structure or dropdowns
   - Footer structure or content
   - Blog metadata layout
   - Blog body styling
   - Key takeaways box styling
   - TL;DR sidebar styling
   - Any CSS classes or structure

---

## Files Using This Standard

**page-template.html users:**
- ✅ pages/cost-of-living.html
- ✅ pages/neighbourhoods.html
- ✅ Future pages in pages/ folder

**template.html users:**
- ✅ lifestyle/index.html
- ✅ lifestyle/moving-checklist.html
- ✅ lifestyle/neighborhoods/nimman.html
- ✅ lifestyle/neighborhoods/old-city.html
- ✅ lifestyle/neighborhoods/riverside.html
- ✅ Future blog posts

---

**This two-template system is locked in. No exceptions. Always specify which template in your prompt.**
