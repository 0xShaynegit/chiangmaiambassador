# Chiang Mai Ambassador

Premium expat guidance site. High-contrast digital editorial design with vanilla JS animations.

## Structure

```
chiang-mai-ambassador/
├── index.html           (Main page)
├── css/
│   ├── tokens.css       (Design system colors, typography)
│   ├── base.css         (Resets, fonts, core styles)
│   ├── sections.css     (Layout components)
│   └── components.css   (Animations, utilities)
├── js/
│   └── main.js          (Vanilla animations)
├── fonts/               (Local WOFF2 files)
├── images/              (WebP hero image)
├── pages/               (Additional pages)
├── blogs/               (Blog posts)
└── README.md
```

## Quick Start

1. Add fonts to `fonts/`:
   - outfit-600.woff2
   - outfit-800.woff2
   - plus-jakarta-400.woff2
   - plus-jakarta-500.woff2

2. Add hero image to `images/`:
   - chiang-mai-hero.webp (responsive, < 150KB)

3. Open index.html in browser. All animations work vanilla (no external libraries).

## Design System

Colors (from tokens.css):
- Ink: #0F172A (midnight blue, authority)
- Marigold: #EAB308 (vibrant gold, energy)
- Purple: #7E22CE (twilight haze)
- Emerald: #10B981 (tropical growth)

Typography:
- Headings: Outfit (600, 800)
- Body: Plus Jakarta Sans (400, 500)

## Animations

All animations are vanilla JS + CSS:
- Reveal animations on scroll (Intersection Observer)
- Floating stat bob (CSS @keyframes)
- Magnetic button effect (mouse tracking)
- Parallax hero image (scroll-based)

## Standards

- WCAG 2.2 AA accessibility
- Semantic HTML (no divitis)
- Responsive grid (3 col desktop, 2 col tablet, 1 col mobile)
- Performance: LCP < 2.5s, CLS < 0.1
- Zero external dependencies or CDNs

## Deployment

Cloudflare Pages or Vercel:
1. Extract folder to GitHub
2. Deploy from repo root
3. No build process required

All assets are local and portable. Folder works immediately on any server.
