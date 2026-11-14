#!/usr/bin/env python3
"""
Replace abbreviated author first names on the QCrypt 2026 site with full names.

The HotCRP export used for the 2026 accepted talks and posters only contained initials
("U. Girish"). This script takes the full given names from the private author export
(private_data/qcrypt2026-authors.csv, not in git) and writes them into:

- data/accepted-papers-2026.json
- data/posters-2026.json
- content/2026/sessions/contributed/<pid>.md (front matter and "## Authors" list)

Only given/family names are read from the CSV; emails and affiliations are never written.
Names are cleaned up (ALL CAPS, LaTeX accents, footnote digits, lowercase).
An author is only updated if the family name and initial match the CSV; everything that
could not be matched is reported and left unchanged.

Usage:
    python3 scripts/fill_full_names_2026.py --dry-run
    python3 scripts/fill_full_names_2026.py
"""

import argparse
import csv
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_FILE = ROOT / "private_data" / "qcrypt2026-authors.csv"
JSON_FILES = [ROOT / "data" / "accepted-papers-2026.json", ROOT / "data" / "posters-2026.json"]
SESSIONS_DIR = ROOT / "content" / "2026" / "sessions" / "contributed"

ROMAN = {"II", "III", "IV", "VI"}
COMBINING = {'"': "\u0308", "'": "\u0301", "´": "\u0301", "`": "\u0300", "^": "\u0302", "~": "\u0303"}


def fix_latex(s):
    """Turn LaTeX-style accents into real characters: H\\"{o}fer -> Höfer, Pi´etri -> Piétri."""
    s = re.sub(r'\\(["\'`^~])\{?([A-Za-z])\}?', lambda m: unicodedata.normalize("NFC", m.group(2) + COMBINING[m.group(1)]), s)
    s = re.sub(r"´([A-Za-z])", lambda m: unicodedata.normalize("NFC", m.group(1) + COMBINING["´"]), s)
    return s


def clean(name):
    """Clean a name from the CSV; returns the cleaned name."""
    name = fix_latex(" ".join(name.split()))
    name = re.sub(r"\d+$", "", name)
    if name and name == name.lower():
        name = " ".join(t[:1].upper() + t[1:] for t in name.split(" "))

    def untitle(token):
        if len(token) > 2 and token.isupper() and token not in ROMAN and "." not in token:
            return token.capitalize()
        return token

    return " ".join("-".join(untitle(p) for p in word.split("-")) for word in name.split(" "))


def norm(s):
    """Compare names ignoring accents, case and punctuation."""
    s = unicodedata.normalize("NFKD", fix_latex(s))
    return re.sub(r"[^a-z]", "", "".join(c for c in s if not unicodedata.combining(c)).lower())


def load_csv():
    papers, titles = defaultdict(list), {}
    with open(CSV_FILE, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            pid = int(row["paper"])
            titles[pid] = row["title"]
            author = (row["given_name"].strip(), row["family_name"].strip())
            if author not in papers[pid]:  # the export contains some authors twice
                papers[pid].append(author)
    return papers, titles


def matches(site, given, family):
    """True if a site author (with initials) is the CSV author given/family."""
    if not given or not site["first"]:
        return False
    initial_ok = norm(site["first"])[:1] == norm(given)[:1]
    if norm(site["last"]) == norm(family):
        return initial_ok
    # site split "S. Abdul" / "Sater" where the CSV has "Sami" / "Abdul Sater"
    rest = site["first"].split(None, 1)[1] if " " in site["first"] else ""
    return initial_ok and bool(rest) and norm(rest + site["last"]) == norm(family)


def new_name(site, given, family):
    """Full name for a matched author; keeps the site's family name unless it was split differently."""
    first = clean(given)
    last = clean(site["last"]) if norm(site["last"]) == norm(family) else clean(family)
    return first, last


def update_paper(paper, papers, titles, report):
    pid = paper["pid"]
    csv_authors = papers.get(pid, [])
    if not csv_authors or norm(titles[pid]) != norm(paper["title"]):
        by_title = [p for p, t in titles.items() if norm(t) == norm(paper["title"])]
        if not by_title:
            report.append(f"pid {pid}: not in CSV, left unchanged")
            return []
        report.append(f"pid {pid}: CSV row has a different title, matched by title to CSV paper {by_title[0]}")
        csv_authors = papers[by_title[0]]

    positional = len(csv_authors) == len(paper["authors"]) and all(
        matches(a, g, f) for a, (g, f) in zip(paper["authors"], csv_authors))
    changes = []
    for i, author in enumerate(paper["authors"]):
        if positional:
            given, family = csv_authors[i]
        else:
            found = [(g, f) for g, f in csv_authors if matches(author, g, f)]
            if len(found) != 1:
                report.append(f"pid {pid}: no unique CSV match for '{author['first']} {author['last']}', left unchanged")
                continue
            given, family = found[0]
        first, last = new_name(author, given, family)
        if (first, last) != (author["first"], author["last"]):
            changes.append((i, first, last))
            if clean(given) != given or clean(family) != family:
                report.append(f"pid {pid}: cleaned '{given} {family}' -> '{first} {last}'")
    return changes


def rewrite_json(path, changes_by_index, ensure_ascii):
    """Replace the first/last values in place so the rest of the file stays byte-identical."""
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(r'("(first|last)":\s*)("(?:[^"\\]|\\.)*")')
    counter = {"n": 0}

    def replace(m):
        idx = counter["n"] // 2
        counter["n"] += 1
        if idx in changes_by_index:
            first, last = changes_by_index[idx]
            value = first if m.group(2) == "first" else last
            return m.group(1) + json.dumps(value, ensure_ascii=ensure_ascii)
        return m.group(0)

    return pattern.sub(replace, text)


def rewrite_session(path, renames):
    """Rename authors in the front matter and in every "Authors" list (merged talks have several)."""
    text = path.read_text(encoding="utf-8")

    def front(m):
        name = json.loads(m.group(1))
        return f'  - {json.dumps(renames.get(name, name), ensure_ascii=False)}'

    text = re.sub(r"^authors:\n(?:  - .*\n)+", lambda b: re.sub(r'^  - (".*")$', front, b.group(0), flags=re.M),
                  text, count=1, flags=re.M)
    text = re.sub(r"^#+ Authors\n\n(?:- .*\n)+",
                  lambda b: re.sub(r"^- (.*)$", lambda m: "- " + renames.get(m.group(1), m.group(1)), b.group(0), flags=re.M),
                  text, flags=re.M)
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="only print what would change")
    args = parser.parse_args()

    papers, titles = load_csv()
    report, talks = [], defaultdict(dict)  # talk pid -> {old name: new name}
    for path in JSON_FILES:
        text = path.read_text(encoding="utf-8")
        data = json.loads(text)
        changes_by_index, idx = {}, 0
        for paper in data:
            changes = update_paper(paper, papers, titles, report)
            for i, first, last in changes:
                old = paper["authors"][i]
                print(f"pid {paper['pid']:>3}: {old['first']} {old['last']}  ->  {first} {last}")
                changes_by_index[idx + i] = (first, last)
                if "accepted-papers" in path.name:
                    talks[paper["pid"]][f"{old['first']} {old['last']}"] = f"{first} {last}"
                old["first"], old["last"] = first, last
            idx += len(paper["authors"])
        if not args.dry_run:
            new_text = rewrite_json(path, changes_by_index, ensure_ascii=text.isascii())
            assert json.loads(new_text) == data, f"{path}: rewrite does not match the updated data"
            path.write_text(new_text, encoding="utf-8")
        print(f"{path.relative_to(ROOT)}: {len(changes_by_index)} authors updated\n")

    for path in sorted(SESSIONS_DIR.glob("[0-9]*.md")):
        pid = int(path.stem)
        merged = re.search(r"^mergedwith: (\d+)$", path.read_text(encoding="utf-8"), re.M)
        renames = {**talks.get(int(merged.group(1)), {}), **talks.get(pid, {})} if merged else talks.get(pid, {})
        if not renames:
            report.append(f"{path.name}: no entry in accepted-papers-2026.json, left unchanged")
            continue
        if not args.dry_run:
            path.write_text(rewrite_session(path, renames), encoding="utf-8")

    print("Report:")
    for line in report:
        print("  " + line)


if __name__ == "__main__":
    main()
