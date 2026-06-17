# CMA Links & Cards - Implementation Checklist

**Status:** CSS & JS updated ✅ Ready for testing & rollout

---

## ✅ Completed (June 4, 2026)

### CSS Updates
- [x] Added link color variables to `css/tokens.css`
  - `--link-gold: #EAB308`
  - `--hover-green: #10B981`
  - `--card-dark-bg: #1a1a1a`
  - `--card-dark-hover: #222222`
  - `--text-light-grey: #e0e0e0`
  - `--text-white: #ffffff`

- [x] Updated global link rules in `css/base.css`
  - Standard link color: gold
  - Hover color: emerald green
  - Explicit rules for `.dark-section a` and `footer a`

- [x] Added `.dark-card` component to `css/components.css`
  - Card styling (background, padding, border-radius)
  - Typography rules (h3, p, .card-link)
  - Hover states (lift, background change, color shift)
  - Mobile responsive (smaller padding on small screens)

### JavaScript Updates
- [x] Added `initDarkCards()` function to `js/main.js`
  - Makes entire card clickable
  - Supports `data-url` attribute
  - Keyboard accessible (Enter key)
  - Runs automatically on page load

---

## 📋 Testing Tasks

### Visual Verification
- [ ] Homepage loads without CSS errors
- [ ] Links display in gold (#EAB308)
- [ ] Links turn green on hover (#10B981)
- [ ] No existing styles broken
- [ ] Navigation still looks correct
- [ ] Footer links match body links

### Card Testing (Create test card first)
- [ ] Card background is dark (#1a1a1a)
- [ ] Card text is readable
- [ ] Card link is gold, bold
- [ ] Card lifts (translateY -5px) on hover
- [ ] Card background darkens on hover
- [ ] Card link turns green on hover
- [ ] Card is clickable (navigates to URL)
- [ ] Card is keyboard accessible (Tab → Enter)

### Responsive Testing
- [ ] Mobile (320px): Card padding looks good
- [ ] Tablet (768px): Card spacing balanced
- [ ] Desktop (1024px+): Card styling crisp
- [ ] No horizontal scroll at any breakpoint

### Browser Testing
- [ ] Chrome/Edge (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Android

---

## 🚀 Phase 2: Rollout

### Week 1: Add Test Card to Homepage
- [ ] Create `.dark-section` below hero (optional)
- [ ] Add 1 test `.dark-card` with visa guide link
- [ ] Verify click behavior
- [ ] Verify hover states
- [ ] Get visual approval

### Week 2: Expand to Guide Pages
- [ ] Add "Related Guides" section to 3-5 guides
- [ ] Use `.dark-card` for related posts
- [ ] Test navigation flow
- [ ] Verify cards improve engagement

### Week 3: Full Site Rollout
- [ ] Add dark card sections to all major guides
- [ ] Update related posts sections
- [ ] Review for consistency
- [ ] Monitor engagement metrics

### Week 4: Monitor & Optimize
- [ ] Check Google Analytics for clicks
- [ ] Review user behavior
- [ ] Gather feedback
- [ ] Make refinements if needed

---

## 🎨 Quick Reference: What Changed

### Before (Scattered)
```
- Links hardcoded colors in multiple places
- No `.dark-card` component
- Cards not clickable (only link text clickable)
- Hover colors inconsistent
```

### After (Unified)
```
✅ All link colors = CSS variables
✅ `.dark-card` component ready to use
✅ Entire card clickable
✅ Consistent hover states (gold → green)
✅ Keyboard accessible
✅ Responsive by default
```

---

## 📝 Test Card HTML (Copy & Paste)

Paste this into any page to test the `.dark-card` component:

```html
<section class="dark-section" style="background: #111; padding: 50px;">
    <h2 style="color: white; margin-bottom: 2rem;">Related Guides</h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; max-width: 1280px;">
        
        <div class="dark-card" data-url="/visa/retirement-visa.html">
            <h3>Retirement Visa (O-A)</h3>
            <p>Complete guide to the Thai retirement visa including age requirements, financial qualifications, and step-by-step process.</p>
            <span class="card-link">Read Guide →</span>
        </div>

        <div class="dark-card" data-url="/guides/90-day-reporting-tm30-chiang-mai.html">
            <h3>90-Day Reporting & TM30</h3>
            <p>Understand Thailand's mandatory 90-day reporting and your landlord's TM30 obligations. Where, when, what to bring.</p>
            <span class="card-link">Full Guide →</span>
        </div>

        <div class="dark-card" data-url="/visa/dtv-visa.html">
            <h3>DTV Visa</h3>
            <p>The new Digital Traveler Visa for remote workers. Eligibility, requirements, and comparison with other digital nomad options.</p>
            <span class="card-link">Learn More →</span>
        </div>

    </div>
</section>
```

---

## 🔧 How to Modify Colors (Easy!)

### Change Link Color
1. Open `css/tokens.css`
2. Find: `--link-gold: #EAB308;`
3. Change to your color: `--link-gold: #FFD700;`
4. Save. All links update automatically.

### Change Hover Color
1. Open `css/tokens.css`
2. Find: `--hover-green: #10B981;`
3. Change to your color: `--hover-green: #9A7008;`
4. Save. All hovers update automatically.

### Change Card Background
1. Open `css/tokens.css`
2. Find: `--card-dark-bg: #1a1a1a;`
3. Change to your color: `--card-dark-bg: #0F172A;`
4. Save. All cards update automatically.

---

## 📊 Files Modified

| File | Changes | Lines |
|------|---------|-------|
| `css/tokens.css` | Added 6 new variables | +18 |
| `css/base.css` | Updated link rules, added dark section rules | +22 |
| `css/components.css` | Added `.dark-card` component | +55 |
| `js/main.js` | Added `initDarkCards()` function | +30 |

**Total Changes:** ~125 lines of new/updated code  
**Breaking Changes:** None  
**Backwards Compatible:** Yes  

---

## ✨ Benefits

✅ **Consistency:** All links look & behave the same  
✅ **Maintainability:** Change colors in one place  
✅ **User Experience:** Larger click targets (entire card)  
✅ **Accessibility:** Keyboard navigation built-in  
✅ **Responsiveness:** Mobile-first design  
✅ **Performance:** No new dependencies, pure vanilla  
✅ **Flexibility:** Works with any content inside cards  

---

## 🚨 Troubleshooting

### Links still not gold?
- [ ] Clear browser cache (Ctrl+Shift+Delete)
- [ ] Check if page has `<link>` to `css/tokens.css` before `css/base.css`
- [ ] Verify `--link-gold: #EAB308` in tokens.css

### Cards not clickable?
- [ ] Check JavaScript console for errors (F12)
- [ ] Verify `js/main.js` is loaded
- [ ] Ensure card has `.dark-card` class
- [ ] Ensure link inside card has `href` or card has `data-url`

### Hover color not changing?
- [ ] Clear cache
- [ ] Check for conflicting CSS (search for `a:hover` in all files)
- [ ] Verify `--hover-green` is defined in tokens.css
- [ ] Check browser developer tools (Inspect element → Styles)

### Mobile cards look wrong?
- [ ] Check responsive breakpoint (@media max-width: 640px)
- [ ] Verify grid is wrapping correctly
- [ ] Check if overflow-x is hidden on body
- [ ] Test on actual mobile device (not just browser resize)

---

## 📞 Support

**For questions about:**
- Link colors → Check `css/tokens.css`
- Link behavior → Check `css/base.css`
- Card styling → Check `css/components.css`
- Card interactivity → Check `js/main.js`

**For full context:**
- See `md/LINKS_AND_CARDS_CONSISTENCY_AUDIT.md` (this audit)
- See `md/INITIAL_PROMPT.md` (full project brief)
- See `md/PRD.md` (product requirements)

---

## 🎯 Success Criteria

### Phase 1: Testing ✅
- [x] CSS variables added
- [x] Link rules updated
- [x] Dark card component added
- [x] JavaScript implemented
- [ ] Tested on 3+ browsers (TODO)
- [ ] Tested on mobile (TODO)

### Phase 2: Rollout (Next Week)
- [ ] Test card added to homepage
- [ ] Card clicks work correctly
- [ ] Hover states display correctly
- [ ] Keyboard navigation works
- [ ] Mobile version tested

### Phase 3: Expansion (Following Week)
- [ ] Dark cards added to 5+ guide pages
- [ ] Related posts sections updated
- [ ] Engagement metrics reviewed
- [ ] User feedback collected

---

**Status:** Ready for testing  
**Estimated Testing Time:** 2-3 hours  
**Estimated Rollout Time:** 1-2 days  
**Estimated Full Expansion:** 1-2 weeks  

Go test! 🚀
