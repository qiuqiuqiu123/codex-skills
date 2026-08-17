import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "tools" / "idd-anchor-scan" / "scan_anchors.py"
SPEC = importlib.util.spec_from_file_location("scan_anchors", SCRIPT_PATH)
assert SPEC and SPEC.loader
SCAN_ANCHORS = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SCAN_ANCHORS
SPEC.loader.exec_module(SCAN_ANCHORS)


class ScanAnchorsTest(unittest.TestCase):
    def make_project(self):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        (root / "intent").mkdir()
        (root / "src").mkdir()
        (root / ".anchors").mkdir()
        return temporary, root

    def test_valid_anchor_and_reverse_index(self):
        temporary, root = self.make_project()
        self.addCleanup(temporary.cleanup)
        (root / "intent" / "pricing.md").write_text("# 定价规则\n\n## 折扣应用\n", encoding="utf-8")
        (root / "src" / "pricing.py").write_text(
            "# @intent: intent/pricing.md#折扣应用\ndef apply_discount():\n    pass\n",
            encoding="utf-8",
        )
        (root / ".anchors" / "reverse.json").write_text(
            json.dumps({"intent/pricing.md#折扣应用": ["src/pricing.py:apply_discount"]}, ensure_ascii=False),
            encoding="utf-8",
        )

        findings, anchor_count = SCAN_ANCHORS.scan(root)

        self.assertEqual(anchor_count, 1)
        self.assertEqual(findings, [])

    def test_missing_anchor_target_is_critical(self):
        temporary, root = self.make_project()
        self.addCleanup(temporary.cleanup)
        (root / "src" / "pricing.py").write_text(
            "# @contract: contracts/missing.md#rule\n",
            encoding="utf-8",
        )
        (root / ".anchors" / "reverse.json").write_text("{}", encoding="utf-8")

        findings, anchor_count = SCAN_ANCHORS.scan(root)

        self.assertEqual(anchor_count, 1)
        self.assertIn("missing-anchor-target", {item["code"] for item in findings})
        self.assertIn("critical", {item["severity"] for item in findings})

    def test_missing_markdown_heading_is_warning(self):
        temporary, root = self.make_project()
        self.addCleanup(temporary.cleanup)
        (root / "intent" / "pricing.md").write_text("# 定价规则\n", encoding="utf-8")
        (root / "src" / "pricing.py").write_text(
            "# @intent: intent/pricing.md#不存在的章节\n",
            encoding="utf-8",
        )
        (root / ".anchors" / "reverse.json").write_text("{}", encoding="utf-8")

        findings, _ = SCAN_ANCHORS.scan(root)

        self.assertIn("missing-anchor-heading", {item["code"] for item in findings})

    def test_missing_reverse_source_is_warning(self):
        temporary, root = self.make_project()
        self.addCleanup(temporary.cleanup)
        (root / "intent" / "pricing.md").write_text("# 定价规则\n", encoding="utf-8")
        (root / ".anchors" / "reverse.json").write_text(
            json.dumps({"intent/pricing.md#定价规则": ["src/missing.py:calculate"]}, ensure_ascii=False),
            encoding="utf-8",
        )

        findings, _ = SCAN_ANCHORS.scan(root)

        self.assertIn("missing-reverse-source", {item["code"] for item in findings})


if __name__ == "__main__":
    unittest.main()
