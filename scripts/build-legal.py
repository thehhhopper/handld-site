#!/usr/bin/env python3
"""Render legal/src/*.md into static pages for GitHub Pages.

Replace the markdown under legal/src and run this script again. It rewrites
the committed HTML in place. GitHub Pages publishes those files as-is.

    python scripts/build-legal.py
    python scripts/build-legal.py --check

--check rebuilds in memory, fails if that HTML differs from what is
committed, and always fails if rendered HTML contains an em dash (U+2014),
a leftover {{ token, the phrase "Every other refusal", or a Handled
paragraph that is not word for word.
"""

from __future__ import annotations

import difflib
import re
import sys
from html import escape, unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "legal" / "src"

# Contact address for every {{LEGAL_CONTACT_EMAIL}} token. One definition.
LEGAL_CONTACT_EMAIL = "therestishandled@gmail.com"
DRAFT_BANNER = "Draft, invite-only beta, pending counsel review."
# Shared outcome sentence. Any page that starts it must continue it exactly.
HANDLED_PARAGRAPH = (
    'Any other outcome reads "Handled." That means the desk processed your idea '
    "under your ruleset. It does not tell you whether a trade was placed, or its size or stop."
)
HANDLED_OPENING = 'Any other outcome reads "Handled."'
FORBIDDEN_PHRASE = "Every other refusal"
MARKDOWN_VERSION = "3.11"

# Filename -> published directory index. Swap the file contents freely.
# A new or renamed source file must be added here so it has a URL.
PAGES = {
    "terms.md": {
        "out": "terms/index.html",
        "href": "/terms/",
    },
    "privacy.md": {
        "out": "privacy/index.html",
        "href": "/privacy/",
    },
    "risk.md": {
        "out": "risk/index.html",
        "href": "/risk/",
    },
    "refusals.md": {
        "out": "legal/refusals/index.html",
        "href": "/legal/refusals/",
    },
}

# Root-relative paths used in the markdown, mapped to directory indexes.
ROUTE_HREFS = {spec["href"].rstrip("/"): spec["href"] for spec in PAGES.values()}
ROUTE_HREFS["/legal"] = "/legal/"

FOOTER_LINKS = (
    ("/terms/", "Terms"),
    ("/privacy/", "Privacy"),
    ("/risk/", "Risk notice"),
    ("/legal/", "Legal"),
)

INDEX_LINKS = (
    ("/terms/", "Terms"),
    ("/privacy/", "Privacy"),
    ("/risk/", "Risk notice"),
    ("/legal/refusals/", "Schedule 1 (refusals)"),
)

LEGAL_INDEX = "legal/index.html"

EM_DASH = "\u2014"
EM_DASH_ENTITY = re.compile(r"&mdash;|&#8212;|&#x2014;", re.IGNORECASE)
TOKEN_LEFT = "{{"
BARE_URL = re.compile(r"https?://[^\s<]+")
MD_TARGET = re.compile(r"\]\(([^)\s]+)\)")
CODE_SPAN = re.compile(r"(```.*?```|`[^`]*`)", re.DOTALL)
TABLE = re.compile(r"<table>.*?</table>", re.DOTALL)
TABLE_ROW = re.compile(r"<tr>\s*(?:<td>.*?</td>\s*)+</tr>", re.DOTALL)
TD = re.compile(r"<td>(.*?)</td>", re.DOTALL)
TH = re.compile(r"<th>(.*?)</th>", re.DOTALL)
TAG = re.compile(r"<[^>]+>")
H1 = re.compile(r"<h1>(.*?)</h1>", re.DOTALL)

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="@@DESCRIPTION@@">
<title>@@TITLE@@</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Schibsted+Grotesk:wght@400;500;600;700&display=swap">
<style>
  :root {
    --paper: #EDF0EF;
    --paper-2: #E3E8E6;
    --rule: #C7CFCC;
    --ink: #0F1A24;
    --ink-2: #4B5760;
    --ink-3: #7A868E;
    --stop: #2440C4;
    --stop-soft: rgba(36, 64, 196, 0.10);
    --mono: "IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace;
    --sans: "Schibsted Grotesk", "Helvetica Neue", Helvetica, Arial, sans-serif;
    color-scheme: light;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --paper: #0B1219; --paper-2: #101922; --rule: #22303B;
      --ink: #E6EAE8; --ink-2: #9AA6AE; --ink-3: #6B7880;
      --stop: #7D93FF; --stop-soft: rgba(125, 147, 255, 0.14);
      color-scheme: dark;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; background: var(--paper); color: var(--ink);
    font-family: var(--sans); font-size: 17px; line-height: 1.6;
    -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility;
  }
  a { color: var(--stop); text-decoration: none; }
  a:hover { text-decoration: underline; text-underline-offset: 3px; }
  :focus-visible { outline: 2px solid var(--stop); outline-offset: 3px; }
  .banner {
    margin: 0; background: var(--stop-soft); color: var(--ink);
    border-bottom: 1px solid var(--rule);
    font-family: var(--mono); font-size: 13px; line-height: 1.45;
    padding: 12px 24px; text-align: center; text-wrap: balance;
  }
  header { border-bottom: 1px solid var(--rule); }
  header .bar, footer .wrap {
    max-width: 1120px; margin: 0 auto; padding-inline: 24px;
  }
  header .bar {
    display: flex; align-items: baseline; justify-content: space-between;
    gap: 12px 24px; flex-wrap: wrap; padding-block: 22px;
  }
  .mark {
    font-family: var(--mono); font-weight: 600; letter-spacing: -0.02em;
    color: var(--ink); font-size: 22px; text-decoration: none;
  }
  .mark .stop { color: var(--stop); }
  a.mark:hover { text-decoration: none; }
  header nav, footer .cols {
    display: flex; flex-wrap: wrap; gap: 10px 18px;
    font-family: var(--mono); font-size: 13px;
  }
  header nav a, footer .cols a { color: var(--ink-2); text-decoration: none; }
  header nav a:hover, footer .cols a:hover { color: var(--stop); text-decoration: underline; text-underline-offset: 3px; }
  header nav a[aria-current="page"] { color: var(--ink); }
  main { padding: 36px 0 72px; }
  article { max-width: 760px; margin: 0 auto; padding-inline: 24px; }
  article h1 {
    font-size: clamp(32px, 6vw, 44px); line-height: 1.08; letter-spacing: -0.025em;
    font-weight: 700; margin: 0 0 18px; text-wrap: balance;
  }
  article h2 {
    font-size: clamp(22px, 3.2vw, 28px); line-height: 1.2; letter-spacing: -0.02em;
    font-weight: 700; margin: 36px 0 12px; text-wrap: balance;
  }
  article h3 { font-size: 18px; line-height: 1.3; margin: 28px 0 8px; font-weight: 600; }
  article p { margin: 0 0 16px; overflow-wrap: break-word; }
  article ul, article ol { margin: 0 0 16px; padding-left: 1.25em; }
  article li { margin: 0.4em 0; padding-left: 0.15em; overflow-wrap: break-word; }
  article li::marker { color: var(--stop); }
  article strong { font-weight: 600; }
  article code {
    font-family: var(--mono); font-size: 0.9em;
    background: var(--paper-2); padding: 0.05em 0.35em; border-radius: 2px;
  }
  article p a, article li a { text-decoration: underline; text-underline-offset: 3px; overflow-wrap: anywhere; }
  ul.index { list-style: none; margin: 8px 0 0; padding: 0; border-top: 1px solid var(--ink); }
  ul.index li { margin: 0; padding: 0; border-bottom: 1px solid var(--rule); }
  ul.index a {
    display: block; padding: 16px 0; color: var(--ink);
    font-size: 20px; font-weight: 600; letter-spacing: -0.015em; text-decoration: none;
  }
  ul.index a:hover { color: var(--stop); }
  .table-scroll { margin: 0 0 20px; }
  table { border-collapse: collapse; width: 100%; font-size: 15px; line-height: 1.45; }
  th, td {
    text-align: left; vertical-align: top; padding: 10px 16px 10px 0;
    border-bottom: 1px solid var(--rule); overflow-wrap: anywhere;
  }
  th {
    font-family: var(--mono); font-size: 12px; font-weight: 500;
    letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-3);
    border-bottom: 1px solid var(--ink);
  }
  footer { border-top: 1px solid var(--ink); }
  footer .wrap {
    display: grid; grid-template-columns: 128px 1fr; column-gap: 40px;
    padding-block: 40px 56px;
  }
  footer .mark { font-size: 20px; }
  @media (max-width: 720px) {
    main { padding: 28px 0 56px; }
    footer .wrap { grid-template-columns: 1fr; row-gap: 20px; }
    table, thead, tbody, tr, th, td { display: block; width: auto; }
    thead {
      position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
      overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border: 0;
    }
    tr { border-bottom: 1px solid var(--rule); padding: 12px 0; }
    td, th { border-bottom: 0; padding: 6px 0; }
    td::before {
      content: attr(data-label);
      display: block; font-family: var(--mono); font-size: 11px;
      letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-3);
      margin-bottom: 2px;
    }
  }
</style>
</head>
<body>
<p class="banner" role="note">@@BANNER@@</p>
<header>
  <div class="bar">
    <a class="mark" href="/">handld<span class="stop">.</span></a>
    <nav aria-label="Legal">
        @@NAV@@
    </nav>
  </div>
</header>
<main>
  <article>
@@BODY@@
  </article>
</main>
<footer>
  <div class="wrap">
    <a class="mark" href="/">handld<span class="stop">.</span></a>
    <div class="cols">
        @@FOOTER@@
    </div>
  </div>
</footer>
</body>
</html>
"""


def fail(messages: list[str]) -> None:
    for message in messages:
        print(message, file=sys.stderr)
    sys.exit(1)


def require_markdown():
    try:
        import markdown
    except ImportError:
        fail(["markdown is not installed. Run: python -m pip install -r requirements.txt"])
    if markdown.__version__ != MARKDOWN_VERSION:
        fail([
            f"markdown {markdown.__version__} is installed; requirements.txt pins {MARKDOWN_VERSION}."
        ])
    return markdown


def outside_code(text: str, fn) -> str:
    parts = CODE_SPAN.split(text)
    rendered = []
    for index, part in enumerate(parts):
        rendered.append(part if index % 2 else fn(part))
    return "".join(rendered)


def trim_url(url: str) -> tuple[str, str]:
    trail = ""
    while url and url[-1] in ".,;:!?":
        trail = url[-1] + trail
        url = url[:-1]
    if url.endswith(")") and url.count("(") < url.count(")"):
        trail = ")" + trail
        url = url[:-1]
    return url, trail


def autolink(text: str) -> str:
    def repl_part(part: str) -> str:
        def repl(match: re.Match[str]) -> str:
            start = match.start()
            if start >= 2 and part[start - 2 : start] == "](":
                return match.group(0)
            if start >= 1 and part[start - 1] == "<":
                return match.group(0)
            url, trail = trim_url(match.group(0))
            return f"<{url}>{trail}"

        return BARE_URL.sub(repl, part)

    return outside_code(text, repl_part)


def rewrite_markdown_targets(text: str) -> str:
    def repl_part(part: str) -> str:
        def repl(match: re.Match[str]) -> str:
            dest = match.group(1)
            path, suffix = split_suffix(dest)
            mapped = ROUTE_HREFS.get(path.rstrip("/") or "/")
            if not mapped:
                return match.group(0)
            return f"]({mapped}{suffix})"

        return MD_TARGET.sub(repl, part)

    return outside_code(text, repl_part)


def split_suffix(url: str) -> tuple[str, str]:
    for mark in ("?", "#"):
        if mark in url:
            path, _, rest = url.partition(mark)
            return path, mark + rest
    return url, ""


def prepare_markdown(source: str) -> str:
    text = source.replace(
        "{{LEGAL_CONTACT_EMAIL}}",
        f"[{LEGAL_CONTACT_EMAIL}](mailto:{LEGAL_CONTACT_EMAIL})",
    )
    text = autolink(text)
    text = rewrite_markdown_targets(text)
    return text


def label_tables(html: str) -> str:
    def repl_table(match: re.Match[str]) -> str:
        table = match.group(0)
        headers = [TAG.sub("", cell).strip() for cell in TH.findall(table)]

        def repl_row(row: re.Match[str]) -> str:
            cells = TD.findall(row.group(0))
            labeled = []
            for index, cell in enumerate(cells):
                label = headers[index] if index < len(headers) else ""
                labeled.append(f'<td data-label="{escape(label, quote=True)}">{cell}</td>')
            return "<tr>\n" + "\n".join(labeled) + "\n</tr>"

        table = TABLE_ROW.sub(repl_row, table)
        return f'<div class="table-scroll">\n{table}\n</div>'

    return TABLE.sub(repl_table, html)


def rewrite_hrefs(html: str) -> str:
    def repl(match: re.Match[str]) -> str:
        href = match.group(1)
        path, suffix = split_suffix(href)
        mapped = ROUTE_HREFS.get(path.rstrip("/") or "/")
        if not mapped or href.startswith("mailto:"):
            return match.group(0)
        return f'href="{mapped}{suffix}"'

    return re.sub(r'href="([^"]*)"', repl, html)


def render_markdown(markdown_mod, source: str) -> str:
    body = markdown_mod.markdown(
        prepare_markdown(source),
        extensions=["tables", "sane_lists", "fenced_code"],
        output_format="html",
    )
    body = rewrite_hrefs(body)
    body = label_tables(body)
    return body.strip("\n")


def plain_h1(body: str, fallback: str) -> str:
    match = H1.search(body)
    if not match:
        return fallback
    return TAG.sub("", match.group(1)).strip() or fallback


def shell(title: str, description: str, body: str, current: str) -> str:
    nav = []
    footer = []
    for href, label in FOOTER_LINKS:
        current_attr = ' aria-current="page"' if href == current else ""
        nav.append(f'<a href="{href}"{current_attr}>{escape(label)}</a>')
        footer.append(f'<a href="{href}">{escape(label)}</a>')
    indented = "\n".join("    " + line if line else "" for line in body.split("\n"))
    html = (
        PAGE.replace("@@TITLE@@", escape(title))
        .replace("@@DESCRIPTION@@", escape(description))
        .replace("@@BANNER@@", escape(DRAFT_BANNER))
        .replace("@@NAV@@", "\n        ".join(nav))
        .replace("@@FOOTER@@", "\n        ".join(footer))
        .replace("@@BODY@@", indented)
    )
    if not html.endswith("\n"):
        html += "\n"
    return html


def document_title(heading: str) -> str:
    if "handld" in heading.lower():
        return heading
    return f"{heading} - handld"


def build_index_body() -> str:
    items = "\n".join(
        f'<li><a href="{href}">{escape(label)}</a></li>' for href, label in INDEX_LINKS
    )
    return f"<h1>Legal</h1>\n<ul class=\"index\">\n{items}\n</ul>"


def build_pages(markdown_mod) -> dict[str, str]:
    if not SRC_DIR.is_dir():
        fail([f"missing source directory {SRC_DIR}"])
    found = {path.name for path in SRC_DIR.glob("*.md")}
    missing = sorted(set(PAGES) - found)
    extra = sorted(found - set(PAGES))
    problems = []
    if missing:
        problems.append("missing legal/src file(s): " + ", ".join(missing))
    if extra:
        problems.append("unrouted legal/src file(s): " + ", ".join(extra))
    if problems:
        fail(problems)

    pages: dict[str, str] = {}
    for name, spec in PAGES.items():
        source = (SRC_DIR / name).read_text(encoding="utf-8")
        body = render_markdown(markdown_mod, source)
        heading = plain_h1(body, name)
        title = document_title(heading)
        pages[spec["out"]] = shell(
            title,
            f"{heading}. {DRAFT_BANNER}",
            body,
            spec["href"],
        )
    pages[LEGAL_INDEX] = shell(
        "Legal - handld",
        f"Legal. {DRAFT_BANNER}",
        build_index_body(),
        "/legal/",
    )
    return pages


def check_index_footer() -> list[str]:
    index = ROOT / "index.html"
    if not index.is_file():
        return ["index.html is missing"]
    html = index.read_text(encoding="utf-8")
    problems = []
    for href, label in FOOTER_LINKS:
        snippet = f'<a href="{href}">{label}</a>'
        if snippet not in html:
            problems.append(f"index.html footer is missing {snippet}")
    return problems


def visible_text(html: str) -> str:
    without_style = re.sub(r"<style\b[^>]*>.*?</style>", " ", html, flags=re.IGNORECASE | re.DOTALL)
    return unescape(TAG.sub("", without_style))


def check_handled_wording(pages: dict[str, str]) -> list[str]:
    """Each Handled paragraph must match word for word, and the old phrase must be gone."""
    problems = []
    documents = dict(pages)
    index = ROOT / "index.html"
    if index.is_file():
        documents.setdefault("index.html", index.read_text(encoding="utf-8"))
    for path, html in documents.items():
        text = visible_text(html)
        if FORBIDDEN_PHRASE in text or FORBIDDEN_PHRASE in html:
            problems.append(f"{path}: contains {FORBIDDEN_PHRASE!r}")
        start = 0
        while True:
            found = text.find(HANDLED_OPENING, start)
            if found < 0:
                break
            if not text.startswith(HANDLED_PARAGRAPH, found):
                problems.append(f"{path}: {HANDLED_OPENING!r} is not the required paragraph, word for word")
                break
            start = found + len(HANDLED_PARAGRAPH)
    return problems


def check_text(pages: dict[str, str]) -> list[str]:
    problems = check_index_footer()
    problems.extend(check_handled_wording(pages))
    for path, html in pages.items():
        if EM_DASH in html or EM_DASH_ENTITY.search(html):
            problems.append(f"{path}: rendered text contains an em dash (U+2014)")
        if TOKEN_LEFT in html:
            problems.append(f"{path}: rendered text still contains a {{{{ token")
        if DRAFT_BANNER not in html:
            problems.append(f"{path}: missing draft banner")
    return problems


def check_matches(pages: dict[str, str]) -> list[str]:
    problems = []
    for rel, html in pages.items():
        disk = ROOT / rel
        if not disk.is_file():
            problems.append(f"{rel}: committed file is missing")
            continue
        committed = disk.read_text(encoding="utf-8")
        if committed == html:
            continue
        diff = "".join(
            difflib.unified_diff(
                committed.splitlines(keepends=True),
                html.splitlines(keepends=True),
                fromfile=f"committed/{rel}",
                tofile=f"fresh/{rel}",
            )
        )
        problems.append(f"{rel}: committed HTML differs from a fresh build\n{diff[:6000]}")
    return problems


def write_pages(pages: dict[str, str]) -> None:
    for rel, html in pages.items():
        dest = ROOT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")


def main(argv: list[str]) -> None:
    check_only = "--check" in argv
    markdown_mod = require_markdown()
    pages = build_pages(markdown_mod)
    problems = check_text(pages)
    if check_only:
        problems.extend(check_matches(pages))
    if problems:
        fail(problems)
    if check_only:
        print("fresh build matches committed HTML; no em dash; no leftover tokens; Handled wording ok")
        return
    write_pages(pages)
    print("wrote " + ", ".join(pages))


if __name__ == "__main__":
    main(sys.argv[1:])
