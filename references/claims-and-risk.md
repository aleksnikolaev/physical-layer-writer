# Claims table, property gates, fact check and risk score

Read this at Stage 4 and again at Stage 6. Do not work from memory of it.

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
