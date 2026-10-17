"""Synthetic packages and dimensions; none are original-game statistics."""

import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from awdev.formation import Member, Purchase, build_formation


class FormationTests(unittest.TestCase):
    def setUp(self):
        self.packages = {'pair': (Member('test_a', 2),),
                         'mixed': (Member('test_b', 1), Member('test_c', 2))}
        self.grid = [[None, Purchase('p1', 'pair'), None],
                     [Purchase('p2', 'mixed'), None, Purchase('p3', 'pair')]]

    def test_scan_expand_split_and_preserve_roster(self):
        before = copy.deepcopy(self.grid)
        result = build_formation(self.grid, self.packages, 4)
        all_entries = result.deployed + result.reserves
        self.assertEqual([e.unit_id for e in all_entries],
                         ['test_a', 'test_a', 'test_b', 'test_c', 'test_c', 'test_a', 'test_a'])
        self.assertEqual([e.purchase_id for e in result.reserves], ['p2', 'p3', 'p3'])
        self.assertEqual([e.copy_index for e in all_entries], [0, 1, 0, 0, 1, 0, 1])
        self.assertEqual(self.grid, before)

    def test_capacity_boundaries_and_conservation(self):
        for capacity in [0, 1, 7, 20]:
            with self.subTest(capacity=capacity):
                result = build_formation(self.grid, self.packages, capacity)
                self.assertEqual(len(result.deployed), min(capacity, 7))
                self.assertEqual(len(result.deployed) + len(result.reserves), 7)

    def test_empty_cells_produce_no_units(self):
        result = build_formation([[None, None]], self.packages, 2)
        self.assertEqual(result.deployed + result.reserves, ())

    def test_reposition_changes_scan_without_changing_purchase_identity(self):
        self.grid[0][0], self.grid[1][0] = self.grid[1][0], self.grid[0][0]
        result = build_formation(self.grid, self.packages, 1)
        self.assertEqual(result.deployed[0].purchase_id, 'p2')

    def test_reject_invalid_inputs(self):
        for grid, packages, capacity in [
            ([], self.packages, 1), ([[None], []], self.packages, 1),
            (self.grid, self.packages, -1), (self.grid, self.packages, True),
            (self.grid, self.packages, None),
            ([[Purchase('x', 'missing')]], self.packages, 1),
            ([[Purchase('x', 'pair'), Purchase('x', 'pair')]], self.packages, 1),
            ([[Purchase('x', 'bad')]], {'bad': ()}, 1),
            ([[Purchase('x', 'bad')]], {'bad': (Member('a', 0),)}, 1),
        ]:
            with self.subTest(grid=grid, capacity=capacity), self.assertRaises(ValueError):
                build_formation(grid, packages, capacity)
