# Contributor guidance

These instructions apply to repository development. The distributed skill must remain usable without this file or any development tooling.

## Product contract

- Keep the English skill instructions authoritative and maintain equivalent English and Spanish user documentation.
- Preserve the eight-field intake, one necessary missing question per turn, and the stop on unresolved required information.
- Keep analysis read-only; separate recipient-visible material from internal context; sanitize public queries; and preserve honest capability disclosure.
- Do not add runtime dependencies, model settings, servers, hooks, credentials, or external actions without an explicit product requirement.
- Maintain one functional `SKILL.md`; keep references self-contained and within the package.

## Validation

- Define observable acceptance criteria before changing behavior. Evaluate behavior semantically, not by exact prose matching.
- Validate the plugin manifest, YAML/frontmatter, package paths, references, links, license declarations, and byte-identical English license copies.
- Use synthetic evaluation data. Store temporary outputs outside normal user profiles and do not copy credentials into test environments.
- Record passed, failed, blocked, and not-run checks with evidence and limits in `evaluations/results.md`.
- Static review is not proof of live model behavior, host isolation, installation, or permission enforcement.

## Changes and releases

- Do not commit or publish unless the user explicitly asks.
- Preserve existing work and configured authorship. Do not add AI attribution or co-author trailers.
- Keep the root English `LICENSE` canonical and `LICENSE.es.md` informational.
