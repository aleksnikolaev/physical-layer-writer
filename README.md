# Physical Layer Writer

A ghostwriting skill for investigative analysis and systems-intelligence briefs: structured
interview, claim gates, fixed post structure, and a pre-publication check.

Documentation for a person. Nothing here is loaded at runtime.

## Layout

| Path | Loaded | Contents |
|---|---|---|
| `SKILL.md` | every activation | trigger, forbidden patterns, hard rules, eight stages that route to the rest |
| `references/voice-guide.md` | Stage 2 | voice model, opening and closing patterns, ten-point binary checklist, interview question bank |
| `references/post-structure.md` | Stages 3 and 5 | interview extraction, the fixed five-part structure |
| `references/claims-and-risk.md` | Stages 4 and 6 | property gates, fact check, risk scoring |
| `references/prepublication.md` | Stage 7 | the half of the final check that needs judgement |
| `references/publishing-surfaces.md` | Stage 8 | Substack mechanics, per-surface distribution rules |
| `scripts/check_prepublication.py` | never, it is executed | the mechanical half of the check |
| `scripts/fixtures/` | never | inputs and recorded output for the checker |

Only `SKILL.md` costs context on every run. A reference is opened by the stage that names it.

## The checker

```bash
python3 scripts/check_prepublication.py --list                      # what it checks
python3 scripts/check_prepublication.py posts/postNN/article_en.md  # one file
python3 scripts/check_prepublication.py posts/postNN/               # the publishable prose in a post
```

Exits nonzero on any failure. `--list` is the only inventory of the mechanical rules;
`references/prepublication.md` deliberately does not restate them, because two restatements drifted
apart twice and both defects reached review.

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
