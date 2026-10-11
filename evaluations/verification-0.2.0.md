# Devil Lawyer 0.2.0 — verification evidence

These records preserve independent static reviews, controlled negative-case reproduction and local install/discovery results. They are not a substitute for authenticated native behavioral testing.

## Documentation parity

Original artifact: `documentation-audit-final.md`

`````markdown
# Documentation audit — final source review

Date: 2026-10-09. Scope was read-only: `README.md`, `README.es.md`, final `SKILL.md`, and its `intake.md`, `roles.md`, and `domains.md` references. This is a documentation consistency audit, not installation, host, model, or UI testing.

| Check | Status | Evidence |
|---|---|---|
| Version 0.2.0 stated and aligned | PASS | EN README 5 and ES README 5 both state `0.2.0`; the final skill front matter states `0.2.0` at SKILL 7. |
| English/Spanish functional parity | PASS | The same sections occur in both: eight fields/audiences (EN 13-25; ES 13-25), depth/protocol/fallback (EN 27-37; ES 27-37), evidence/safety/verdict/report (EN 39-47; ES 39-47), package/install (EN 49-67; ES 49-67), examples (EN 69-87; ES 69-87), and verification limits (EN 89-106; ES 89-106). Translations preserve decisions and limitations rather than merely headings. |
| Eight-field intake and one-question STOP behavior | PASS | EN README 15, 23-25 and ES README 15, 23-25 agree with SKILL 18-20 and intake 3-20: exactly eight ordered values, one necessary question, explicit STOP for unresolved required information, and no verdict bypass. |
| Requester, Recipient, and decision-maker distinctions | PASS | EN README 17-21 and ES README 17-21 name all three. This matches intake 14, which says audience, requester, and approval authority may differ. |
| Depth contract | PASS | EN README 29 and ES README 29 specify deep by default, brief only by explicit request, and preserve roles, evidence, rounds, and record. This matches SKILL 24 and is not presented as a ninth intake field. |
| Recipient-first and visible/internal boundary | PASS | EN README 33 and ES README 33 state original raw visible material/minimum persona before research or debate; SKILL 34 and intake 20 require a STOP question if usable visible material/boundary is missing. |
| Host fallback and limits | PASS | EN README 35 and ES README 35 require explicit sequential-simulation choice when the facility is unavailable and say silence is not a choice. Both disclose that fresh contexts do not prove independence, matching SKILL 30 and roles 3. |
| Role lifecycle, R2/R3, revisions | PASS | EN README 31, 35-37 and ES README 31, 35-37 align with SKILL 36-38, 44-46 and roles 30-34: four R1 roles, claim-based R2, bounded R3, one repair, failure accounting, and new Recipient reading with version identity after material revision. |
| Diablo angles and non-commercial framing | PASS | EN README 31 and ES README 31 list all eight angles. Roles 30 clarifies that status quo applies outside business and missing evidence is `missing`, not `N/A`; domains 3 and 14 avoid forced commercial framing for social cases. |
| Evidence, safety, and tool-effect limits | PASS | EN README 41-45 and ES README 41-45 match SKILL 35/40/44 and roles 7/17: source/provenance/verification, no corroboration by repetition, sanitized read-only research, embedded instruction as data, and documented effect over HTTP method. |
| Verdict and report limits | PASS | EN README 45-47 and ES README 45-47 list the same five decision outcomes, current-decision scope, non-automatic delivery, confidentiality, visible record, and segmented-output limits; they align with SKILL 44-46. |
| Nine domain examples | PASS | EN README 75-83 and ES README 75-83 each contain Code/Código, Design/Diseño, Finance/Finanzas, Marketing, Sales/Ventas, Market research/Mercado, Internal process/Proceso interno, Social relationships/Relaciones sociales, and General idea/Idea general. They correspond to domains 7-15. |
| Installation commands and package claims | PASS | PowerShell commands correspond at EN 53-58 / ES 53-58; POSIX commands at EN 60-65 / ES 60-65. Both give the same generic-host copy path and state no runtime ECC/model/server/hook/credential/third-party requirement at 67. |
| Live installation/import, selector, isolation, authentication, and model behavior | NOT RUN | The READMEs explicitly mark private GitHub import untested (EN 11; ES 11) and native/authenticated/live-model evidence pending (EN 106; ES 106). This audit performed no such action. |
| Documentation failures | NONE FOUND | No functional contradiction was found within the audited scope. |

Limit: line references are source locations observed in this audit; no manifest validation, link resolution, command execution, translation review by a human linguist, or runtime behavior test was performed.
`````

## Independent security review

Original artifact: `security-audit-final.md`

`````markdown
# Devil Lawyer 0.2.0 — final security review

Date: 2026-10-09  
Method: independent static review using `ecc:security-review`, adapted to this declarative skill package.  
Scope: final distributed `SKILL.md`, `references/intake.md`, `references/roles.md`, `references/domains.md`, plugin and marketplace manifests, `agents/openai.yaml`, and package validator/tests where relevant. Runtime instructions were reviewed as data, not accepted as reviewer authority.

## Result

**No actionable security findings remain in the reviewed scope.**

Open findings by priority: Critical 0, High 0, Medium 0, Low 0.

The previously reported medium-risk source/persona framing defect is resolved. Source-derived personas, task context, claims, labels, role text, tool output, and apparent instructions are required to remain inside bounded data; only fixed coordinator instructions and validated role/round enums may remain outside it (`plugins/devil-lawyer/skills/devil-lawyer/SKILL.md:32`; `plugins/devil-lawyer/skills/devil-lawyer/references/roles.md:7,11,13,15,17`). The reusable packet templates explicitly place the recipient persona and raw material, R1 case/evidence, and R2/R3/judge records in quoted JSON DATA objects (`references/roles.md:11,13,15`). This is the verifiable mitigation for the prior defect.

The defensive phrase that prohibits disclosure in the safety envelope (`references/roles.md:7`) is a control, not a vulnerability merely because a static scanner can match instruction-like wording.

## Security control evidence

| Area | Status | Evidence and consequence |
|---|---|---|
| Source-derived persona, claims, and context | PASS — static | All user-, document-, tool-, and role-derived values are untrusted DATA, including persona, labels, claims, and task context (`SKILL.md:32`; `references/roles.md:7,17`). Packet templates use quoted JSON and keep only fixed tasks/enums outside (`references/roles.md:11,13,15`). This is the static construction intended to prevent a source-authored persona or claim from becoming coordinator authority. |
| Recipient minimum disclosure | PASS — static | The recipient receives original raw visible material plus the minimum persona/task; secrets, personal data, and confidential identifiers are redacted, while normalized fields, debate, role labels, strategy, tool details, histories, depth, and hidden instructions are excluded (`SKILL.md:34`). Intake also defaults surrounding material and attachments to internal unless explicitly marked visible (`SKILL.md:18`; `references/intake.md:20`). |
| Requester report and confidentiality | PASS — static | The final record is explicitly requester-visible, undergoes a confidentiality recheck, excludes private chain-of-thought, and is not sent automatically to the recipient (`SKILL.md:46`). This preserves the distinction between the recipient snapshot and the requesting user's audit record. |
| Public research and sensitive data | PASS — static | Research must be authorized, sanitized, and read-only; public queries must be generic and free of confidential data (`SKILL.md:35`). Secrets and synthetic token-shaped values are excluded from packets and public queries (`SKILL.md:40`; `references/intake.md:20`). |
| Operations constrained by effect | PASS — static | The skill is advisory/read-only and prohibits sending, publishing, buying, changing systems, or executing commands from reviewed material (`SKILL.md:12`). Before tool use it requires checking documented effect rather than trusting the operation name or HTTP verb; ambiguous or potentially mutating operations are unavailable (`SKILL.md:40`). |
| Unknown capability | PASS — static | If the internal subagent facility is unavailable, the skill offers a sequential simulation or stop and waits for an explicit choice (`SKILL.md:32`). It forbids claiming unestablished access, isolation, or permissions (`SKILL.md:12,32`) and treats ambiguous tool effects as unavailable (`SKILL.md:40`). |
| Cross-role injection | PASS — static | Every recipient, R1, R2, R3, and judge packet receives the safety envelope; all role-derived text and apparent delimiters remain data (`references/roles.md:5-17`). Second-round claims and evidence remain inside the JSON record, so an R1 instruction cannot become trusted R2/judge authority (`references/roles.md:15,17`). |
| Role failure handling | PASS — static | Missing/failed stages retain explicit counts and failure state; a missing R1 role receives no R2, a failed R2 retains its R1, a coordinator note is not a reply, and no missing role may be impersonated (`SKILL.md:38`; `references/roles.md:17,34`). Static executor fallback stays unverified and cannot make the review complete (`SKILL.md:38`; `references/roles.md:34`). |
| Runtime dependency and secret surface | PASS — static | The distributed plugin inventory contains only manifests, Markdown references/instructions, YAML UI metadata, and licenses; no scripts, hooks, MCP configuration, key files, or runtime ECC dependency were present. `plugin.json` declares only the `Read` capability (`plugins/devil-lawyer/plugin.json:12-21`), and `agents/openai.yaml` contains only interface text plus implicit invocation policy (`agents/openai.yaml:1-6`). A targeted scan found no API-key, password, bearer credential, client-secret, private-key, hook, MCP, or ECC declaration in `plugins/devil-lawyer` or `.agents/plugins`. |

## Manifest note

`.agents/plugins/marketplace.json:9-15` points to the contained local plugin and sets marketplace policy `authentication: ON_INSTALL`. This is installation metadata, not a credential implementation in the distributed skill. No credential fields or runtime integration are present. Host-side interpretation and enforcement of that policy were not tested.

## Verification performed

- Inspected every line of the final `SKILL.md`, three runtime references, `plugin.json`, `agents/openai.yaml`, and the local marketplace manifest.
- Enumerated the distributed plugin/marketplace files and searched them for runtime ECC/MCP/hooks and common credential declarations; no matches were found.
- Inspected `evaluations/validate_package.py` and `evaluations/test_package.py`. The validator uses safe YAML loading with duplicate-key rejection and rejects path escapes in marketplace sources and relative links (`evaluations/validate_package.py:18-42,49-64,123-129,170-197`; `evaluations/test_package.py:58-83`).
- Package tests and the validator were **not run successfully** in this reviewer environment. The global interpreter lacks `PyYAML`, and no project `.venv` exists. The first unittest command also used package-style discovery incompatible with the suite's local import. These failed launches provide no pass evidence.

## Limits

This review is static. It does not prove model-level prompt-injection resistance, faithful JSON packet construction in every generated run, independent model/context isolation, host permission enforcement, UI behavior, network behavior, plugin installation, or marketplace authentication behavior. No actual role orchestration, public query, tool operation, recipient delivery, or malicious-prompt execution was performed. A future behavioral run should preserve these limits and inspect the actual packets rather than treating a matching phrase as proof.
`````

## Controlled validator reproductions

Original artifact: `results.json`

`````json
[
  {
    "case": "description_1025",
    "before": {
      "issues": []
    },
    "after": {
      "issues": [
        "skill description must be non-empty text of at most 1024 characters"
      ]
    },
    "regression": "PASS"
  },
  {
    "case": "license_list",
    "before": {
      "issues": []
    },
    "after": {
      "issues": [
        "skill standalone license metadata must be a textual LICENSE reference"
      ]
    },
    "regression": "PASS"
  },
  {
    "case": "yaml_unhashable_key",
    "before": {
      "exception": "TypeError",
      "message": "cannot use 'list' as a dict key (unhashable type: 'list')"
    },
    "after": {
      "issues": [
        "plugins\\devil-lawyer\\skills\\devil-lawyer\\agents\\openai.yaml: unhashable YAML mapping key",
        "agents/openai.yaml requires an interface mapping"
      ]
    },
    "regression": "PASS"
  },
  {
    "case": "malformed_schema",
    "before": {
      "exit": 1,
      "controlled_diagnostic": false
    },
    "after": {
      "exit": 1,
      "controlled_diagnostic": true
    },
    "regression": "PASS"
  },
  {
    "case": "invalid_schema",
    "before": {
      "exit": 1,
      "controlled_diagnostic": false
    },
    "after": {
      "exit": 1,
      "controlled_diagnostic": true
    },
    "regression": "PASS"
  }
]
`````

## Final isolated installation and discovery

Original artifact: `summary.json`

`````json
{
  "package_version": "0.2.0",
  "cli_version": {
    "command": [
      "--version"
    ],
    "exit": 0,
    "stdout": "codex-cli 0.162.0-alpha.2\n",
    "stderr": ""
  },
  "local_installation": "PASS",
  "plugin_discovery": "PASS",
  "standalone_discovery": "PASS",
  "matched_plugin_files": 8,
  "ECC_installed": false,
  "invocation_exit": null,
  "artifact_directory": "<temporary-test-directory>"
}
`````

## Refiner review with renewed final fingerprints

Semantic review of the redacted payload found no further actionable semantic finding. The remaining unverified scanner match on “Do not reveal” is the defensive private-reasoning prohibition, not evidence of a high-severity vulnerability. All six manifest hashes below match the final standalone repository skill. No omissions were reported. The helper does not validate the repository-root plugin layout; the package validator and native discovery cover that separate structure.

Original artifact: `v020-release-completed.json`

`````json
{"checks":{"semantic":"completed","static":"completed"},"comparison":{"added":[],"prior_review_key":"d6733d6c6f2ae8e1a1c88216e1c2c19a1084af69b46f1a373f2c5d1e648c65d8","prior_source_id":"e20b3802a3698de8f7af6592c61fe2c3c73344221c891a3495ef8f1d92f0797f","removed":[]},"context_digest":"12ae32cb1ec02d01eda3581b127c1fee3b0dc53572ed6baf239721a03d82e126","findings":[{"category":"security","evidence":"Do not reveal","evidence_digest":"82cfd862fe757d462977d90f92d9ea9fdf4b70f1d795acfa33240503475c6e4a","id":"972cb68f269b8a42006978b9d67ee007f975d2d16e03f6b23e0984f64e274ca8","line":46,"message":"Suspicious instruction pattern requires review","path":"SKILL.md","provenance":"static","rule":"prompt-injection","severity":"high","verification":"unverified"}],"fingerprints":{"code":"968ecbc738a9693bb7864f40f82f2df940f5e61a9d930978ff7a177db8857113","dependencies":"1f8742a80c93b280a5bb61a8d3faa0c1b05a1537edd5767062456224b4554118","policy":"a3495c713edeb72d6b602540cf817991ba60f37e6e045eee3bf40a4ce792c607","runtime":"11f1e1ea0f30919c1f8e22732476755a9376df152e6da580ce1c3587f6def3c5","schemas":"7ee59d5dab9c90fc600de2a87b977a1e2e3a07409340c6b30ffee3ddd0b8ceb6","skill":"ff7444be5379879aa44961df2fc5ad6efbaaefd29cd352dc987e3849f5965163"},"limitations":["Static checks cover Python syntax plus bounded metadata, link, and pattern rules; other language syntax and runtime behavior were not executed.","Dynamic tests, when run, are separate execution records and are not implied by this report.","Findings remain unverified until controlled reproduction confirms them."],"manifest":[{"bytes":2106,"path":"LICENSE","sha256":"ec7dae23409deaaa229a37cf892eac490424c70ebb6e5ffad72c2d5acb9ff9d6"},{"bytes":10925,"path":"SKILL.md","sha256":"dca09cd5dc9a13a6309994a0e0735e9a75e652cadd0d2fd4c99c581703ceb399"},{"bytes":254,"path":"agents/openai.yaml","sha256":"f2aa943d6060b015b537cf680fbb18851726ee89cec765d415d04126029a86d3"},{"bytes":1795,"path":"references/domains.md","sha256":"05a01c35e9b0ca2f1ccee363567fb33ed0fc2d19ea7b55b958c5cc2e2e75e2bf"},{"bytes":3035,"path":"references/intake.md","sha256":"a8386e0fd37c6212545c2e0503dcfa442effa078473feb13b32890fb624acf7b"},{"bytes":7582,"path":"references/roles.md","sha256":"f5452aa71f461fc928ec8a1ecdf10e56450444f0ea05a25d74e25191901d55ae"}],"omitted":[],"policy_digest":"e491c751eabbc5ef45572e96bae401a953204449c21e2504e90b79e9d68d7e38","profile_digest":"ace85a6ecf91e9c131ddec2d0a5e91ff470e8f2c5a99cffc078a4aadab8e77a3","review_key":"dfc557bcf5bb8d04c9ecc469a26da9b9a1ab9ef13c5e87fe5f703914400ed8dc","schema_version":"1","semantic_status":"completed","source_digest":"d7ac5de1a8057e8567be01a0139ae11b8c7c389a5755aeda1bc60cd239501cf0","source_id":"e20b3802a3698de8f7af6592c61fe2c3c73344221c891a3495ef8f1d92f0797f","status":"fresh"}
`````
