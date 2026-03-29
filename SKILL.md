---
name: physical-layer-writer
description: Collaborative ghostwriting for investigative analysis and systems intelligence briefs. Extracts thesis, evidence, and counter-arguments through structured interview. Produces sourced, risk-scored content in the author's analytical voice. Use when user wants to write a Physical Layer post, investigative article, systems analysis, or says things like "new post", "write about", "draft analysis", "next article".
license: MIT
metadata:
  author: Alex Nikolaev
  based_on: founder-voice-ghostwriter by Bayram Annakov (https://github.com/BayramAnnakov/founder-voice-ghostwriter)
---

# Physical Layer Writer

Transform raw signals and data into sourced, risk-scored investigative analysis in the author's voice.

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

### Stage 4: Draft in Fixed Structure

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
9. **Closing line**: resonant observation + "Corrections and responses welcome"

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

### Stage 5: Fact Check & Risk Score

Before showing the draft to the author, self-check:

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

### Stage 6: Refinement

After showing the draft:

- Ask for specific feedback: "What feels off? What's missing? What's too strong?"
- Iterate on flagged sections
- Watch for AI-sounding phrases: uniform rhythm, superlatives, hedging chains
- Verify the Manipulation Analysis section is honest and specific
- Run the 10-point binary checklist (see references)

### Stage 7: Publishing Prep

When ready to publish:

- Format for Substack (WYSIWYG, not raw markdown; render via stackedit.io)
- Archive key source URLs via web.archive.org/save/
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
