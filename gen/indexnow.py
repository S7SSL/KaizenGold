#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex, Seznam, Naver…) with URLs changed in the last push.
Usage: python3 gen/indexnow.py <before-sha> <after-sha>   (or --all)
"""
import json, os, re, subprocess, sys, urllib.request
sys.path.insert(0, os.path.dirname(__file__))
SITE, HOST = "https://kaizengold.com", "kaizengold.com"
KEY = re.search(r'INDEXNOW_KEY = "(\w+)"', open(os.path.join(os.path.dirname(__file__), "build.py")).read()).group(1)
urls = re.findall(r"<loc>(.*?)</loc>", open("sitemap.xml").read())
if len(sys.argv) == 3 and not set(sys.argv[1]) <= {"0"}:
    changed = subprocess.run(["git", "diff", "--name-only", sys.argv[1], sys.argv[2]], capture_output=True, text=True).stdout.split()
    keep = set()
    for f in changed:
        if f.endswith("index.html"):
            keep.add(SITE + "/" + f[: -len("index.html")])
    urls = [u for u in urls if u in keep]
if not urls:
    print("IndexNow: nothing to submit"); sys.exit(0)
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"{SITE}/{KEY}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow: {r.status} for {len(urls)} URL(s)")
except Exception as e:
    print(f"IndexNow: {e}")  # never fail the workflow on a ping
