#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
from pathlib import Path

LABEL_RE = re.compile(r"^label\s+(\w+):")
CALL_RE = re.compile(r"\b(jump|call)\s+(\w+)")


def collect_labels(root: Path):
    labels = {}
    for path in root.rglob("*.rpy"):
        text = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        for line in text:
            m = LABEL_RE.match(line.strip())
            if m:
                labels.setdefault(m.group(1), []).append(str(path))
    return labels


def collect_references(root: Path):
    refs = []
    for path in root.rglob("*.rpy"):
        text = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        for line in text:
            for m in CALL_RE.finditer(line):
                target = m.group(2)
                if target == "screen":
                    continue
                refs.append((target, str(path)))
    return refs


def main():
    if len(sys.argv) < 2:
        print("Usage: check_labels.py <game_dir>")
        return 1
    root = Path(sys.argv[1])
    labels = collect_labels(root)
    refs = collect_references(root)

    duplicates = {k: v for k, v in labels.items() if len(v) > 1}
    if duplicates:
        print("Дублирующиеся label:")
        for name, paths in duplicates.items():
            print(f"  {name}: {paths}")

    missing = {}
    for ref, src in refs:
        if ref not in labels:
            missing.setdefault(ref, []).append(src)
    if missing:
        print("Отсутствующие label для jump/call:")
        for name, sources in missing.items():
            print(f"  {name}: {sources}")

    if not duplicates and not missing:
        print("Проверка прошла успешно: дубли и отсутствующие label не найдены.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
