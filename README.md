# Physical Layer Writer

A ghostwriting skill for investigative analysis and systems-intelligence briefs: structured
interview, claim gates, fixed post structure, and a pre-publication check.

## Layout

| Path | Read at | Contents |
|---|---|---|
| `SKILL.md` | activation | trigger, forbidden patterns, hard rules, the eight stages |
| `references/voice-guide.md` | Stage 2 | voice model, opening and closing patterns, ten-point binary checklist, interview question bank |
| `references/post-structure.md` | Stages 3 and 5 | interview extraction, the nine-part post structure and the correction-issue structure |
| `references/claims-and-risk.md` | Stages 4 and 6 | property gates, fact check, risk scoring |
| `references/prepublication.md` | Stages 7 and 8 | the half of the final check that needs judgement |
| `references/publishing-surfaces.md` | Stage 8 | Substack mechanics, per-surface distribution rules |
| `scripts/check_prepublication.py` | executed | the mechanical half of the check |
| `scripts/fixtures/` | executed | inputs and recorded output for the checker |

## The checker

```bash
python3 scripts/check_prepublication.py --list                      # what it checks
python3 scripts/check_prepublication.py posts/postNN/article_en.md  # one file
python3 scripts/check_prepublication.py posts/postNN/               # the publishable prose in a post
```

Exits nonzero on any failure. `--list` is the only inventory of the mechanical rules.

Run it at Stage 7 on the draft and again after Stage 8 on the files that ship: Stage 8 produces the
Substack variant and the distribution copy, which carry their own checks.

After changing the checker, re-run the fixtures and regenerate their recorded output in the same
commit. See `scripts/fixtures/README.md`.

## Post directories

Each post lives in `posts/postNN/`: `article.md` or `article_en.md` (final text),
`FACT_CHECK_AUDIT.md` (per-claim verification), `RISK_SCORING.md` (per-claim risk),
`SOURCES.md` (archive log), and `sources/` (local copies).

Shared assets in `posts/_shared/`: `PUBLISH_CHECKLIST.md`, `RISK_SCORING_FRAMEWORK.md`,
`METHODOLOGY.md`, `archive_sources.js`.

---

*Based on [Founder Voice Ghostwriter](https://github.com/BayramAnnakov/founder-voice-ghostwriter)
by [Bayram Annakov](https://linkedin.com/in/bayramannakov). Adapted for investigative analysis and
systems intelligence.*
