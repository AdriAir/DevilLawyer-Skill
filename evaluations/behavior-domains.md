# Intake and domain-routing evidence

This report covers **INTAKE/DOMAIN-ROUTING ONLY**. It is not nine full debate passes. The cases are independent synthetic inputs; no case's facts, answers, or evidence are inserted into another case. Generation used the raw fenced YAML fields from `evaluations/cases.md`, the current intake/domain/role guidance, and these declared host conditions: native selector available, internal subagents unavailable, web unavailable. No action authorization was inferred.

## C-01 — code

### Raw input

```yaml
id: C-01
proposal: "Adopt an in-memory cache for GET /weather to reduce p95 latency."
domain-current: "A small ASP.NET API currently calls the provider on every request; no cache exists."
objective-decision: "Decide whether to prototype this change for the next release."
recipient: "API maintainer who owns reliability and can approve a prototype."
recipient-visible-vs-internal: "visible: maintainer persona, proposal, current state, objective; internal: role arguments and hidden test hypotheses."
success: "A reversible prototype has a measured latency improvement and no stale-data or outage regression."
resources-limits: "One engineer, one week, provider rate-limit documentation, synthetic data only; no production writes."
horizon-maturity: "Two-week prototype decision; early-stage idea."
```

### Generated next user-visible turn

> The intake is complete. I understand a proposal to prototype an in-memory cache for `GET /weather` in a small ASP.NET API, for an API maintainer deciding on the next release. Success means measured p95 improvement without stale-data or outage regression, within one engineer, one week, synthetic data, and no production writes. This is an early-stage, two-week prototype decision. The host cannot provide the required internal subagents and web research is unavailable. I can continue as an explicitly sequential, simulated review; it will be non-independent and cannot substitute for real-user or external evidence. No action will be taken.

### Empirical scope

Observed only: all eight fields resolved; code routing is supported by the explicit ASP.NET/API context; sequential fallback disclosed; no research or action claimed.

## C-02 — design

### Raw input

```yaml
id: C-02
proposal: "Move the primary action in a settings dialog to the bottom right."
domain-current: "Desktop web dialog has a top-right Save button and a Cancel link beside it."
objective-decision: "Choose whether to prepare a revised proposal and then test it with five real representative users."
recipient: "Product designer responsible for the settings flow."
recipient-visible-vs-internal: "visible: designer persona, screenshot description, proposal, objective; internal: adversarial arguments and role labels."
success: "The revised proposal can be tested: representative users find Save without errors, keyboard focus remains predictable, and task time does not worsen."
resources-limits: "Five simulated first readings for evaluation only, no analytics access, one design iteration; a real-user test is the next step."
horizon-maturity: "One-week usability test; existing interaction with a small proposed change."
```

### Generated next user-visible turn

> The intake is complete. I understand a small desktop web dialog change moving Save from the top right to the bottom right, for a product designer deciding whether to prepare a revised proposal and test it with five representative users. Success means users find Save without errors, keyboard focus stays predictable, and task time does not worsen. The scope allows simulated first readings for evaluation, with real-user testing as the next step. The host lacks internal subagents and web research. I can continue with an explicitly sequential, simulated review, which is non-independent and is not usability evidence. No real users will be contacted and no action will be taken.

### Empirical scope

Observed only: all eight fields resolved; design routing is supported by dialog and interaction details; simulation limits preserved; no real-user evidence claimed.

## C-03 — finance

### Raw input

```yaml
id: C-03
proposal: "Allocate 10% of a fictional EUR 100,000 operating reserve to a broad index fund."
domain-current: "The reserve covers six months of synthetic fixed costs; no investment policy is defined."
objective-decision: "Decide whether to commission a suitability review, not whether to place an order."
recipient: "Fictional finance committee with authority to request analysis."
recipient-visible-vs-internal: "visible: committee persona, synthetic figures, proposal, objective; internal: objections, role deliberation, and test prompts."
success: "A review documents liquidity, loss tolerance, fees, tax assumptions, and approval conditions before any transaction."
resources-limits: "Synthetic numbers only, no broker access, no personal financial data, analysis limited to one meeting."
horizon-maturity: "One-month review; exploratory proposal."
```

### Generated next user-visible turn

> The intake is complete. I understand an exploratory proposal to commission a suitability review of allocating 10% of a fictional EUR 100,000 reserve to a broad index fund. The fictional finance committee is the recipient; success requires documenting liquidity, loss tolerance, fees, tax assumptions, and approval conditions before any transaction. Inputs are synthetic, there is no broker access or personal data, and the review fits one meeting within a month. The host lacks internal subagents and web research. I can continue as an explicitly sequential, simulated review, non-independent and limited to the supplied facts. This will not place an order or provide a transaction decision.

### Empirical scope

Observed only: all eight fields resolved; finance routing matches a suitability-review objective; synthetic scope and no-order boundary preserved; no jurisdiction or transaction advice invented.

## C-04 — marketing

### Raw input

```yaml
id: C-04
proposal: "Run an English landing-page experiment claiming setup is 30% faster."
domain-current: "The fictional product has a Spanish page and no measured setup baseline."
objective-decision: "Decide whether to prepare a copy experiment with a substantiated claim."
recipient: "Marketing lead who approves public copy."
recipient-visible-vs-internal: "visible: lead persona, product context, proposal, objective; internal: challenge angles and alternate wording."
success: "The claim is backed by a defined measurement, copy is understandable, and the experiment has a stop condition."
resources-limits: "Synthetic traffic plan, no ad spend, one copywriter, two weeks."
horizon-maturity: "Two-week experiment design; claim is unvalidated."
```

### Generated next user-visible turn

> The intake is complete. I understand a two-week proposal for an English landing-page copy experiment about setup speed, for a marketing lead who approves public copy. The current product page is Spanish and no setup baseline is measured. Success requires a defined measurement, understandable copy, and a stop condition; the traffic plan is synthetic, with no ad spend and one copywriter. The claim is currently unvalidated. The host lacks internal subagents and web research. I can continue with an explicitly sequential, simulated review, non-independent and limited to the supplied facts. No public copy will be published.

### Empirical scope

Observed only: all eight fields resolved; marketing routing is supported by the claim/baseline/stop-condition facts; the claim remains unvalidated; no publication or measurement was claimed.

## C-05 — sales

### Raw input

```yaml
id: C-05
proposal: "Offer a fictional pilot with a 14-day cancellation clause to three mid-market prospects."
domain-current: "Sales has a standard 30-day pilot and no approved 14-day template."
objective-decision: "Decide whether to draft an experiment for legal and sales-ops review."
recipient: "Sales operations manager who controls approved templates."
recipient-visible-vs-internal: "visible: manager persona, current template state, proposal, objective; internal: negotiation hypotheses and role arguments."
success: "No prospect receives unapproved terms; a reviewed template records price, scope, cancellation and owner."
resources-limits: "Three synthetic prospects, no outbound messages, legal review slot unavailable this week."
horizon-maturity: "One-month pilot design; proposed change is unapproved."
```

### Generated next user-visible turn

> The intake is complete. I understand a one-month proposal to draft, for legal and sales-ops review, a fictional pilot changing the standard cancellation period from 30 to 14 days. The sales-operations manager controls approved templates. Success means no unapproved terms reach prospects and a reviewed template records price, scope, cancellation, and owner. The exercise uses three synthetic prospects, sends no outbound messages, and legal review is unavailable this week. The host lacks internal subagents and web research. I can continue as an explicitly sequential, simulated review, non-independent and limited to drafting analysis. No prospect will be contacted and no terms will be approved.

### Empirical scope

Observed only: all eight fields resolved; sales routing and read-only boundary are explicit; legal review unavailability retained; no outreach or approval claimed.

## C-06 — market

### Raw input

```yaml
id: C-06
proposal: "Enter a fictional regional market with a localized starter plan."
domain-current: "The product is sold in one region; demand, regulation and competitors in the target region are unknown."
objective-decision: "Decide whether to fund discovery interviews and a regulatory scan."
recipient: "Strategy lead who can authorize research budget."
recipient-visible-vs-internal: "visible: lead persona, known region facts, proposal, objective; internal: debate and unverified market hypotheses."
success: "Discovery produces a target segment, regulatory constraints, competitor map and a quantified go/no-go threshold."
resources-limits: "Synthetic budget of EUR 5,000, four interviews, no market purchase or public claims."
horizon-maturity: "Six-week discovery; early market hypothesis."
```

### Generated next user-visible turn

> The intake is complete. I understand an early hypothesis about entering a fictional regional market with a localized starter plan, and a decision about funding discovery interviews plus a regulatory scan. The strategy lead is the recipient. Success means discovery produces a target segment, regulatory constraints, a competitor map, and a quantified go/no-go threshold. The proposed six-week work has a synthetic EUR 5,000 budget, four interviews, no market purchase, and no public claims. Demand, regulation, and competitors remain unknown. The host lacks internal subagents and web research. I can continue as an explicitly sequential, simulated review, non-independent and limited to supplied facts; it cannot replace discovery evidence.

### Empirical scope

Observed only: all eight fields resolved; market routing preserves unknown demand/regulation/competitors as unknowns; discovery scope is not converted into a market conclusion; no research performed.

## C-07 — internal-process

### Raw input

```yaml
id: C-07
proposal: "Require a lightweight incident review within two business days after every synthetic outage."
domain-current: "The fictional team records incidents inconsistently and has no review deadline."
objective-decision: "Decide whether to pilot the process for one month."
recipient: "Engineering manager who owns the incident process."
recipient-visible-vs-internal: "visible: manager persona, current process, proposal, objective; internal: challenge arguments and private role notes."
success: "Reviews name impact, timeline, owner and follow-up; completion rate is observable without blaming individuals."
resources-limits: "One template, no new tooling, four synthetic incidents, read-only recommendation."
horizon-maturity: "One-month pilot; process change is draft."
```

### Generated next user-visible turn

> The intake is complete. I understand a draft process change requiring a lightweight review within two business days after each synthetic outage, for an engineering manager deciding whether to run a one-month pilot. Success means reviews record impact, timeline, owner, and follow-up, while completion remains observable without blaming individuals. The scope is one template, no new tooling, four synthetic incidents, and a read-only recommendation. The host lacks internal subagents and web research. I can continue as an explicitly sequential, simulated review, non-independent and limited to these facts. No process will be imposed and no personnel information will be added.

### Empirical scope

Observed only: all eight fields resolved; internal-process routing is supported by owner, measurement, workload scope, and humane boundary; no personnel data or rollout claimed.

## C-08 — social

### Raw input

```yaml
id: C-08
proposal: "Publish a fictional weekly post explaining one accessibility improvement."
domain-current: "The team has improvements but no publishing cadence or accessibility review checklist."
objective-decision: "Decide whether to draft a four-post educational series."
recipient: "Community editor who reviews drafts before publication."
recipient-visible-vs-internal: "visible: editor persona, improvement examples, proposal, objective; internal: persuasion attempts and review arguments."
success: "Posts are accurate, understandable, accessible, and each source or limitation is disclosed."
resources-limits: "Four synthetic drafts, no platform posting, two editorial hours per week."
horizon-maturity: "One-month draft series; educational concept."
```

### Generated next user-visible turn

> The intake is complete. I understand an educational concept for a one-month, four-post series explaining accessibility improvements, for a community editor who reviews drafts before publication. Success requires accurate, understandable, accessible posts with each source or limitation disclosed. The team has no publishing cadence or accessibility checklist; the scope is four synthetic drafts, no platform posting, and two editorial hours per week. The host lacks internal subagents and web research. I can continue as an explicitly sequential, simulated review, non-independent and limited to supplied facts. No post will be published and no audience response will be claimed.

### Empirical scope

Observed only: all eight fields resolved; social routing preserves source, limitation, accessibility, and no-publication constraints; no publication or social evidence claimed.

## C-09 — general-idea

### Raw input

```yaml
id: C-09
proposal: "Create a fictional neighborhood tool library."
domain-current: "There is an idea and a volunteer, but demand, insurance, storage and maintenance are unknown."
objective-decision: "Decide whether to run a small feasibility survey."
recipient: "Volunteer coordinator deciding what to investigate next."
recipient-visible-vs-internal: "visible: coordinator persona, idea, known facts, objective; internal: debate, uncertainty, and role prompts."
success: "The survey measures demand, safe storage, maintenance ownership and a feasible trial boundary."
resources-limits: "Ten synthetic responses, no money collected, no equipment transfer, one weekend."
horizon-maturity: "Two-week feasibility check; raw idea."
```

### Generated next user-visible turn

> The intake is complete. I understand a raw idea for a fictional neighborhood tool library and a decision about running a small feasibility survey, for a volunteer coordinator deciding what to investigate next. Success means measuring demand, safe storage, maintenance ownership, and a feasible trial boundary. The two-week check allows ten synthetic responses over one weekend, with no money collected or equipment transferred. Demand, insurance, storage, and maintenance remain unknown. The host lacks internal subagents and web research. I can continue as an explicitly sequential, simulated review, non-independent and limited to these facts; it cannot establish feasibility. No lending or transfer will begin.

### Empirical scope

Observed only: all eight fields resolved; general-idea routing preserves safety/stewardship unknowns and bounded survey scope; no feasibility verdict or lending action claimed.

## Independent assessment

Assessment was performed after generation against `evaluations/rubric.md`; it is limited to intake and domain routing.

- **Fixture coverage: PASS (static).** Each fixture contains all eight fields in the prescribed order. The generated turns summarize the decision and offer the sequential fallback without redundant questions. They do not restate every field or the visible/internal boundary, so complete eight-field summary fidelity is not established by this run.
- **Adaptive prerequisite discipline: PASS (static).** Domain details are used only where material: API behavior for code, interaction behavior for design, suitability scope for finance, baseline/claim for marketing, approved terms for sales, unknown discovery evidence for market, measurement/owners for process, sources/accessibility for social, and safety/stewardship for the general idea. No extra universal questionnaire was introduced.
- **Unknown handling and STOP boundary: PASS for this stage (static).** Unknown demand, regulation, competitors, and insurance remain unknown or evidence gaps. Because each objective asks whether to prepare or fund bounded discovery/review, the generated next turn offers the allowed sequential fallback instead of issuing a verdict. A later request for an immediate commitment would require STOP; that later branch was not generated here.
- **Native selector fallback: NOT EXERCISED.** No necessary field was missing, so no choice menu was needed. The available native selector is therefore not evidenced by these fixtures.
- **Recipient/internal separation: PASS (static).** Outputs expose only the stated recipient-facing summary and scope. Internal role arguments, hidden hypotheses, and prompts are not leaked.
- **Action boundary: PASS (static).** No output claims publication, outreach, order placement, lending, process rollout, measurement, research, or real-user testing. The sequential path is explicitly simulated and non-independent.
- **Scope and reproducibility: PASS.** This is nine independent synthetics and one stage decision per case, not nine completed debate records. Web and subagent-dependent evidence was not run. No external action or user-owned chat was used.

Residual risk: these cases do not empirically exercise missing-field clarification, a native selector interaction, a later STOP branch, recipient snapshot content, redaction, or the full R1/R2/R3 debate. Those remain unverified by this report.
