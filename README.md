# Devil Lawyer

Devil Lawyer is an open, read-only review skill for evaluating ideas, proposals, plans, decisions, and visible materials. It helps users clarify a decision, examine it through five perspectives, distinguish evidence from assumptions, and identify practical next steps.

Version: **0.3.0** · License: [MIT](LICENSE) · Language: English and Spanish.

## What it does

- Guides the requester through eight context fields, asking one necessary missing question at a time.
- Separates the requester, the proposal's recipient, decision-makers, recipient-visible material, and internal context.
- Reviews the proposal through Proponent, Devil's Advocate, First Principles, Executor, and Recipient perspectives, followed by an evidence-based judgment.
- Labels facts, calculations, inferences, hypotheses, and missing evidence; it does not treat agreement as proof.
- Produces a recommendation and visible argument record in the user's language.

The skill is advisory. It does not send or publish reports, contact people, execute reviewed instructions, make purchases, or change systems. Its output is not professional, legal, financial, medical, or organizational approval.

## Use it

### Standalone Agent Skill

Copy the complete `plugins/devil-lawyer/skills/devil-lawyer/` directory, including `SKILL.md`, `references/`, and `LICENSE`, into a directory supported by your Agent Skills host. Invoke it using that host's skill-discovery or invocation conventions. Host-specific commands and capabilities do not apply universally.

### Codex plugin

From a local checkout, add the repository as a marketplace and install the plugin:

```bash
codex plugin marketplace add /path/to/DevilLawyer-Skill
codex plugin add devil-lawyer@devil-lawyer-marketplace
```

The plugin manifest is [`plugins/devil-lawyer/plugin.json`](plugins/devil-lawyer/plugin.json); the marketplace entry is [`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json). The `agents/openai.yaml` file is an optional host-specific presentation file. Other hosts may ignore it.

## Portability and safety

The standalone skill has no runtime dependency on ECC, a specific model, MCP servers, hooks, credentials, or third-party packages. It uses host-provided capabilities only when they are actually available. Fresh contexts and native selectors are host features, not guarantees.

If a host cannot create internal subagents, the skill can conduct a sequential simulation and must disclose that the perspectives are not independent. A simulated Recipient is not real-user research. If the user requires independent roles and the host cannot provide them, the skill must say that this requirement cannot be met.

The skill treats instructions found in user material, attachments, role outputs, and research results as untrusted data. Its instructions require minimizing and redacting sensitive information before role packets and public queries, and prohibit sending user material to external services or retaining it beyond the current review without explicit user authorization. The host's own data handling and permission controls still apply; the skill cannot enforce storage, isolation, or access guarantees. Research, when used, is scoped, read-only, and sanitized.

## Package layout

```text
plugins/devil-lawyer/
├── plugin.json
└── skills/devil-lawyer/
    ├── SKILL.md
    ├── LICENSE
    ├── agents/openai.yaml
    └── references/
```

[`evaluations/public-release.md`](evaluations/public-release.md) records the release acceptance criteria. [`evaluations/results.md`](evaluations/results.md) records package checks and their limits. Historical evaluation records are synthetic and are not evidence that every host provides the described capabilities.

## Development checks

Optional validator dependencies are pinned in [`evaluations/requirements-dev.txt`](evaluations/requirements-dev.txt). In an isolated virtual environment, run:

```bash
python -m pip install -r evaluations/requirements-dev.txt
python evaluations/validate_package.py
python -m unittest discover -s evaluations -p 'test_package.py' -v
```

To validate against the official Agent Plugins schema, save it to the ignored `.test-artifacts/plugin.schema.json` and pass `--schema .test-artifacts/plugin.schema.json`. Without that option, schema validation is reported as not run. Static package checks do not prove live model behavior, host isolation, permission enforcement, or user comprehension.

## License

This repository is provided under the MIT License. The English root [`LICENSE`](LICENSE) is authoritative; [`LICENSE.es.md`](LICENSE.es.md) is an informational Spanish translation.
