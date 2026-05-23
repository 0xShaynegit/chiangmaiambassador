# Open Graph Tags Optimization - 54 Pages

**Formula Applied:**
- og:title: Use page title (already optimized)
- og:description: Use meta description (already optimized)
- og:type: "article" for guides/lifestyle/food, "website" for root/pages
- og:url: Full canonical URL
- og:site_name: "Chiang Mai Ambassador"
- og:image: Single default image (will add specific image URLs if available)

---

## OG Tags Template

```html
<meta property="og:title" content="[Page Title]">
<meta property="og:description" content="[Meta Description]">
<meta property="og:type" content="article|website">
<meta property="og:url" content="[Full Canonical URL]">
<meta property="og:site_name" content="Chiang Mai Ambassador">
<meta property="og:image" content="https://chiangmaiambassador.com/images/og-image.webp">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

---

## URL Mapping by Page Type

### Root Pages (base domain)
- index.html → https://chiangmaiambassador.com/
- best-chiang-mai.html → https://chiangmaiambassador.com/best-chiang-mai/
- cheapest-border-run-chiang-mai.html → https://chiangmaiambassador.com/cheapest-border-run-chiang-mai/
- getting-social-in-chiang-mai.html → https://chiangmaiambassador.com/getting-social-in-chiang-mai/
- khun-joe-school.html → https://chiangmaiambassador.com/khun-joe-school/
- motorbike-registration-chiang-mai.html → https://chiangmaiambassador.com/motorbike-registration-chiang-mai/
- thai-eating-etiquette.html → https://chiangmaiambassador.com/thai-eating-etiquette/
- understanding-thai-culture.html → https://chiangmaiambassador.com/understanding-thai-culture/
- womens-prison-massage.html → https://chiangmaiambassador.com/womens-prison-massage/
- yunnan-farmers-market.html → https://chiangmaiambassador.com/yunnan-farmers-market/

### Food Folder (10 pages)
- food/auf-der-au-best-buffet-chiang-mai.html → https://chiangmaiambassador.com/food/auf-der-au-best-buffet-chiang-mai/

### Guides Folder (13 pages)
- guides/chiang-mai-driving.html → https://chiangmaiambassador.com/guides/chiang-mai-driving/

### Lifestyle Folder (16 pages)
- lifestyle/chiang-mai-arrival.html → https://chiangmaiambassador.com/lifestyle/chiang-mai-arrival/

### Pages Folder (4 pages)
- pages/about.html → https://chiangmaiambassador.com/about/
- pages/cost-of-living.html → https://chiangmaiambassador.com/cost-of-living/
- pages/neighbourhoods.html → https://chiangmaiambassador.com/neighbourhoods/
- pages/visas.html → https://chiangmaiambassador.com/visas/

---

## Implementation Notes

- OG image will use default: `https://chiangmaiambassador.com/images/og-image.webp`
- Image dimensions: 1200x630px (standard for social share)
- All URLs include trailing slash (canonical format)
- og:type: "article" for content pages, "website" for info pages
- Placement: After canonical tag in `<head>`

---

## Status: Ready for Batch Application

Total pages to optimize: 54
Folders: root (10) + food (10) + guides (13) + lifestyle (16) + pages (4)
Deployment: After Python script execution
