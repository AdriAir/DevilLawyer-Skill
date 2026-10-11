# Devil Lawyer 0.1.0 — verification record

Date: 2026-10-08. Package version: 0.1.0. Development used optional development tooling; none is a runtime dependency. This record covers pre-publication validation. No normal-profile installation was performed. Repository URLs and local machine paths have been omitted from this historical record.

## Passed checks

| Check | Method and result | Assurance boundary |
|---|---|---|
| Distribution validation | `python evaluations/validate_package.py --schema .test-artifacts/plugin.schema.json`: PASS, official Agent Plugins 1.0.0 schema checked | JSON/YAML/frontmatter, names/version, policy types, contained paths, links, required references and three byte-identical English licenses |
| Structural regression | `python -m unittest discover -s evaluations -p test_package.py -v`: **14/14 PASS** | Negative cases include duplicate keys, missing/escaping links, orphan guide, license drift, malformed types/UTF-8 and disabled discovery; not model behavior |
| Skill-creator | Official `quick_validate.py plugins/devil-lawyer/skills/devil-lawyer`: `Skill is valid!` | Frontmatter/skill structure, not behavioral validation |
| Final local installation | Codex CLI **0.162.0-alpha.2**, new `.test-artifacts/codex-profile-final-2`, local marketplace add/list and plugin add/list: exit 0 | New test profile only; no credentials copied and no ECC installed |
| Native discovery | App-server `skills/list`, final test profile: enabled `devil-lawyer:devil-lawyer`, correct display metadata, no load errors | Native registration and discovery; does not prove model invocation or selector UI |
| Installed integrity | SHA-256 comparison of all **8 plugin files** against source: identical | Includes current instructions, references, manifests, metadata and license |
| Documentation parity | Independent read-only comparison of README EN/ES: equivalent functional instructions | Static review of installation, intake, protocol, examples, limits and license translation |
| Intake generation | Corrected runs B–D in [behavior-intake.md](behavior-intake.md) | Numbered selector fallback, one requested fact, unknown-answer STOP without verdict, Spanish/English; no native UI |
| Intake edge cases | [behavior-edge-intake.md](behavior-edge-intake.md) | Coherent `no budget limit` and reasoned horizon `N/A` preserved; unresolved recipient `N/A` produces one question and STOP without verdict. Case 1C detects conflicting budget values and asks one clarification. Generated turns, not native UI. |
| Coordinated role execution | [behavior-debate-final.md](behavior-debate-final.md) | Actual internal recipient, four fresh R1 actors, four R2 replies, coordinator judge, fresh revised recipient; synthetic social fixture only, trace-backed rather than a reproducible CLI harness |
| Single adversarial fixture | Corrected role run retained malicious text as data, redacted token and excluded irrelevant internal sentinel; no role tool/action/private-disclosure call observed | One fixture; not universal injection immunity or host-enforced isolation certification |

Validation ran on Python 3.14 with optional development-only PyYAML 6.0.3 and jsonschema 4.26.0 in ignored `.test-artifacts/validation-deps`. The official schema and local machine outputs are also ignored; do not ship them as runtime requirements. Reproduce the structural commands using the README's isolated-development instructions. Repeat local installation with a fresh child-process `CODEX_HOME`, not the user's normal profile.

## Partial coverage and failed observations

- [behavior-domains.md](behavior-domains.md) records nine generated domain/intake turns. This is routing coverage, **not nine full debates**. The summaries do not repeat every field or the visible/internal boundary; complete summary fidelity is not established by this test.
- [behavior-fallback.md](behavior-fallback.md) records a sequential simulated review and an unavailable Executor with an explicitly unverified checklist. Its R2 notes are **partial**: three notes plus a coordinator availability note do not establish complete cross-role replies. Missing work remains visible.
- The historical first intake run bundled recipient and authority: FAIL, retained and superseded by corrected runs B–D.
- The first no-limit edge fixture contained conflicting budget restrictions and generation silently retained them: FAIL, preserved in the edge report. The intake guide now explicitly requires a one-fact clarification of conflicting values. Case 1B demonstrates a coherent no-limit response with corrected input; Case 1C reuses the original conflicting input after the instruction update and correctly asks one budget question without debate or verdict.
- [behavior-debate.md](behavior-debate.md) is a failed historical evaluator harness, including incomplete R2 context. Its unrequested user-owned chats were archived; that run is excluded from final conformance evidence. The corrected run used internal agents only.
- Corrected R1 outputs sometimes overlabel assumptions as facts, omit claim IDs or collide with evidence IDs. Originals remain visible. Coordinator-assigned/scoped IDs and judge rejection of unsupported factual assumptions address the observed errors; repetition of an objection is not counted as evidence.

## Blocked and pending

| Check | Status | Reason / next prerequisite |
|---|---|---|
| Native clean-profile model invocation | **BLOCKED** | Attempted with isolated profile; authorized network retry returned **HTTP 401: Missing bearer or basic authentication**. No user credentials were copied. Needs an authenticated authorized test profile. |
| Clickable native selector UI | **NOT RUN** | Text outputs and tool availability checks do not exercise native UI. Needs an authenticated interactive test host. |
| Full behavioral corpus | **NOT RUN in full** | Nine-domain full debates, a genuinely unconditioned `advance` case, timed question continuation, actual R3 activation, public-query sanitization with research tools, and all verdict outcomes need additional forward tests. Written requirements/cases are not counted as passes. |
| Standalone native invocation | **NOT RUN** | Standalone structure/licenses/contained references passed static checks, but no separate authenticated model run completed. |
| Private GitHub import | **PENDING** | Not exercised in pre-publication validation. Needs published content, repository access and a separate isolated import check. Local installation does not demonstrate this path. |
| Other-device/system integration and real-user research | **NOT RUN** | Outside current installation scope; generic Agent Skills portability is structural, not a promise of named integrations. |

## Final independent security review

An independent security reviewer inspected the current runtime instructions, role packets, manifests, licenses and behavioral records after corrections. **No remaining actionable high, medium or low security findings** were reported. The review confirmed trusted tasks outside reviewed data, per-packet boundaries, minimum recipient context before research, read-only authorized research, sanitized generic queries, no runtime scripts/hooks/MCP/credentials, and identical license copies. This is static review plus the one executed synthetic adversarial fixture; it does not prove general resistance to injection or external query sanitization at runtime.

The implementation is ready for review and isolated authenticated testing. This record does not claim full acceptance-suite completion.
