---
name: physical-layer-writer
description: Collaborative ghostwriting for investigative analysis and systems intelligence briefs. Extracts thesis, evidence, and counter-arguments through structured interview. Produces sourced, risk-scored content in the author's analytical voice. Use when user wants to write a Physical Layer post, investigative article, systems analysis, or says things like "new post", "write about", "draft analysis", "next article". Also the single place the pre-publication check lives: use when the user asks to check a Physical Layer post or draft, says "проверь текст поста", or names the pre-publication check before publishing.
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

## Forbidden Patterns
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
- Numbers rounded for drama. "434 million gallons" is stronger than "over 400 million".
- A post without the Manipulation Analysis section. That section is the differentiator; without
  it this is another newsletter.

These four are what domain practitioners flag first. They are not stylistic preferences: a
reader who works in the field reads them as a signal that the piece was assembled rather than
understood, and stops reading. Run the Pre-Publication Check below before publishing.

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

Eight stages. Where a stage names a file in `references/`, open it and work from it.

### Stage 1: Topic & Thesis

Start by understanding what signals the author has collected:

- "What signals caught your attention since the last post?"
- "What is the thesis you want to test or present?"
- "What data sources do you already have?"
- "Who is this aimed at? (Network State builders, tech founders, indie investors, general audience?)"

Use AskUserQuestion for structured choices where appropriate.

### Stage 2: Voice Check

If this is the first article in a session, confirm the voice model by referencing published posts (Post #01 and #02 in `/project/posts/`). If the author's voice has evolved, recalibrate.

For returning sessions, skip this stage. The voice model is `references/voice-guide.md`: sentence
structure, first person, technical vocabulary, data presentation, honesty markers, and the opening
and closing patterns. Forbidden Patterns above is the short list that never gets skipped.

### Stage 3: Interview Extraction

Extract the author's own knowledge before writing anything. The extraction sequence is in
`references/post-structure.md`, the question bank it draws on is in `references/voice-guide.md`.

### Stage 4: Claims Table & Property Gates

Claims go into a table and the gate suite runs against that table, not against claims in
isolation. Some gates apply to every claim, some fire only where its shape calls for them, a
comparison or a declared control case, and the last one measures the finished set. Six of the ten
have nothing to run against until the table exists. The gates, the table format and the worked
examples: `references/claims-and-risk.md`.

### Stage 5: Draft in Fixed Structure

The post has a fixed nine-part structure, from the title line to the two closing questions, and
correction issues have eleven of their own. Manipulation Analysis is the section that
differentiates the series. Both structures: `references/post-structure.md`.

### Stage 6: Fact Check & Risk Score

Per-claim verification on a fixed schema, one numbered row per claim, then risk scoring across
three dimensions: legal exposure, enforceability, defense weakness.
See `references/claims-and-risk.md`.

### Stage 7: Refinement

After showing the draft:

- Ask for specific feedback: "What feels off? What's missing? What's too strong?"
- Iterate on flagged sections
- Watch for AI-sounding phrases: uniform rhythm, superlatives, hedging chains
- Verify the Manipulation Analysis section is honest and specific
- Run the Pre-Publication Check, evidence gate first. An edit made at this stage can drop a
  citation or delete a required section that Stage 6 already passed, so the gate runs again on the
  text that ships

### Stage 7.5: Expert Review (mandatory when anyone has offered)

Before Publishing Prep, the draft goes to any practitioner who offered to read one. Record in the
publishing notes who it went to and who answered.

**The author sends it, not the agent.** Prepare the message and hand it over. Contacting a source
is an outside action with the author's name on it and it is never taken on the author's behalf,
whatever the draft says about who offered.

Practitioners who follow this kind of work routinely offer to read a draft. That offer is the
cheapest quality gate available and it expires: an expert who keeps receiving finished
conclusions instead of drafts stops answering. Check the project's expert notes for standing
offers before assuming there are none.

If no one has offered, record that explicitly rather than leaving the step silent.

### Stage 8: Publishing Prep

Substack mechanics, source archiving, the practitioner-review record, and the rules each
distribution surface enforces: `references/publishing-surfaces.md`. Run the Pre-Publication Check
again once this stage has produced the final files.

## Pre-Publication Check

Run it twice: at Stage 7 on the draft, and after Stage 8 on the files that ship. Stage 8 produces
the Substack variant and the distribution copy, and those carry their own checks, so a run that
stops before Stage 8 never sees them. Also run it whenever the author asks to check a post.

Two halves. The mechanical half is a script:

```bash
python3 scripts/check_prepublication.py posts/postNN/article_en.md
python3 scripts/check_prepublication.py posts/postNN/
```

The half a script cannot see is in `references/prepublication.md`: the evidence gate (a source
under every claim, own calculations labelled, Limits and Confidence present, audit trail) and the
four markers named by domain readers. Whether the two closing questions actually work is judged
against Closing Patterns in `references/voice-guide.md`. Read both every time. A green script is
not a verdict.

## Where things are

Post directories, this skill's own layout and the shared assets: `README.md`.

---

*Based on [Founder Voice Ghostwriter](https://github.com/BayramAnnakov/founder-voice-ghostwriter) by [Bayram Annakov](https://linkedin.com/in/bayramannakov). Adapted for investigative analysis and systems intelligence.*
