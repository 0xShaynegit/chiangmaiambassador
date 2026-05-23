# Phase 1 QA & Testing Checklist

**Target Completion:** May 29, 2026
**Estimated Time:** 3.5 hours

---

## 1. Link Validation (1 hour)

### Internal Links
- [ ] No broken links to .html files
- [ ] All relative paths resolve correctly
- [ ] Navigation links work in root and subfolders
- [ ] Breadcrumb links functional
- [ ] Cross-folder links use correct relative paths

### External Links
- [ ] All external links use https://
- [ ] External links open in new tab (target="_blank")
- [ ] No dead links to external sites

### Redirect Testing
- [ ] Test 5+ old URLs from _redirects file
- [ ] Verify 301 redirects work correctly
- [ ] Confirm new URLs load properly after redirect

---

## 2. Image & Media Audit (1 hour)

### Image Alt Text
- [ ] All images have descriptive alt text
- [ ] Alt text is concise (max 125 chars)
- [ ] Alt text describes image content, not just "image"
- [ ] Decorative images have empty alt (alt="")

### Image Quality
- [ ] All images are WebP format
- [ ] Images have width/height attributes (CLS prevention)
- [ ] Images under 200KB budget per page (total)
- [ ] Image dimensions appropriate for layout

### Image Placement
- [ ] Images render correctly in root pages
- [ ] Images render correctly in subfolder pages
- [ ] No broken image references
- [ ] Image paths use ../images/ in subfolders

---

## 3. Spelling & Grammar (0.75 hours)

### Content Review
- [ ] No obvious typos in titles
- [ ] No obvious typos in meta descriptions
- [ ] No grammatical errors in page content
- [ ] Consistent terminology throughout

### Format Consistency
- [ ] Title format consistent (Title Case or Sentence case)
- [ ] Meta descriptions follow formula
- [ ] No em dashes (—) or en dashes (–)
- [ ] Proper spacing around punctuation

---

## 4. Mobile Responsive Testing (0.75 hours)

### Viewport Testing
- [ ] Test at 640px (mobile)
- [ ] Test at 768px (tablet)
- [ ] Test at 1024px (tablet landscape)
- [ ] Test at 1440px (desktop)

### Responsive Checklist
- [ ] Navigation works on mobile
- [ ] Text is readable at all sizes
- [ ] Images scale properly
- [ ] No horizontal scrolling
- [ ] Touch targets are adequate (48px minimum)
- [ ] Spacing/padding looks good at all sizes

### Browser Testing (if possible)
- [ ] Chrome
- [ ] Firefox
- [ ] Safari (if available)
- [ ] Edge (if available)

---

## 5. Technical Validation (0.25 hours)

### Meta Tags
- [ ] Title tags present and optimized (all pages)
- [ ] Meta descriptions present and optimized (all pages)
- [ ] Canonical tags present (all pages)
- [ ] OG tags present (all pages)
- [ ] Robots meta tag present

### Favicon & Assets
- [ ] Favicon loads without 404
- [ ] Favicon appears in browser tab
- [ ] All CSS files load (no 404s)
- [ ] All JS files load (no 404s)
- [ ] All fonts load (no 404s)

### Structured Data
- [ ] JSON-LD schema present (if applicable)
- [ ] Schema markup is valid format
- [ ] No console errors in browser DevTools

---

## 6. Performance Check (0.25 hours)

### Core Web Vitals
- [ ] Largest Contentful Paint (LCP) reasonable
- [ ] Cumulative Layout Shift (CLS) minimal
- [ ] First Input Delay (FID) acceptable

### Page Load
- [ ] Homepage loads in < 3 seconds
- [ ] Subpages load in < 2 seconds
- [ ] Assets cached properly

---

## Page Sample Testing Plan

### Root Pages (Test 3 of 10)
- [ ] index.html (homepage)
- [ ] best-chiang-mai.html
- [ ] getting-social-in-chiang-mai.html

### Food Pages (Test 2 of 10)
- [ ] food/auf-der-au-best-buffet-chiang-mai.html
- [ ] food/food-delivery-services.html

### Guides Pages (Test 3 of 13)
- [ ] guides/chiang-mai-driving.html
- [ ] guides/motorcycle-rentals.html
- [ ] guides/work-permit-medical-certificate.html

### Lifestyle Pages (Test 2 of 16)
- [ ] lifestyle/chiang-mai-arrival.html
- [ ] lifestyle/vientiane-visa-run.html

### Pages Folder (Test all 4)
- [ ] pages/about.html
- [ ] pages/cost-of-living.html
- [ ] pages/neighbourhoods.html
- [ ] pages/visas.html

---

## Testing Log

### Link Validation Results
- Tested: _____ pages
- Broken links found: _____
- Fixed: _____
- Status: [ ] PASS [ ] NEEDS WORK

### Image Audit Results
- Total images checked: _____
- Missing alt text: _____
- Fixed: _____
- Status: [ ] PASS [ ] NEEDS WORK

### Spelling & Grammar
- Issues found: _____
- Fixed: _____
- Status: [ ] PASS [ ] NEEDS WORK

### Mobile Responsive
- Viewport tests completed: _____
- Issues found: _____
- Status: [ ] PASS [ ] NEEDS WORK

### Technical Validation
- Meta tags: [ ] OK
- Favicon: [ ] OK
- Assets: [ ] OK
- Schema: [ ] OK

---

## Sign-Off

- [ ] All QA tests completed
- [ ] Critical issues resolved
- [ ] Ready for deployment
- [ ] Backup created before any fixes

**QA Completed:** _____________
**Issues Found & Fixed:** _____
**Final Status:** READY / NEEDS WORK
