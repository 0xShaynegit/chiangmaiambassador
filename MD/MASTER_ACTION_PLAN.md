# CMA Master Action Plan - SEO & Authority Overhaul
**May 23, 2026**

## OVERVIEW

Comprehensive audit of Chiang Mai Ambassador has identified clear opportunities to strengthen SEO, build authority, and become the most informative Chiang Mai resource for expats and travellers.

**Two detailed reports available:**
- `SEO_AUDIT_REPORT_2026.md` — Technical SEO, on-page optimization, pre-deployment checklist
- `CONTENT_AUTHORITY_AUDIT.md` — E-E-A-T signals, local knowledge gaps, voice assessment

**This document:** Consolidated action plan with priorities, timelines, and team assignments.

---

## CRITICAL PATH TO LAUNCH (Do Before Deployment)

### Week 1: Technical SEO Foundation (8–10 hours)

**Must complete before going live.**

| Task | Effort | Owner | Due |
|------|--------|-------|-----|
| Add canonical tags to 54 pages | 2 hrs | Dev | May 24 |
| Create robots.txt | 0.5 hrs | Dev | May 24 |
| Generate sitemap.xml | 0.5 hrs | Dev | May 24 |
| Add _redirects file (43 redirects) | 1 hr | Dev | May 24 |
| Test redirects locally (no 404s) | 1 hr | QA | May 25 |
| Verify all relative paths working | 1 hr | QA | May 25 |
| Run HTML validation (W3C) | 0.5 hrs | QA | May 25 |
| Test mobile-friendly | 0.5 hrs | QA | May 25 |
| Test on PageSpeed Insights | 0.5 hrs | QA | May 25 |
| **Subtotal** | **8 hours** | | **May 25** |

**Blocker:** Cannot deploy without these tasks complete.

---

### Week 1-2: On-Page SEO Optimization (8–10 hours)

**Complete before deployment. Impacts CTR.**

| Task | Effort | Owner | Pages | Due |
|------|--------|-------|-------|-----|
| Optimize title tags (keyword-focused, 50-60 chars) | 3 hrs | Content | 54 | May 27 |
| Optimize meta descriptions (150-160 chars, compelling) | 3 hrs | Content | 54 | May 27 |
| Add OG tags (og:title, og:description, og:image) | 2 hrs | Dev | 54 | May 28 |
| **Subtotal** | **8 hours** | | | **May 28** |

**Impact:** Estimated +15% CTR improvement.

---

### Week 2: Pre-Deployment QA (3–4 hours)

| Task | Effort | Owner | Due |
|------|--------|-------|-----|
| Link checker (no broken internal/external links) | 1 hr | QA | May 29 |
| Image alt text audit (all images have descriptive alt) | 1 hr | QA | May 29 |
| Spelling & grammar check (tools + human) | 1 hr | Content | May 29 |
| Final mobile test (640px, 1024px viewport) | 0.5 hrs | QA | May 29 |
| **Subtotal** | **3.5 hours** | | **May 29** |

---

### Timeline: Ready to Deploy by May 30

```
May 24 (Fri): Technical SEO complete
May 25 (Fri): All QA tests pass
May 27-28 (Mon-Tue): On-page optimization complete
May 29 (Wed): Final QA + spelling check
May 30 (Thu): Push to GitHub, deploy to Cloudflare Pages
```

---

## POST-DEPLOYMENT PRIORITY WORK (Do After Launch)

### Phase 1: Immediate Post-Deployment (First 2 weeks)

**Goals:** Build trust signals, establish credibility, monitor indexation

| Task | Effort | Owner | Priority | Due |
|------|--------|-------|----------|-----|
| Submit sitemap to Google Search Console | 0.5 hrs | SEO | HIGH | June 1 |
| Monitor GSC for crawl errors (should be 0) | 0.5 hrs/day | SEO | HIGH | Ongoing |
| Monitor indexation rate (track daily) | 0.5 hrs/day | SEO | HIGH | Ongoing |
| Add author byline to every page | 2 hrs | Content | HIGH | June 3 |
| Add "Last Updated: May 2026" to every page | 1 hr | Dev | HIGH | June 3 |
| Create `/about/` page with author credentials | 2 hrs | Content | HIGH | June 5 |
| Create `/contact/` page | 1 hr | Dev | MEDIUM | June 5 |
| Create `/privacy/` and `/terms/` pages | 1 hr | Dev | MEDIUM | June 5 |
| **Subtotal** | **~10 hours** | | | **June 5** |

**Impact:** Complete E-E-A-T foundation + establish trust signals.

---

### Phase 2: Voice & Authenticity Injection (Weeks 3-4, ~20 hours)

**Goals:** Make pages feel local, authentic, and grounded

| Task | Effort | Pages | Example | Priority | Due |
|------|--------|-------|---------|----------|-----|
| Add "Guru Tip" (unique local insight) to every page | 4 hrs | 54 | "The Yunnan market closes by noon on weekends—go early" | HIGH | June 10 |
| Add first-person anecdotes to major pages | 6 hrs | 10 | "I learned this when..." storytelling | HIGH | June 12 |
| Add source citations (Thai Immigration, gov sites) | 4 hrs | 20 | Link to official guides, visa office | MEDIUM | June 14 |
| Strengthen disclaimers where needed | 2 hrs | 10 | "I'm not a lawyer/accountant/doctor..." | MEDIUM | June 14 |
| Inject contrarian takes (honest assessment) | 4 hrs | 15 | "Most guides say X, but actually..." | MEDIUM | June 17 |
| **Subtotal** | **~20 hours** | | | | **June 17** |

**Impact:** Pages feel local, trustworthy, and written by someone who actually lives here.

---

### Phase 3: Content Gap Filling (Weeks 5-8, ~41 hours)

**Goals:** Dominate high-opportunity keywords and topics**

**Tier 1: Must-Create Hub Pages**

| Page | Focus | Est. Length | Effort | Keyword Value | Priority | Due |
|------|-------|------------|--------|---------------|----------|-----|
| Complete Guide to Thai Visas | ED, DTV, Elite, Retirement, comparison table | 2500+ | 6 hrs | VERY HIGH | HIGH | June 21 |
| Chiang Mai Accommodation Guide | Neighborhoods, rental tips, pricing | 3000+ | 8 hrs | VERY HIGH | HIGH | June 28 |
| Surviving Smoky Season | AQI, masks, indoor activities, honest advice | 1500+ | 4 hrs | HIGH | MEDIUM | June 25 |
| Thai Language Learning Hub | Schools, resources, integration | 2000+ | 6 hrs | HIGH | MEDIUM | July 2 |
| Banks & Money for Expats | Accounts, transfers, taxes, disclaimers | 2000+ | 5 hrs | HIGH | MEDIUM | July 5 |

**Tier 2: Secondary Pages (Choose 3-4)**

| Page | Effort | Priority | Target Month |
|------|--------|----------|---------------|
| Healthcare in Chiang Mai | 6 hrs | MEDIUM | July |
| Co-working Spaces & Remote Work | 5 hrs | MEDIUM | July |
| Transportation Guide (Songthaew, Tuk-Tuk, Motorcycle) | 4 hrs | MEDIUM | July |
| Expat Social Scene (honest breakdown) | 4 hrs | MEDIUM | July |
| Hiking Trails (with seasonal awareness) | 4 hrs | LOW | August |

**Subtotal:** 41 hours over 6 weeks

**Impact:** 
- Capture 5-10K+ monthly searches (visa guides alone)
- Establish authority across new topic clusters
- 3-5x organic traffic increase (12-month projection)

---

### Phase 4: Internal Linking & Topical Authority (Weeks 7-9, ~12 hours)

**Goals:** Connect pages for maximum SEO impact

| Task | Effort | Details | Priority | Due |
|------|--------|---------|----------|-----|
| Map topical clusters | 2 hrs | Visas, Transport, Living, Food, Culture | HIGH | July 10 |
| Add related posts to every page | 8 hrs | 3–5 contextual links per page (54 pages) | HIGH | July 17 |
| Update site navigation | 2 hrs | Sidebar/footer hub links | MEDIUM | July 17 |
| **Subtotal** | **12 hours** | | | **July 17** |

**Impact:**
- Pages reinforce each other's authority
- Users discover related content
- Internal link equity concentrated on important pages

---

## RESOURCE ALLOCATION

### Team Structure (Assuming Solo or Small Team)

If **solo (you doing everything):**
- **Weeks 1-2 (May 24-June 5):** Technical SEO + on-page + credibility signals (20 hours)
- **Weeks 3-4 (June 5-18):** Voice & authenticity (20 hours)
- **Weeks 5-8 (June 18-July 17):** Content gaps (41 hours)
- **Weeks 7-9 (overlapping, July 1-17):** Internal linking (12 hours)
- **Total:** ~93 hours over 8 weeks (~12 hours/week)

If **small team (2-3 people):**
- **Dev (2-3 hrs/week):** Technical SEO, canonical tags, redirects, OG tags, _redirects
- **Content (5-6 hrs/week):** Titles, descriptions, author bylines, new content, voice injection
- **QA (1-2 hrs/week):** Testing, validation, GSC monitoring
- **Total:** Can complete in 6-7 weeks

---

## SUCCESS METRICS & MONITORING

### Week 1 Post-Deployment (Daily)
- [ ] GSC: 0 crawl errors
- [ ] GSC: 0 redirect errors
- [ ] GSC: All 54 pages indexed or pending
- [ ] GA4: No 404s on traffic

### Week 2-4 Post-Deployment (Weekly)
- [ ] GSC impressions trending upward
- [ ] No noticeable drop in rankings (redirects working)
- [ ] CTR improving (new titles/descriptions)
- [ ] Average time on page stable/increasing

### Month 2-3 Post-Deployment (Monthly)
- [ ] Organic traffic +20-30% (baseline recovery post-redirect)
- [ ] Impressions +30% (new content indexing)
- [ ] Target keyword rankings improving
- [ ] Internal click-through +25% (related links working)
- [ ] Core Web Vitals maintained (80+)

### Month 3-6 Post-Deployment (Ongoing)
- [ ] Organic traffic 2-3x baseline (content gaps filled)
- [ ] Visa-related keywords ranking top 10
- [ ] Accommodation guide becoming traffic driver
- [ ] Backlinks increasing (authority signals)
- [ ] Testimonials/feedback positive

---

## RISK MITIGATION

### Before Deployment
- **Risk:** Broken redirects → 404s → lost traffic
- **Mitigation:** Test all 43 redirects locally, verify no 404s, monitor GSC day 1

- **Risk:** Canonical tag errors → duplicate content confusion
- **Mitigation:** Validate all canonicals point to correct URLs, self-referencing

- **Risk:** New site structure breaks relative paths (CSS, fonts, images)
- **Mitigation:** Test on mobile, desktop, different browsers

### After Deployment
- **Risk:** Redirect performance (how fast Cloudflare serves redirects)
- **Mitigation:** Monitor Core Web Vitals, check redirect latency (should be <100ms)

- **Risk:** Content gaps aren't what users actually search for
- **Mitigation:** Use GSC "Search Results" tab to see what queries people use, adjust content

- **Risk:** New content doesn't rank quickly (takes 4-8 weeks)
- **Mitigation:** Internal links to new pages, wait 30 days before judging rankings

---

## BUDGET & TIMELINE SUMMARY

| Phase | Start | End | Effort | Cost (if outsourced) |
|-------|-------|-----|--------|----------------------|
| **Pre-Deployment (Technical + On-Page)** | May 24 | May 29 | 16 hrs | $800–$1,200 |
| **Post-Deployment 1 (Trust Signals)** | June 1 | June 5 | 10 hrs | $500–$800 |
| **Post-Deployment 2 (Voice)** | June 5 | June 17 | 20 hrs | $1,000–$1,500 |
| **Post-Deployment 3 (Content Gaps)** | June 18 | July 17 | 41 hrs | $2,000–$3,000 |
| **Post-Deployment 4 (Internal Linking)** | July 1 | July 17 | 12 hrs | $600–$900 |
| **Total** | May 24 | July 17 | **99 hours** | **$4,900–$7,400** |

---

## QUICK START: THIS WEEK

**If you do nothing else this week, do these 5 things:**

1. ✅ Add canonical tags to all 54 pages (2 hrs)
2. ✅ Create robots.txt (0.5 hrs)
3. ✅ Generate sitemap.xml (0.5 hrs)
4. ✅ Optimize 10 key title tags as proof of concept (1 hr)
5. ✅ Read both audit reports and share with team (1 hr)

**Time investment: ~5 hours**
**Impact: 80% of the way to being deployment-ready**

---

## FINAL RECOMMENDATION

**Launch the restructured site by May 30** with all critical SEO fixes in place. Then run the 8-week content and authority program in parallel with normal operations.

**By August 30, CMA will be:**
- ✅ Technically sound (SEO best practices)
- ✅ Trust-worthy (author, dates, contact)
- ✅ Authoritative (complete guides, no gaps)
- ✅ Authentic (Guru tips, first-person stories)
- ✅ Discoverable (3-5x traffic potential)

**The result: The go-to resource for anyone moving to or living in Chiang Mai.**

---

**Questions? Check the detailed reports:**
- Technical issues → `SEO_AUDIT_REPORT_2026.md`
- Content strategy → `CONTENT_AUTHORITY_AUDIT.md`
- Redirects & deployment → `RESTRUCTURE_NOTES.md`
