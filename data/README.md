# Definition format (schema version 1)

classic.json holds only confirmed constants from the supplied specification.
Null means unknown, never free/zero/default. Empty catalogs mean no original
units or factions have yet been researched. This file is not runtime-ready.

The validator in tools/awdev/definitions.py is the executable schema. Unknown
fields are rejected to catch misspellings. IDs use lowercase snake_case.

- faction: `id`, `name` (nonempty string).
- unit: `id`, `faction_id` (existing faction), `catalog_link` (SC2 unit ID or null),
  `stats` (object with positive `life` or null, nonnegative `damage` or null).
- package: `id`, `members` (nonempty ordered list of `unit_id` and positive `count`),
  `gold_cost` (nonnegative integer or null), `wood_cost` (same).

Member order is a provisional tooling convention for heterogeneous packages;
the original game's within-package ordering is unverified. Tests use synthetic
data and must not be copied into Classic as historical evidence.

Grid rows increase front-to-back; columns increase left-to-right. Dimensions
and deployment capacity remain unknown. Economy values are scalar placeholders;
replace with a versioned schema if observation reveals context-dependent rewards.
Stats are observation metadata, not an SC2 GameData compiler. No unit GameData is
generated. Future community rules should use a separate explicit ruleset file.
