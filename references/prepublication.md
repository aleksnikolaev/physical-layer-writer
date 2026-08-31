# Pre-publication check

Read this at Stage 7 on the draft, and again after Stage 8 on the files that ship.

One order, both times: the evidence gate below, then `scripts/check_prepublication.py`, then the
practitioner-named markers. The gate comes first because a failing required check is a stop and
there is no point scoring punctuation on a piece that cannot ship.

If no file is named, check the publishable prose in the current post directory: `article*.md`,
`reddit_*.md`, `twitter_*.md`. The audit records (`FACT_CHECK_AUDIT.md`, `RISK_SCORING.md`,
`SOURCES.md`) are not prose and are not checked as prose. They are what the evidence gate reads.

### Evidence gate, main articles only

Run the 10-Point Binary Checklist in `voice-guide.md`. It is the canonical list, do not restate it
here. A required check failing is a stop regardless of how the
mechanical pass scores: a source URL under every factual claim, own calculations labelled as model
or analysis, no motive imputed without a quote, a Limits and Confidence section, projections
hedged, and an audit trail (METHODOLOGY plus FACT_CHECK_AUDIT).

Stage 6 runs this gate too, but every stage after it permits edits: a refinement can introduce an
uncited claim, and Stage 8 can drop a required section while reflowing the text for a platform.
So the gate runs on each pass of this check, and the pass after Stage 8 is the one that sees what
actually ships. The mechanical checks cannot see any of it.

### Mechanical checks

Not listed here. They are implemented in `../scripts/check_prepublication.py` and inventoried by
that script itself:

```bash
python3 scripts/check_prepublication.py --list
python3 scripts/check_prepublication.py posts/postNN/article_en.md
```

Do not restate them here. One inventory, kept next to the code that runs.

### Practitioner-named markers, checked by hand

The four markers domain readers flag first are in Forbidden Patterns above. Do not restate them
here and do not copy them anywhere else, the copies drift apart. Check them separately and by
hand: the mechanical list catches punctuation, forbidden words, rhythm and self-promo, and it
caught none of what actually cost this channel a source. Two readers read the writing as
machine-made; one of them was the second-deepest expert contact of the channel and he left over
it. Verbatim threads stay in local project files and never enter this repository.

### Output

```
## Check: [filename]

### FAIL (fix before publish)
- [line N] Em-dash: "text — text" → "text. Text"
- [line N] Red line: "fraud"

### WARN
- [line N] "we have" → rephrase
- Sentences 12-14: uniform rhythm (18, 19, 17 words)

### PASS
- No exclamation marks, no emojis, no CTA
- Disclaimer present
- Links: N URLs, all full paths

Score: X FAIL / Y WARN / Z PASS
Verdict: PUBLISH / FIX FIRST
```

When checking a whole post directory, run against `article_en.md`, `article_substack.md`,
`article_ru.md`, every `reddit_*.md` and every `twitter_*.md`, report per file, then summarise.
