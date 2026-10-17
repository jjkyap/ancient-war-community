#!/usr/bin/env python3
"""Generate confirmed constants only; does not build or compile an SC2 map."""

import argparse
from pathlib import Path

from awdev.definitions import load

ROOT = Path(__file__).resolve().parents[1]


def render(data):
    return (
        '// Validation: not compiled/type-checked in Galaxy Editor or Modkit yet.\n'
        '// Source: supplied gameplay specification. Generated equivalents: tools/generate.py.\n'
        f'const int c_awRegularRounds = {data["regular_rounds"]};\n'
        f'const int c_awArmyGroupsPerPlayer = {data["army_groups_per_player"]};\n'
        f'const int c_awMaxFlagsPerLane = {data["max_flags_per_lane"]};\n'
        'const int c_awLaneUpper = 0;\n'
        'const int c_awLaneLower = 1;\n'
        'const int c_awInvalidId = -1;\n'
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='check committed constants match data')
    args = parser.parse_args()
    content = render(load(ROOT / 'data/classic.json'))
    if args.check:
        if (ROOT / 'src/galaxy/core/Constants.galaxy').read_text(encoding='utf-8') != content:
            parser.exit(1, 'Galaxy constants differ from data; review generated output.\n')
        print('Confirmed constants match; Galaxy syntax/engine validation NOT performed.')
    else:
        target = ROOT / 'build/AW/core/Constants.galaxy'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
        print(f'Generated {target.relative_to(ROOT)} (not compiled).')


if __name__ == '__main__':
    main()
