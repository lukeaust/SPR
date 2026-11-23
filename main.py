#!/usr/bin/env python3
"""Single public entry point for every SPR reproduction stage."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.cli import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
