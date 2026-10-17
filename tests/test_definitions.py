import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from awdev.definitions import DefinitionError, load, unique_object, validate

ROOT = Path(__file__).resolve().parents[1]


class DefinitionTests(unittest.TestCase):
    def setUp(self):
        self.data = load(ROOT / 'data/classic.json')

    def test_unknowns_remain_unknown(self):
        self.assertIsNone(self.data['deployment_capacity'])
        self.assertIsNone(self.data['economy']['starting_gold'])
        self.assertEqual(self.data['units'], [])

    def test_synthetic_catalog_and_references(self):
        self.data['factions'] = [{'id': 'test', 'name': 'Synthetic'}]
        self.data['units'] = [{'id': 'test_unit', 'faction_id': 'test', 'catalog_link': None,
                               'stats': {'life': None, 'damage': None}}]
        self.data['packages'] = [{'id': 'test_pack', 'members': [{'unit_id': 'test_unit', 'count': 2}],
                                 'gold_cost': None, 'wood_cost': 0}]
        validate(self.data)
        for mutate in [lambda d: d['units'][0].update(faction_id='missing'),
                       lambda d: d['packages'][0]['members'][0].update(unit_id='missing'),
                       lambda d: d['packages'][0]['members'][0].update(count=True),
                       lambda d: d['packages'][0].update(gold_cost=-1),
                       lambda d: d['units'].append(copy.deepcopy(d['units'][0]))]:
            invalid = copy.deepcopy(self.data)
            mutate(invalid)
            with self.subTest(mutation=mutate), self.assertRaises(DefinitionError):
                validate(invalid)

    def test_reject_invalid_top_level_and_configuration(self):
        mutations = [lambda d: d.update(unexpected=1), lambda d: d.update(regular_rounds=8),
                     lambda d: d.update(deployment_capacity=True),
                     lambda d: d['purchase_grid'].update(rows=0),
                     lambda d: d['economy'].update(wood_to_gold=0),
                     lambda d: d.update(units={}), lambda d: d.update(schema_version=True)]
        for mutate in mutations:
            invalid = copy.deepcopy(self.data)
            mutate(invalid)
            with self.subTest(mutation=mutate), self.assertRaises(DefinitionError):
                validate(invalid)

    def test_duplicate_json_keys_rejected(self):
        with self.assertRaises(DefinitionError):
            json.loads('{"ruleset":"classic","ruleset":"other"}', object_pairs_hook=unique_object)
