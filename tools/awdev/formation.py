"""Logical scan/expansion reference; no SC2 coordinates or game statistics.

Member list order and reserve suffix order are provisional tooling conventions.
Reserve release order remains an unverified original mechanic.
"""

from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True)
class Member:
    unit_id: str
    count: int


@dataclass(frozen=True)
class Purchase:
    purchase_id: str
    package_id: str


@dataclass(frozen=True)
class Entry:
    purchase_id: str
    unit_id: str
    member_index: int
    copy_index: int


@dataclass(frozen=True)
class Formation:
    deployed: tuple[Entry, ...]
    reserves: tuple[Entry, ...]


def build_formation(grid: Sequence[Sequence[Purchase | None]],
                    packages: Mapping[str, Sequence[Member]], capacity: int) -> Formation:
    """Scan rows front-to-back, columns left-to-right; preserve caller's grid.

    Capacity is a caller-supplied experiment parameter, never a Classic default.
    This utility accepts zero capacity for boundary testing, not as a game rule.
    """
    if type(capacity) is not int or capacity < 0:
        raise ValueError('capacity must be a nonnegative integer')
    if not grid or not grid[0] or any(len(row) != len(grid[0]) for row in grid):
        raise ValueError('grid must be a nonempty rectangle')
    expanded = []
    seen = set()
    for row in grid:
        for purchase in row:
            if purchase is None:
                continue
            if not isinstance(purchase, Purchase) or not isinstance(purchase.purchase_id, str) or not purchase.purchase_id:
                raise ValueError('invalid purchase identity')
            if purchase.purchase_id in seen:
                raise ValueError('purchase occupies multiple cells')
            seen.add(purchase.purchase_id)
            if not isinstance(purchase.package_id, str) or purchase.package_id not in packages:
                raise ValueError('unknown package')
            members = packages[purchase.package_id]
            if not members:
                raise ValueError('package must have members')
            for member_index, member in enumerate(members):
                if (not isinstance(member, Member) or not isinstance(member.unit_id, str)
                        or not member.unit_id or type(member.count) is not int or member.count <= 0):
                    raise ValueError('invalid package member')
                expanded.extend(Entry(purchase.purchase_id, member.unit_id, member_index, copy_index)
                                for copy_index in range(member.count))
    return Formation(tuple(expanded[:capacity]), tuple(expanded[capacity:]))
