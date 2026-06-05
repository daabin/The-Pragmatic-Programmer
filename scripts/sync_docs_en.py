#!/usr/bin/env python3
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "docs-en"
DOC_PATHS = [
    "README.md",
    "00 Foreword",
    "00 Preface First Edition",
    "00 Preface Second Edition",
    "01 Pragmatic Philosophy",
    "02 Pragmatic Approach",
    "03 Basic Tools",
    "04 Pragmatic Paranoia",
    "05 Bend or Break",
    "06 Concurrency",
    "07 While Coding",
    "08 Before the Project",
    "09 Pragmatic Projects",
    "10 Postface",
    "A1 Bibliography",
    "A2 Exercise Answers",
]


def reset_target() -> None:
    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.mkdir()


def copy_entry(relative_path: str) -> None:
    source = ROOT / relative_path
    destination = TARGET / relative_path
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def main() -> None:
    reset_target()
    for relative_path in DOC_PATHS:
        copy_entry(relative_path)


if __name__ == "__main__":
    main()
