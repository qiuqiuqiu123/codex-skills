#!/usr/bin/env python3
"""Read-only validation of IDD anchors and reverse-index paths."""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ANCHOR = re.compile(r"@(intent|contract):\s*((?:intent|contracts)/[^\s`，。）,;]+)")
SOURCE_SUFFIXES = {
    ".c", ".cc", ".cpp", ".cs", ".go", ".h", ".hpp", ".java",
    ".js", ".jsx", ".kt", ".kts", ".php", ".py", ".rb", ".rs",
    ".scala", ".swift", ".ts", ".tsx", ".vue",
}
IGNORED = {".git", ".venv", "__pycache__", "node_modules", "vendor", "dist", "build"}


def add(findings, severity, code, message, source=None):
    findings.append({"severity": severity, "code": code, "message": message, "source": source})


def slug(value):
    value = re.sub(r"[^\w\-\s\u4e00-\u9fff]", "", unquote(value).lower())
    return re.sub(r"[-\s]+", "-", value).strip("-")


def headings(path):
    result = set()
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
            if match:
                result.add(slug(match.group(1)))
    except (OSError, UnicodeError):
        pass
    return result


def validate_ref(root, reference, source, findings):
    path_text, separator, fragment = reference.strip("`'\".,;)").partition("#")
    target = (root / path_text).resolve()
    try:
        target.relative_to(root)
    except ValueError:
        add(findings, "critical", "anchor-outside-root", reference, source)
        return
    if not target.is_file():
        add(findings, "critical", "missing-anchor-target", reference, source)
        return
    if separator and target.suffix.lower() == ".md" and slug(fragment) not in headings(target):
        add(findings, "warning", "missing-anchor-heading", reference, source)


def source_files(root):
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SOURCE_SUFFIXES:
            continue
        if any(part in IGNORED for part in path.parts):
            continue
        try:
            data = path.read_bytes()
            if len(data) <= 2 * 1024 * 1024 and b"\x00" not in data:
                yield path, data.decode("utf-8")
        except (OSError, UnicodeError):
            continue


def scan_sources(root, findings):
    count = 0
    for path, text in source_files(root):
        relative = path.relative_to(root).as_posix()
        for line_number, line in enumerate(text.splitlines(), 1):
            for match in ANCHOR.finditer(line):
                count += 1
                validate_ref(root, match.group(2), f"{relative}:{line_number}", findings)
    return count


def implementation_exists(root, entry):
    if not isinstance(entry, str):
        return False
    return (root / entry).exists() or (root / entry.split(":", 1)[0]).exists()


def scan_reverse(root, findings):
    path = root / ".anchors" / "reverse.json"
    if not path.exists():
        add(findings, "warning", "missing-reverse-index", str(path.relative_to(root)))
        return
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError("top-level value must be an object")
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        add(findings, "critical", "invalid-reverse-index", str(error), ".anchors/reverse.json")
        return
    for reference, implementations in value.items():
        validate_ref(root, reference, ".anchors/reverse.json", findings)
        if not isinstance(implementations, list):
            add(findings, "critical", "invalid-reverse-entry", reference, ".anchors/reverse.json")
            continue
        for entry in implementations:
            if not implementation_exists(root, entry):
                add(findings, "warning", "missing-reverse-source", str(entry), ".anchors/reverse.json")


def scan(root):
    root = root.resolve()
    findings = []
    count = scan_sources(root, findings)
    scan_reverse(root, findings)
    return findings, count


def markdown(root, findings, count):
    critical = sum(item["severity"] == "critical" for item in findings)
    warnings = sum(item["severity"] == "warning" for item in findings)
    lines = [
        "# IDD Anchor Scan", "", f"- Root: `{root}`", f"- Anchors scanned: {count}",
        f"- Critical: {critical}", f"- Warnings: {warnings}", "", "## Findings", "",
    ]
    if not findings:
        lines.append("No deterministic anchor findings.")
    for item in findings:
        location = f" at `{item['source']}`" if item["source"] else ""
        lines.append(f"- **{item['severity'].upper()} {item['code']}**{location}: {item['message']}")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error(f"project root is not a directory: {root}")
    findings, count = scan(root)
    if args.format == "json":
        output = json.dumps({"root": str(root), "anchors_scanned": count, "findings": findings}, indent=2)
    else:
        output = markdown(root, findings, count)
    sys.stdout.write(output + ("\n" if not output.endswith("\n") else ""))
    return 2 if any(item["severity"] == "critical" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
