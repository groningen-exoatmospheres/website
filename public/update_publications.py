#!/usr/bin/env python3
"""
update_publications.py — create Hugo (Wowchemy/HugoBlox) publication bundles
for the exoaim.space website from a SciX/ADS public library (or arXiv).

Usage (run from the ExoAIM_Pub folder, or pass --pubdir):

    export ADS_API_TOKEN=xxxxxxxx          # https://scixplorer.org/user/settings/token
    python3 update_publications.py                     # SciX library -> new folders
    python3 update_publications.py --dry-run           # only list what would be created
    python3 update_publications.py --source arxiv      # no token needed: query arXiv instead
    python3 update_publications.py --since 2024        # ignore older papers in the library
    python3 update_publications.py --fill-figures      # add images to folders that have none

For each paper that is not yet on the site it creates

    publication/<firstauthor><year>_<keyword>/
        index.md              front matter in the same format as the existing pages
        cite.bib              BibTeX (ADS export when available)
        featured.png|jpg      proposed image = first figure of the arXiv HTML version
        candidate_figN.*      a few alternative figures (delete or rename to featured.*)

Papers it has already proposed are remembered in publication/.autopub_seen.json,
so a folder you delete will NOT come back next week. Use --forget <arxiv_id|bibcode>
to make it eligible again.

Only the Python standard library is used.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

# --------------------------------------------------------------------------- config
LIBRARY_ID = "Bt4TNyP4RTOi1UoeyWElYg"          # scixplorer.org/public-libraries/<id>
ADS_API = "https://api.adsabs.harvard.edu/v1"
ARXIV_API = "https://export.arxiv.org/api/query"
ARXIV_AUTHOR_QUERY = "au:Changeat_Q"
ADMIN_SURNAME = "changeat"                      # rendered as `admin` in authors:
MAX_LISTED_AUTHORS = 6                          # beyond this: first 5 (+admin) + "et al."
N_CANDIDATE_FIGS = 3
USER_AGENT = "exoaim-publication-updater/1.0 (mailto:q.changeat@rug.nl)"

# arXiv-mode filter (the SciX library is assumed to be curated already):
ARXIV_MAX_AUTHORS = 8      # keep papers with at most this many authors ...
ARXIV_MAX_POSITION = 3     # ... or where Changeat is within the first N authors

ALLOWED_TAGS = [
    "JWST", "HST", "CHEOPS", "PLATO", "HWO", "Ariel",
    "Transit", "Eclipse", "Phase-curve", "Direct Imaging",
    "Gaseous Planets", "Rocky Planets", "Sub-Neptunes",
    "Data Reduction", "Modeling", "Atmospheric Retrievals", "Ideas",
]
TAG_RULES = {  # tag -> regexes searched in title+abstract (case-insensitive)
    "JWST": [r"\bJWST\b", r"James Webb"],
    "HST": [r"\bHST\b", r"Hubble"],
    "CHEOPS": [r"\bCHEOPS\b"],
    "PLATO": [r"\bPLATO\b"],
    "HWO": [r"\bHWO\b", r"Habitable Worlds Observatory"],
    "Ariel": [r"\bAriel\b"],
    "Transit": [r"\btransit", r"transmission spectr"],
    "Eclipse": [r"\beclipse", r"emission spectr", r"\bdayside"],
    "Phase-curve": [r"phase[- ]curve"],
    "Direct Imaging": [r"direct(ly)? imag", r"white dwarf", r"brown dwarf"],
    "Gaseous Planets": [r"hot[- ]Jupiter", r"\bJupiter", r"gas giant", r"Saturn", r"giant planet"],
    "Rocky Planets": [r"rocky", r"super[- ]Earth", r"terrestrial", r"lava", r"magma"],
    "Sub-Neptunes": [r"sub[- ]Neptune", r"mini[- ]Neptune"],
    "Data Reduction": [r"data reduction", r"pipeline", r"systematic", r"light[- ]curve fit"],
    "Modeling": [r"simulation", r"\bmodel(l)?ing\b", r"radiative transfer", r"dynamics", r"\bGCM\b"],
    "Atmospheric Retrievals": [r"retriev"],
}
JOURNALS = {  # ADS bibstem -> display name used on the site
    "ApJ": "ApJ", "ApJL": "ApJL", "ApJS": "ApJS", "AJ": "AJ", "A&A": "A&A",
    "MNRAS": "MNRAS", "RNAAS": "RNAAS", "RASTI": "RASTI", "ExA": "ExA",
    "Natur": "Nature", "NatAs": "Nature Astronomy", "PASJ": "PASJ", "PASP": "PASP",
    "PSJ": "PSJ", "Icar": "Icarus", "FaDi": "Faraday Discuss.",
}
STOPWORDS = set("""a an the of on in for and with from to via by at as is are its into
towards toward using new first ii iii iv i ii. jwst hst ariel exoplanet exoplanets
exoplanetary atmosphere atmospheres atmospheric planet planets spectrum spectra study
analysis observations""".split())


# --------------------------------------------------------------------------- utils
def http_get(url: str, headers: dict | None = None, data: bytes | None = None,
             timeout: int = 60) -> bytes:
    h = {"User-Agent": USER_AGENT}
    h.update(headers or {})
    req = urllib.request.Request(url, headers=h, data=data)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 2:
                time.sleep(5 * (attempt + 1))
                continue
            raise
        except urllib.error.URLError:
            if attempt < 2:
                time.sleep(5)
                continue
            raise
    raise RuntimeError("unreachable")


def ascii_slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


def clean_text(s: str) -> str:
    """Strip HTML tags / simple LaTeX from ADS & arXiv abstracts."""
    s = html.unescape(s or "")
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\$([^$]*)\$", lambda m: m.group(1), s)             # $...$ -> ...
    s = re.sub(r"\\(rm|mathrm|textit|textbf|it|bf)\s*\{([^}]*)\}", r"\2", s)
    s = re.sub(r"\\(rm|mathrm|it|bf|textit|textbf)\b\s*", "", s)
    s = re.sub(r"_\{([^}]*)\}", r"\1", s).replace("_", "")
    s = re.sub(r"\^\{([^}]*)\}", r"^\1", s)
    s = s.replace("\\pm", "±").replace("\\sim", "~").replace("\\,", " ").replace("\\%", "%")
    s = s.replace("{", "").replace("}", "").replace("\\", "")
    return re.sub(r"\s+", " ", s).strip()


def yaml_sq(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def first_sentence(s: str, limit: int = 300) -> str:
    m = re.match(r"(.+?[.!?])(\s|$)", s)
    out = m.group(1) if m else s
    return out if len(out) <= limit else out[:limit].rsplit(" ", 1)[0] + "…"


# --------------------------------------------------------------------------- paper model
class Paper(dict):
    """keys: title, authors[list 'First Last'], date(YYYY-MM-DD), year, doi, arxiv,
    publication, abstract, bibcode, bibtex"""


def name_first_last(ads_name: str) -> str:
    # ADS: "Changeat, Quentin" -> "Quentin Changeat"
    if "," in ads_name:
        last, first = [x.strip() for x in ads_name.split(",", 1)]
        return f"{first} {last}".strip()
    return ads_name.strip()


def surname(full: str) -> str:
    return full.split()[-1] if full.split() else full


# --------------------------------------------------------------------------- sources
def fetch_ads(token: str, library: str) -> list[Paper]:
    fl = "bibcode,title,author,pubdate,year,doi,identifier,bibstem,volume,page,abstract,doctype"
    q = urllib.parse.urlencode({"q": f"docs(library/{library})", "fl": fl,
                                "rows": 500, "sort": "date desc"})
    hdr = {"Authorization": f"Bearer {token}"}
    docs = json.loads(http_get(f"{ADS_API}/search/query?{q}", hdr))["response"]["docs"]
    papers = []
    for d in docs:
        arx = next((i.split(":", 1)[1] for i in d.get("identifier", [])
                    if i.lower().startswith("arxiv:")), "")
        pubdate = d.get("pubdate", f"{d.get('year', '2000')}-01-00")
        y, m, _ = (pubdate + "-00-00").split("-")[:3]
        date = f"{y}-{m if m != '00' else '01'}-01"
        stem = (d.get("bibstem") or [""])[0]
        doi = (d.get("doi") or [""])[0]
        if stem == "arXiv" or not stem:
            publication = f"arxiv:{arx}" if arx else "preprint"
            doi = doi or (f"10.48550/arXiv.{arx}" if arx else "")
        else:
            j = JOURNALS.get(stem, stem)
            vol, page = d.get("volume", ""), (d.get("page") or [""])[0]
            sep = ", " if j == "A&A" else " "
            publication = f"{j} {vol}{sep}{page}".strip()
        papers.append(Paper(
            title=clean_text((d.get("title") or [""])[0]),
            authors=[name_first_last(a) for a in d.get("author", [])],
            date=date, year=y, doi=doi, arxiv=arx, publication=publication,
            abstract=clean_text(d.get("abstract", "")), bibcode=d["bibcode"], bibtex=""))
    # BibTeX in one call
    if papers:
        body = json.dumps({"bibcode": [p["bibcode"] for p in papers]}).encode()
        bib = json.loads(http_get(f"{ADS_API}/export/bibtex",
                                  {**hdr, "Content-Type": "application/json"}, body))["export"]
        entries = re.split(r"\n(?=@)", bib.strip())
        for p in papers:
            key = p["bibcode"]
            p["bibtex"] = next((e for e in entries if key in e.split("\n", 1)[0]), "")
    return papers


def fetch_arxiv(query: str, max_results: int = 60) -> list[Paper]:
    q = urllib.parse.urlencode({"search_query": query, "sortBy": "submittedDate",
                                "sortOrder": "descending", "max_results": max_results})
    root = ET.fromstring(http_get(f"{ARXIV_API}?{q}"))
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    out = []
    for e in root.findall("a:entry", ns):
        aid = re.sub(r"v\d+$", "", e.findtext("a:id", "", ns).split("/abs/")[-1])
        authors = [a.findtext("a:name", "", ns) for a in e.findall("a:author", ns)]
        pos = next((i for i, a in enumerate(authors) if ADMIN_SURNAME in a.lower()), 99)
        if not (len(authors) <= ARXIV_MAX_AUTHORS or pos < ARXIV_MAX_POSITION):
            continue
        date = e.findtext("a:published", "", ns)[:10]
        jref = (e.findtext("x:journal_ref", "", ns) or "").strip()
        doi = (e.findtext("x:doi", "", ns) or "").strip() or f"10.48550/arXiv.{aid}"
        title = clean_text(e.findtext("a:title", "", ns))
        p = Paper(title=title, authors=authors, date=date, year=date[:4], doi=doi,
                  arxiv=aid, publication=jref or f"arxiv:{aid}",
                  abstract=clean_text(e.findtext("a:summary", "", ns)), bibcode="")
        last = ascii_slug(surname(authors[0])).capitalize()
        p["bibtex"] = (
            f"@ARTICLE{{{last}{date[:4]}_{aid.replace('.', '')},\n"
            f"       author = {{{' and '.join(authors)}}},\n"
            f"        title = \"{{{title}}}\",\n"
            f"      journal = {{arXiv e-prints}},\n"
            f"         year = {date[:4]},\n"
            f"          doi = {{{doi}}},\n"
            f"archivePrefix = {{arXiv}},\n"
            f"       eprint = {{{aid}}}\n}}")
        out.append(p)
    return out


# --------------------------------------------------------------------------- existing site
def scan_existing(pubdir: Path) -> tuple[set, set, set, dict]:
    """Return (arxiv_ids, dois, normalised titles, surname->profile_id)."""
    arx, dois, titles, profiles = set(), set(), set(), {ADMIN_SURNAME: "admin"}
    for d in pubdir.iterdir():
        if not d.is_dir():
            continue
        text = ""
        for f in ("index.md", "cite.bib"):
            if (d / f).exists():
                text += (d / f).read_text(errors="ignore") + "\n"
        arx |= set(re.findall(r"(\d{4}\.\d{4,5})", text))
        dois |= {x.lower() for x in re.findall(r"(10\.\d{4,9}/[^\s\"'}]+)", text)}
        m = re.search(r'^title:\s*"(.*)"', text, re.M)
        if m:
            titles.add(ascii_slug(m.group(1))[:60])
        # authors given as bare lowercase ids (e.g. "- bonhof") are site profiles
        block = re.search(r"^authors:\n((?:- .*\n)+)", text, re.M)
        if block:
            for a in re.findall(r"- (.*)", block.group(1)):
                a = a.strip()
                if re.fullmatch(r"[a-z0-9_-]+", a) and a != "admin":
                    profiles[a] = a
    return arx, dois, titles, profiles


def paper_key(p: Paper) -> str:
    return p.get("arxiv") or p.get("bibcode") or p.get("doi")


def already_on_site(p: Paper, arx, dois, titles) -> bool:
    if p.get("arxiv") and p["arxiv"] in arx:
        return True
    if p.get("doi") and p["doi"].lower() in dois:
        return True
    return ascii_slug(p["title"])[:60] in titles


# --------------------------------------------------------------------------- rendering
def site_authors(authors: list[str], profiles: dict) -> list[str]:
    def conv(a):
        s = ascii_slug(surname(a))
        return profiles.get(s, a)
    conv_all = [conv(a) for a in authors]
    if len(conv_all) <= MAX_LISTED_AUTHORS:
        return conv_all
    out = conv_all[:5]
    if "admin" in conv_all and "admin" not in out:
        out.append("admin")
    return out + ["et al."]


def guess_tags(p: Paper) -> list[str]:
    text = f"{p['title']} {p['abstract']}"
    tags = [t for t, pats in TAG_RULES.items()
            if any(re.search(x, text, re.I) for x in pats)]
    return [t for t in ALLOWED_TAGS if t in tags] or ["Ideas"]


def folder_name(p: Paper, pubdir: Path) -> str:
    last = ascii_slug(surname(p["authors"][0])) or "paper"
    words = [w for w in re.findall(r"[A-Za-z0-9\-]+", p["title"])]
    # prefer a planet name (WASP-121b, K2-18, TOI-270 ...) else first non-stopword
    planet = next((w for w in words if re.match(r"(WASP|HAT|KELT|TOI|K2|GJ|LHS|TRAPPIST|Kepler|HD|XO|TrES|LTT)-?\d", w, re.I)), None)
    kw = planet or next((w for w in words if w.lower() not in STOPWORDS and len(w) > 3), "paper")
    base = f"{last}{p['year']}_{re.sub(r'[^A-Za-z0-9]', '', kw).lower()}"
    name, i = base, 2
    while (pubdir / name).exists():
        name, i = f"{base}{i}", i + 1
    return name


TEMPLATE = """---
title: "{title}"
authors:
{authors}
#author_notes:
#- "Equal contribution"
#- "Equal contribution"
date: "{date}T00:00:00Z"
doi: "{doi}"

# Schedule page publish date (NOT publication's date).
publishDate: "{date}T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "{publication}"
publication_short: ""

abstract: {abstract}

# Summary. An optional shortened abstract.
# AUTO-GENERATED (first sentence of the abstract) -- please rewrite.
summary: {summary}


### TAGS TO USE:
# JWST, HST, CHEOPS, PLATO, HWO, Ariel
# Transit, Eclipse, Phase-curve, Direct Imaging,
# Gaseous Planets, Rocky Planets, Sub-Neptunes,
# Data Reduction, Modeling, Atmospheric Retrievals, Ideas
# AUTO-GENERATED from keywords -- please check.
tags:
{tags}
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: '{url_pdf}'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: {caption}
  focal_point: "Center"
  placement: 2
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
"""


def render_index(p: Paper, profiles: dict, caption: str) -> str:
    return TEMPLATE.format(
        title=p["title"].replace('"', "'"),
        authors="\n".join(f"- {a}" for a in site_authors(p["authors"], profiles)),
        date=p["date"], doi=p["doi"], publication=p["publication"].replace('"', "'"),
        abstract=yaml_sq(p["abstract"]), summary=yaml_sq(first_sentence(p["abstract"])),
        tags="\n".join(f"- {t}" for t in guess_tags(p)),
        url_pdf=f"https://arxiv.org/pdf/{p['arxiv']}" if p.get("arxiv") else "",
        caption=yaml_sq(caption))


# --------------------------------------------------------------------------- figures
class _FigParser(HTMLParser):
    """Collect <figure class="ltx_figure"> blocks: their <img src> / <object data>
    (arXiv HTML uses both; vector figures come as SVG <object>s) and captions."""

    def __init__(self):
        super().__init__()
        self.depth = 0
        self.figs: list[dict] = []
        self._cap = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class") or ""
        if tag == "figure":
            if self.depth == 0 and "ltx_figure" in cls and "ltx_table" not in cls:
                self.figs.append({"srcs": [], "caption": ""})
                self.depth = 1
            elif self.depth:
                self.depth += 1                     # nested sub-figure panels
        elif self.depth and tag == "img" and a.get("src"):
            self.figs[-1]["srcs"].append(a["src"])
        elif self.depth and tag == "object" and a.get("data"):
            self.figs[-1]["srcs"].append(a["data"])
        elif self.depth and tag == "figcaption" and self._cap is None:
            self._cap = []

    def handle_endtag(self, tag):
        if tag == "figure" and self.depth:
            self.depth -= 1
        elif tag == "figcaption" and self._cap is not None:
            if not self.figs[-1]["caption"]:
                self.figs[-1]["caption"] = re.sub(r"\s+", " ", "".join(self._cap)).strip()
            self._cap = None

    def handle_data(self, data):
        if self._cap is not None:
            self._cap.append(data)


def svg_to_png(svg: Path) -> Path | None:
    """Convert an SVG to PNG with whatever is available: cairosvg, rsvg-convert,
    inkscape, or macOS Quick Look (qlmanage). Returns the PNG path or None."""
    png = svg.with_suffix(".png")
    try:
        import cairosvg  # type: ignore
        cairosvg.svg2png(url=str(svg), write_to=str(png), output_width=1600)
        return png
    except Exception:
        pass
    import shutil, subprocess, tempfile
    cmds = []
    if shutil.which("rsvg-convert"):
        cmds.append(["rsvg-convert", "-w", "1600", "-o", str(png), str(svg)])
    if shutil.which("inkscape"):
        cmds.append(["inkscape", str(svg), "--export-type=png", "-w", "1600",
                     f"--export-filename={png}"])
    for cmd in cmds:
        if subprocess.run(cmd, capture_output=True).returncode == 0 and png.exists():
            return png
    if shutil.which("qlmanage"):                       # macOS built-in
        with tempfile.TemporaryDirectory() as td:
            subprocess.run(["qlmanage", "-t", "-s", "1600", "-o", td, str(svg)],
                           capture_output=True)
            out = Path(td) / (svg.name + ".png")
            if out.exists():
                shutil.move(str(out), png)
                return png
    return None


def fetch_figures(arxiv_id: str, outdir: Path, n: int) -> str:
    """Download up to n figures from the arXiv HTML render (largest panel of each
    figure). The first becomes featured.*, the others candidate_figN.*.
    Returns the caption of the featured figure, or '' if none."""
    if not arxiv_id:
        return ""
    page_url = f"https://arxiv.org/html/{arxiv_id}"   # NB: no trailing slash —
    try:                                              # srcs look like '<id>v1/fig.png'
        page = http_get(page_url).decode("utf-8", "ignore")
    except Exception as e:
        print(f"     no arXiv HTML version ({e.__class__.__name__})")
        return ""
    parser = _FigParser()
    parser.feed(page)
    saved, featured_caption = 0, ""
    for fig in parser.figs:
        best = None                                    # (size, data, ext)
        for src in fig["srcs"]:
            m = re.search(r"\.(png|jpe?g|svg)$", src, re.I)
            if not m:
                continue
            try:
                data = http_get(urllib.parse.urljoin(page_url, src))
            except Exception:
                continue
            ext = "." + m.group(1).lower().replace("jpeg", "jpg")
            if ext != ".svg" and len(data) < 15_000:  # skip logos / tiny panels
                continue
            if best is None or len(data) > best[0]:
                best = (len(data), data, ext)
        if best is None:
            continue
        _, data, ext = best
        name = "featured" if saved == 0 else f"candidate_fig{saved + 1}"
        target = outdir / f"{name}{ext}"
        target.write_bytes(data)
        if ext == ".svg":                              # Hugo can't resize SVGs
            png = svg_to_png(target)
            target.unlink()
            if png is None:
                print("     (skipped an SVG figure: install `pip install cairosvg` to convert)")
                continue
        if saved == 0:
            featured_caption = re.sub(r"^Figure\s*\d+[:.]?\s*", "", fig["caption"])
        saved += 1
        if saved >= n:
            break
    print(f"     saved {saved} figure(s)")
    return featured_caption


def fill_missing_figures(pubdir: Path, n: int):
    """For existing folders without featured.*: fetch figures and fill an empty caption."""
    for d in sorted(x for x in pubdir.iterdir() if x.is_dir()):
        if any(d.glob("featured.*")) or not (d / "index.md").exists():
            continue
        text = (d / "index.md").read_text()
        m = re.search(r"arxiv\.org/(?:pdf|abs)/(\d{4}\.\d{4,5})", text) or \
            re.search(r"arXiv\.(\d{4}\.\d{4,5})", text)
        if not m:
            m = re.search(r"eprint\s*=\s*\{(\d{4}\.\d{4,5})\}",
                          (d / "cite.bib").read_text() if (d / "cite.bib").exists() else "")
        if not m:
            print(f"  - {d.name}: no arXiv id, skipped")
            continue
        print(f"  * {d.name} ({m.group(1)})")
        cap = fetch_figures(m.group(1), d, n)
        if cap and re.search(r"^  caption: ''\s*$", text, re.M):
            first = re.search(r"^authors:\n- (.*)$", text, re.M)
            credit = ""
            if first and first.group(1) not in ("admin", "et al."):
                nm = first.group(1).split()
                credit = f" -- Image credit: {nm[0][0]}. {nm[-1]}" if len(nm) > 1 else ""
            elif first and first.group(1) == "admin":
                credit = " -- Image credit: Q. Changeat"
            new_cap = yaml_sq(first_sentence(cap, 120).rstrip(".") + credit)
            text = re.sub(r"^  caption: ''\s*$", lambda _: f"  caption: {new_cap}",
                          text, count=1, flags=re.M)
            (d / "index.md").write_text(text)


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pubdir", default=str(Path(__file__).resolve().parent / "publication"))
    ap.add_argument("--source", choices=["ads", "arxiv"], default=None,
                    help="default: ads if ADS_API_TOKEN is set, otherwise arxiv")
    ap.add_argument("--library", default=LIBRARY_ID)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-figures", action="store_true")
    ap.add_argument("--figures", type=int, default=N_CANDIDATE_FIGS,
                    help="max figures to download per paper (1st becomes featured)")
    ap.add_argument("--include-seen", action="store_true",
                    help="also re-propose papers whose folder you deleted earlier")
    ap.add_argument("--fill-figures", action="store_true",
                    help="only download figures for existing folders that have no featured image")
    ap.add_argument("--since", type=int, default=None,
                    help="only consider papers from this year onwards (e.g. 2024)")
    ap.add_argument("--forget", nargs="*", default=[],
                    help="remove arXiv ids / bibcodes from the 'seen' list and exit")
    args = ap.parse_args()

    pubdir = Path(args.pubdir)
    if not pubdir.is_dir():
        sys.exit(f"publication folder not found: {pubdir}")
    seen_file = pubdir / ".autopub_seen.json"
    seen = set(json.loads(seen_file.read_text())) if seen_file.exists() else set()

    if args.forget:
        seen -= set(args.forget)
        seen_file.write_text(json.dumps(sorted(seen), indent=1))
        print(f"forgot {len(args.forget)} id(s)")
        return

    if args.fill_figures:
        fill_missing_figures(pubdir, args.figures)
        return

    token = os.environ.get("ADS_API_TOKEN") or os.environ.get("ADS_TOKEN")
    source = args.source or ("ads" if token else "arxiv")
    if source == "ads":
        if not token:
            sys.exit("Set ADS_API_TOKEN (get one at https://scixplorer.org/user/settings/token)")
        print(f"Reading SciX/ADS library {args.library} …")
        papers = fetch_ads(token, args.library)
    else:
        print(f"Querying arXiv ({ARXIV_AUTHOR_QUERY}) …")
        papers = fetch_arxiv(ARXIV_AUTHOR_QUERY)
    print(f"  {len(papers)} paper(s) in source")

    arx, dois, titles, profiles = scan_existing(pubdir)
    new = []
    for p in papers:
        if not p["authors"] or not p["title"]:
            continue
        if args.since and int(p["year"] or 0) < args.since:
            continue
        if already_on_site(p, arx, dois, titles):
            seen.add(paper_key(p))
            continue
        if paper_key(p) in seen and not args.include_seen:
            continue
        new.append(p)

    if not new:
        print("Nothing new — the site is up to date.")
    for p in new:
        name = folder_name(p, pubdir)
        print(f"  + {name}: {p['title'][:90]}  [{p['publication']}]")
        if args.dry_run:
            continue
        d = pubdir / name
        d.mkdir()
        caption = ""
        if not args.no_figures:
            figcap = fetch_figures(p.get("arxiv", ""), d, args.figures)
            if figcap:
                fa = p["authors"][0]
                credit = "Q. Changeat" if ADMIN_SURNAME in fa.lower() else \
                    f"{fa.split()[0][0]}. {surname(fa)}"
                caption = f"{first_sentence(figcap, 120).rstrip('.')} -- Image credit: {credit}"
        (d / "index.md").write_text(render_index(p, profiles, caption))
        (d / "cite.bib").write_text((p.get("bibtex") or "").strip() + "\n")
        seen.add(paper_key(p))

    if not args.dry_run:
        seen_file.write_text(json.dumps(sorted(seen), indent=1))
        if new:
            print(f"\nCreated {len(new)} folder(s). Review summary/tags/caption, pick a "
                  f"featured image (rename a candidate_fig*), delete candidates you don't use, "
                  f"and delete any folder you don't want — it won't be re-created.")


if __name__ == "__main__":
    main()
