#!/usr/bin/env python3
"""Mechanical half of the Physical Layer pre-publication check.

Deterministic only. Everything requiring judgement (the evidence gate, the four
practitioner-named markers, whether a closing question can be answered from working
experience) lives in references/prepublication.md and is read by a human or an agent.
A green run here is not a verdict to publish.

Exit codes: 0 no FAIL, 1 at least one FAIL, 2 bad invocation.
"""
import argparse
import pathlib
import re
import sys

# anywhere in the line
FORBIDDEN_WORDS = [
    "unprecedented", "revolutionary", "game-changing", "game changing",
    "might potentially", "could perhaps",
]
# openers: matched only where a sentence starts. "the highest number in this article" is a
# legitimate self-reference; "In this article, we will" is not.
FORBIDDEN_OPENERS = [
    "In an era of", "In this article", "Here's the breakdown", "Here's what I found",
]
CTA = ["subscribe", "follow for more", "share this", "like and retweet", "подпишитесь"]
RED_LINES = ["fraud", "conspiracy", "cover-up", "coverup"]
ADVICE = [r"\byou should buy\b", r"\byou should sell\b", r"\binvest in\b"]
EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF⭐❤]"
)
URL = re.compile(r"https?://[^\s)\]<>\"']+")
# a heading, a list marker, or a table pipe is not prose
NON_PROSE = re.compile(r"^\s*(#{1,6}\s|[-*+]\s|\d+\.\s|\|)")

PUBLISHABLE = {"article", "social"}
ARTICLE = re.compile(r"^article.*\.md$")
SOCIAL = re.compile(r"^(reddit|twitter)_.*\.md$")
RECORDS = {"FACT_CHECK_AUDIT.md", "RISK_SCORING.md", "SOURCES.md", "METHODOLOGY.md"}


def classify(path):
    n = path.name
    if n in RECORDS:
        return "record"
    if ARTICLE.match(n):
        return "article"
    if SOCIAL.match(n):
        return "social"
    return "prose"


def strip_code(text):
    """Blank out fenced code so samples inside it are not flagged as prose."""
    out, fence = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
            out.append("")
            continue
        out.append("" if fence else line)
    return out


def sentences(lines):
    prose = " ".join(l for l in lines if l.strip() and not NON_PROSE.match(l))
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", prose) if s.strip()]


def check(path):
    raw = path.read_text(encoding="utf-8")
    lines = strip_code(raw)
    kind = classify(path)
    fails, warns, passes = [], [], []

    def hit(store, lineno, msg):
        store.append((lineno, msg))

    for n, line in enumerate(lines, 1):
        for ch, name in ((chr(0x2014), "em-dash"), (chr(0x2013), "en-dash")):
            if ch in line:
                hit(fails, n, f'{name}: "{line.strip()[:70]}"')
        if re.search(r"(?<!-)--(?!-)", line):
            hit(fails, n, f'double hyphen: "{line.strip()[:70]}"')
        if "!" in line and not NON_PROSE.match(line):
            hit(fails, n, f'exclamation mark: "{line.strip()[:70]}"')
        if EMOJI.search(line):
            hit(fails, n, "emoji")
        for w in FORBIDDEN_WORDS:
            if w.lower() in line.lower():
                hit(fails, n, f'forbidden: "{w}"')
        for w in FORBIDDEN_OPENERS:
            if re.search(rf"(?:^|(?<=[.!?])\s+|^[>*_#\s]*){re.escape(w)}", line, re.I):
                hit(fails, n, f'forbidden opener: "{w}"')
        for w in CTA:
            if w in line.lower():
                hit(fails, n, f'CTA / self-promo: "{w}"')
        for w in RED_LINES:
            if re.search(rf"\b{re.escape(w)}\b", line, re.I):
                hit(fails, n, f'red line: "{w}"')
        for pat in ADVICE:
            if re.search(pat, line, re.I):
                hit(fails, n, "red line: reads as investment advice")
        for m in re.finditer(r"\bwe\b", line, re.I):
            hit(warns, n, f'"we" at col {m.start() + 1}, rewrite unless a specific team action')

    if not any(chr(0x2014) in l or chr(0x2013) in l for l in lines):
        passes.append("no em-dashes or en-dashes")
    if not any(EMOJI.search(l) for l in lines):
        passes.append("no emoji")

    # rhythm: three consecutive sentences within five words of each other
    sent = sentences(lines)
    lengths = [len(s.split()) for s in sent]
    for i in range(len(lengths) - 2):
        w = lengths[i:i + 3]
        if max(w) - min(w) <= 5 and min(w) >= 8:
            warns.append((None, f"uniform rhythm, sentences {i+1}-{i+3}: {w} words"))
            break

    urls = URL.findall(raw)
    truncated = [u for u in urls if u.endswith(("...", "…"))]
    for u in truncated:
        fails.append((None, f"truncated URL: {u}"))
    bare_home = [u for u in urls if re.fullmatch(r"https?://[^/]+/?", u)]
    for u in bare_home:
        warns.append((None, f"link points at a homepage, not a page: {u}"))
    if urls and not truncated:
        passes.append(f"{len(urls)} URL{'s' if len(urls) != 1 else ''}, none truncated")

    if kind == "article":
        low = raw.lower()
        if "not a" not in low or "corrections and responses welcome" not in low:
            fails.append((None, "disclaimer incomplete: needs the 'not a domain expert' line "
                                "and 'Corrections and responses welcome' at the end"))
        else:
            passes.append("disclaimer present")
        tail = "\n".join([l for l in lines if l.strip()][-12:])
        if tail.count("?") < 2:
            fails.append((None, "closing: an article ends with two practitioner questions, "
                                f"found {tail.count('?')} question marks in the last lines"))
        else:
            passes.append("two closing questions present")

    if kind == "article" and "_substack" in path.name:
        for n, line in enumerate(lines, 1):
            if re.match(r"^\s*\|.*\|", line):
                hit(fails, n, "markdown table: Substack does not render tables, "
                              "convert to a structured list")
            if re.search(r"\[[^\]]+\]\([^)]+\)", line):
                hit(warns, n, "raw link syntax in the production file, "
                              "confirm it rendered before pasting")
            if re.search(r"\*\*[^*]+\*\*", line):
                hit(warns, n, "raw bold syntax in the production file, "
                              "confirm it rendered before pasting")

    if kind == "social":
        if path.name.startswith("twitter_"):
            for n, line in enumerate(lines, 1):
                body = line.strip()
                if body and not NON_PROSE.match(line) and len(body) > 280:
                    fails.append((n, f"tweet is {len(body)} characters, limit is 280"))

    if kind == "record":
        return kind, [], [], ["audit record, not prose: only the evidence gate reads this"]

    return kind, fails, warns, passes


def report(path, kind, fails, warns, passes):
    print(f"\n## Check: {path.name}  [{kind}]")
    print("\n### FAIL (fix before publish)")
    print("\n".join(f"- [line {n}] {m}" if n else f"- {m}" for n, m in fails) or "- none")
    print("\n### WARN")
    print("\n".join(f"- [line {n}] {m}" if n else f"- {m}" for n, m in warns) or "- none")
    print("\n### PASS")
    print("\n".join(f"- {m}" for m in passes) or "- none")
    print(f"\nScore: {len(fails)} FAIL / {len(warns)} WARN / {len(passes)} PASS")
    print("Verdict: " + ("FIX FIRST" if fails else "MECHANICAL PASS"))


def collect(target):
    p = pathlib.Path(target)
    if p.is_file():
        return [p]
    if p.is_dir():
        return [f for f in sorted(p.glob("*.md")) if classify(f) in PUBLISHABLE]
    print(f"not found: {target}", file=sys.stderr)
    sys.exit(2)


INVENTORY = """Mechanical checks implemented here. This is the only inventory of them.
Everything needing judgement is in references/prepublication.md.

  dashes         em-dash, en-dash, double hyphen                          FAIL
  words          unprecedented, revolutionary, game-changing,
                 might potentially, could perhaps                         FAIL
  openers        In an era of, In this article, Here's the breakdown,
                 Here's what I found, at a sentence start only            FAIL
  punctuation    exclamation marks, emoji                                 FAIL
  cta            subscribe, follow for more, share this, like and
                 retweet                                                  FAIL
  red lines      fraud, conspiracy, cover-up; investment advice           FAIL
                 (client names, private life, categorical prediction
                 are NOT readable here, a person checks those)
  we             every \\bwe\\b occurrence                                  WARN
  rhythm         3 consecutive sentences within 5 words                   WARN
  links          truncated URL                                            FAIL
                 link to a homepage rather than a page                    WARN
  articles       disclaimer complete, two closing questions               FAIL
  substack       pipe tables in *_substack.md                             FAIL
                 raw link and bold syntax there                           WARN
  tweets         over 280 characters in twitter_*.md                      FAIL
  records        FACT_CHECK_AUDIT, RISK_SCORING, SOURCES, METHODOLOGY
                 are skipped, they are not prose
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("target", nargs="?", help="a file, or a post directory")
    ap.add_argument("--list", action="store_true",
                    help="print the mechanical checks this script implements, then exit")
    a = ap.parse_args()
    if a.list:
        print(INVENTORY)
        return
    if not a.target:
        ap.error("give a file or a directory, or --list")
    files = collect(a.target)
    if not files:
        print("nothing to check: no publishable prose found", file=sys.stderr)
        sys.exit(2)
    worst = 0
    for f in files:
        kind, fails, warns, passes = check(f)
        report(f, kind, fails, warns, passes)
        worst = max(worst, 1 if fails else 0)
    print("\nThe judgement half of the check is in references/prepublication.md. "
          "A green run here is not a verdict.")
    sys.exit(worst)


if __name__ == "__main__":
    main()
