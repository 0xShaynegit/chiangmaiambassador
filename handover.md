# CMA Handover: Hamburger Menu Restoration

**Date:** 16 June 2026
**Status:** Hamburger menu REMOVED - Desktop dropdowns only
**Next Step:** Restore mobile hamburger menu when issues are resolved

---

## What Was Removed

On 16 June 2026, the entire hamburger mobile menu system was removed due to non-functioning click handlers. This included:

1. Hamburger button element from HTML templates
2. Mobile menu open/close handlers
3. Mobile search bar (was appearing as duplicate at bottom of menu)
4. Auto-focus prevention on search input
5. Menu close triggers (click outside, Escape key)

**Files affected:**
- `index.html` - hamburger button removed
- `blog-template.html` - hamburger button removed  
- `pages/page-template.html` - hamburger button removed
- `js/main.js` - 150+ lines of mobile menu code removed

**Desktop navigation still works:** Dropdown menus function on desktop/tablet (>640px).

---

## To Restore: Step-by-Step

### 1. Add Hamburger Button to HTML Templates

Add this button **inside `<nav class="nav-wrapper">` AFTER the closing `</div>` of nav-links, BEFORE the closing `</nav>`:**

```html
<button class="nav-hamburger" id="nav-hamburger" aria-label="Toggle menu">
    <span></span>
    <span></span>
    <span></span>
</button>
```

**Add to all three files:**
- `index.html` (around line 327, before `</nav>`)
- `blog-template.html` (around line 591, before `</nav>`)
- `pages/page-template.html` (around line 258, before `</nav>`)

---

### 2. Restore Mobile Menu JavaScript

Replace the `initNavigation()` function in `js/main.js` with the complete version from the git history (commit 7cc881a or earlier).

**Key features:**
- Hamburger click toggles mobile menu open/close
- Mobile search bar created dynamically at top of menu
- Guard clause prevents duplicate search bars
- Menu closes on: link click, outside click, Escape key
- NO auto-focus on search input (prevents keyboard opening)
- Desktop dropdowns still work on hover

---

## Key Features to Verify After Restoration

1. **Hamburger visible on mobile** - Toggle appears when screen < 640px
2. **Menu opens/closes** - Click hamburger to toggle mobile menu
3. **Search bar at top** - Input field appears inside menu (no auto-focus)
4. **No duplicate search bars** - Only ONE search bar at top of menu
5. **Menu closes on**:
   - Clicking a link
   - Clicking outside the menu
   - Pressing Escape key
6. **No keyboard auto-opening** - Search input does NOT auto-focus
7. **Desktop dropdowns still work** - Hover to expand on desktop

---

## Troubleshooting

**Issue:** Hamburger not showing
- Check window size (< 640px = mobile view)
- Verify button added to all three HTML files
- Check CSS for `.nav-hamburger` display rules

**Issue:** Menu doesn't open when clicked
- Check browser console for JavaScript errors
- Verify `getElementById('nav-hamburger')` finds the button (F12 Inspector)
- Confirm `initNavigation()` is called in DOMContentLoaded

**Issue:** Duplicate search bar appearing
- Guard clause prevents duplicates: `if (!navLinks.querySelector('.mobile-search-bar'))`
- If still appearing, check for hardcoded search bars in HTML

**Issue:** Keyboard opens when menu opens
- The `setTimeout(() => searchInput.focus(), 80)` line must be REMOVED from openMenu()
- Do NOT add it back - it causes unwanted keyboard opening

---

## Git Reference

Previous working versions:
- **Commit 7cc881a:** Mobile menu with duplicate search bar fix
- **Commit f7d7cda:** Mobile menu with hamburger button added
- **Commit c4b3eee:** CURRENT - All mobile menu code removed

---

**Last Updated:** 16 June 2026
**By:** Claude
**Status:** REMOVED - Ready for restoration when debugging complete
