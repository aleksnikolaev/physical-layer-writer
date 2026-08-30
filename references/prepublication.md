# Pre-publication check

Read this at Stage 7, before Stage 8, and whenever the author asks to check a post.
The mechanical part of it is also implemented as `scripts/check_prepublication.py`, run the
script first and read this file for everything the script cannot see.

Run this against every file before publishing. It lives here, in this skill. There is no separate
checker skill to invoke and no second copy of these rules anywhere.

If no file is named, check the publishable prose in the current post directory: `article*.md`,
`reddit_*.md`, `twitter_*.md`. The audit records (`FACT_CHECK_AUDIT.md`, `RISK_SCORING.md`,
`SOURCES.md`) are not prose and are not checked as prose. They are what the evidence gate reads.

### Evidence gate, main articles only

Run the 10-Point Binary Checklist in `references/voice-guide.md` before anything below. It is the
canonical list, do not restate it here. A required check failing is a stop regardless of how the
mechanical pass scores: a source URL under every factual claim, own calculations labelled as model
or analysis, no motive imputed without a quote, a Limits and Confidence section, projections
hedged, and an audit trail (METHODOLOGY plus FACT_CHECK_AUDIT).

Stage 6 runs this gate too, but Stage 7 permits edits afterwards. A refinement can introduce an
uncited claim or delete a required section, so the gate runs again here, last, on the text that
actually ships. The mechanical checks below cannot see any of it.

### Mechanical checks

1. **Dashes.** Search for the em-dash `—` (U+2014) everywhere, titles and closing lines included.
   Replace with a period, a comma, or parentheses. Search the en-dash `–` (U+2013) and the double
   hyphen `--` in the same pass, they arrive as substitutes.
2. **Forbidden words.** `unprecedented`, `revolutionary`, `game-changing`, `In an era of`,
   `In this article`, `might potentially`, `could perhaps`, exclamation marks, emojis. See
   Forbidden Patterns above for the full list and the reasoning.
3. **"We" audit.** Search `\bwe\b`. Keep it only for a specific team action ("we deployed").
   Generic use ("we have", "we can see", "we need") gets rewritten to passive or to what the data
   shows.
4. **Uniform rhythm.** Three or more consecutive sentences within five words of each other is the
   single most common machine fingerprint. Break one long sentence, combine two short ones.
5. **CTA and self-promo.** No "Subscribe", "Follow for more", "Share this", "Like and retweet".
   The piece closes with two practitioner questions. Reddit posts may carry an engagement
   question, a thread may link the article, nothing else.
6. **Raw markdown in Substack files.** In `*_substack.md`, check for table syntax, unrendered
   `[text](url)`, and bold that Substack will not render.
7. **Link integrity.** Every URL full, not truncated, pointing at a specific page rather than a
   homepage. Repeated links to the same source are not a defect: one report legitimately carries
   several claims, and every claim needs its own URL. Source concentration is the Stage 4 gate's
   job, not this one.
8. **Disclaimer.** Main articles only: present at the top, states the author is not a domain
   expert, states the piece is commentary and analysis rather than expert assessment, and carries
   "Corrections and responses welcome" at the bottom.
9. **Red lines.** Scan for accusations of crime (fraud, conspiracy, cover-up), investment advice
   (buy, sell, invest in), names of clients or of any company from the author's commercial work,
   private life details of an individual, and categorical prediction ("WILL collapse"). Any hit is
   a stop, not a warning, and the script exits nonzero on it.

   The script only reads the first two of those five. Client names, private life details and
   categorical prediction need a person: they cannot be told from a word list. A green run says
   nothing about them.
10. **Closing questions, main articles only.** Social copy is governed by check 5 instead: a
    Reddit post may close on a single engagement question, a thread may simply link the article.
    An article ends with two questions to practitioners. Fail when the
    closing is only a generic invitation or a resonant line with no question after it, and when a
    question can be answered with an opinion rather than from working experience. Warn when a
    question does not name the specific thing the author looked for and could not find. For each
    question, take two or three plausible answers and say what the author does next. An answer that
    leaves no next move means the question ships without a follow-up.

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
