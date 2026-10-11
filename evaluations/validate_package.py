"""Offline distribution validation. Optional official schema is supplied by the caller.

Development dependencies: PyYAML; jsonschema only with --schema. No network calls.
"""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml

SKILL = Path("plugins/devil-lawyer/skills/devil-lawyer")
LICENSE_ID = "MIT"
TARGET_VERSION = "0.3.0"
EXPECTED_REPOSITORY = "https://github.com/AdriAir/DevilLawyer-Skill.git"


def unique_pairs(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate key: {key}")
        value[key] = item
    return value


class UniqueLoader(yaml.SafeLoader):
    pass


def yaml_mapping(loader, node):
    loader.flatten_mapping(node)
    pairs = []
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, (str, int, float, bool, type(None), tuple)):
            raise ValueError("unhashable YAML mapping key")
        pairs.append((key, loader.construct_object(value_node)))
    return unique_pairs(pairs)


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, yaml_mapping)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)


def validate_package(root, schema=None, expected_version=TARGET_VERSION):
    root = Path(root).resolve()
    issues = []
    required = ["AGENTS.md", "README.md", "README.es.md", "LICENSE", "LICENSE.es.md",
                ".agents/plugins/marketplace.json", "plugins/devil-lawyer/plugin.json",
                "plugins/devil-lawyer/LICENSE", "evaluations/cases.md", "evaluations/rubric.md"]
    required += [str(SKILL / name) for name in ("SKILL.md", "LICENSE", "agents/openai.yaml",
                 "references/intake.md", "references/roles.md", "references/domains.md")]
    for name in required:
        path = root / name
        if not path.resolve().is_relative_to(root):
            issues.append(f"required path escapes repository: {name}")
        elif not path.is_file():
            issues.append(f"missing required file: {name}")
    if issues:
        return issues

    def load(name, reader):
        try:
            return reader(root / name)
        except (UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError, OSError, yaml.YAMLError) as error:
            issues.append(f"{name}: {error}")
            return None

    plugin = load("plugins/devil-lawyer/plugin.json", read_json)
    market = load(".agents/plugins/marketplace.json", read_json)
    ui = load(str(SKILL / "agents/openai.yaml"),
              lambda p: yaml.load(p.read_text(encoding="utf-8"), Loader=UniqueLoader))
    skill_text = load(str(SKILL / "SKILL.md"), lambda p: p.read_text(encoding="utf-8"))
    if skill_text is None:
        return issues
    front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", skill_text, re.S)
    metadata = None
    if not front:
        issues.append("SKILL.md: missing YAML frontmatter")
    else:
        try:
            metadata = yaml.load(front.group(1), Loader=UniqueLoader)
        except (ValueError, yaml.YAMLError) as error:
            issues.append(f"SKILL.md: {error}")

    if not isinstance(plugin, dict):
        issues.append("plugin manifest must be an object")
    else:
        expected = (("name", "devil-lawyer"), ("license", LICENSE_ID),
                    ("repository", EXPECTED_REPOSITORY),
                    ("$schema", "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"))
        for key, value in expected:
            if plugin.get(key) != value:
                issues.append(f"plugin {key} must equal {value}")
        if expected_version is not None and plugin.get("version") != expected_version:
            issues.append(f"plugin version must equal {expected_version}")
        extensions = plugin.get("extensions")
        if not isinstance(extensions, dict) or not isinstance(extensions.get("com.openai"), dict):
            issues.append("missing extensions.com.openai")
        if schema is not None:
            import jsonschema
            try:
                jsonschema.validate(plugin, schema)
            except (jsonschema.ValidationError, jsonschema.SchemaError) as error:
                issues.append(f"official plugin schema: {error.message}")

    if not isinstance(market, dict):
        issues.append("marketplace must be an object")
    else:
        if market.get("name") != "devil-lawyer-marketplace":
            issues.append("wrong marketplace name")
        entries = market.get("plugins")
        if not isinstance(entries, list) or len(entries) != 1:
            issues.append("marketplace must contain one plugin")
        else:
            entry = entries[0]
            if not isinstance(entry, dict):
                issues.append("marketplace entry must be an object")
            else:
                source = entry.get("source", {})
                value = source.get("path") if isinstance(source, dict) else None
                if (not isinstance(value, str) or not value.startswith("./")
                        or not (root / value).resolve().is_relative_to(root)
                        or value != "./plugins/devil-lawyer"
                        or source.get("source") != "local"):
                    issues.append("marketplace source must be a contained local plugin path")
                if (entry.get("name") != "devil-lawyer" or entry.get("category") != "Productivity"
                        or entry.get("policy") != {"installation": "AVAILABLE", "authentication": "ON_USE"}):
                    issues.append("marketplace identity/category/policy mismatch")

    if not isinstance(ui, dict) or not isinstance(ui.get("interface"), dict):
        issues.append("agents/openai.yaml requires an interface mapping")
    else:
        interface = ui["interface"]
        short = interface.get("short_description")
        prompt = interface.get("default_prompt")
        if interface.get("display_name") != "Devil Lawyer":
            issues.append("wrong skill display_name")
        if not isinstance(short, str) or not 25 <= len(short) <= 64:
            issues.append("short_description must have 25-64 characters")
        if not isinstance(prompt, str) or "$devil-lawyer" not in prompt:
            issues.append("default_prompt must invoke $devil-lawyer")
        policy = ui.get("policy")
        if not isinstance(policy, dict):
            issues.append("agents/openai.yaml policy must be a mapping")
        elif policy.get("allow_implicit_invocation") is not True:
            issues.append("implicit discovery must remain enabled")

    if not isinstance(metadata, dict) or metadata.get("name") != "devil-lawyer":
        issues.append("skill identity metadata invalid")
    else:
        description = metadata.get("description")
        if (not isinstance(description, str) or not description.strip()
                or len(description) > 1024):
            issues.append("skill description must be non-empty text of at most 1024 characters")
        license_reference = metadata.get("license")
        if license_reference != "MIT":
            issues.append("skill standalone license metadata must declare MIT")
        if metadata.get("version") != TARGET_VERSION:
            issues.append(f"skill version must equal {TARGET_VERSION}")

    canonical = load("LICENSE", lambda p: p.read_bytes())
    copies = [load(p, lambda p: p.read_bytes()) for p in
              ("plugins/devil-lawyer/LICENSE", str(SKILL / "LICENSE"))]
    if canonical is not None and any(value != canonical for value in copies):
        issues.append("English license copies differ")

    entry_targets = []
    for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", skill_text):
        parsed = urlsplit(target.strip().strip("<>"))
        if not parsed.scheme and not parsed.netloc:
            entry_targets.append((root / SKILL / unquote(parsed.path)).resolve())
    for reference in ("intake.md", "roles.md", "domains.md"):
        if (root / SKILL / "references" / reference).resolve() not in entry_targets:
            issues.append(f"unlinked runtime reference: {reference}")

    # Relative links in the standalone skill must work without the repository.
    markdown_files = (list((root / SKILL).rglob("*.md"))
                      + list((root / "evaluations").rglob("*.md"))
                      + [root / "README.md", root / "README.es.md", root / "LICENSE.es.md"])
    for path in markdown_files:
        content = load(str(path.relative_to(root)), lambda p: p.read_text(encoding="utf-8"))
        if content is None:
            continue
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", content):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            boundary = root / SKILL if path.is_relative_to(root / SKILL) else root
            if not resolved.is_relative_to(boundary):
                issues.append(f"{path.relative_to(root)}: link escapes standalone skill/repository: {target}")
            elif not resolved.exists():
                issues.append(f"{path.relative_to(root)}: missing linked file {target}")
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--schema", type=Path, help="Downloaded official Agent Plugins JSON schema")
    parser.add_argument("--expected-version", default=TARGET_VERSION,
                        help="Release version required for this validation (default: %(default)s)")
    args = parser.parse_args()
    schema = None
    if args.schema:
        try:
            schema = read_json(args.schema)
        except (UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError, OSError) as error:
            print(f"FAIL: schema: {error}")
            print("Official schema: NOT RUN (schema could not be loaded)")
            return 1
    issues = validate_package(args.root, schema, expected_version=args.expected_version)
    for issue in issues:
        print(f"FAIL: {issue}")
    if not issues:
        print("PASS: package structure, metadata, paths, YAML, links and license copies")
    print("Official schema: " + ("checked" if args.schema else "NOT RUN (supply --schema)"))
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
