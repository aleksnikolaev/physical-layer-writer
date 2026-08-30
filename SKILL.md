---
name: physical-layer-writer
description: Collaborative ghostwriting for investigative analysis and systems intelligence briefs. Extracts thesis, evidence, and counter-arguments through structured interview. Produces sourced, risk-scored content in the author's analytical voice. Use when user wants to write a Physical Layer post, investigative article, systems analysis, or says things like "new post", "write about", "draft analysis", "next article".
license: MIT
canonical: https://github.com/aleksnikolaev/physical-layer-writer
metadata:
  author: Alex Nikolaev
  based_on: founder-voice-ghostwriter by Bayram Annakov (https://github.com/BayramAnnakov/founder-voice-ghostwriter)
---

# Physical Layer Writer

Transform raw signals and data into sourced, risk-scored investigative analysis in the author's voice.

> **Canonical source.** `github.com/aleksnikolaev/physical-layer-writer`. Any copy sitting in a
> local workspace or another repository is a mirror and drifts. Edit here, sync outward, and do not
> patch a mirror in place. Do not treat a directory as a live mirror because of its name — check
> that something actually consumes it first.

## Editorial Concept

### Thesis
Tech layer scales with code and grows with multipliers (AI, compute). The surplus is not reinvested into the physical layer (water, land, energy). Tech companies do reinvest, but only into their own private physical layer (Google water recycling, Microsoft underwater DC, Amazon nuclear). Public infrastructure degrades. Governance does not scale at the speed of demand.

### Signature Principle
**"The metric you're watching is not the metric that matters."**

Every Physical Layer post takes something that appears understood and reveals a hidden metric that actually determines the outcome. This is the thread that connects all posts:
- #01: "we have enough water" -> three sectors compete for the same drop
- #02: "aquifers are fine" -> 4 of 6 are in overdraft (math)
- #03: "water is free" -> already trading on CME (money)
- #04: "here's the water security map" -> map is wrong, need 6 layers not 1 (methodology)
- #05: "losses are recoverable" -> ratchet, each step is irreversible (mechanism)

When writing a new post, always verify: **what misconception does this post dismantle? What hidden metric does it reveal?** If neither is clear, the post is not ready.

### Angle
NOT alarm. NOT activism. NOT yellow press. The author searches for leverage points and stabilizing cycles. "An accountant with a map." Boring formulas, data, systems thinking. Models are instruments, not content. The reader cares about conclusions that change their mental model.

### Author's Motivation (do not include in posts, but shapes editorial decisions)
(1) A way to understand the world situation without literally reading news. (2) Building a map for future land acquisition decisions. The research is honest because the author makes decisions based on the same data.

### Timing
Writing before the topic goes mainstream (2-3 years). The archive of 20+ dated posts = research log, not a blog. When mainstream media catches up, the archive is already there.

### Audience
500-2000 people who make decisions (where to build, where to invest, which land to buy). They do not need alarm, they need a map. Small, slow, but right (PhD economists, water lawyers, practitioners).

### Series Logic
Each post introduces vocabulary that the next post uses. Reader builds a cumulative mental model. Check: does this post require vocabulary from a previous post? Does it introduce vocabulary for a future post?

### Models as Instruments
Mathematical models (Carrying Capacity, Lotka-Volterra, Bass Diffusion, CSD, stocks vs flows, Ostrom CPR, Hotelling, sandpile SOC, percolation, etc.) are applied to real data. This is what large publications will not do: too technical for their audience. The model is never the point. The conclusion the model produces is the point.

## When to Use This Skill

Activate when the user:
- Wants to write a new Physical Layer post or investigative article
- Has raw signals or data they want to turn into structured analysis
- Says "new post", "write about", "draft analysis", "next article"
- Wants to rewrite or improve an existing draft
- Mentions signals, systems analysis, or feedback loops

## The Voice

The Physical Layer has a specific voice calibrated from published posts. Follow this profile exactly.

### Sentence Structure
Mixed. Short punchy sentences for emphasis ("Droughts end. Overdraft of a 6,000-year aquifer operates on a different timescale."). Longer flowing sentences for complex analysis with inline sources. No sentence exceeds 40 words unless it contains a data series.

### Tone
Analytical, understated, honest about limitations. First person singular ("I") sparingly and only for direct experience or methodology disclosure. Never promotional. Never alarmist. Let the data carry the weight.

### Technical Depth
Accessible technical. Explains frameworks inline for a non-specialist audience ("Lotka-Volterra Competition models three sectors competing for one declining aquifer. It shows which sector faces cuts first."). Uses precise numbers, never rounds for drama.

### Opening Pattern
Context bridge from the previous issue, then a direct statement of what this issue does differently. No abstractions. No "In this article we'll explore." Example:

> "Last issue mapped the competition between water, energy, and compute. This issue does something different: it applies mathematical models to publicly available aquifer data and reports what they show."

### Closing Pattern
A short, resonant observation that reframes the analysis. No CTA, no "subscribe", no sales pitch. Example:

> "Droughts end. Overdraft of a 6,000-year aquifer operates on a different timescale."

Followed by: "Corrections and responses welcome."

Then two questions to practitioners. These carry the reconnaissance load of the whole issue, so write them last and write them hard. Each must be answerable from someone's working experience rather than from opinion, and each must name the specific thing you looked for and could not find. "Corrections and responses welcome" is an invitation, not a question, and on its own it produces nothing.

Test every question before publishing. Write down two or three plausible answers and the next move each one gives you. If any answer leaves you with no next move, the question is wrong and gets rewritten before the issue ships. Example that worked:

> "And has anyone dealt with the over-recovery side in practice? Waterlogging or buoyancy problems after levels came back up? I can find the mechanism described but almost nothing on how managers set the upper bound."

### Forbidden Patterns
- Em dashes (---). Use periods, commas, or parentheses instead.
- Superlatives ("revolutionary", "game-changing", "unprecedented")
- Listicle titles ("7 Ways...", "Top 5...")
- Abstract openings ("In an era of...", "The world is changing...")
- Hedging without commitment ("might potentially", "could perhaps")
- Exclamation marks
- Emojis
- "We" (unless referring to a specific team action)
- Self-promotion or product mentions
- The segue before a breakdown ("Here's the breakdown:", "Here's what I found:"). Launch into
  the thing instead.
- Bolded mini-headings more often than roughly every two paragraphs, or headings that carry no
  claim of their own.
- A database number stated without how it was derived and what the field actually contains.
- A system-level conclusion with no operational detail under it: no permit number, no
  measurement method, no named actor, nothing that breaks.

These four are what domain practitioners flag first. They are not stylistic preferences: a
reader who works in the field reads them as a signal that the piece was assembled rather than
understood, and stops reading. Run the voice checker before publishing.

## Hard rules

**Empty column is not absence.** Before writing that a category is missing from a dataset,
check whether the field is populated for anything at all. A public registry will often leave a
field blank for most of its records, so the absence of a value proves nothing about any one
category. State what the field actually contains and for how many records, then draw the
conclusion, or drop the claim.

**Naming people.** Name only someone who spoke publicly, under their own handle, in a thread
attached to one of your own posts. Never name a source from private correspondence, and never
publish a private message, even in a working note that might later be shared. Permission to use
material is not permission to attach a name to it. When a private source has agreed their
material can be used, describe them by role and jurisdiction and nothing else.

**Send the draft to a practitioner before publishing.** See Stage 7.5.

## The Process

### Stage 1: Topic & Thesis

Start by understanding what signals the author has collected:

- "What signals caught your attention since the last post?"
- "What is the thesis you want to test or present?"
- "What data sources do you already have?"
- "Who is this aimed at? (Network State builders, tech founders, indie investors, general audience?)"

Use AskUserQuestion for structured choices where appropriate.

### Stage 2: Voice Check

If this is the first article in a session, confirm the voice model by referencing published posts (Post #01 and #02 in `/project/posts/`). If the author's voice has evolved, recalibrate.

For returning sessions, skip this stage. The voice profile above is the baseline.

### Stage 3: Interview Extraction

This is the core differentiator. Extract first-hand analysis through specific questions. Encourage voice input for richer responses.

**Thesis questions:**
- "State your central thesis in one sentence"
- "What is the strongest evidence for it?"
- "What is the strongest evidence against it?"
- "What would change your mind?"

**Data questions:**
- "What specific numbers do you have? Exact figures, dates, sources"
- "Which of these are from government/official sources vs. your own calculations?"
- "Where is the data noisy or uncertain?"

**Systems questions:**
- "What feedback loops are at work here? Reinforcing or balancing?"
- "Where is the bottleneck in this system?"
- "What indicators would you tell someone to watch?"

**Honesty questions:**
- "Where are you framing rather than reporting?"
- "What alternative explanation exists for this data?"
- "What are you NOT covering, and why?"

**Story questions (use sparingly):**
- "What specific moment or data point triggered this investigation?"
- "Walk me through how you found this"

Push for specifics. "628.2 feet" is better than "low levels". "4-11x overshoot" is better than "significantly over capacity". Real numbers with sources are what separate this from opinion journalism.

### Stage 4: Claims Table & Property Gates

The fact check in Stage 6 verifies one property: that each claim matches the text it cites.
Errors that live *between* claims, or in the properties of the record a number came from,
pass it by construction. Build the table before the prose and run the gates over the table.

#### The table

One row per number and per attributed statement. Columns:

| Field | What goes in it |
|---|---|
| `id` | referenced from the draft |
| `value` / `unit` | as published by the source |
| `measures` | the physical or legal quantity, not the label |
| `interest` | ownership, entitlement, delivery, consumption |
| `period` | span covered, **and the date the data window closes** |
| `source` | source id; note whether full text was read or only an abstract |
| `filer` | who fills this record, and what happens to them if the number is high or low |
| `absent` | what cannot enter this dataset by construction |

Prose is written over the table. Every number in the draft resolves to a row id.
A number with no row does not go in.

#### The ten gates

Run over the table, before drafting. Each carries the instance where it has fired.

1. **Commensurability.** Two numbers may be compared only if `measures`, `interest`, unit and
   period all match. *Fired:* a price table set a perpetual water right against a subsidised annual delivery
   tariff and reported the ratio as a single multiple. *Fired:* one figure served as both "total
   supply" and "total consumption" in the same section, with percentages taken against both.
2. **What cannot enter.** Name the category of record structurally absent from each dataset, and
   why. If unknown, no share-of-total claim is made. *Fired:* California rights predating 1914
   transfer outside the board; our own pull returned 363,000 rows and zero pre-1914 entries.
3. **Who fills the record.** Name the filer and the direction of their incentive. *Fired:*
   California right-holders report full use because under-reporting risks the right. *Fired:* a demand-side ledger filed by the same
   authorities being measured against the quota, printed beside physical well measurements and
   treated as equally hard.
4. **Name is not purpose.** Any inference about end use, industry or buyer drawn from an entity's
   name is flagged and separately confirmed. *Fired:* transfers read as agriculture-to-urban
   because the buying districts had urban names; they are usually agriculture-to-agriculture.
   *Fired:* "water-intensive industry phased out" — stopped and relocated to another basin are
   different outcomes and the phrase hides which one happened.
5. **Shelf life.** Every quantity carries the date its window closes. Present tense only where the
   gap is small against the length of the trend. *Fired:* a lead sentence in the present tense over a data
   window that closed four years before publication.
6. **Declared control case.** If a comparison is framed as a control, list at least three other
   variables that differ and say why the effect does not sit on them. *Fired:* a two-country comparison named an
   institutional difference as the only variable, while the same claim table showed confined and
   unconfined aquifers recovering at rates differing by roughly six times — a physical difference
   the comparison never mentioned.
7. **Source concentration.** If one source carries more than a third of the claims, that source
   becomes an object of verification: who contested it, who replicated it. *Fired:* an issue resting 31 of 53 claims on a
   single paper, with that paper never itself examined.
8. **Thesis variable: measured or inferred.** The variable carrying the argument needs a direct
   measurement. If it is only inferred from the outcome it explains, the argument is circular.
   *Fired:* an argument resting on "a cap somebody enforces" that contained no count of inspections,
   sanctions or violations anywhere in its claim table. Enforcement was inferred from the fall in
   withdrawal that enforcement was invoked to explain.
9. **Quantifier fidelity.** The claim's quantifier may not exceed the source's. *Often* does not
   become *in every case*; *many* does not become *all*; *may be key* does not become *neither half
   worked alone*. *Fired:* three times in one issue, in the three sentences carrying its
   thesis, against a source brief that says often, many and most.

10. **Unverified share of the set.** Gates 1-9 test one claim at a time; this one tests the set.
   Count what share of the argument rests on claims that were never confirmed. "Zero incorrect" is
   not a passing condition — absence of disproof is not proof, and an audit summary that leads with
   it hides the real state. *Fired:* an issue published on 1 confirmed, 10 partially
   confirmed and 4 unverified claims out of 15, under a summary reading "0 INCORRECT". Its thesis
   was retracted two issues later.
   *Correct behaviour, same situation:* a later issue cut two claims rather than publish them on a
   summary source.

#### Running the gates: what greps and what does not

Measured across the full archive on 27.08.2026.

| Gate | How it runs |
|---|---|
| 5, 7, 9 | usable as text greps over the draft and the audit files |
| 1, 6 | fire only where the wording happens to be literal ("2,800 times", "control case"). Run them on the **table**, never as a grep — gate 1 is a column comparison, and the grep found the case above only because the literal number was known in advance |
| 2, 3, 4, 8, 10 | not greppable at all; they need the claims table to exist |

Six of ten have nothing to run against until Stage 4 has produced the table. That is the reason
Stage 4 sits before the draft rather than after it.

**Gate 9 regex and its noise.** `in every|every time|across all|in all cases|without exception|universally|every documented|always |never |no [a-z]+ has ever`
Precision on the raw archive was about 40%, three of five hits were noise. Known false-positive
classes, discard on sight: rhetorical negation ("most people have never done this math"), counts
quoted from a source headline ("across all 44 counties"), and enumerable sets of the author's own
("across all three scenarios"). The true hit it found: #05, "It never goes back down."

#### Suite validation record

A suite that has never gone red on a known defect has not been shown to work. Positive control run
27.08.2026: gate 1 fires on a published "over 2,800 times more per acre-foot" comparison — a
perpetual right against an annual delivery — which that issue's own audit had passed as GREEN with
both figures correctly sourced. Re-run this control whenever the gate definitions change.

#### Growing the suite

Two generators, run over the table when a new domain or data type appears:

- **Inversion.** How is this claim false while every citation stays correct?
- **Measurement chain.** What instrument produced this number, who read it, what is the direction
  of systematic error?
- **Pre-mortem** (untested as of 27.08.2026). Assume the piece is publicly demolished in six months
  and write the demolition. Aimed at social failure modes, which the other two do not reach.

**Pruning rule.** A gate enters the suite only with a named instance where it fires, in this
archive or in a plausible artifact. No instance, no gate. A gate that has never fired has not been
shown to test anything. This rule is what keeps the suite at ten instead of thirty.

#### What the gates do not do

They catch repeating classes. A class you have never met still arrives from a practitioner who has
handled the physical thing — the aquifer as a layered cake rather than a bank account was not
derivable from the desk. And none of them makes the prose readable; that is Stage 7's problem.

### Stage 5: Draft in Fixed Structure

Every Physical Layer post follows this structure. Do not deviate.

#### Required Sections

1. **Title line**: "[Topic]. [One-sentence framing.]"
2. **Disclaimer**: Standard text (see below)
3. **Context bridge**: 2-3 paragraphs connecting to previous work, stating what this issue does, and disclosing author's position/limitations
4. **Section 0: Map of the Period**
   - 3 structural shifts (numbered)
   - 5 bottlenecks (bulleted)
   - 5 indicators to watch (bulleted)
5. **Signals** (2-5 per post, each with):
   - Signal: what happened (with source links)
   - Systemic significance: why it matters structurally
   - Loop: R (reinforcing) or B (balancing), described precisely
   - Bottleneck: the constraint
   - Indicator: what to watch going forward
   - Sources: inline links + collected at end of each signal
6. **Strategy Patches**: 30-90 day actions for the reader
7. **Limits and Confidence**: where data is weak, alternative explanations, model assumptions
8. **Manipulation Analysis**: where the author is framing vs. reporting (UNIQUE differentiator)
9. **Closing line**: resonant observation, then the two practitioner questions per Closing Pattern

#### Correction Issue (alternative structure)

When the subject of an issue is an error in your own earlier claim, the structure above does not apply. Use this one. It has produced the highest substantive response of any issue so far.

1. **Title line**: the earlier claim, that it was wrong, and what the correction rests on
2. **Disclaimer**: standard
3. **The earlier claim**: what you argued, in which issue, and the reasoning behind it. State plainly which part of it still stands
4. **What you missed**: the evidence and where it was. If it sat in a source you were already citing, say so
5. **The careful reading**: what the corrected figure does and does not mean. Take apart any number that pools several different states into one
6. **The mechanism**: how the corrected effect actually works, sorted into categories
7. **The case with a full public ledger**: one case documented end to end, with the supply side and the demand side reported separately
8. **The control case**: a comparable case that did not work, and the single difference that accounts for it
9. **The failure mode of the correction itself**: what goes wrong when the thing you were wrong about goes too far
10. **Where this is weak**: what you did not read, what you left out and why, what selection is built into the evidence
11. **Closing questions** per Closing Pattern

Do not soften the admission. The admission is the reason the issue gets read.

#### Disclaimer (standard, place at top)

> *Disclaimer: This publication presents systems analysis based on publicly available data from cited sources. The author is not a [domain expert]. This is commentary and analysis, not expert assessment. Model outputs are projections under stated assumptions, not predictions. Verify all data with primary sources before making decisions.*

#### Writing Rules

- Every factual claim must have an inline URL to source
- Own calculations must be labeled "the model projects" / "our analysis shows"
- Projections must include "if [condition] continues" / "under stated assumptions"
- No imputation of motive without direct quote ("deliberately", "intentionally")
- No mention of RF or KZ companies or individuals (red line)
- Numbers: use exact figures from sources, not rounded for drama
- Tables for comparative data
- Bold for signal headers and key terms, not for emphasis of every third word

### Stage 6: Fact Check & Risk Score

Before showing the draft to the author, self-check.

Scope note: this stage checks **citation fidelity** — does the source say what the draft says.
It is one property. It cannot see a comparison of unlike quantities, an incomplete universe, a
self-interested filer, a stale window, an unexamined confound, or a quantifier stronger than the
source's. Those are Stage 4's job and they are not re-checked here. A green audit at this stage
means the citations hold, not that the argument does.

**Schema (fixed, do not vary per issue).** One numbered row per claim, columns
`# | claim | source | status`, status one of GREEN / YELLOW / RED. Earlier issues each invented their own format —
no numbered rows in one, CONFIRMED/PARTIAL/UNVERIFIED in another, GREEN/YELLOW in the rest — so the
archive cannot be queried across issues. Do not add a new vocabulary.

**Fact Check (per claim):**
- Is the source URL valid and accessible?
- Does the source actually say what the draft claims?
- Is the number exact (not approximated)?
- Own calculations: is methodology disclosed?

Flag any claim where source is uncertain as [NEEDS VERIFICATION].

**Risk Score (per claim, 0-10):**

| Dimension | 0 | 1-2 | 3-5 |
|-----------|---|-----|-----|
| Legal exposure | No target | Public company + public data | Private person or imputation of motive |
| Enforceability | No jurisdiction | Theoretical | C&D possible |
| Defense weakness | Fair Report + Truth | Opinion + disclosed facts | Factual claim without source |

Post Risk = max(claim score) + (ELEVATED claims * 3). Score 9+ = do not publish, rework.

**Red Lines (NEVER cross):**
1. No accusations of crimes ("fraud", "conspiracy", "cover-up")
2. No imputation of motive without direct quote
3. No leaked/confidential documents directly
4. No private life of individuals
5. No investment recommendations ("buy", "sell")
6. No Russian companies or individuals
7. No Kazakh companies or individuals
8. No categorical predictions ("WILL lose water")

### Stage 7: Refinement

After showing the draft:

- Ask for specific feedback: "What feels off? What's missing? What's too strong?"
- Iterate on flagged sections
- Watch for AI-sounding phrases: uniform rhythm, superlatives, hedging chains
- Verify the Manipulation Analysis section is honest and specific
- Run the 10-point binary checklist (see references)

### Stage 7.5: Expert Review (mandatory when anyone has offered)

Before Publishing Prep, send the draft to any practitioner who offered to read one. Record in
the publishing notes who it went to and who answered.

Practitioners who follow this kind of work routinely offer to read a draft. That offer is the
cheapest quality gate available and it expires: an expert who keeps receiving finished
conclusions instead of drafts stops answering. Check the project's expert notes for standing
offers before assuming there are none.

If no one has offered, record that explicitly rather than leaving the step silent.

### Stage 8: Publishing Prep

When ready to publish:

- Format for Substack (WYSIWYG, not raw markdown; render via stackedit.io)
- Archive key source URLs via web.archive.org/save/
- **Practitioner review — record sent / not sent, with name and date.** This step no-ops silently
  when skipped and nothing downstream notices. A standing offer from a domain practitioner to read drafts went
  unused for six months because nothing in the pipeline surfaced it. Either send, or record an
  explicit waiver with a reason.
- Generate Substack subtitle (under 160 chars)
- Suggest distribution plan (Reddit subreddits, HN angle, Twitter thread)
- Record in FACT_CHECK_AUDIT and RISK_SCORING files per post

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| Abstract openings ("In an era of...") | Readers bounce. Lead with data or a specific moment. |
| Listicle format | Screams SEO/AI content. Not compatible with systems analysis. |
| Superlatives ("unprecedented crisis") | The data speaks for itself. Inflation weakens credibility. |
| Uniform sentence rhythm | AI fingerprint. Mix short and long deliberately. |
| Hedging chains ("might potentially perhaps") | Pick a position and state confidence level explicitly. |
| Rounding numbers for drama | "Over 400 million gallons" is weaker than "434 million gallons." |
| Missing Manipulation Analysis | This section IS the differentiator. Without it, this is just another newsletter. |
| CTA closings ("Subscribe for more") | Breaks the analytical voice. End with insight, not a pitch. |
| Closing with a generic invitation only ("thoughts?", "corrections welcome") | Produces no replies. The two specific practitioner questions are what bring people who know the field into the thread. |
| Using em dashes | Author's style avoids them. Use periods or parentheses. |

## File Structure

Each post lives in `/project/posts/postNN/` with:
- `article.md` or `article_en.md` (final text)
- `FACT_CHECK_AUDIT.md` (per-claim verification)
- `RISK_SCORING.md` (per-claim risk assessment)
- `SOURCES.md` (archive log)
- `sources/` (local copies of key sources)

Shared assets in `/project/posts/_shared/`:
- `PUBLISH_CHECKLIST.md`
- `RISK_SCORING_FRAMEWORK.md`
- `METHODOLOGY.md`
- `archive_sources.js`

---

*Based on [Founder Voice Ghostwriter](https://github.com/BayramAnnakov/founder-voice-ghostwriter) by [Bayram Annakov](https://linkedin.com/in/bayramannakov). Adapted for investigative analysis and systems intelligence.*
