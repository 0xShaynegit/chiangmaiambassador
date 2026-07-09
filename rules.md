# PROJECT RULES chiangmaiambassador

Read before touching anything. These rules do not change between sessions.

## Project Identity
- Project Name: Chiang Mai Ambassador
- What it is: Content and SEO site about Chiang Mai (guides, blog, SEO pages).
- Owner: Shayne
- Local folder: C:\ZZZWebsites\chiangmaiambassador

## Stack and Deploy
- Pure static HTML, CSS, JS. _headers and _redirects present for Cloudflare.
- Deploy: Cloudflare Pages only. Never Vercel.

## Hard Rules
- TEMPLATE FIRST is the overriding principle (full detail in CLAUDE.md in this folder). Every page is built FROM a template: single pages, batch SEO pages, blog posts, new sections. If you do not know which template to use, ASK. Never build HTML from scratch.
- blog-template.html is the blog template. blog-backlog.md holds the content queue.
- No dev servers unless explicitly requested.
- Update handover.md at the end of every session. A separate handover-khun-joe-school.md exists for that sub-project; keep it separate.
