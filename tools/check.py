#!/usr/bin/env python3
"""Run local data and model checks. This is NOT a Galaxy compiler/map build."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    for arguments in [
        ['tools/validate_data.py'],
        ['tools/generate.py', '--check'],
        ['-m', 'unittest', 'discover', '-s', 'tests', '-v'],
    ]:
        subprocess.run([sys.executable, *arguments], cwd=ROOT, check=True)
    print('Local checks passed. Galaxy compilation and in-game checks remain pending.')


if __name__ == '__main__':
    main()
