# Rinquest marketing site (static, GitHub Pages ready)

Plain HTML/CSS. No framework, no build step on the host, no JavaScript needed to read any page
(search engines and AI crawlers see full content). 17 indexable pages plus 404, sitemap.xml, robots.txt, llms.txt.

## Put it on GitHub Pages
1. Create a new GitHub repo (e.g. `rinquest-site`) and upload everything in this folder.
2. Repo Settings > Pages > Source: "Deploy from a branch" > branch `main`, folder `/docs`.
3. Your preview appears at `https://<username>.github.io/<repo>/`.
   - Because that is a project URL, open build.py, set `BASE_PATH = "/<repo>"`, run `python3 build.py`, commit the updated /docs.
4. Custom domain later: Settings > Pages > Custom domain. Keep `BASE_PATH = ""`. Set `SITE_URL` to the final domain.

## Editing
Copy lives in build.py (search "CONFIRM"). Change it, run `python3 build.py`, commit /docs.
Styles: src/style.css (copied to docs/assets on build).

## Before this replaces the live site (CONFIRM list)
- APP_URL: sign-up, search, login and contact pages are the live app. If this site takes over rinquest.com,
  the app must move to another address (e.g. app.rinquest.com) and APP_URL updated. Ask your developer.
- PARENT_ROLE: parent sign-up currently uses role=player. Change once the app supports a parent role.
- FOUNDING_UNTIL: set a real deadline or leave empty. The old 31 Aug 2026 date has passed.
- Club/Premium boundary: site shows 2-19 / 20+ (the live site says 2-20, 20+ and "30+" in different places).
- Safeguarding and Verification pages are drafts (noindex) until SAFEGUARDING_APPROVED / VERIFICATION_APPROVED are True.
  Have a solicitor or data-protection adviser review anything about children.
- About page: add founder names and photos.
- Guides are short starter drafts. Replace with the existing guide text.
- Logo: docs/assets/logo.svg is a placeholder ring mark. Drop in the real logo.
- Testimonials: get permission on file for the three quotes used.
- Search Console: add the property, submit sitemap.xml, use URL Inspection on the home page.
