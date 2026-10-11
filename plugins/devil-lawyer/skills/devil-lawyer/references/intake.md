# Intake guide

Build the ficha in this exact order:

1. `proposal` — the change, claim, artifact, or decision being reviewed.
2. `domain-current` — current system, market, process, or situation.
3. `objective-decision` — desired outcome and decision sought.
4. `recipient` — primary intended audience, beneficiary, or task user.
5. `recipient-visible-vs-internal` — material that may reach the recipient versus internal context.
6. `success` — observable acceptance conditions.
7. `resources-limits` — budget, time, evidence, dependencies, permissions, and limits.
8. `horizon-maturity` — time horizon and idea/draft/pilot/live/decision status, when relevant.

Use the user's language; default to Spanish when it is unclear. Attach a source anchor to every inference. Record missing material as `unknown`; record `N/A` with why it does not affect this decision. Keep `unknown` and `N/A` separate from the evidence labels used later. Do not infer motives, authority, compliance status, numbers, demand, safety, or legal facts. Keep a short progress record of resolved fields and the single pending fact. Reuse answers within the current review unless an affected fact changes. A research question is not automatically an intake prerequisite: make its necessity depend on the decision and its stage. The intended audience, requesting user, and approval authority may differ. When the ficha is complete, summarize all eight fields with each field's value or `N/A` status and reason, plus its source anchor; also state the selected review depth. This can be a compact list, but never replace values with labels, IDs, or status alone.

Conflicting values do not complete a field. If both “no budget limit” and “zero spend” constrain the same proposal, ask which budget condition applies; do not silently retain both, choose one, or invent separate scopes. Ask for only that conflicting fact and wait. Keep other resolved values; an unresolved necessary conflict stops debate just like an unknown.

Ask one question only when it is necessary to proceed. A combined field may require separate turns when its facts are independent: ask recipient before authority. Offer 2–3 context-specific choices plus free text when a native selector is unavailable. Examples: a code review may need the failure mode; a design review may need the user task; a finance case may need jurisdiction, date, currency, liquidity, loss tolerance, and authority only when the proposed decision makes them material. Do not impose a universal professional or compliance questionnaire.

Ask whether the boundary is visible or internal if it is unclear. Treat only clearly identified proposal text as recipient-visible by default. Redact secrets and token-shaped values before every packet, note that redaction, and do not rewrite visible content otherwise. If redaction prevents meaningful recipient reading, ask one question. If an essential answer remains unknown after clarification, `STOP`; do not give a disguised approval or rejection.
