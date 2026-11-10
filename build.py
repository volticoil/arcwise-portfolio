"""Builds the standalone index.html from arcwise-portfolio.html (the page source).

Run:  python3 build.py

The standalone build is flagged with data-embed so videos play inline when hosted,
and gets the tags a hosted page needs (icon, link-preview text).
"""
import pathlib

SITE_URL = "https://volticoil.github.io/arcwise-portfolio/"
TITLE = "Arcwise | Roblox programmer"
SUMMARY = (
    "Jonathan Jackson Ameche (Arcwise). Roblox backend programmer and technical lead: "
    "Slap Battles, Sunshine Valley, Paradise Life, Anime Warriors, Combat Warriors."
)
ICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Crect x='2' y='2' width='28' height='28' rx='7' fill='%23C4281C' stroke='%23152238' stroke-width='3'/%3E"
    "%3Ccircle cx='16' cy='16' r='7' fill='%23DC4A3D' stroke='%23152238' stroke-width='3'/%3E%3C/svg%3E"
)

here = pathlib.Path(__file__).resolve().parent
src = (here / "arcwise-portfolio.html").read_text(encoding="utf-8")
head, body = src.split("<!--BODY-->", 1)

hosted = "\n".join([
    '<link rel="icon" href="%s">' % ICON,
    '<link rel="canonical" href="%s">' % SITE_URL,
    '<meta name="theme-color" content="#C4281C">',
    '<meta property="og:type" content="website">',
    '<meta property="og:url" content="%s">' % SITE_URL,
    '<meta property="og:title" content="%s">' % TITLE,
    '<meta property="og:description" content="%s">' % SUMMARY,
    '<meta name="twitter:card" content="summary">',
])

out = (
    '<!doctype html>\n<html lang="en" data-embed>\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + head.strip() + "\n" + hosted + "\n</head>\n<body>\n" + body.strip() + "\n</body>\n</html>\n"
)
(here / "index.html").write_text(out, encoding="utf-8")
print("built index.html", len(out))
