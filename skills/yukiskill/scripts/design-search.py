#!/usr/bin/env python3
"""Run the pinned UI UX Pro Max search engine with bundled data."""
from pathlib import Path
import subprocess
import sys

if __name__ == '__main__':
    entry = Path(__file__).resolve().parents[1] / 'vendor/ui-ux-pro-max/scripts/search.py'
    if not entry.is_file():
        raise SystemExit('Bundled design search is missing; reinstall the complete yukiskill folder.')
    raise SystemExit(subprocess.call([sys.executable, '-X', 'utf8', str(entry), *sys.argv[1:]]))
