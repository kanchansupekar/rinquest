#!/usr/bin/env python3
"""
Rinquest marketing site generator.

Run:  python3 build.py
Output: ./docs  (plain HTML/CSS, no framework, no build step needed on the host)

Edit the CONFIG block and the page copy below, then re-run. Search this file for
"CONFIRM" to find every claim that needs a product / legal decision before launch.
"""
import json, os, shutil, html, datetime

# ─────────────────────────── CONFIG ───────────────────────────
SITE_URL   = "https://rinquest.com"   # canonical public domain of the marketing site (pick ONE of www / non-www)
APP_URL    = "https://rinquest.com"   # where the live app (sign-up, search, login, contact) lives. If the marketing
                                      # site takes over rinquest.com, move the app to e.g. https://app.rinquest.com
BASE_PATH  = ""                       # "" for a custom domain or user site; "/repo-name" for a GitHub project site
FOUNDING_UNTIL = ""                   # CONFIRM: e.g. "31 December 2026". Leave empty to hide any deadline.
SAFEGUARDING_APPROVED = False         # CONFIRM: set True only once the safeguarding page is signed off
VERIFICATION_APPROVED = False         # CONFIRM: set True only once the verification page describes the real process
PARENT_ROLE = "player"                # CONFIRM: change to "parent" if/when the app supports role=parent
TODAY = datetime.date.today().isoformat()
OG_IMAGE = "https://rinquest.com/seo/rinquest_SEO_image.png"   # existing share image
OUT = "docs"

COMPANY = dict(
    name="Rinquest Ltd", number="17024691",
    street="Ranmore House, Hook Heath Road", town="Woking", postcode="GU22 0DT",
)
SOCIAL = {
    "LinkedIn": "https://www.linkedin.com/company/rinquest/",
    "Instagram": "https://www.instagram.com/rinquesthq/",
    "X": "https://x.com/rinquesthq",
    "Facebook": "https://www.facebook.com/profile.php?id=61590543427293",
}

def u(path):            # internal link
    return f"{BASE_PATH}{path}"
def app(path):          # link into the live app
    return f"{APP_URL}{path}"

SIGNUP_PLAYER = app("/auth/login?mode=signup&role=player")
SIGNUP_PARENT = app(f"/auth/login?mode=signup&role={PARENT_ROLE}")
SIGNUP_TEAM   = app("/auth/login?mode=signup&role=team")
LOGIN         = app("/auth/login?mode=login")

# ─────────────────────────── DATA ───────────────────────────
SPORTS = {
  "football": dict(
    name="Football",
    title="Grassroots football: find teams and players near you",
    desc="Find grassroots football teams and players on Rinquest. Build a profile, filter by level, location and availability, and connect directly with clubs, coaches and parents.",
    intro="Grassroots football runs on people turning up. Rinquest helps players find a team that fits their level and week, and helps managers fill gaps without endless group-chat messages.",
    roles=["Goalkeeper","Full-back","Centre-back","Defensive midfielder","Central midfielder","Attacking midfielder","Winger","Striker"],
    faq=[("Can I find youth football teams on Rinquest?","Yes. Parents can create and manage a profile for their child, and teams can look for players across age groups."),
         ("Do I need to be in a league to join?","No. Rinquest is built for grassroots football, from Sunday leagues to junior clubs. Teams say what level they play at, and players say what level they are.")]),
  "cricket": dict(
    name="Cricket",
    title="Grassroots cricket: find clubs and players near you",
    desc="Find grassroots cricket clubs and players on Rinquest. Show your role, level and availability, and connect directly with captains, coaches and parents.",
    intro="A cricket side needs the right mix, not just eleven names. Rinquest lets players show their role, level and availability, and lets captains search for exactly what the side is missing.",
    roles=["Opening batter","Middle-order batter","Wicketkeeper","Pace bowler","Spin bowler","All-rounder"],
    faq=[("Can I list more than one sport?","Sport is part of every profile, and parents of multi-sport children can manage more than one profile from a single account."),
         ("Can clubs run several teams?","Yes. Club plans let you manage several teams and coaches under one club profile.")]),
  "rugby": dict(
    name="Rugby",
    title="Grassroots rugby: find clubs and players near you",
    desc="Find grassroots rugby clubs and players on Rinquest. Share your position, level and availability, and connect directly with coaches and team managers.",
    intro="Rugby squads need specific positions filled and enough bodies on match day. Rinquest helps clubs search by what they need and helps players be found for the position they play.",
    roles=["Prop","Hooker","Lock","Flanker","Number 8","Scrum-half","Fly-half","Centre","Wing","Full-back"],
    faq=[("Can I join if I am returning to rugby?","Yes. Say your level and availability honestly on your profile, and teams looking for someone like you can get in touch."),
         ("Is there a fee for players?","No. Rinquest is free to join for players and teams.")]),
  "hockey": dict(
    name="Hockey",
    title="Grassroots hockey: find clubs and players near you",
    desc="Find grassroots hockey clubs and players on Rinquest. Show your position, level and availability, and connect directly with coaches and team managers.",
    intro="Hockey clubs often run several sides and juggle availability every week. Rinquest gives players a place to be found and gives clubs a way to search for who they need.",
    roles=["Goalkeeper","Defender","Midfielder","Forward"],
    faq=[("Can a club list several teams?","Yes. Club plans let a club manage every team from one profile."),
         ("Can I message a team directly?","Yes. Rinquest supports direct messaging between players, parents, coaches and teams.")]),
}

GUIDES = [
 dict(slug="find-the-right-players-faster", title="Find the right players faster",
      blurb="Smarter ways to identify players who match your team's level, availability and culture.",
      body="""
<p>Most squads do not need "a good player". They need a specific gap filled by someone who can actually make training and matches. Recruiting works faster when you start there.</p>
<h2>Write down the gap before you search</h2>
<p>Name the position, the age group and the level you play at. A clear brief stops you scrolling through profiles that were never going to fit.</p>
<h2>Check availability first</h2>
<p>A brilliant player who works Saturdays is not a signing. Filter by availability early and you will save yourself several conversations that go nowhere.</p>
<h2>Be honest about your level</h2>
<p>Tell players what your team really is: relaxed Sunday league, competitive, or somewhere in between. Players who read that and still get in touch are far more likely to stay.</p>
<h2>Message early and keep it short</h2>
<p>Introduce the team, say what you are looking for and suggest a short chat or a taster session. A quick, specific message gets replies.</p>
<h2>Keep a shortlist</h2>
<p>Save the profiles you like so that when someone drops out mid-season you already know who to call.</p>"""),
 dict(slug="what-coaches-value-beyond-ability", title="What coaches value beyond ability",
      blurb="Technical skill matters, but attitude, commitment, reliability and team fit often make the difference.",
      body="""
<p>At grassroots level, most players are within touching distance of each other on ability. What separates the ones who stay in a squad is usually everything else.</p>
<h2>Attitude</h2>
<p>Coaches remember who encourages teammates and who sulks after a substitution. Players who are easy to coach get more minutes and more chances.</p>
<h2>Commitment and reliability</h2>
<p>Turning up on time, telling the manager early when you cannot make it, and being there in week ten as well as week one all count for a lot.</p>
<h2>Team fit</h2>
<p>Some sides are intense, some are social, most are a blend. A player who fits the culture makes the whole squad better.</p>
<h2>How to show it on your profile</h2>
<ul>
<li>State your availability clearly and keep it up to date.</li>
<li>Describe what you want from a team in your own words.</li>
<li>Mention past teams and roles, such as captain, vice-captain or club volunteer.</li>
</ul>"""),
 dict(slug="how-players-get-noticed", title="How players get noticed",
      blurb="How a strong profile, clear availability and the right information help you stand out to teams recruiting.",
      body="""
<p>Teams searching for players scan quickly. A profile that answers their first questions in a few seconds gets contacted more often than one that leaves them guessing.</p>
<h2>Complete the basics</h2>
<p>Sport, position, level and location are the first things a coach checks. If they are missing, you will not appear in the right searches.</p>
<h2>Say when you can play</h2>
<p>Clear availability is one of the strongest signals you can give. It tells a manager you are ready to commit.</p>
<h2>Be honest about your level</h2>
<p>Overselling leads to a bad taster session. Honest profiles lead to better matches and longer stays.</p>
<h2>Add what makes you you</h2>
<p>A short bio about your experience, what you enjoy and what you are after gives coaches something to say in their first message.</p>
<h2>Reply quickly</h2>
<p>Teams often need a player soon. A fast reply, even a simple "thanks, can we talk this week?", keeps you in the running.</p>"""),
 dict(slug="player-poaching-vs-player-development", title="Player poaching vs player development",
      blurb="How grassroots football coaches in the UK can recruit the right players faster, and fairly.",
      body="""
<p>Every grassroots manager has lost a player to another team, and every manager has been tempted to make the same approach. The difference between poaching and recruiting is mostly about how you go about it.</p>
<h2>Recruiting openly</h2>
<p>Recruiting through a public profile, where players have chosen to be found and have said what they are looking for, is a different thing from approaching another club's players directly.</p>
<h2>Think about development, not just results</h2>
<p>Teams that give players a path to improve keep them longer. If you can say what a player will gain by joining, you do not need to rely on persuasion.</p>
<h2>Fit beats flash</h2>
<p>Availability, location and team culture predict who will still be in your squad next season better than a single good trial does.</p>
<h2>Involve parents for young players</h2>
<p>For under-18s, involve parents or guardians in every conversation, and check your league and county FA rules on recruitment and approaches.</p>"""),
]

FAQ = [
 ("What is Rinquest?","Rinquest is a platform that connects grassroots players, parents, teams and coaches through profiles, smart matching and direct messaging."),
 ("Who can use Rinquest?","Players, parents registering a child, coaches, team managers and clubs across grassroots sport."),
 ("Which sports are supported?","Football, cricket, rugby and hockey. We plan to add more sports over time."),
 ("Is Rinquest free?","Yes to join. Players can create a profile for free, and teams can start on the free Starter plan. Paid team plans add unlimited outreach, advanced search filters, a verified team badge and more."),
 ("How does matching work?","Rinquest connects players and teams using profile information such as sport, position, level, location and availability, plus what each side says they are looking for."),
 ("How do I get started?","Choose whether you are a player, a parent or a team, create your profile and start exploring matches or connecting with people."),
 ("Can a parent create a profile for a child?","Yes. Parents can add a profile for their child from their own account and manage it there."),
 ("How long is a paid team season?","A season runs for 12 months from the date you subscribe."),
 ("Can I upgrade my plan later?","Yes. You can upgrade at any time and pay only the difference, pro-rata, for the rest of the season."),
 ("Is my information secure?","We take privacy and data protection seriously and handle your information securely. Read our Privacy Policy for details."),
 ("Who runs Rinquest?",f"Rinquest is run by {COMPANY['name']}, a company registered in England and Wales, company number {COMPANY['number']}, based in {COMPANY['town']}, UK."),
]

# ─────────────────────────── LAYOUT ───────────────────────────
LOGO_MARK = ('<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="12" fill="none" stroke="#034E28" stroke-width="4"/>'
             '<circle cx="16" cy="16" r="4.2" fill="#FFC93C"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23034E28'/%3E"
           "%3Ccircle cx='16' cy='16' r='9' fill='none' stroke='%23fff' stroke-width='3.5'/%3E%3Ccircle cx='16' cy='16' r='3.2' fill='%23FFC93C'/%3E%3C/svg%3E")

NAV = [("For players","/for-players/"),("For parents","/for-parents/"),("For teams","/for-teams/"),("Pricing","/pricing/"),("Insights","/insights/")]

def header(current):
    links = "".join(
        f'<a href="{u(p)}"{" aria-current=\"page\"" if p==current else ""}>{t}</a>' for t,p in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap bar">
<a class="logo" href="{u('/')}" aria-label="Rinquest home">{LOGO_MARK}Rinquest</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="nav" id="nav" aria-label="Main">{links}</nav>
<div class="bar-actions"><a class="btn btn-quiet" href="{LOGIN}">Log in</a><a class="btn btn-solid" href="{u('/join/')}">Join free</a></div>
</div></header>"""

def footer():
    soc = "".join(f'<li><a href="{h}" rel="noopener">{n}</a></li>' for n,h in SOCIAL.items())
    sports = "".join(f'<li><a href="{u("/"+k+"/")}">{v["name"]}</a></li>' for k,v in SPORTS.items())
    return f"""<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="logo" href="{u('/')}">{LOGO_MARK.replace('#034E28','#ffffff')}Rinquest</a>
<p style="margin-top:1rem">Built for grassroots sport communities.</p></div>
<div><h3>Platform</h3><ul>
<li><a href="{u('/for-players/')}">For players</a></li><li><a href="{u('/for-parents/')}">For parents</a></li>
<li><a href="{u('/for-teams/')}">For teams</a></li><li><a href="{u('/pricing/')}">Pricing</a></li>
<li><a href="{app('/search?type=team')}">Find a team</a></li><li><a href="{app('/search?type=player')}">Find players</a></li></ul></div>
<div><h3>Sports</h3><ul>{sports}</ul></div>
<div><h3>Company</h3><ul>
<li><a href="{u('/about/')}">About us</a></li><li><a href="{u('/faq/')}">FAQs</a></li><li><a href="{u('/insights/')}">Insights</a></li>
<li><a href="{u('/safeguarding/')}">Safeguarding</a></li><li><a href="{u('/verification/')}">Verification</a></li>
<li><a href="{app('/contact')}">Contact</a></li></ul></div>
<div><h3>Follow</h3><ul>{soc}</ul></div>
</div>
<div class="legal">
<p>{COMPANY['name']} · Company number {COMPANY['number']} · {COMPANY['street']}, {COMPANY['town']}, {COMPANY['postcode']}, United Kingdom</p>
<p><a href="{app('/privacy')}">Privacy policy</a> · <a href="{app('/terms')}">Terms of service</a> · <a href="{app('/cookies')}">Cookie policy</a> · © {datetime.date.today().year} Rinquest</p>
</div></div></footer>
<script src="{u('/assets/site.js')}" defer></script>"""

ORG_LD = {
  "@context":"https://schema.org","@type":"Organization","name":"Rinquest","legalName":COMPANY["name"],
  "url":SITE_URL,"logo":f"{SITE_URL}/assets/logo.svg","sameAs":list(SOCIAL.values()),
  "description":"Rinquest connects grassroots players, parents, teams and coaches across football, cricket, rugby and hockey.",
  "address":{"@type":"PostalAddress","streetAddress":COMPANY["street"],"addressLocality":COMPANY["town"],
             "postalCode":COMPANY["postcode"],"addressCountry":"GB"},
}
WEB_LD = {"@context":"https://schema.org","@type":"WebSite","name":"Rinquest","url":SITE_URL}

SITEMAP = []
def page(path, title, desc, body, current="", ld=None, noindex=False, crumbs=None, og_type="website", sitemap=True):
    url = SITE_URL + path
    lds = list(ld or [])
    if path == "/":
        lds += [ORG_LD, WEB_LD]
    if crumbs:
        lds.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":i+1,"name":n,"item":SITE_URL+p} for i,(n,p) in enumerate([("Home","/")]+crumbs)]})
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in lds)
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    t = html.escape(title, quote=True); d = html.escape(desc, quote=True)
    doc = f"""<!doctype html>
<html lang="en-GB"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
{robots}
<meta name="theme-color" content="#034E28">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="Rinquest">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{OG_IMAGE}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;800&family=DM+Sans:wght@400;500;700&display=swap">
<link rel="stylesheet" href="{u('/assets/style.css')}">
<script>document.documentElement.className="js"</script>
{ld_html}
</head><body>
{header(current)}
<main id="main">
{body}
</main>
{footer()}
</body></html>"""
    out = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(doc)
    if sitemap and not noindex:
        SITEMAP.append(path)

def roles_block(primary="player"):
    def row(cls, label, sub, href):
        return f'<li><a class="role {cls}" href="{href}"><div><strong>{label}</strong><span>{sub}</span></div><i aria-hidden="true">›</i></a></li>'
    return f"""<ul class="roles">
{row("role-primary" if primary=="player" else "", "I'm a player", "Build a profile and get found by teams near you", SIGNUP_PLAYER)}
{row("", "I'm a parent", "Add a profile for your child and manage it yourself", SIGNUP_PARENT)}
{row("role-primary" if primary=="team" else "", "I run a team or club", "Find players who fit your squad", SIGNUP_TEAM)}
</ul>"""

def crumbs_html(items):
    parts = [f'<a href="{u("/")}">Home</a>'] + [f'<a href="{u(p)}">{n}</a>' if p else n for n,p in items]
    return f'<nav class="wrap crumbs" aria-label="Breadcrumb">{" / ".join(parts)}</nav>'

def faq_html(items):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in items)

def faq_ld(items):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}

def cta_band(title, sub, buttons):
    return f"""<section class="sec sec-dark"><div class="wrap split split-start">
<div><h2>{title}</h2><p class="lead">{sub}</p></div>
<div class="btn-row" style="align-self:center;margin:0">{buttons}</div></div></section>"""

# ─────────────────────────── HOME ───────────────────────────
PITCH_SVG = """<svg class="pitch" viewBox="0 0 360 520" role="img" aria-label="A football pitch seen from above, with three players linked by lines to the teams that suit them">
<defs><pattern id="mow" width="360" height="65" patternUnits="userSpaceOnUse"><rect width="360" height="32.5" fill="#0A6836"/><rect y="32.5" width="360" height="32.5" fill="#0C7039"/></pattern></defs>
<rect width="360" height="520" fill="url(#mow)"/>
<g fill="none" stroke="#fff" stroke-width="2.5" opacity=".85">
<rect x="24" y="24" width="312" height="472" rx="4"/><line x1="24" y1="260" x2="336" y2="260"/>
<circle cx="180" cy="260" r="46"/><rect x="88" y="24" width="184" height="80"/><rect x="132" y="24" width="96" height="34"/>
<rect x="88" y="416" width="184" height="80"/><rect x="132" y="462" width="96" height="34"/></g>
<circle cx="180" cy="260" r="4" fill="#fff"/>
<g fill="none" stroke="#fff" stroke-width="3.5"><circle cx="252" cy="92" r="14"/><circle cx="94" cy="330" r="14"/><circle cx="262" cy="410" r="14"/></g>
<g fill="#FFC93C"><circle cx="110" cy="150" r="9"/><circle cx="250" cy="250" r="9"/><circle cx="150" cy="446" r="9"/></g>
<path class="match match-1" pathLength="1" d="M119 145 Q190 100 238 92"/>
<path class="match match-2" pathLength="1" d="M242 254 Q170 300 108 328"/>
<path class="match match-3" pathLength="1" d="M159 444 Q210 440 248 414"/>
</svg>"""

def build_home():
    sports = "".join(f'<a class="sport" href="{u("/"+k+"/")}"><strong>{v["name"]}</strong><span>{len(v["roles"])} positions to search by</span></a>' for k,v in SPORTS.items())
    guides = "".join(f'<li><a href="{u("/insights/"+g["slug"]+"/")}">{g["title"]}</a><p>{g["blurb"]}</p></li>' for g in GUIDES)
    body = f"""
<section class="hero"><div class="wrap hero-grid">
<div>
<h1>Find your next team. Find your next player.</h1>
<p class="lead">Rinquest connects grassroots players, parents, coaches and clubs across football, cricket, rugby and hockey. Pick who you are to get started.</p>
{roles_block()}
<p class="fine">Free to join for players and teams.</p>
</div>
<div class="pitch-wrap">{PITCH_SVG}
<div class="chip chip-a"><b>Centre-back</b>Sunday mornings, within 5 miles</div>
<div class="chip chip-b"><b>Team needs a centre-back</b>Sunday league, plays in your area</div>
</div></div></section>

<section class="sec sec-turf" id="what-is-rinquest"><div class="wrap">
<p class="answer">Rinquest is a UK platform where grassroots players and teams find each other. Players and parents build profiles, teams search by position, level, location and availability, and both sides talk directly, so squads fill faster and players get seen.</p>
</div></section>

<section class="sec" id="how-it-works"><div class="wrap split split-start">
<div><h2>How Rinquest works</h2><p class="lead">Two sides of the same match. Both start free.</p></div>
<div>
<h3>If you play</h3>
<ol class="steps">
<li><h4>Build your profile</h4><p>Your sport, position, level, availability and ambitions.</p></li>
<li><h4>Get discovered</h4><p>Coaches and teams searching for players like you can find you.</p></li>
<li><h4>Find your next team</h4><p>Message teams directly and explore the opportunities that suit you.</p></li>
</ol>
<h3 style="margin-top:1.5rem">If you run a team</h3>
<ol class="steps">
<li><h4>Create your team profile</h4><p>Show players what makes your team a good place to play.</p></li>
<li><h4>Find the right players</h4><p>Search and filter player profiles to match what your squad needs.</p></li>
<li><h4>Grow your squad</h4><p>Connect directly with players and parents to recruit faster.</p></li>
</ol>
</div></div></section>

<section class="sec sec-turf"><div class="wrap">
<h2>What makes the match better</h2>
<ul class="rows">
<li><h3>Verified profiles</h3><p>Profiles teams and players can trust. <a href="{u('/verification/')}">See how verification works.</a></p></li>
<li><h3>Smart matching</h3><p>Opportunities based on level, location, availability and ambition, so you spend time on real fits.</p></li>
<li><h3>Direct connections</h3><p>Message the right people directly and start the conversation the same day.</p></li>
<li><h3>Built for families</h3><p>Parents can create and manage a profile for their child. <a href="{u('/for-parents/')}">Read the parents' guide.</a></p></li>
</ul></div></section>

<section class="sec" id="sports"><div class="wrap">
<h2>Four sports, one place to be found</h2>
<p class="lead">Pick a sport to see how players and teams use Rinquest.</p>
<div class="sports">{sports}</div></div></section>

<section class="sec sec-dark"><div class="wrap split split-start">
<div><p class="quote-main">"Absolute game-changer! Finding reliable players used to be a nightmare, and this would have been a lifesaver."</p>
<p class="quote-by">James Snelgrove<span>Former Team Coordinator, Woking Town FC</span></p></div>
<div>
<blockquote class="quote-side"><p>"Rinquest has helped us showcase his ability properly and explore opportunities that feel more closely aligned with his current level and development goals."</p><p class="quote-by">Lovee Chandna<span>Parent</span></p></blockquote>
<blockquote class="quote-side"><p>"Rinquest fills a real gap by helping players and teams discover each other more easily and efficiently."</p><p class="quote-by">Hyder Roohani<span>Team Manager, Burpham Juniors FC</span></p></blockquote>
</div></div></section>

<section class="sec"><div class="wrap">
<h2>Insights for players, coaches and teams</h2>
<p class="lead">Practical advice on recruitment, availability and getting noticed.</p>
<ul class="guides">{guides}</ul></div></section>

{cta_band("Ready to get started?", "Join Rinquest free and start finding the right players and opportunities.",
  f'<a class="btn btn-card" href="{u("/join/")}">Create a free profile</a><a class="btn btn-ghost" style="color:#fff;border-color:#fff" href="{u("/pricing/")}">See team plans</a>')}
"""
    page("/", "Rinquest | Grassroots player and team matching for football, cricket, rugby and hockey",
         "Rinquest connects grassroots players, parents, teams and coaches across football, cricket, rugby and hockey. Build a profile, get discovered and find the right fit. Free to join.",
         body, current="/")

# ─────────────────────────── JOIN ───────────────────────────
def build_join():
    body = f"""<section class="sec"><div class="wrap split split-start">
<div><h1>Join Rinquest free</h1><p class="lead">Tell us who you are so we can set up the right profile. It only takes a moment, and you can add more profiles later, such as one for a child.</p>
<p class="fine">Already have an account? <a href="{LOGIN}">Log in</a>.</p></div>
<div>{roles_block()}</div></div></section>"""
    page("/join/", "Join Rinquest free | Player, parent or team sign-up",
         "Create a free Rinquest profile as a player, a parent registering a child, or a team or club looking for players.", body, sitemap=True)

# ─────────────────────────── AUDIENCE PAGES ───────────────────────────
def build_players():
    body = f"""{crumbs_html([("For players",None)])}
<section class="sec"><div class="wrap split split-start">
<div><h1>Get seen by teams that need a player like you</h1>
<p class="lead">Build one profile with your position, level and availability, and let teams come to you. Free to join.</p>
<div class="btn-row"><a class="btn btn-card" href="{SIGNUP_PLAYER}">Create free profile</a><a class="btn btn-ghost" href="{app('/search?type=team')}">Browse teams first</a></div></div>
<div><h2 style="font-size:1.6rem">What goes on your profile</h2>
<ul class="rows">
<li><h3>Your game</h3><p>Sport, position and level, so you appear in the right searches.</p></li>
<li><h3>Your week</h3><p>Availability that tells a manager you can commit.</p></li>
<li><h3>Your goals</h3><p>What you want from a team, in your own words.</p></li></ul></div></div></section>
<section class="sec sec-turf"><div class="wrap split split-start">
<div><h2>How you find your next team</h2></div>
<ol class="steps">
<li><h4>Build your profile</h4><p>Highlight your skills, experience, availability and ambitions.</p></li>
<li><h4>Get discovered</h4><p>Be visible to coaches and teams searching for players like you.</p></li>
<li><h4>Connect directly</h4><p>Message teams and explore the opportunities that fit.</p></li></ol></div></section>
<section class="sec"><div class="wrap"><h2>Tips for getting noticed</h2>
<ul class="guides"><li><a href="{u('/insights/how-players-get-noticed/')}">How players get noticed</a><p>What a strong profile looks like.</p></li>
<li><a href="{u('/insights/what-coaches-value-beyond-ability/')}">What coaches value beyond ability</a><p>Show attitude and reliability, not just skill.</p></li></ul></div></section>
{cta_band("Your next team is looking", "Create your free profile and be visible today.", f'<a class="btn btn-card" href="{SIGNUP_PLAYER}">Create free profile</a>')}"""
    page("/for-players/", "For players | Get discovered by grassroots teams | Rinquest",
         "Build a Rinquest player profile with your position, level and availability and get found by grassroots football, cricket, rugby and hockey teams. Free to join.",
         body, current="/for-players/", crumbs=[("For players","/for-players/")])

def build_parents():
    body = f"""{crumbs_html([("For parents",None)])}
<section class="sec"><div class="wrap split split-start">
<div><h1>Help your child be seen, and stay in charge</h1>
<p class="lead">Create and manage your child's profile from your own account, so the right teams can find them and you decide what happens next.</p>
<div class="btn-row"><a class="btn btn-card" href="{SIGNUP_PARENT}">Create free profile</a><a class="btn btn-ghost" href="{u('/safeguarding/')}">Read our safeguarding approach</a></div></div>
<div><ol class="steps">
<li><h4>Sign up as a parent</h4><p>One account for you. Add a profile for each child who plays.</p></li>
<li><h4>Add your child's profile</h4><p>Sport, position, level and availability. Manage or edit it any time from your account.</p></li>
<li><h4>Connect with teams</h4><p>Teams looking for players like your child can get in touch, and you can explore the opportunities that suit their level and goals.</p></li></ol></div></div></section>
<section class="sec sec-turf"><div class="wrap split split-start">
<div><h2>For families who play more than one sport</h2></div>
<div><p>Many children split their week between sports. Rinquest supports football, cricket, rugby and hockey, so you can look for the right fit in each.</p>
<blockquote class="quote-side"><p>"As a parent of a 13-year-old who plays both football and cricket, Rinquest has helped us showcase his ability properly."</p><p class="quote-by">Lovee Chandna<span>Parent</span></p></blockquote></div></div></section>
<section class="sec"><div class="wrap narrow"><h2>Questions parents ask</h2>
{faq_html([("Can I create a profile for my child?","Yes. Add a profile for your child from your own account and manage it from there."),
("Is it free?","Rinquest is free to join for players and teams."),
("Where can I read about safeguarding?",f'On our <a href="{u("/safeguarding/")}">safeguarding page</a>.')])}
</div></section>"""
    page("/for-parents/", "For parents | Create a profile for your child player | Rinquest",
         "Parents can create and manage a Rinquest profile for their child and help them get found by grassroots football, cricket, rugby and hockey teams.",
         body, current="/for-parents/", crumbs=[("For parents","/for-parents/")])

def build_teams():
    body = f"""{crumbs_html([("For teams",None)])}
<section class="sec"><div class="wrap split split-start">
<div><h1>Fill your squad without the group-chat chaos</h1>
<p class="lead">Search player profiles by what your team needs and message the right people directly. Start free, upgrade when you want unlimited outreach.</p>
<div class="btn-row"><a class="btn btn-card" href="{SIGNUP_TEAM}">Create free team profile</a><a class="btn btn-ghost" href="{app('/search?type=player')}">Browse players first</a></div></div>
<div><ol class="steps">
<li><h4>Create your team profile</h4><p>Show players what makes your team a great place to play.</p></li>
<li><h4>Find the right players</h4><p>Search and filter player profiles to match your team's needs.</p></li>
<li><h4>Grow your squad</h4><p>Connect directly with players and parents to recruit faster and more effectively.</p></li></ol></div></div></section>
<section class="sec sec-turf"><div class="wrap"><h2>Plans that grow with your club</h2>
<ul class="rows">
<li><h3>Starter (free)</h3><p>Team profile, appear in player searches, browse players, receive enquiries and limited outreach.</p></li>
<li><h3>Recruit</h3><p>Unlimited outreach, advanced filters, a verified team badge, priority visibility and new-match alerts.</p></li>
<li><h3>Club and Premium Club</h3><p>One club profile across every team, multi-coach management, and for larger clubs onboarding support and analytics.</p></li></ul>
<div class="btn-row"><a class="btn btn-solid" href="{u('/pricing/')}">Compare plans</a></div></div></section>
<section class="sec"><div class="wrap"><h2>Recruiting guides for coaches</h2><ul class="guides">
<li><a href="{u('/insights/find-the-right-players-faster/')}">Find the right players faster</a><p>Start with the gap, check availability, message early.</p></li>
<li><a href="{u('/insights/player-poaching-vs-player-development/')}">Player poaching vs player development</a><p>Recruit openly and fairly.</p></li></ul></div></section>
{cta_band("Start recruiting today", "Create your team profile for free.", f'<a class="btn btn-card" href="{SIGNUP_TEAM}">Create free team profile</a>')}"""
    page("/for-teams/", "For teams and clubs | Find grassroots players | Rinquest",
         "Create a free Rinquest team profile, search grassroots player profiles by level, location and availability, and message players and parents directly.",
         body, current="/for-teams/", crumbs=[("For teams","/for-teams/")])

# ─────────────────────────── PRICING ───────────────────────────
def build_pricing():
    if FOUNDING_UNTIL:
        founding = f"Join before {FOUNDING_UNTIL} to lock in founding pricing for your first season."
    else:
        founding = "Founding rates are available while launch pricing is open. Sign up now to lock in the lower price for your first season."
    Y='<span class="yes" aria-label="Included">✓</span>'; N='<span class="no" aria-label="Not included">–</span>'
    rows = [("Appear in player searches",Y,Y,Y,Y),("Team profile",Y,Y,Y,Y),("Browse players",Y,Y,Y,Y),("Receive player interest",Y,Y,Y,Y),
            ("Player outreach","Limited","Unlimited","Unlimited","Unlimited"),("Advanced search filters",N,Y,Y,Y),("Verified team badge",N,Y,Y,Y),
            ("Priority visibility in search",N,Y,Y,Y),("New player match alerts",N,Y,Y,Y),("Manage multiple teams and coaches",N,N,Y,Y),
            ("One shared club profile",N,N,Y,Y),("Dedicated onboarding support",N,N,N,Y),("Club recruitment analytics",N,N,N,Y),("Priority support",N,N,N,Y)]
    trs = "".join("<tr><td>"+r[0]+"</td>"+"".join(f"<td>{c}</td>" for c in r[1:])+"</tr>" for r in rows)
    pricing_faq = [
      ("Is Rinquest free to use?","Yes. Players are free, and teams can use the Starter plan free to create a profile, be discovered, browse players and start making connections."),
      ("What is the founding rate?","A limited-time price for early adopters. You lock in the lower price for your first season when you sign up during the launch period."),
      ("How long is a season?","A season runs for 12 months from the date you subscribe."),
      ("Is Recruit for one team or a whole club?","Recruit is designed for individual teams. If your club has several teams or coaches, Club or Premium Club gives you the management and visibility you need."),
      ("Which plan suits a larger club?","Clubs with 2 to 19 teams suit Club. Clubs with 20 or more teams suit Premium Club, which adds dedicated onboarding, analytics and priority support."),  # CONFIRM: 20-team boundary (site currently says 2-20 and 20+, and FAQ says 30+)
      ("Can I upgrade later?","Yes, at any time. You pay only the difference, pro-rata, for the rest of the season."),
    ]
    body = f"""{crumbs_html([("Pricing",None)])}
<section class="sec"><div class="wrap">
<h1>Simple pricing for grassroots recruitment</h1>
<p class="lead">Players join free. Teams start free and upgrade when they want more reach. {founding}</p>
<div class="plans">
<div class="plan"><h3>Starter</h3><div class="price">Free</div><div class="per">for every team</div>
<ul><li>Create a team profile</li><li>Be discovered by players</li><li>Browse player profiles</li><li>Receive player enquiries</li><li>Limited player outreach</li></ul>
<a class="btn btn-ghost" href="{SIGNUP_TEAM}">Start free</a></div>
<div class="plan plan-feature"><span class="plan-flag">Most popular</span><h3>Recruit</h3><div class="price"><s>£99</s>£49</div><div class="per">founding rate, per team per season</div>
<ul><li>Unlimited player outreach</li><li>Advanced search filters</li><li>Verified team badge</li><li>Priority visibility in search</li><li>New player match alerts</li><li>Everything in Starter</li></ul>
<a class="btn btn-card" href="{SIGNUP_TEAM}">Upgrade to Recruit</a></div>
<div class="plan"><h3>Club</h3><div class="price"><s>£79</s>£39</div><div class="per">founding rate, per team per season (2 to 19 teams)</div>
<ul><li>Everything in Recruit</li><li>One club profile for all teams</li><li>Manage multiple coaches and teams</li><li>Shared recruitment activity</li><li>Club-wide visibility</li></ul>
<a class="btn btn-solid" href="{app('/contact?topic=club-standard')}">Choose Club</a></div>
<div class="plan"><h3>Premium Club</h3><div class="price"><s>£59</s>£29</div><div class="per">founding rate, per team per season (20+ teams)</div>
<ul><li>Everything in Club</li><li>Dedicated onboarding support</li><li>Club recruitment analytics</li><li>Priority feature requests</li><li>Priority support</li></ul>
<a class="btn btn-ghost" href="{app('/contact?topic=club-enterprise')}">Talk to us</a></div>
</div>
<h2 style="margin-top:3.5rem">What changes as you grow</h2>
<div class="table-scroll"><table><thead><tr><th scope="col">Feature</th><th scope="col">Starter</th><th scope="col">Recruit</th><th scope="col">Club</th><th scope="col">Premium Club</th></tr></thead><tbody>{trs}</tbody></table></div>
</div></section>
<section class="sec sec-turf"><div class="wrap narrow"><h2>Pricing questions</h2>{faq_html(pricing_faq)}</div></section>"""
    page("/pricing/", "Pricing for teams and clubs | Rinquest",
         "Rinquest is free for players and free for teams to start. Compare Starter, Recruit, Club and Premium Club plans, with founding rates for early adopters.",
         body, current="/pricing/", ld=[faq_ld(pricing_faq)], crumbs=[("Pricing","/pricing/")])

# ─────────────────────────── FAQ / ABOUT ───────────────────────────
def build_faq():
    body = f"""{crumbs_html([("FAQs",None)])}
<section class="sec"><div class="wrap narrow"><h1>Frequently asked questions</h1>
<p class="lead">Everything you need to know about Rinquest. Can't find your answer? <a href="{app('/contact')}">Get in touch</a>.</p>
{faq_html(FAQ)}</div></section>"""
    page("/faq/", "FAQs | How Rinquest works for players, parents and teams",
         "Answers to common questions about Rinquest: who it is for, which sports it covers, how matching works, pricing, parent profiles and security.",
         body, ld=[faq_ld(FAQ)], crumbs=[("FAQs","/faq/")])

def build_about():
    body = f"""{crumbs_html([("About",None)])}
<section class="sec"><div class="wrap split split-start">
<div><h1>The trusted platform for grassroots talent discovery</h1>
<p class="lead">Rinquest helps players and teams connect through verified profiles, smarter matching and direct communication.</p></div>
<div class="prose">
<p>The idea for Rinquest came from firsthand experience in grassroots sport: seeing talented players struggle to reach the right opportunities, while coaches and teams faced the same challenge finding the right fit.</p>
<p>Too often, recruitment has depended on fragmented networks and informal connections rather than transparent, merit-based discovery. Rinquest was built to change that.</p>
<p>Our mission is simple: to help players find the right opportunities and help teams build stronger squads through better matches.</p>
<div class="todo">CONFIRM before launch: add founder names, photos and one line each on why they built Rinquest. A named, visible team is one of the strongest trust signals a young platform can show.</div>
</div></div></section>
<section class="sec sec-turf"><div class="wrap"><h2>What we stand for</h2><ul class="rows">
<li><h3>Better opportunities</h3><p>Helping players get discovered based on talent, potential and fit.</p></li>
<li><h3>Smarter recruitment</h3><p>Helping teams identify the right players through transparent, efficient matching.</p></li>
<li><h3>Trusted connections</h3><p>A more reliable, merit-based recruitment experience for everyone involved.</p></li></ul></div></section>
<section class="sec"><div class="wrap"><h2>Company details</h2>
<p>{COMPANY['name']}, company number {COMPANY['number']}<br>{COMPANY['street']}, {COMPANY['town']}, {COMPANY['postcode']}, United Kingdom</p></div></section>
{cta_band("Ready to find the right match?", "Join Rinquest free as a player, parent or team.", f'<a class="btn btn-card" href="{u("/join/")}">Join Rinquest</a>')}"""
    page("/about/", "About Rinquest | Grassroots recruitment, made fairer",
         "Rinquest was built from firsthand experience in grassroots sport to help players get discovered and teams find the right fit through verified profiles and direct communication.",
         body, current="", crumbs=[("About","/about/")])

# ─────────────────────────── TRUST PAGES (draft-gated) ───────────────────────────
def build_safeguarding():
    banner = "" if SAFEGUARDING_APPROVED else '<div class="draft"><strong>Draft.</strong> This page is a structure to complete. It is hidden from search engines until <code>SAFEGUARDING_APPROVED</code> is set to True in build.py.</div>'
    def sec(h, q):
        t = "" if SAFEGUARDING_APPROVED else f'<div class="todo">CONFIRM: {q}</div>'
        return f"<h2>{h}</h2>{t}"
    body = f"""{crumbs_html([("Safeguarding",None)])}
<section class="sec"><div class="wrap narrow prose"><h1>Safeguarding on Rinquest</h1>
{banner}
<p class="lead">Many players on Rinquest are children, and their parents and carers are part of every conversation. This page explains how we protect them.</p>
{sec("What is shown about a child","Which fields are public, which are visible to logged-in teams only, and whether photo and exact location are optional or hidden.")}
{sec("Who can contact a child or their parent","Do messages go to the parent or to the child? Can coaches message under-18s directly? Any age thresholds.")}
{sec("How coaches and teams are checked","What checks exist today (email, verification badge, DBS or safeguarding-certificate prompts), and what is planned.")}
{sec("How to report a concern","Reporting route, response time, blocking, and who reviews reports.")}
{sec("Guidance we follow","Which governing-body guidance you align with (for example FA, ECB, RFU, England Hockey) and how you handle UK data-protection duties for children. Have a solicitor or DPO review this page.")}
</div></section>"""
    page("/safeguarding/", "Safeguarding on Rinquest | Keeping young players safe",
         "How Rinquest protects young players and supports parents and carers: what is shown, who can make contact, how teams are checked and how to report a concern.",
         body, crumbs=[("Safeguarding","/safeguarding/")], noindex=not SAFEGUARDING_APPROVED)

def build_verification():
    banner = "" if VERIFICATION_APPROVED else '<div class="draft"><strong>Draft.</strong> Describe the real verification process here. Hidden from search engines until <code>VERIFICATION_APPROVED</code> is True in build.py.</div>'
    t = "" if VERIFICATION_APPROVED else '<div class="todo">CONFIRM: what exactly is verified (identity, club affiliation, league registration, coaching qualifications), who verifies it, how long it takes and what the badge means.</div>'
    body = f"""{crumbs_html([("Verification",None)])}
<section class="sec"><div class="wrap narrow prose"><h1>How verification works</h1>{banner}
<p class="lead">Verified profiles are one of Rinquest's core promises, so we want to be specific about what they mean.</p>{t}
<h2>The Verified Team badge</h2><p>Teams on the Recruit plan and above receive a Verified Team badge.</p></div></section>"""
    page("/verification/", "How verification works on Rinquest | Verified teams and profiles",
         "What a verified profile or Verified Team badge means on Rinquest, who checks it and how to get one.",
         body, crumbs=[("Verification","/verification/")], noindex=not VERIFICATION_APPROVED)

# ─────────────────────────── SPORT + INSIGHT PAGES ───────────────────────────
def build_sports():
    for k, s in SPORTS.items():
        tags = "".join(f"<li>{r}</li>" for r in s["roles"])
        others = ", ".join(f'<a href="{u("/"+o+"/")}">{v["name"]}</a>' for o,v in SPORTS.items() if o != k)
        body = f"""{crumbs_html([(s["name"],None)])}
<section class="sec"><div class="wrap split split-start">
<div><h1>{s["title"]}</h1><p class="lead">{s["intro"]}</p>
<div class="btn-row"><a class="btn btn-card" href="{app('/search?sport='+s['name'])}">Browse {s['name'].lower()} profiles</a><a class="btn btn-ghost" href="{u('/join/')}">Join free</a></div></div>
<div><h2 style="font-size:1.6rem">Search and be found by position</h2><ul class="tags">{tags}</ul>
<p class="muted">Also on Rinquest: {others}.</p></div></div></section>
<section class="sec sec-turf"><div class="wrap narrow"><h2>{s['name']} questions</h2>{faq_html(s['faq'])}</div></section>
{cta_band(f"Find your place in {s['name'].lower()}", "Create a free profile as a player, parent or team.", f'<a class="btn btn-card" href="{u("/join/")}">Join Rinquest</a>')}"""
        page(f"/{k}/", f"{s['title']} | Rinquest", s["desc"], body, crumbs=[(s["name"],f"/{k}/")], ld=[faq_ld(s["faq"])])

def build_insights():
    items = "".join(f'<li><a href="{u("/insights/"+g["slug"]+"/")}">{g["title"]}</a><p>{g["blurb"]}</p></li>' for g in GUIDES)
    body = f"""{crumbs_html([("Insights",None)])}
<section class="sec"><div class="wrap"><h1>Insights for players, coaches and teams</h1>
<p class="lead">Practical advice on recruitment, availability and getting noticed in grassroots sport.</p>
<ul class="guides">{items}</ul></div></section>"""
    page("/insights/", "Insights and guides for grassroots players and coaches | Rinquest",
         "Practical guides on how grassroots players get noticed, what coaches value beyond ability, and how teams recruit the right players faster.",
         body, current="/insights/", crumbs=[("Insights","/insights/")])
    for g in GUIDES:
        ld = {"@context":"https://schema.org","@type":"Article","headline":g["title"],"description":g["blurb"],
              "author":{"@type":"Organization","name":"Rinquest"},"publisher":{"@type":"Organization","name":"Rinquest"},
              "datePublished":TODAY,"dateModified":TODAY,"mainEntityOfPage":f"{SITE_URL}/insights/{g['slug']}/"}
        body = f"""{crumbs_html([("Insights","/insights/"),(g["title"],None)])}
<article class="sec"><div class="wrap narrow prose"><h1>{g["title"]}</h1><p class="lead">{g["blurb"]}</p>{g["body"]}
<div class="btn-row"><a class="btn btn-card" href="{u('/join/')}">Join Rinquest free</a></div></div></article>"""
        page(f"/insights/{g['slug']}/", f"{g['title']} | Rinquest Insights", g["blurb"], body,
             current="/insights/", ld=[ld], crumbs=[("Insights","/insights/"),(g["title"],f"/insights/{g['slug']}/")], og_type="article")

def build_404():
    body = f"""<section class="sec"><div class="wrap narrow"><h1>That page has left the pitch</h1>
<p class="lead">The page you are looking for does not exist or has moved.</p>
<div class="btn-row"><a class="btn btn-solid" href="{u('/')}">Go to the homepage</a><a class="btn btn-ghost" href="{u('/join/')}">Join free</a></div></div></section>"""
    page("/404/", "Page not found | Rinquest", "This page could not be found.", body, noindex=True, sitemap=False)
    os.replace(os.path.join(OUT, "404", "index.html"), os.path.join(OUT, "404.html"))
    os.rmdir(os.path.join(OUT, "404"))

# ─────────────────────────── FILES ───────────────────────────
def write_support_files():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    shutil.copy("src/style.css", os.path.join(OUT, "assets", "style.css"))
    open(os.path.join(OUT, "assets", "site.js"), "w").write(
        "(function(){var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');if(!b||!n)return;"
        "b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);});})();")
    open(os.path.join(OUT, "assets", "logo.svg"), "w").write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="12" fill="none" stroke="#034E28" stroke-width="4"/><circle cx="16" cy="16" r="4.2" fill="#FFC93C"/></svg>')
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    urls = "".join(f"<url><loc>{SITE_URL}{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in SITEMAP)
    open(os.path.join(OUT, "sitemap.xml"), "w").write(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    bots = ["GPTBot","OAI-SearchBot","ChatGPT-User","ClaudeBot","Claude-SearchBot","PerplexityBot","Google-Extended","Applebot-Extended"]
    txt = "User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {SITE_URL}/sitemap.xml\n"
    open(os.path.join(OUT, "robots.txt"), "w").write(txt)
    llms = f"""# Rinquest

> Rinquest is a UK platform that connects grassroots players, parents, teams and coaches across football, cricket, rugby and hockey through profiles, smart matching and direct messaging. Free to join for players and teams.

## Key pages
- [For players]({SITE_URL}/for-players/): build a profile and get discovered
- [For parents]({SITE_URL}/for-parents/): create and manage a profile for your child
- [For teams]({SITE_URL}/for-teams/): search players and recruit
- [Pricing]({SITE_URL}/pricing/): Starter (free), Recruit, Club, Premium Club
- [FAQs]({SITE_URL}/faq/)
- [Insights]({SITE_URL}/insights/): recruitment and getting-noticed guides

## Company
{COMPANY['name']}, company number {COMPANY['number']}, {COMPANY['street']}, {COMPANY['town']}, {COMPANY['postcode']}, UK
"""
    open(os.path.join(OUT, "llms.txt"), "w").write(llms)

def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    build_home(); build_join(); build_players(); build_parents(); build_teams()
    build_pricing(); build_faq(); build_about(); build_safeguarding(); build_verification()
    build_sports(); build_insights(); build_404(); write_support_files()
    print(f"Built {len(SITEMAP)} indexable pages into ./{OUT}")

if __name__ == "__main__":
    main()
