#!/usr/bin/env python3
"""Standalone analysis entry point; equivalent to ``python main.py analyze``."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.analysis.main import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
