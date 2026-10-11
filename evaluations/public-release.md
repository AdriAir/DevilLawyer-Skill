# Public release acceptance criteria

Target package version: **0.3.0**.

## Observable acceptance criteria

- The root, plugin, and standalone skill licenses grant worldwide public use and redistribution under the same SPDX license; Spanish legal text is clearly informational.
- README instructions distinguish the Codex plugin path from copying the standalone Agent Skill and do not imply that host-specific features are universal.
- A host without internal subagents can complete the review with a sequential simulation, while explicitly reporting that roles are not independent.
- No proposal, attachment, role packet, or report is sent to an external service or retained beyond the current review without the user's explicit authorization.
- Public package files and Git history have been checked for credentials, personal/local paths, private operational data, and stale repository/license claims. Findings and anything not remediated are recorded.
- The plugin manifest, marketplace metadata, package validator, and tests agree on package version, license, repository, and public availability.

These criteria test observable package properties and capability disclosure; matching wording alone does not establish runtime behavior.
