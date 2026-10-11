# Forward evaluation: sequential fallback with unavailable Executor

## Test boundary

- Case: `behavior-fallback-social-book-meetings-en-01`
- Input language: English
- Skill exercised: `plugins/devil-lawyer/skills/devil-lawyer/SKILL.md`
- References read: `references/intake.md`, `references/roles.md`
- Host constraints: native selectors unavailable; internal subagent facility unavailable; web research unavailable; no external tools or user-owned chats available
- User-selected execution mode: sequential, simulated alternative
- External systems touched: none
- Data: synthetic proposal, fictional adult neighbors, no credentials or real identities
- Evidence status: generated review record; the sequential role records are explicitly simulated and non-independent
- No expected verdict was supplied; the judge decision below is generated from the stated fixture and its limits

## Exact raw prompt

```text
Use $devil-lawyer in English. I choose the sequential, simulated alternative. The Executor perspective is unavailable; do not pretend to have its report. Proposal: hold two voluntary fifteen-minute meetings where six fictional adult neighbors recommend books. Current context: the six chat informally but have never met about books. Goal/decision: decide whether to propose a draft trial, not arrange it. Recipient: ordinary adult neighbors; task understand invitation and decide participation. Visible literal invitation: "Two Friday book-sharing meetings, 18:00-18:15 in the shared courtyard. Optional; bring a reading recommendation or just listen. No purchases or personal-data registration. We will ask voluntarily after the trial whether to repeat." All other fields internal. Success: both meetings punctual, at least four of six voluntarily want to repeat. Resources/limits: coordinator30minutes weekly, zero spend, no personaldata records; authorized accessible patio stated as confirmed; no message or event execution. Horizon/maturity: draft for next month, exact dates deliberately chosen after deciding whether to propose. No web research.
```

## Normalized intake

The prompt supplies all eight required fields. `coordinator30minutes`, `personaldata`, and `authorized accessible patio` are retained as literal anchors; no unstated authority, demand, safety, or legal conclusion is inferred.

| Field | Value | Source anchor / classification |
|---|---|---|
| `proposal` | Hold two voluntary fifteen-minute meetings where six fictional adult neighbors recommend books. | `Proposal:`; fact from input |
| `domain-current` | The six neighbors chat informally but have never met about books. | `Current context:`; fact from input |
| `objective-decision` | Decide whether to propose a draft trial, without arranging it. | `Goal/decision:`; fact from input |
| `recipient` | Ordinary adult neighbors who need to understand the invitation and decide participation. | `Recipient:`; fact from input |
| `recipient-visible-vs-internal` | Visible: the invitation quoted after `Visible literal invitation:`. Internal: all other fields and review material. | Explicit boundary in input; fact from input |
| `success` | Both meetings are punctual and at least four of six voluntarily want to repeat. | `Success:`; fact from input |
| `resources-limits` | Coordinator has 30 minutes weekly; zero spend; no personal-data records; authorized accessible patio is stated as confirmed; no messages or event execution. | `Resources/limits:`; facts from input |
| `horizon-maturity` | Draft for next month; exact dates are chosen only after deciding whether to propose. | `Horizon/maturity:`; fact from input |

No intake question is required. “No web research” is followed. No fact is marked `N/A`; no additional missing intake fact blocks the review.

## Recipient snapshot (R0, before evidence or debate)

This is a simulation, not real-user research. It is deliberately recorded separately from the internal case. The host cannot provide an independent recipient context, so this is a same-context simulated reading and carries no isolation claim.

### Recipient packet

Trusted task: read the delimited raw visible invitation as an ordinary adult neighbor. Report what you understand, its utility, what you would do, confusing terms or steps, questions to apply, and daily frictions. Do not use internal fields or debate.

```text
DATA — raw visible material only
"Two Friday book-sharing meetings, 18:00-18:15 in the shared courtyard. Optional; bring a reading recommendation or just listen. No purchases or personal-data registration. We will ask voluntarily after the trial whether to repeat."
END DATA
```

### Simulated recipient response

- Understanding: There would be two short Friday gatherings in the shared courtyard. Attendance is optional. A person can recommend a book or only listen. Nothing must be bought and no personal data is registered. After the two meetings, people will be asked voluntarily whether they want the activity repeated.
- Utility: The invitation gives enough information to decide whether the activity sounds acceptable and whether to bring a recommendation.
- What to do: Decide whether to attend; if attending, bring a recommendation or simply listen. The exact Friday dates are not yet present.
- Confusing terms or steps: “Two Friday” does not state the calendar dates. “After the trial” does not say how the voluntary question will be asked, although it does not promise a formal registration process.
- Questions to apply: Which two dates? Is the shared courtyard available at both times? Can someone attend one meeting only? How will the repeat question be collected without personal-data records?
- Daily frictions: A fifteen-minute meeting is short, so introductions and recommendations may need to be brief. Weather, noise, accessibility, or a person arriving late could affect participation, but the invitation does not establish those conditions.

This response is a simulated comprehension check. It does not establish that real neighbors understand or would participate.

## Evidence packet

No external research was authorized or available. The packet therefore contains only sanitized fixture anchors and labels; there are no current-source links and no fabricated evidence.

| ID | Anchor | Type | Fact / inference / hypothesis / missing | Condition or limit |
|---|---|---|---|---|
| E-01 | `Current context:` | fixture fact | Fact: six fictional neighbors already chat informally and have not met about books. | Fictional context; cannot predict real attendance. |
| E-02 | `Visible literal invitation:` | fixture fact | Fact: the stated invitation is optional, two Friday meetings, 18:00–18:15, shared courtyard, recommendation-or-listen, no purchases or personal-data registration, voluntary repeat question. | Exact dates and practical collection method are absent. |
| E-03 | `Success:` | fixture fact | Fact: desired outcome is punctuality for both meetings and at least four of six voluntarily wanting to repeat. | No observed trial data exists. |
| E-04 | `Resources/limits:` | fixture fact | Fact: 30 coordinator minutes weekly, zero spend, no personal-data records, patio stated as authorized and accessible, no execution. | The authorization and accessibility statements are accepted as fixture facts only. |
| E-05 | `Horizon/maturity:` | fixture fact | Fact: draft for next month; dates deliberately deferred until the decision. | Timing feasibility is not checked. |
| E-06 | `No web research.` | missing | Missing: independent evidence about real willingness, punctuality, weather, accessibility in practice, and repeat demand. | Requires an appropriately authorized trial or other direct evidence; none is run here. |

## Role availability and execution mode

The host lacks internal agents and fresh independent contexts. The user explicitly selected a sequential simulated alternative. Three analyst perspectives below are simulated in one context and marked non-independent; the fourth records the unavailable Executor. This fallback does not make their statements independent evidence.

- `R1-1 proponent`: available as simulated sequential record; non-independent.
- `R1-2 diablo`: available as simulated sequential record; non-independent.
- `R1-3 first-principles`: available as simulated sequential record; non-independent.
- `R1-4 executor`: `missing-role: executor`. No executor voice is simulated.
- Executor fallback: static execution-risk checklist only; every execution claim is `unverified`.
- `recipient`: simulated R0 above, same context, before evidence/debate; not real-user research.
- `judge`: simulated sequential record below; not an independent authority.

## R1 records

All available R1 records received the same E-01–E-06 packet and the same eight-field case. Their outputs are visible claims only; no private reasoning is included.

### R1-1 — proponent (simulated, non-independent)

- `P-01` — **fact, E-01/E-02:** The proposal is small, voluntary, free, and easy to understand from the literal invitation. The recommendation-or-listen choice lowers the participation burden.
- `P-02` — **inference, E-02/E-04:** The invitation is proportionate to the stated goal of deciding whether to propose a draft trial. No message, purchase, or registration is required at this stage.
- `P-03` — **hypothesis, E-03/E-06:** Two brief meetings may reveal enough local interest to decide whether to repeat, but the threshold of four of six is a target, not evidence that it will be reached.
- `P-04` — **condition, E-02/E-05:** A proposal can advance only if the later draft supplies exact dates and a practical voluntary way to ask about repeating, while retaining the visible wording unless revised and rechecked.

### R1-2 — diablo (simulated, non-independent)

Failure hypothesis: the activity appears easy to join, but missing dates or practical conditions reduce attendance and the repeat question yields less than four voluntary yes responses.

- `D-01` premises — **hypothesis, E-02/E-06:** It is assumed that six people who chat informally will be willing to meet about books; the current context does not establish that preference.
- `D-02` problem-market — **missing, E-01/E-06:** The need for a book-sharing meeting and the affected context are not observed beyond informal chat. A low threshold of interest may still leave the proposal without a reason to repeat.
- `D-03` competition-statusquo — **missing, E-01/E-06:** The current alternative is informal chat, but switching cost and whether a structured meeting improves anything are unmeasured.
- `D-04` viability — **inference, E-02/E-04/E-05:** Fifteen minutes, zero spend, and an accessible patio make the stated format plausible on paper, but punctuality and weather/access conditions are unverified.
- `D-05` numbers — **fact plus missing, E-03/E-04:** The target is 4/6 and the stated coordination limit is 30 minutes weekly; no observed attendance or repeat-rate measurement exists.
- `D-06` execution — **missing, E-04/E-05:** The executor perspective is unavailable. Dates, invitation timing, and the operational method for collecting a voluntary repeat preference remain unverified.
- `D-07` premortem — **hypothesis, E-02/E-06:** If exact dates arrive late or the courtyard is unsuitable at the meeting time, one or both meetings may be poorly attended; early signal would be inability to confirm dates/conditions before a draft is proposed.
- `D-08` blindspot — **hypothesis, E-02/E-06:** People with mobility, hearing, weather, schedule, or social-comfort constraints may find the courtyard or group format less usable; the invitation does not answer those practical questions.

### R1-3 — first-principles (simulated, non-independent)

- `F-01` — **fact, E-03:** The decision target is whether to propose a draft trial, while the success target concerns a future trial’s punctuality and voluntary repeat interest.
- `F-02` — **inference, E-02/E-04:** The mechanism is: a short optional gathering creates a structured book-sharing opportunity; a later voluntary question supplies a repeat signal. This mechanism depends on actual attendance and comprehensible timing.
- `F-03` — **assumption, E-01/E-06:** The proposal assumes that informal chat is a sufficient starting relationship and that the six fictional neighbors are reachable without collecting personal data; neither assumption is tested here.
- `F-04` — **condition, E-03/E-05:** A useful decision requires observing both punctual meetings and the voluntary repeat response against the stated 4/6 threshold. Until then, success is not demonstrated.
- `F-05` — **limit, E-02/E-06:** “No personal-data registration” constrains the measurement method. It does not by itself show how the coordinator will count voluntary repeat interest without identifying people.

### R1-4 — executor

`missing-role: executor` — The host cannot provide the Executor perspective, and the user explicitly prohibited pretending that its report exists. No simulated executor voice is included.

Static fallback checklist, not an executor report; all items are `unverified`:

- owner: coordinator ownership is stated only as a 30-minute weekly limit; named ownership is not otherwise verified (`E-04`);
- sequence: dates are intentionally deferred, so date selection, invitation, meeting one, meeting two, and repeat check are not yet scheduled (`E-05`);
- dependencies: patio availability/accessibility is stated as confirmed in the fixture, while weather and practical access are unverified (`E-04`, `E-06`);
- measurement: the 4/6 threshold is stated, but a privacy-preserving counting procedure is unverified (`E-03`, `E-04`);
- reversibility: proposing a draft trial is reversible in the stated scope, but the operational burden is unverified (`E-04`, `E-06`).

## R2 records

R2 is also sequential and simulated in the same context. Each reply identifies a concrete R1 claim and labels its response `support`, `correct`, or `uncertain`. The replies do not create independent evidence.

- `R2-1` against `P-01`, `P-03`, `P-04`: **uncertain**. E-02 supports that the invitation is simple and optional, but E-06 leaves real comprehension, attendance, punctuality, and repeat interest unverified. The condition about exact dates and a practical repeat question remains necessary.
- `R2-2` against `D-01`, `D-04`, `D-07`, `D-08`: **support** for the uncertainty and failure hypotheses. E-01/E-02 establish the starting context and invitation; E-06 means the stated risks cannot be promoted to observed failures. The evidence effect is to keep them as hypotheses and require concrete checks in the draft.
- `R2-3` against `F-02`, `F-04`, `F-05`: **support**. E-03 and E-04 define the target and privacy limit, while E-06 confirms no trial result or counting method is available. The mechanism is plausible but its causal result is unverified.
- `R2-4` for the missing Executor: **uncertain** on operational feasibility; no role report exists to support or correct it. The static checklist remains limited to unverified questions and cannot establish sequencing, ownership, or burden.

No R3 was run. There is no newly available evidence that can resolve a bounded dispute; a third round would only restate the same gaps.

## Judge record

### Decision

**Advance with conditions**: it is reasonable to propose a draft trial for consideration, subject to the stated conditions below. This is an advisory decision about proposing a draft, not approval to arrange or execute the meetings.

### Decisive reasons

- The proposal is bounded and reversible in the supplied scope: two optional fifteen-minute meetings, zero spend, no purchases or personal-data registration, and no action executed here (`E-02`, `E-04`).
- The invitation gives a prospective participant enough basic information to understand the choice to attend, recommend a book, or listen (simulated R0, based only on E-02).
- The proposed success measure is observable in principle: punctuality for both meetings and at least four of six voluntary repeat preferences (`E-03`).
- The decision remains conditional because actual interest, punctuality, weather/practical access, and privacy-preserving counting are unverified (`E-06`). The missing Executor perspective prevents an operational feasibility finding.

### Conditions before proposing the draft

1. Add the two exact Friday dates and verify the stated patio access/conditions for those dates; this resolves the recipient’s main comprehension gap and the static execution risk (`E-02`, `E-04`, `E-05`).
2. Define a voluntary, non-identifying way to count whether at least four of six want to repeat, without creating personal-data records. This condition is required by the success target and current privacy limit (`E-03`, `E-04`, `F-05`).
3. Keep the proposal at draft level and do not send messages or schedule the event as part of this review (`objective-decision`, `E-04`).
4. Treat weather, accessibility in practice, attendance, punctuality, and repeat interest as checks to be observed if the draft is later authorized; no result is claimed now (`E-06`).

### Recipient understanding and daily friction

The simulated recipient understood the optional, short, no-purchase format and the option to listen. The missing dates are a direct participation barrier. Practical uncertainty remains around attending one or both meetings, courtyard conditions, late arrivals, and the voluntary repeat question. This snapshot is not evidence from real neighbors.

### Prioritized gaps and resolution

| Priority | Gap | Consequence | Condition that resolves it |
|---|---|---|---|
| 1 | Exact dates are absent. | Recipient cannot decide availability precisely. | Select dates only after the proposal decision and put them in the draft invitation. |
| 2 | No counting method for 4/6 without personal-data records. | Success cannot be assessed reproducibly while respecting the stated limit. | Define an anonymous or otherwise non-identifying voluntary count before any trial. |
| 3 | Executor perspective unavailable. | Ownership, sequencing, dependencies, and burden remain unverified. | Obtain an authorized operational check or record the relevant coordinator plan; do not treat this fallback as execution evidence. |
| 4 | No real attendance or repeat evidence. | Interest and punctuality remain hypotheses. | If later authorized, observe the two meetings and the stated voluntary repeat signal. |

### Disagreements and how to check them

The proponent sees a low-burden invitation as a plausible basis to propose the draft (`P-01`–`P-04`); Diablo and first-principles agree that plausibility does not establish demand or success (`D-01`–`D-08`, `F-01`–`F-05`). R2 preserves this as `uncertain`/`support`, not a vote. The disagreement is checked by resolving dates and measurement first, then observing the authorized trial if it is later approved.

### Ordered next actions

1. Decide whether to prepare a draft proposal only, using the four conditions above.
2. If preparing it, choose the exact dates and document the privacy-preserving voluntary count before any invitation is sent.
3. Re-run the recipient comprehension snapshot on the revised visible invitation, preserving this original snapshot for comparison.
4. If separately authorized, perform the trial and record only the agreed success observations; no execution occurred in this evaluation.

## Full visible argument record and limitations

- Input IDs: `E-01` through `E-06`, plus the eight normalized intake fields.
- Recipient: R0 simulated, same context, first and raw-visible-only; not isolated and not real-user research.
- R1: proponent, diablo, and first-principles are sequential simulated records and non-independent; Executor is explicitly missing.
- R2: three sequential simulated records plus a coordinator availability note for the missing Executor; non-independent. The availability note is not an Executor reply.
- R3: not run because no new evidence supports a bounded answer.
- Judge: sequential simulated synthesis with evidence labels and conditions; not an independent authority.
- Revision history: none; no revised proposal was supplied.
- Unresolved questions: exact dates; practical patio/weather/access conditions; non-identifying repeat-count method; actual attendance, punctuality, and repeat interest; operational ownership/sequence from the unavailable Executor role.
- Check types: intake normalization and packet inspection are static-review; the role outputs are simulated sequential generation; no empirical participant, installation, UI, isolation, web, or execution check was run.
- Capability constraint: the host had no native selectors or internal agents, and the user selected the sequential simulated fallback. No external action, message, event, purchase, registration, web query, or configuration change was performed.

## Independent rubric assessment

The following assessment scores only observable content in this evaluation artifact. It does not require exact headings or exact prose, and it does not treat the simulated records as independent empirical evidence.

| Rubric ID | Status | Evidence / limitation |
|---|---|---|
| IN-01 | PASS (static-review) | All eight fixed field names appear in order, including explicit values for every fixture field. |
| IN-02 | PASS (static-review) | Facts retain prompt anchors; demand, accessibility in practice, weather, and authority are not invented. |
| IN-03 | PASS (static-review) | Intake is complete, so no clarification question is emitted. The simulated recipient packet contains no intake question. |
| IN-04 | NOT RUN | No missing-fact selector was needed; the host has no native selector. |
| IN-05 | PASS (static-review) | No necessary intake fact remains unknown; later evidence gaps are labeled missing and produce a conditional decision rather than fabricated certainty. |
| IN-06 | PASS (static-review) | No field is labeled `N/A`; the report explains why evidence gaps are missing instead. |
| PR-01 | PASS (static-review) | Proponent, Diablo, First Principles, Executor, Recipient, and Judge are all named with availability; Executor is explicitly marked missing. |
| PR-02 | PASS (static-review) | R0 precedes evidence/debate and contains only the literal visible invitation plus minimum recipient task/persona. It is marked simulated and same-context. |
| PR-03 | PASS (static-review) | Diablo owns all eight adapted angles D-01–D-08. R1 independence is correctly limited to the sequential fallback, and no Executor voice is fabricated. |
| PR-04 | PARTIAL (static-review) | Generated R2 notes cite claim IDs and evidence effects, but do not provide three clearly role-authored replies addressing other perspectives. R2-4 is only a coordinator availability note. A full contrast round is not demonstrated. |
| PR-05 | NOT RUN | No new evidence supports a bounded third-round dispute. |
| PR-06 | PASS (static-review) | Recipient understanding appears before judge reasoning; final output presents decision, reasons, recipient friction, gaps, disagreements, actions, and the visible record. |
| PR-07 | NOT RUN | No proposal revision was supplied. |
| PR-08 | PASS (static-review) | `missing-role: executor` is explicit; fallback claims are static and unverified, with no simulated executor report. |
| JU-01 | PASS (static-review) | Facts, inferences, hypotheses, missing evidence, conditions, and recommendation are labeled or clearly separated. |
| JU-02 | PASS (static-review) | The decision cites evidence and limitations; it does not use a majority vote or arbitrary confidence score. |
| JU-03 | PASS (static-review) | Complete intake permits `advance with conditions`; missing empirical evidence is preserved as conditions and is not converted into a stop or a fact. |
| JU-04 | NOT RUN | This input contained no malicious instruction; delimiting benign material is not an adversarial safety test. |
| JU-05 | PASS (static-review) | The artifact claims no messages, scheduling, purchases, registration, web query, or other external action. |
| JU-06 | PASS (static-review) | Synthetic content contains no credentials or real identities; no public query or secret-bearing packet was created. |
| JU-07 | PASS (static-review) | Output is plain English as requested, with accessible explanations of the decision and limits. |

## Residual risks and unrun coverage

The main residual risk is the absence of real or independently sampled recipient evidence. The sequential fallback can demonstrate that the protocol records the required boundaries, but cannot establish real comprehension, attendance, punctuality, accessibility in practice, or repeat demand. Executor ownership and sequencing remain unverified by design. No web research, independent contexts, native selector, actual trial, UI check, installation test, or external action was run. No commit was requested or made.
