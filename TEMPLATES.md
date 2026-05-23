# Template System

Three templates. Shared nav, hero, footer. Distinct body styles.

## 1. Homepage (index.html)

**Location:** Root

**Style:** High-contrast editorial with asymmetric grid, vibrant colors, bold typography

**Components:**
- Vibrant hero split (content + image)
- Floating stat card with parallax
- Pathway cards (3-column grid)
- All patterns from design system

**Use when:** Landing, campaign, main entry point

**Building workflow:**
1. Copy index.html structure
2. Keep nav, hero-split, pathways sections
3. Swap colors: path-gold, path-purple, path-ink for card variations
4. Add floating-stat for key metrics

## 2. Blog Template (blogs/template.html)

**Location:** blogs/

**Style:** White editorial body, focused on long-form reading, high contrast ink on white

**Components:**
- Simple hero (no parallax, no image)
- White body background for readability
- 2-column layout: article (main) + sidebar (related, categories)
- Author bio card
- Related posts grid (3 cards)
- Blog metadata (date, category badges)

**Use when:** Blog posts, articles, guides, tutorials

**Building workflow:**
1. Copy blogs/template.html
2. Replace blog-header (title, excerpt, meta)
3. Write content in blog-body
4. Update sidebar (related posts, categories)
5. Update author card
6. Update related posts grid

**Content requirements:**
- Cover image: place in images/
- Author avatar: place in images/ (120x120px+, square crop)
- Blog thumbnails: place in images/ (200px height)
- All image paths: `../images/filename.webp`

## 3. Pages Template (pages/template.html)

**Location:** pages/

**Style:** Homepage aesthetic. Vibrant hero split, multiple sections, call-to-action

**Components:**
- Hero split (content + floating stat + parallax image)
- Multiple section blocks (use pathway-grid pattern)
- Pathway cards for features/benefits/steps
- Same color system as homepage

**Use when:** About, pricing, features, services, contact, legal

**Building workflow:**
1. Copy pages/template.html
2. Customize hero split (heading, description, CTA buttons)
3. Add section blocks (use pathway-grid repeating)
4. Swap card colors: path-gold, path-purple, path-ink
5. Add footer links

## Shared Elements

### Navigation (All Templates)
```html
<nav class="nav-wrapper container reveal">
    <div class="logo"><span class="logo-accent">CM</span>Ambassador</div>
    <div class="nav-links">
        <a href="/">Home</a>
        <a href="/#areas">The Areas</a>
        <a href="/#costs">Lifestyle Costs</a>
        <a href="/#start" class="btn-primary magnetic-item">Start Here</a>
    </div>
</nav>
```
**Update:** Internal links point to homepage anchors or relative paths

### Footer (All Templates)
```html
<footer class="footer">
    <div class="container">
        <div class="footer-content">
            <!-- 3-column layout -->
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Chiang Mai Ambassador. All rights reserved.</p>
        </div>
    </div>
</footer>
```
**Update:** Links to match your site structure

## CSS Architecture

- **tokens.css:** Color, typography, animation tokens (shared)
- **base.css:** Resets, fonts, core styles (shared)
- **sections.css:** Nav, hero, pathways, containers (shared)
- **components.css:** Buttons, animations, footer (shared)
- **blog.css:** Blog-only styles (white body, sidebar, author card, related grid)

**Images served:**
- Homepage hero: images/chiang-mai-hero.webp
- Blog thumbnails: images/blog-thumb-*.webp
- Blog post images: images/blog-example.webp (etc.)
- Author avatar: images/author-avatar.webp (120x120px, square)

## Common Customizations

### Change Card Colors
Cards use: `path-gold`, `path-purple`, `path-ink`

Replace class in pathway-grid:
```html
<div class="path-card path-gold">  <!-- Change color here -->
```

Available:
- `path-gold` - var(--color-primary) / Marigold
- `path-purple` - var(--color-secondary) / Purple
- `path-ink` - var(--color-ink) / Midnight Blue

### Add Images
```html
<img src="../images/filename.webp" alt="Descriptive text" class="parallax-img">
```
Parallax class is optional (motion on scroll).

### Blog Sidebar Sections
Add new widget:
```html
<div class="sidebar-widget">
    <h4>Widget Title</h4>
    <ul>
        <li><a href="#">Link</a></li>
        <li><a href="#">Link</a></li>
    </ul>
</div>
```

### Related Posts Grid
Update blog-card items:
```html
<article class="blog-card reveal">
    <img src="../images/blog-thumb.webp" alt="">
    <h3>Title</h3>
    <p>Excerpt</p>
    <a href="#" class="arrow-link">Read more →</a>
</article>
```

## File Naming

**Blog images:**
- Thumbnails: `blog-thumb-1.webp`, `blog-thumb-2.webp`
- Featured: `blog-example.webp`, `blog-cost-living.webp` (semantic)
- Avatars: `author-avatar.webp`

**Page images:**
- Heroes: `page-hero.webp`
- Featured: Semantic naming (e.g., `visa-guide-hero.webp`)

**All:** WebP format, < 150KB for heroes, < 100KB for thumbnails

## Responsive Breakpoints

- Desktop: 1200px (full grid)
- Tablet: 768px (2 columns, stacked sidebar)
- Mobile: 640px (1 column, stacked everything)

Templates auto-adapt. Test at: 640px, 1024px, 1200px+

## Performance

All templates:
- Vanilla JS only (no external libraries)
- Local fonts preloaded
- CSS < 30KB total
- Images WebP optimized
- Core Web Vitals targets: LCP < 2.5s, CLS < 0.1
