#!/usr/bin/env python3
"""Kaizen Gold static site generator — AEO build.
Run from repo root:  python3 gen/build.py
Generates /about/, /knowledge/, answer pages, /faq/, sitemap.xml, robots.txt,
assets/site.css and patches index.html (nav, footer, Organization schema).
"""
import json, os, glob, importlib.util, html, re, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://kaizengold.com"
TODAY = "2026-06-10"
EMAIL = "sat@kaizengold.com"

# ---------------------------------------------------------------- CSS
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--black:#0a0a0a;--black-light:#111111;--card-bg:#161616;--gold:#e8a828;
--gold-light:#f5c342;--gold-dark:#c48a1a;--text-primary:#ffffff;
--text-secondary:#b0b0b0;--border:#222222}
html{scroll-behavior:smooth}
body{font-family:'Poppins',sans-serif;background:var(--black);color:var(--text-primary);line-height:1.6;overflow-x:hidden}
nav{position:fixed;top:0;width:100%;z-index:1000;padding:1rem 2rem;background:rgba(10,10,10,.95);backdrop-filter:blur(20px);border-bottom:1px solid rgba(232,168,40,.15)}
.nav-container{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center}
.logo{font-family:'DM Serif Display',serif;font-size:1.6rem;font-weight:700;letter-spacing:3px;color:var(--gold);text-decoration:none;text-transform:uppercase}
.nav-links{display:flex;list-style:none;gap:2.5rem}
.nav-links a{color:var(--text-secondary);text-decoration:none;font-size:.85rem;letter-spacing:1.5px;text-transform:uppercase;transition:color .3s ease;font-weight:400}
.nav-links a:hover,.nav-links a.active{color:var(--gold)}
.mobile-toggle{display:none;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:5px}
.mobile-toggle span{width:24px;height:2px;background:var(--gold);transition:all .3s ease}
main{max-width:840px;margin:0 auto;padding:9rem 2rem 5rem}
main.wide{max-width:1100px}
.breadcrumb{font-size:.8rem;color:var(--text-secondary);margin-bottom:2rem;letter-spacing:1px}
.breadcrumb a{color:var(--text-secondary);text-decoration:none}
.breadcrumb a:hover{color:var(--gold)}
.breadcrumb span{color:var(--gold)}
.page-label{font-size:.75rem;letter-spacing:4px;text-transform:uppercase;color:var(--gold);margin-bottom:1rem;display:flex;align-items:center;gap:1rem}
.page-label::before{content:'';width:40px;height:1px;background:var(--gold)}
h1{font-family:'DM Serif Display',serif;font-size:clamp(2rem,5vw,3rem);font-weight:600;line-height:1.2;margin-bottom:1.5rem}
article h2{font-family:'DM Serif Display',serif;font-size:1.6rem;font-weight:600;margin:3rem 0 1rem;color:var(--gold-light)}
article h3{font-family:'DM Serif Display',serif;font-size:1.2rem;font-weight:600;margin:2rem 0 .75rem}
article p,article li{color:var(--text-secondary);font-weight:300;line-height:1.85;margin-bottom:1.25rem;font-size:1rem}
article ul,article ol{padding-left:1.4rem;margin-bottom:1.5rem}
article li{margin-bottom:.6rem}
article a{color:var(--gold);text-decoration:none;border-bottom:1px solid rgba(232,168,40,.35)}
article a:hover{color:var(--gold-light)}
.lead{font-size:1.1rem;color:var(--text-primary);font-weight:300;line-height:1.9;padding:1.5rem;background:var(--card-bg);border-left:3px solid var(--gold);margin-bottom:2.5rem}
.lead strong{color:var(--gold-light);font-weight:500}
.takeaways{background:var(--black-light);border:1px solid var(--border);padding:2rem;margin:2.5rem 0}
.takeaways h2{margin-top:0}
table{width:100%;border-collapse:collapse;margin:1.5rem 0;font-size:.92rem}
th,td{border:1px solid var(--border);padding:.75rem 1rem;text-align:left;color:var(--text-secondary);font-weight:300;vertical-align:top}
th{color:var(--gold);font-weight:500;background:var(--card-bg);letter-spacing:.5px}
.faq-block details{background:var(--card-bg);border:1px solid var(--border);margin-bottom:.75rem}
.faq-block summary{cursor:pointer;padding:1.1rem 1.25rem;font-weight:400;color:var(--text-primary);list-style:none;position:relative;padding-right:2.5rem}
.faq-block summary::after{content:'+';position:absolute;right:1.25rem;top:50%;transform:translateY(-50%);color:var(--gold);font-size:1.3rem;font-weight:300}
.faq-block details[open] summary::after{content:'\\2212'}
.faq-block details p{padding:0 1.25rem 1.25rem;margin:0;color:var(--text-secondary);font-weight:300;line-height:1.8}
.faq-cat{font-family:'DM Serif Display',serif;font-size:1.5rem;color:var(--gold-light);margin:3rem 0 1.25rem}
.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem;margin-top:2.5rem}
.k-card{display:block;padding:1.75rem;background:var(--card-bg);border:1px solid var(--border);text-decoration:none;transition:all .3s ease}
.k-card:hover{border-color:rgba(232,168,40,.4);transform:translateY(-3px)}
.k-card h3{font-family:'DM Serif Display',serif;font-size:1.15rem;color:var(--text-primary);margin-bottom:.6rem}
.k-card p{color:var(--text-secondary);font-size:.85rem;font-weight:300;line-height:1.7;margin:0}
.k-card .tag{display:inline-block;font-size:.7rem;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:.75rem}
.related{margin-top:4rem;padding-top:2.5rem;border-top:1px solid var(--border)}
.related h2{font-family:'DM Serif Display',serif;font-size:1.4rem;margin-bottom:.5rem;color:var(--gold-light)}
.cta-band{margin-top:4rem;padding:2.5rem;background:var(--black-light);border:1px solid rgba(232,168,40,.25);text-align:center}
.cta-band p{color:var(--text-secondary);font-weight:300;margin-bottom:1.5rem}
.cta-band h2{font-family:'DM Serif Display',serif;font-size:1.5rem;margin-bottom:.75rem}
.btn-gold{display:inline-block;padding:.9rem 2.2rem;background:var(--gold);color:var(--black);text-decoration:none;font-size:.8rem;letter-spacing:2px;text-transform:uppercase;font-weight:600;transition:all .3s ease}
.btn-gold:hover{background:var(--gold-light);transform:translateY(-2px)}
footer{padding:3rem 2rem;border-top:1px solid var(--border);background:var(--black-light)}
.footer-grid{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr;gap:3rem}
.footer-grid h4{font-size:.8rem;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:1rem;font-weight:500}
.footer-grid p,.footer-grid a{color:var(--text-secondary);font-size:.85rem;font-weight:300;text-decoration:none;display:block;margin-bottom:.5rem}
.footer-grid a:hover{color:var(--gold)}
.footer-bottom{max-width:1200px;margin:2.5rem auto 0;padding-top:1.5rem;border-top:1px solid var(--border);font-size:.8rem;color:var(--text-secondary);font-weight:300}
@media(max-width:768px){
.nav-links{display:none;position:fixed;top:60px;left:0;width:100%;flex-direction:column;background:rgba(10,10,10,.98);padding:2rem;gap:1.5rem;border-bottom:1px solid var(--border)}
.nav-links.active{display:flex}
.mobile-toggle{display:flex}
main{padding:7rem 1.5rem 4rem}
.footer-grid{grid-template-columns:1fr}}
"""

NAV_ITEMS = [("Home", "/"), ("About", "/about/"), ("Services", "/#services"),
             ("Knowledge", "/knowledge/"), ("FAQ", "/faq/"), ("Contact", "/#contact")]

FOOTER = """
<footer>
  <div class="footer-grid">
    <div>
      <h4>Kaizen Gold</h4>
      <p>Specialist broker for dor&eacute; and bullion gold transactions, working with a leading UAE refinery. Banking instruments issued on a guaranteed CIF basis to Dubai.</p>
      <p>London, UK &amp; Dubai, UAE</p>
      <a href="mailto:__EMAIL__">__EMAIL__</a>
    </div>
    <div>
      <h4>Company</h4>
      <a href="/about/">About Kaizen Gold</a>
      <a href="/#services">Services</a>
      <a href="/#process">Our Process</a>
      <a href="/#contact">Contact</a>
    </div>
    <div>
      <h4>Knowledge</h4>
      <a href="/knowledge/">Knowledge Centre</a>
      <a href="/faq/">Gold Trading FAQ</a>
      <a href="/knowledge/what-is-gold-dore/">What Is Gold Dor&eacute;?</a>
      <a href="/knowledge/what-is-a-cif-gold-transaction/">CIF Gold Transactions</a>
    </div>
  </div>
  <div class="footer-bottom">&copy; 2026 Kaizen Gold. All rights reserved.</div>
</footer>
<script>
const t=document.querySelector('.mobile-toggle'),l=document.querySelector('.nav-links');
if(t){t.addEventListener('click',()=>l.classList.toggle('active'));}
</script>""".replace("__EMAIL__", EMAIL)


def nav_html(active):
    cls = ' class="active"'
    lis = "".join(
        f'<li><a href="{u}"{cls if u == active else ""}>{n}</a></li>'
        for n, u in NAV_ITEMS)
    return f"""<nav>
  <div class="nav-container">
    <a href="/" class="logo">Kaizen Gold</a>
    <ul class="nav-links">{lis}</ul>
    <button class="mobile-toggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
  </div>
</nav>"""


def page(path, title, desc, body, schemas, active="/", wide=False):
    schema_tags = "\n".join(
        '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + "</script>"
        for s in schemas)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{SITE}{path}">
<meta name="twitter:card" content="summary">
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{schema_tags}
</head>
<body>
{nav_html(active)}
<main{' class="wide"' if wide else ''}>
{body}
</main>
{FOOTER}
</body>
</html>"""


def breadcrumb_schema(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
                for i, (n, u) in enumerate(crumbs)]}


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
                           for q, a in faqs]}


def org_ref():
    return {"@type": "Organization", "name": "Kaizen Gold", "url": SITE + "/",
            "email": EMAIL,
            "description": "Specialist broker for doré and bullion gold transactions, partnered with a leading UAE refinery. Banking instruments issued on a guaranteed CIF basis to Dubai.",
            "areaServed": ["GB", "AE"],
            "location": [{"@type": "Place", "name": "London, United Kingdom"},
                         {"@type": "Place", "name": "Dubai, United Arab Emirates"}],
            "knowsAbout": ["Gold trading", "Gold brokerage", "Gold doré", "Gold bullion",
                            "CIF gold transactions", "Documentary letters of credit",
                            "Trade finance", "Precious metals compliance", "Gold refining"]}


def article_schema(mod, path):
    return {"@context": "https://schema.org", "@type": "Article",
            "headline": mod.TITLE, "description": mod.DESC,
            "datePublished": TODAY, "dateModified": TODAY,
            "inLanguage": "en", "url": SITE + path,
            "mainEntityOfPage": {"@type": "WebPage", "@id": SITE + path},
            "author": org_ref(), "publisher": org_ref(),
            "about": getattr(mod, "ABOUT", []),
            "isPartOf": {"@type": "WebSite", "name": "Kaizen Gold", "url": SITE + "/"}}


def faq_html(faqs):
    return '<div class="faq-block">' + "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs) + "</div>"


def load_articles():
    mods = []
    for f in sorted(glob.glob(os.path.join(ROOT, "gen", "content", "a_*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        mods.append(m)
    return mods


def write(relpath, content):
    p = os.path.join(ROOT, relpath.lstrip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(content)
    print("wrote", relpath)


def render_article(mod, all_mods):
    path = f"/knowledge/{mod.SLUG}/"
    by_slug = {m.SLUG: m for m in all_mods}
    related = "".join(
        f'<a class="k-card" href="/knowledge/{s}/"><span class="tag">{by_slug[s].CATEGORY}</span>'
        f'<h3>{by_slug[s].TITLE}</h3><p>{by_slug[s].CARD}</p></a>'
        for s in mod.RELATED if s in by_slug)
    takeaways = "".join(f"<li>{t}</li>" for t in mod.TAKEAWAYS)
    body = f"""
<div class="breadcrumb"><a href="/">Home</a> &rsaquo; <a href="/knowledge/">Knowledge Centre</a> &rsaquo; <span>{mod.TITLE}</span></div>
<div class="page-label">{mod.CATEGORY}</div>
<article>
<h1>{mod.TITLE}</h1>
<p class="lead">{mod.LEAD}</p>
{mod.BODY}
<div class="takeaways"><h2>Key Takeaways</h2><ul>{takeaways}</ul></div>
<h2>Frequently Asked Questions</h2>
{faq_html(mod.FAQS)}
</article>
<div class="related"><h2>Related Reading</h2><div class="card-grid">{related}</div></div>
<div class="cta-band">
<h2>Speak to Kaizen Gold</h2>
<p>Kaizen Gold facilitates dor&eacute; and bullion gold transactions through a leading UAE refinery, with banking instruments issued on a guaranteed CIF basis to Dubai.</p>
<a class="btn-gold" href="/#contact">Get in Touch</a>
</div>"""
    schemas = [article_schema(mod, path), faq_schema(mod.FAQS),
               breadcrumb_schema([("Home", "/"), ("Knowledge Centre", "/knowledge/"), (mod.TITLE, path)])]
    write(f"knowledge/{mod.SLUG}/index.html",
          page(path, f"{mod.TITLE} | Kaizen Gold", mod.DESC, body, schemas, active="/knowledge/"))
    return path


def render_hub(mods):
    cards = "".join(
        f'<a class="k-card" href="/knowledge/{m.SLUG}/"><span class="tag">{m.CATEGORY}</span>'
        f'<h3>{m.TITLE}</h3><p>{m.CARD}</p></a>' for m in mods)
    body = f"""
<div class="breadcrumb"><a href="/">Home</a> &rsaquo; <span>Knowledge Centre</span></div>
<div class="page-label">Knowledge Centre</div>
<h1>Gold Trading Knowledge Centre</h1>
<article>
<p class="lead">Clear, practical explanations of how international gold transactions actually work &mdash; from dor&eacute; sourcing and refinery assays to documentary letters of credit, CIF delivery and LBMA pricing. Written by Kaizen Gold, a specialist broker for dor&eacute; and bullion gold transactions.</p>
</article>
<div class="card-grid">{cards}</div>
<div class="cta-band">
<h2>Have a question we haven't covered?</h2>
<p>Browse the <a href="/faq/" style="color:var(--gold)">Gold Trading FAQ</a> or contact us directly.</p>
<a class="btn-gold" href="/#contact">Contact Kaizen Gold</a>
</div>"""
    schemas = [{"@context": "https://schema.org", "@type": "CollectionPage",
                "name": "Gold Trading Knowledge Centre", "url": SITE + "/knowledge/",
                "description": "Expert articles on international gold trading, trade finance, refining and compliance from Kaizen Gold.",
                "publisher": org_ref()},
               breadcrumb_schema([("Home", "/"), ("Knowledge Centre", "/knowledge/")])]
    write("knowledge/index.html",
          page("/knowledge/", "Gold Trading Knowledge Centre | Kaizen Gold",
               "Expert articles on international gold trading, doré, refinery assays, CIF transactions, documentary letters of credit and LBMA pricing.",
               body, schemas, active="/knowledge/", wide=True))


def render_faq():
    spec = importlib.util.spec_from_file_location("faqs", os.path.join(ROOT, "gen", "content", "faqs.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    sections, all_faqs = "", []
    for cat, faqs in m.CATEGORIES:
        all_faqs += faqs
        sections += f'<h2 class="faq-cat">{cat}</h2>' + faq_html(faqs)
    body = f"""
<div class="breadcrumb"><a href="/">Home</a> &rsaquo; <span>FAQ</span></div>
<div class="page-label">Frequently Asked Questions</div>
<h1>Gold Trading FAQ</h1>
<article>
<p class="lead">Direct answers to the questions we are asked most often about international gold transactions &mdash; pricing, shipping, refining, settlement, trade finance instruments and compliance. For deeper explanations, visit the <a href="/knowledge/">Knowledge Centre</a>.</p>
{sections}
</article>
<div class="cta-band">
<h2>Ask us directly</h2>
<p>If your question isn't answered here, the Kaizen Gold team is happy to help.</p>
<a class="btn-gold" href="/#contact">Contact Kaizen Gold</a>
</div>"""
    schemas = [faq_schema(all_faqs),
               breadcrumb_schema([("Home", "/"), ("FAQ", "/faq/")])]
    write("faq/index.html",
          page("/faq/", "Gold Trading FAQ — Pricing, Shipping, Assay, Settlement | Kaizen Gold",
               "Answers to common questions about gold pricing, CIF delivery, refinery assays, settlement, off-take agreements, DLCs, SBLCs and precious metals compliance.",
               body, schemas, active="/faq/"))
    return len(all_faqs)


def render_about():
    body = f"""
<div class="breadcrumb"><a href="/">Home</a> &rsaquo; <span>About</span></div>
<div class="page-label">About Us</div>
<h1>About Kaizen Gold</h1>
<article>
<p class="lead"><strong>Kaizen Gold is a specialist precious metals brokerage</strong> facilitating dor&eacute; and bullion gold transactions between sellers and a leading refinery in the United Arab Emirates. The firm operates from London, United Kingdom and Dubai, United Arab Emirates, and structures transactions on a guaranteed CIF (Cost, Insurance and Freight) basis with delivery exclusively to Dubai.</p>

<h2>What Kaizen Gold Does</h2>
<p>Kaizen Gold acts as a facilitator &mdash; the connecting party between gold suppliers and a top-tier UAE refinery. The firm's role covers three core activities:</p>
<ul>
<li><strong>Dor&eacute; gold facilitation.</strong> Arranging the sale and delivery of semi-pure <a href="/knowledge/what-is-gold-dore/">dor&eacute; gold</a> sourced through verified supply chains, refined at the partner refinery to internationally recognised purity standards.</li>
<li><strong>Bullion gold brokerage.</strong> Brokering refined gold bullion bars, fully assayed and certified, for institutional buyers and high-net-worth individuals seeking physical gold allocation.</li>
<li><strong>Banking instruments.</strong> Coordinating the issuance of banking instruments &mdash; such as <a href="/knowledge/what-is-an-mt700-dlc/">documentary letters of credit</a> &mdash; on a guaranteed CIF basis to Dubai, with documentation that meets international trade finance standards.</li>
</ul>

<h2>How a Transaction Works</h2>
<p>Every transaction follows a defined four-stage process:</p>
<ol>
<li><strong>Enquiry.</strong> An initial consultation establishes requirements, volumes and transaction parameters.</li>
<li><strong>Due diligence.</strong> Comprehensive KYC and compliance verification is carried out on all parties before any commercial step is taken.</li>
<li><strong>Instruments.</strong> Banking instruments are issued on a guaranteed CIF basis, structured to the requirements of the transaction.</li>
<li><strong>Delivery.</strong> Secure <a href="/knowledge/what-is-a-cif-gold-transaction/">CIF delivery to Dubai</a> is coordinated through the established refinery partnership, followed by <a href="/knowledge/how-does-a-gold-refinery-assay-work/">refinery assay</a> and settlement.</li>
</ol>

<h2>Markets Served</h2>
<p>Kaizen Gold works with gold suppliers, institutional buyers and high-net-worth individuals engaged in international physical gold transactions. Delivery is made exclusively to Dubai, one of the world's foremost gold trading hubs, via the firm's UAE refinery partnership.</p>

<h2>Compliance Approach</h2>
<p>Rigorous due diligence sits at the centre of the firm's process. Comprehensive KYC and compliance verification is performed on all parties involved in a transaction, and documentation is prepared to international trade finance standards. Kaizen Gold is committed to transparency at every stage of the transaction.</p>

<h2>Why Dubai</h2>
<p>Dubai is one of the largest physical gold trading centres in the world, with established refining capacity, vault infrastructure and a deep buyer market. Delivering on a CIF basis to Dubai gives both sellers and buyers a recognised, liquid settlement venue with clear customs and assay procedures.</p>
</article>
<div class="cta-band">
<h2>Work With Kaizen Gold</h2>
<p>Discuss your requirements, volumes and transaction parameters with our team.</p>
<a class="btn-gold" href="/#contact">Get in Touch</a>
</div>"""
    org = org_ref()
    org["@context"] = "https://schema.org"
    schemas = [{"@context": "https://schema.org", "@type": "AboutPage",
                "name": "About Kaizen Gold", "url": SITE + "/about/",
                "description": "Kaizen Gold is a specialist precious metals brokerage facilitating doré and bullion gold transactions through a leading UAE refinery on a guaranteed CIF basis to Dubai.",
                "mainEntity": org},
               breadcrumb_schema([("Home", "/"), ("About", "/about/")])]
    write("about/index.html",
          page("/about/", "About Kaizen Gold — Specialist Gold Brokerage | London & Dubai",
               "Kaizen Gold facilitates doré and bullion gold transactions through a leading UAE refinery, issuing banking instruments on a guaranteed CIF basis to Dubai.",
               body, schemas, active="/about/"))


def patch_index(paths):
    p = os.path.join(ROOT, "index.html")
    src = open(p, encoding="utf-8").read()
    # 1. nav links
    old_nav = """<ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#process">Process</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>"""
    new_nav = """<ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="/about/">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="/knowledge/">Knowledge</a></li>
                <li><a href="/faq/">FAQ</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>"""
    if old_nav in src:
        src = src.replace(old_nav, new_nav)
    elif new_nav not in src:
        raise AssertionError("nav anchor not found")
    # 2. Organization + WebSite schema before </head>
    org = org_ref(); org["@context"] = "https://schema.org"
    org["contactPoint"] = {"@type": "ContactPoint", "email": EMAIL, "contactType": "sales"}
    website = {"@context": "https://schema.org", "@type": "WebSite",
               "name": "Kaizen Gold", "url": SITE + "/",
               "publisher": {"@type": "Organization", "name": "Kaizen Gold", "url": SITE + "/"}}
    if "application/ld+json" not in src:
        tags = ("<script type=\"application/ld+json\">" + json.dumps(org, ensure_ascii=False) + "</script>\n"
                "<script type=\"application/ld+json\">" + json.dumps(website, ensure_ascii=False) + "</script>\n")
        src = src.replace("</head>", tags + "</head>")
    # 3. footer with links
    old_footer = """<footer>
        <p>&copy; 2025 Kaizen Gold. All rights reserved.</p>
    </footer>"""
    new_footer = """<footer>
        <p style="margin-bottom:1rem;">
            <a href="/about/" style="color:var(--text-secondary);text-decoration:none;margin:0 1rem;">About</a>
            <a href="/knowledge/" style="color:var(--text-secondary);text-decoration:none;margin:0 1rem;">Knowledge Centre</a>
            <a href="/faq/" style="color:var(--text-secondary);text-decoration:none;margin:0 1rem;">FAQ</a>
        </p>
        <p>&copy; 2026 Kaizen Gold. All rights reserved.</p>
    </footer>"""
    if old_footer in src:
        src = src.replace(old_footer, new_footer)
    open(p, "w", encoding="utf-8").write(src)
    print("patched index.html")


def render_sitemap(paths):
    urls = "".join(
        f"<url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in paths)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n'
          f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")


def render_llms(mods):
    by_cat = {}
    for m in mods:
        by_cat.setdefault(m.CATEGORY, []).append(m)
    lines = ["# Kaizen Gold", "",
             "> Kaizen Gold is a specialist precious metals brokerage facilitating doré and bullion gold transactions through a leading UAE refinery, with banking instruments issued on a guaranteed CIF basis to Dubai. Operating from London, UK and Dubai, UAE.",
             "",
             "Kaizen Gold publishes a Gold Trading Knowledge Centre: practical, expert explanations of international gold transactions — doré, refinery assays, CIF delivery, documentary letters of credit, LBMA pricing, compliance and the Dubai market.",
             "",
             "## Company", "",
             f"- [About Kaizen Gold]({SITE}/about/): what the firm does, its process, markets served and compliance approach",
             f"- [Gold Trading FAQ]({SITE}/faq/): direct answers to common questions on pricing, shipping, assay, settlement, trade finance, compliance and fraud prevention",
             f"- [Knowledge Centre]({SITE}/knowledge/): all expert articles", ""]
    for cat in sorted(by_cat):
        lines.append(f"## {cat}")
        lines.append("")
        for m in by_cat[cat]:
            lines.append(f"- [{m.TITLE}]({SITE}/knowledge/{m.SLUG}/): {m.CARD}")
        lines.append("")
    lines += ["## Contact", "", f"- Email: {EMAIL}", "- Locations: London, UK & Dubai, UAE", ""]
    write("llms.txt", "\n".join(lines))


def main():
    write("assets/site.css", CSS)
    mods = load_articles()
    paths = ["/", "/about/", "/knowledge/", "/faq/"]
    for m in mods:
        paths.append(render_article(m, mods))
    render_hub(mods)
    n = render_faq()
    render_about()
    patch_index(paths)
    render_sitemap(paths)
    render_llms(mods)
    print(f"\nDone: {len(mods)} articles, {n} FAQs, {len(paths)} URLs in sitemap.")


if __name__ == "__main__":
    main()
