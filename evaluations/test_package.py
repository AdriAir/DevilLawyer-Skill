"""Regression tests for distribution failures, not tests of generated prose."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import unittest
import uuid
import re

from validate_package import TARGET_VERSION, validate_package

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path("plugins/devil-lawyer/skills/devil-lawyer")


class PackageTests(unittest.TestCase):
    def setUp(self):
        artifacts = ROOT / ".test-artifacts"
        artifacts.mkdir(exist_ok=True)
        # Inherit the workspace ACL: Python 3.14 TemporaryDirectory's 0700 ACL
        # prevents the Windows sandbox token from accessing its own test files.
        self.temp = artifacts / ("package-test-" + uuid.uuid4().hex)
        self.temp.mkdir()
        self.addCleanup(self.cleanup)
        self.root = self.temp.resolve() / "package"
        if not self.root.is_relative_to(self.temp.resolve()):
            raise ValueError("Test directory escaped its temporary root")
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(
            ".git", ".venv", "__pycache__", ".test-artifacts"))

    def cleanup(self):
        if not self.temp.resolve().is_relative_to((ROOT / ".test-artifacts").resolve()):
            raise ValueError("Temporary cleanup target escaped test artifacts")
        shutil.rmtree(self.temp)

    def assertRejected(self, part, *, expected_version=TARGET_VERSION):
        issues = validate_package(self.root, expected_version=expected_version)
        self.assertTrue(any(part in issue for issue in issues), issues)

    def test_actual_package_is_consistent(self):
        self.assertEqual([], validate_package(self.root))

    def test_release_target_is_0_3_0(self):
        path = self.root / "plugins/devil-lawyer/plugin.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(TARGET_VERSION, data["version"])
        self.assertEqual([], validate_package(self.root))

    def test_missing_standalone_license_is_rejected(self):
        (self.root / SKILL / "LICENSE").unlink()
        self.assertRejected("LICENSE")

    def test_license_drift_is_rejected(self):
        (self.root / SKILL / "LICENSE").write_text("different terms", encoding="utf-8")
        self.assertRejected("license copies")

    def test_stale_repository_url_is_rejected(self):
        path = self.root / "plugins/devil-lawyer/plugin.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["repository"] = "https://example.invalid/old-repository.git"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertRejected("repository must equal")

    def test_public_marketplace_defers_authentication(self):
        path = self.root / ".agents/plugins/marketplace.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["plugins"][0]["policy"]["authentication"] = "ON_INSTALL"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertRejected("identity/category/policy mismatch")

    def test_marketplace_escape_is_rejected(self):
        path = self.root / ".agents/plugins/marketplace.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["plugins"][0]["source"]["path"] = "../../outside"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertRejected("marketplace source")

    def test_missing_reference_is_rejected(self):
        with (self.root / SKILL / "SKILL.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Missing reference](references/missing.md)\n")
        self.assertRejected("missing.md")

    def test_standalone_link_escape_is_rejected(self):
        with (self.root / SKILL / "SKILL.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Repository-only reference](../../../plugin.json)\n")
        self.assertRejected("escapes standalone skill")

    def test_duplicate_manifest_keys_are_rejected(self):
        path = self.root / "plugins/devil-lawyer/plugin.json"
        path.write_text('{"name":"devil-lawyer","name":"other"}', encoding="utf-8")
        self.assertRejected("duplicate key")

    def test_duplicate_yaml_keys_are_rejected(self):
        path = self.root / SKILL / "agents/openai.yaml"
        path.write_text("policy:\n  allow_implicit_invocation: true\n  allow_implicit_invocation: false\n", encoding="utf-8")
        self.assertRejected("duplicate key")

    def test_disabled_discovery_is_rejected(self):
        path = self.root / SKILL / "agents/openai.yaml"
        content = path.read_text(encoding="utf-8")
        path.write_text(content.replace("allow_implicit_invocation: true",
                                        "allow_implicit_invocation: false"), encoding="utf-8")
        self.assertRejected("implicit discovery")

    def test_wrong_release_is_rejected(self):
        path = self.root / "plugins/devil-lawyer/plugin.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["version"] = "1.0.0"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertRejected("version", expected_version=TARGET_VERSION)

    def test_wrong_release_is_rejected_by_default(self):
        path = self.root / "plugins/devil-lawyer/plugin.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["version"] = "1.0.0"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertRejected("version")

    def test_malformed_plugin_json_reports_a_cli_diagnostic(self):
        path = self.root / "plugins/devil-lawyer/plugin.json"
        path.write_text("{not json", encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(ROOT / "evaluations/validate_package.py"), "--root", str(self.root)],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("plugins/devil-lawyer/plugin.json:", result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_non_text_description_is_rejected(self):
        path = self.root / SKILL / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        path.write_text(re.sub(r"^description:.*$", "description: [not, text]", content,
                               count=1, flags=re.M), encoding="utf-8")
        self.assertRejected("description")

    def test_description_over_1024_characters_is_rejected(self):
        path = self.root / SKILL / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        replacement = "description: " + ("x" * 1025)
        path.write_text(re.sub(r"^description:.*$", replacement, content, count=1, flags=re.M),
                        encoding="utf-8")
        self.assertRejected("description")

    def test_non_text_license_metadata_is_rejected(self):
        path = self.root / SKILL / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        path.write_text(content.replace("license: MIT", "license: [MIT]"), encoding="utf-8")
        self.assertRejected("license metadata")

    def test_unhashable_yaml_key_is_reported(self):
        path = self.root / SKILL / "agents/openai.yaml"
        path.write_text("? [unhashable, key]\n: value\n", encoding="utf-8")
        self.assertRejected("unhashable")

    def test_list_or_null_marketplace_source_is_reported(self):
        path = self.root / ".agents/plugins/marketplace.json"
        for source in ([], None):
            with self.subTest(source=source):
                data = json.loads(path.read_text(encoding="utf-8"))
                data["plugins"][0]["source"] = source
                path.write_text(json.dumps(data), encoding="utf-8")
                self.assertRejected("marketplace source")

    def test_missing_schema_reports_a_diagnostic(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "evaluations/validate_package.py"), "--root", str(self.root),
             "--schema", str(self.root / "missing-schema.json")],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("schema:", result.stdout)

    def test_invalid_schema_reports_a_diagnostic(self):
        path = self.root / "invalid-schema.json"
        path.write_text("[]", encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(ROOT / "evaluations/validate_package.py"), "--root", str(self.root),
             "--schema", str(path)],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("official plugin schema", result.stdout)

    def test_malformed_schema_json_reports_a_diagnostic(self):
        path = self.root / "malformed-schema.json"
        path.write_text("{not json", encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(ROOT / "evaluations/validate_package.py"), "--root", str(self.root),
             "--schema", str(path)],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("schema:", result.stdout)

    def test_wrong_extension_type_is_reported(self):
        path = self.root / "plugins/devil-lawyer/plugin.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["extensions"] = []
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertRejected("extensions")

    def test_wrong_ui_policy_type_is_reported(self):
        path = self.root / SKILL / "agents/openai.yaml"
        content = path.read_text(encoding="utf-8")
        content = content[:content.index("policy:")] + "policy: []\n"
        path.write_text(content, encoding="utf-8")
        self.assertRejected("policy")

    def test_invalid_utf8_is_reported(self):
        (self.root / SKILL / "SKILL.md").write_bytes(b"\xff\xfe\xff")
        self.assertRejected("SKILL.md")

    def test_orphaned_role_guide_is_rejected(self):
        path = self.root / SKILL / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        import re
        content = re.sub(r"\[[^\]]+\]\(references/roles\.md\)", "role guide", content)
        path.write_text(content, encoding="utf-8")
        self.assertRejected("unlinked runtime reference")


if __name__ == "__main__":
    unittest.main()
