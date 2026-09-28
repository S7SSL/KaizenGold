#!/usr/bin/env python3
"""SEO/AEO lint for kaizengold.com. Run from repo root: python3 gen/seo_check.py
Fails (exit 1) on: title >65 / meta description >160 chars, missing description,
h1 count != 1, missing or non-trailing-slash canonical on indexable pages,
JSON-LD that does not parse, placeholders or AggregateRating in JSON-LD,
FAQPage questions not visible on the page, broken internal links,
indexable pages missing from sitemap.xml, noindex pages listed in it.
"""
import glob, html, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://kaizengold.com"
SKIP = {"google9fcd04f81cb998a6.html"}
errors = []
os.chdir(ROOT)
sitemap = open("sitemap.xml").read()
sm_urls = set(re.findall(r"<loc>(.*?)</loc>", sitemap))
pages = [f for f in glob.glob("**/*.html", recursive=True) if f not in SKIP and not f.startswith(("gen/", ".github/"))]
for f in sorted(pages):
    s = open(f, encoding="utf-8").read()
    url = SITE + "/" + (f[:-len("index.html")] if f.endswith("index.html") else f)
    noindex = re.search(r'<meta name="robots" content="[^"]*noindex', s)
    title = re.search(r"<title>(.*?)</title>", s, re.S)
    desc = re.search(r'<meta name="description" content="(.*?)"', s)
    t = html.unescape(title.group(1)).strip() if title else ""
    d = html.unescape(desc.group(1)) if desc else ""
    def err(m): errors.append(f"{f}: {m}")
    if not t: err("missing <title>")
    elif len(t) > 65: err(f"title {len(t)} chars > 65")
    if not noindex:
        if not d: err("missing meta description")
        elif len(d) > 160: err(f"meta description {len(d)} chars > 160")
        c = re.search(r'<link rel="canonical" href="(.*?)"', s)
        if not c: err("missing canonical")
        elif not c.group(1).endswith("/"): err(f"canonical without trailing slash: {c.group(1)}")
        elif c.group(1) != url: err(f"canonical {c.group(1)} != {url}")
        if url not in sm_urls: err("indexable page missing from sitemap.xml")
    elif url in sm_urls: err("noindex page listed in sitemap.xml")
    if f != "kyc/index.html":
        n = len(re.findall(r"<h1[\s>]", s))
        if n != 1: err(f"{n} <h1> elements (want 1)")
    visible = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", "", s, flags=re.S)))
    visible = re.sub(r"\s+", " ", visible)
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            data = json.loads(block)
        except Exception as e:
            err(f"JSON-LD does not parse: {e}"); continue
        if re.search(r"\[[A-Z_ ]+\]", block): err("placeholder in JSON-LD")
        if "AggregateRating" in block: err("AggregateRating in JSON-LD (no independent source)")
        if data.get("@type") == "FAQPage":
            for q in data.get("mainEntity", []):
                name = re.sub(r"\s+", " ", q["name"]).strip()
                if name not in visible: err(f"FAQ question not visible: {name[:60]}")
    for href in re.findall(r'href="(/[^"#?]*)', s):
        target = href.lstrip("/")
        if not target or target.endswith("/"):
            path = os.path.join(target, "index.html")
        else:
            path = target
        if not os.path.exists(path): err(f"broken internal link {href}")
for u in sm_urls:
    rel = u.replace(SITE + "/", "")
    if not os.path.exists(os.path.join(rel, "index.html") if (rel == "" or rel.endswith("/")) else rel):
        errors.append(f"sitemap.xml: {u} has no file")
if errors:
    print("\n".join(errors)); print(f"\nSEO check FAILED: {len(errors)} problem(s)"); sys.exit(1)
print(f"SEO check passed: {len(pages)} HTML files, {len(sm_urls)} sitemap URLs.")
