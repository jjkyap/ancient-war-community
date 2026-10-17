#!/usr/bin/env python3
"""Validate bootstrap definitions; nulls mean research is still required."""

import argparse
from pathlib import Path

from awdev.definitions import DefinitionError, load


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', type=Path,
                        default=Path(__file__).resolve().parents[1] / 'data/classic.json')
    args = parser.parse_args()
    try:
        data = load(args.path)
    except (ValueError, OSError, DefinitionError) as error:
        parser.exit(1, f'Invalid definitions: {error}\n')
    print(f'Valid {data["ruleset"]} bootstrap schema; unknown values allowed, not runtime-ready.')


if __name__ == '__main__':
    main()
