"""Strict bootstrap schema. Unknown values are accepted only as explicit nulls."""

import json
import re
from pathlib import Path


class DefinitionError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise DefinitionError(message)


def fields(value, names, where):
    require(isinstance(value, dict), f"{where}: expected object")
    require(set(value) == set(names.split()), f"{where}: expected fields {names}")


def integer(value, minimum, where, *, nullable=False):
    if value is None and nullable:
        return
    require(type(value) is int and value >= minimum,
            f"{where}: expected integer >= {minimum}" + (" or null" if nullable else ""))


def identifier(value, where):
    require(isinstance(value, str) and re.fullmatch(r"[a-z][a-z0-9_]*", value) is not None,
            f"{where}: expected lowercase snake_case ID")


def catalog(items, names, where):
    require(isinstance(items, list), f"{where}: expected list")
    indexed = {}
    for item in items:
        fields(item, names, where)
        identifier(item['id'], where)
        require(item['id'] not in indexed, f"{where}: duplicate ID {item['id']}")
        indexed[item['id']] = item
    return indexed


def validate(data):
    fields(data, "schema_version ruleset regular_rounds army_groups_per_player lanes "
           "max_flags_per_lane purchase_grid deployment_capacity economy factions units packages", "root")
    integer(data['schema_version'], 1, 'schema_version')
    require(data['schema_version'] == 1, 'unsupported schema_version')
    require(data['ruleset'] == 'classic', 'only Classic schema is currently supported')
    for key, expected in [('regular_rounds', 7), ('army_groups_per_player', 3),
                          ('max_flags_per_lane', 2)]:
        integer(data[key], 1, key)
        require(data[key] == expected, f'{key}: conflicts with supplied Classic specification')
    require(data['lanes'] == ['upper', 'lower'], 'lanes: expected upper, lower')
    fields(data['purchase_grid'], 'rows columns', 'purchase_grid')
    for key, value in data['purchase_grid'].items():
        integer(value, 1, f'purchase_grid.{key}', nullable=True)
    integer(data['deployment_capacity'], 1, 'deployment_capacity', nullable=True)
    fields(data['economy'], 'starting_gold starting_wood kill_wood victory_wood wood_to_gold', 'economy')
    for key, value in data['economy'].items():
        integer(value, 1 if key == 'wood_to_gold' else 0, f'economy.{key}', nullable=True)
    factions = catalog(data['factions'], 'id name', 'factions')
    for faction in factions.values():
        require(isinstance(faction['name'], str) and bool(faction['name'].strip()), 'faction: empty name')
    units = catalog(data['units'], 'id faction_id catalog_link stats', 'units')
    for unit in units.values():
        identifier(unit['faction_id'], 'unit.faction_id')
        require(unit['faction_id'] in factions, 'unit: unknown faction_id')
        link = unit['catalog_link']
        require(link is None or (isinstance(link, str) and bool(link.strip())), 'unit: invalid catalog_link')
        fields(unit['stats'], 'life damage', 'unit.stats')
        for key, minimum in [('life', 1), ('damage', 0)]:
            integer(unit['stats'][key], minimum, f'unit.stats.{key}', nullable=True)
    packages = catalog(data['packages'], 'id members gold_cost wood_cost', 'packages')
    for package in packages.values():
        for key in ['gold_cost', 'wood_cost']:
            integer(package[key], 0, f'package.{key}', nullable=True)
        require(isinstance(package['members'], list) and bool(package['members']), 'package: empty members')
        for member in package['members']:
            fields(member, 'unit_id count', 'package.member')
            identifier(member['unit_id'], 'package.member.unit_id')
            require(member['unit_id'] in units, 'package.member: unknown unit_id')
            integer(member['count'], 1, 'package.member.count')
    return data


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'duplicate JSON key: {key}')
        result[key] = value
    return result


def load(path: Path):
    return validate(json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object))
