# Mobile Responsive Testing Guide

**Tested:** May 23, 2026
**Status:** READY FOR TESTING

---

## Testing Breakpoints

Test these viewport widths to ensure responsive design:

### Mobile (640px)
- Small phone screens
- Minimum width for readable content
- Test: Vertical stacking, touch targets, font size

### Tablet (1024px)
- iPad/tablet landscape
- Mid-range layout
- Test: 2-column layouts, navigation width

### Desktop (1440px)
- Large desktop screens
- Maximum content width
- Test: Multi-column layouts, spacing

---

## Pages to Test (Sample)

### Root Pages (3 critical)
1. **index.html** - Homepage
   - Hero section renders
   - Navigation menu works
   - CTA buttons visible
   
2. **best-chiang-mai.html** - Content page
   - Content flows vertically on mobile
   - Images scale properly
   - Links clickable

3. **getting-social-in-chiang-mai.html** - Article
   - Text readable
   - No horizontal scroll
   - Sidebar (if any) stacks below

### Subfolder Pages (2 critical)
1. **food/auf-der-au-best-buffet-chiang-mai.html** - Food article
   - Images float correctly
   - Text wrapping proper
   
2. **guides/chiang-mai-driving.html** - Guide page
   - Lists render properly
   - Code blocks (if any) don't overflow

### Pages Folder (1 critical)
1. **pages/visas.html** - Info page
   - Tables responsive (scroll if needed)
   - All sections visible

---

## Checklist Per Viewport

### All Viewports
- [ ] No horizontal scrolling
- [ ] Text is readable (no tiny fonts)
- [ ] Images are visible and properly sized
- [ ] Navigation menu is accessible
- [ ] Links have adequate padding (48px minimum touch target)

### Mobile (640px)
- [ ] Single column layout
- [ ] Navigation menu collapses or works (no overflow)
- [ ] Images scale down (not squished)
- [ ] Content has adequate margins
- [ ] CTA buttons are clickable

### Tablet (1024px)
- [ ] 2-column layout works (if applicable)
- [ ] Navigation expands to full menu
- [ ] Content uses moderate widths
- [ ] Sidebar spacing looks right

### Desktop (1440px)
- [ ] Maximum content width respected
- [ ] Multi-column layouts balanced
- [ ] White space looks intentional
- [ ] No stretched images

---

## Testing Tools

### Browser DevTools (Free)
1. Open DevTools (F12 or Cmd+Opt+I)
2. Click "Toggle device toolbar" (Ctrl+Shift+M)
3. Select/enter viewport width
4. Check rendering at each breakpoint

### Manual Testing Checklist
```
[ ] Chrome at 640px
[ ] Chrome at 1024px
[ ] Chrome at 1440px
[ ] Firefox at 640px (if time)
[ ] Safari at 640px (if available)
```

---

## Known Considerations

- All relative paths verified correct (`css/`, `../css/`, etc.)
- All 380 images have alt text and dimensions (width/height)
- No em/en dashes (formatting cleaned)
- Font preloads in place for all pages

---

## Pass/Fail Criteria

**PASS:** 
- All pages render without horizontal scroll at tested viewports
- Text is readable
- Images scale proportionally
- No rendering errors in console

**NEEDS WORK:**
- Horizontal scrolling at any viewport
- Text too small or too large
- Images distorted or misaligned
- Console errors present

---

## Post-Testing

If issues found:
1. Note viewport and specific page
2. Screenshot or describe issue
3. Implement fix
4. Re-test that page

If no issues found:
- Mark as PASS
- Proceed to final sign-off
