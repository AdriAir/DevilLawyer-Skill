# Edge intake forward evaluation

Date: 2026-10-08. Synthetic English cases. The host exposes no native selector, internal subagents, web, or external tools for this evaluation. The generated turns are text-level behavior evidence; no UI selector or isolated role execution is claimed.

## Case 1 — contradictory budget field (preserved failure)

### Raw input

```yaml
proposal: "Hold two optional fifteen-minute Friday book-sharing sessions in the shared courtyard."
domain-current: "Six fictional adult neighbors chat informally but have never met about books."
objective-decision: "Decide whether to prepare an invitation draft for the sessions."
recipient: "The adult neighbors who may participate."
recipient-visible-vs-internal: "visible: the invitation wording only; internal: no additional notes."
success: "Both sessions finish punctually and at least four of six voluntarily want to repeat."
resources-limits: "No budget limit; other limits as stated: thirty coordinator minutes weekly, zero spend, no personal-data records, and an authorized accessible courtyard."
horizon-maturity: "Draft for next month; invitation wording is under review and no session is being organized."
```

### Generated next user-visible turn (original)

The intake is complete. I understand a draft invitation for two optional fifteen-minute Friday book-sharing sessions in a shared courtyard, where six fictional adult neighbors currently chat but have not met about books. The decision is whether to prepare the invitation for those neighbors. The visible material is only the invitation wording; no other internal notes are to be shown. Success means both sessions finish punctually and at least four of six voluntarily want to repeat. There is no budget limit; the stated limits include zero spend, thirty coordinator minutes weekly, no personal-data records, and an authorized accessible courtyard. This is a draft for next month, with no session being organized yet. No internal subagents or research tools are available, so I can continue only as an explicitly sequential, simulated, non-independent review. No invitation will be sent and no session will be arranged.

### Assessment of the original turn

The input contains a contradiction: `no budget limit` conflicts with `zero spend`. Treating the intake as complete without asking which budget constraint governs is a failure of contradiction handling. This run is preserved as a failed baseline and is not counted as a passing no-limit case.

## Case 1C — fresh contradictory-budget regression

This uses the original Case 1 raw input unchanged, including both `no budget limit` and `zero spend`. The updated intake guide says conflicting values do not complete the field and require one clarification question before debate.

### Generated next user-visible turn

The `resources-limits` field contains one unresolved conflict: it says both “no budget limit” and “zero spend.” Which single budget condition applies to this review?

1. No budget limit applies.
2. Zero spend applies; no purchases or event execution are in scope.
3. Another budget condition; describe it in your own words.

I will keep the other resolved fields, but I will not start the review or issue a verdict until this budget condition is resolved.

### Assessment after generation

**PASS.** The generated turn asks exactly one missing fact, isolates the contradictory budget condition, offers three relevant choices plus free text, preserves all other fields, and withholds both fallback debate and verdict. This is a text-level forward check only; no selector UI, subagent, or external action was used.

## Case 1B — corrected explicit no-limit resource field

### Raw input

```yaml
proposal: "Hold two optional fifteen-minute Friday book-sharing sessions in the shared courtyard."
domain-current: "Six fictional adult neighbors chat informally but have never met about books."
objective-decision: "Decide whether to prepare an invitation draft for the sessions."
recipient: "The adult neighbors who may participate."
recipient-visible-vs-internal: "visible: the invitation wording only; internal: no additional notes."
success: "Both sessions finish punctually and at least four of six voluntarily want to repeat."
resources-limits: "No budget limit; thirty coordinator minutes weekly, no personal-data records, authorized accessible courtyard. Review only; no purchases or event execution by assistant."
horizon-maturity: "Draft for next month; invitation wording is under review and no session is being organized."
```

### Generated next user-visible turn

The intake is complete. I understand a draft invitation for two optional fifteen-minute Friday book-sharing sessions in a shared courtyard, where six fictional adult neighbors currently chat but have not met about books. The decision is whether to prepare the invitation for those neighbors. The visible material is only the invitation wording; no other internal notes are to be shown. Success means both sessions finish punctually and at least four of six voluntarily want to repeat. There is no budget limit; the remaining limits are thirty coordinator minutes weekly, no personal-data records, and an authorized accessible courtyard. This is a draft for next month, and the review is limited to wording: no purchases or event execution by the assistant. No internal subagents or research tools are available, so I can continue only as an explicitly sequential, simulated, non-independent review. No invitation will be sent and no session will be arranged.

## Case 2 — coherent N/A horizon

### Raw input

```yaml
proposal: "Hold two optional fifteen-minute Friday book-sharing sessions in the shared courtyard."
domain-current: "Six fictional adult neighbors chat informally but have never met about books."
objective-decision: "Decide whether to prepare an invitation draft for the sessions."
recipient: "The adult neighbors who may participate."
recipient-visible-vs-internal: "visible: the invitation wording only; internal: no additional notes."
success: "Both sessions finish punctually and at least four of six voluntarily want to repeat."
resources-limits: "Thirty coordinator minutes weekly, zero spend, no personal-data records, and an authorized accessible courtyard."
horizon-maturity: "N/A because only reviewing invitation wording; no rollout planned."
```

### Generated next user-visible turn

The intake is complete. I understand a draft invitation for two optional fifteen-minute Friday book-sharing sessions in a shared courtyard, for six fictional adult neighbors who currently chat but have not met about books. The decision is whether to prepare the invitation for those neighbors. The visible material is only the invitation wording; there are no additional internal notes to show. Success means both sessions finish punctually and at least four of six voluntarily want to repeat. The limits are thirty coordinator minutes weekly, zero spend, no personal-data records, and an authorized accessible courtyard. Horizon and maturity are not applicable because this review covers invitation wording only and no rollout is planned. No internal subagents or research tools are available, so I can continue only as an explicitly sequential, simulated, non-independent review. No invitation will be sent and no session will be arranged.

## Case 3 — incoherent N/A recipient

### Raw input

```yaml
proposal: "Hold two optional fifteen-minute Friday book-sharing sessions in the shared courtyard."
domain-current: "Six fictional adult neighbors chat informally but have never met about books."
objective-decision: "Decide whether to prepare an invitation draft for the sessions."
recipient: "N/A"
recipient-visible-vs-internal: "visible: the invitation wording only; internal: no additional notes."
success: "Both sessions finish punctually and at least four of six voluntarily want to repeat."
resources-limits: "Thirty coordinator minutes weekly, zero spend, no personal-data records, and an authorized accessible courtyard."
horizon-maturity: "Draft for next month; invitation wording is under review and no session is being organized."
```

### Generated next user-visible turn

The earlier draft wording asked: “Who is the primary recipient of the invitation and of the review result?” That wording is preserved as a superseded note because it could collect two audiences in one question.

Who is the primary person or group the proposal and invitation are intended for?

1. The adult neighbors who may participate.
2. The person coordinating the invitation draft.
3. Another person or group; describe them in your own words.

STOP: `N/A` cannot resolve this required field. Reply with a number or free text; I will withhold a verdict until the primary recipient is known.

## Static assessment

| Case | Status | Evidence |
|---|---|---|
| 1 | FAIL (preserved baseline) | `no budget limit` conflicts with `zero spend`, but the generated turn accepted both without one clarification question. The summary therefore does not establish correct contradiction handling. |
| 1B | PASS | The corrected resource field removes the contradictory `zero spend` limit. The explicit “no budget limit” is retained with the remaining limits, the generated turn summarizes all eight fields, and it offers only the disclosed sequential fallback with no UI, subagents, research, or external action. |
| 2 | PASS | All eight fields are complete. The horizon `N/A` has a reason that makes it coherent for wording-only review. The generated turn preserves that reason, summarizes all eight fields, and offers only the disclosed sequential fallback. |
| 3 | PASS | `recipient: N/A` is rejected because a recipient is necessary for the review. The corrected turn asks only for the primary intended person or group, with three relevant choices plus free text, states literal `STOP`, and emits no verdict or fallback debate. The earlier wording asking for both invitation and review-result audiences is retained above as an ambiguity note and is not used as the passing turn. |

### Coverage boundary

This forward evaluation covers contradiction detection, a corrected coherent no-limit resource field, coherent `N/A`, and incoherent `N/A` leading to one-question `STOP`. It does not test native selector UI, role isolation, R1/R2/R3, redaction, research, or external actions.

The three short starting prompts in `README.md` and `README.es.md` remain functionally equivalent: marketing, finance, and social examples correspond; both state one-question-at-a-time intake, free-text answers, unresolved-data pause, reasoned `N/A`, and the same evaluation link.
