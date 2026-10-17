# Proposed architecture

This is a module plan with a small set of pure records and interfaces, not a
working game framework. Avoid global arrays with invented player/grid limits.
Choose bounded storage only after measuring actual map requirements and Galaxy
constraints in Editor.

| Module | Responsibility | Current state |
| --- | --- | --- |
| Core / phases | Internal IDs, confirmed match constants, legal transitions | Constants and phase record; transitions deferred |
| Player state | Ownership, resources, stable group IDs | Persistent records |
| Economy | Validate and atomically commit purchases/conversions/rewards | Pure affordability predicate; no transactions |
| Roster / grid | Stable purchases, occupied cells, move/swap operations | Records and contract |
| Formation | Scan, expand, split active prefix and reserves | Galaxy entry record, tested Python reference |
| Definitions | Factions, package members, SC2 catalog links, explicit ruleset | Strict JSON validator; empty Classic catalogs |
| Deployment | Validate flag locations and 2/1 lane allocation | Planned; no geometry guessed |
| Combat lifecycle | Create/dispose temporary unit instances, resolve battle | Planned |
| Reinforcement | One reserve release per eligible group death | Planned; release policy unknown |
| Round / matchmaking | Seven regular rounds, pairings, outcomes | Planned |
| Tournament | Knockout progression and champion | Planned |
| AI | Submit actions through the same validated interfaces as UI | Planned |
| UI | Present state and request actions; never mutate balances directly | Planned |

## Persistent versus temporary state

Persistent: player identity and resources, three group identities, purchase
identities and definitions, and grid occupancy. A purchase ID is distinct from a
package definition ID: buying the same package twice creates two purchases.

Per battle: flag snapshot, formation entries, temporary unit handles, reserve
tracking, and outcome events. An expanded unit carries its purchase identity and
member/copy indices so a battle instance can be traced without removing ownership
when it dies. Battle teardown releases temporary handles only.

Formation generation must read the roster without mutation. Snapshot the group's
original deployment flag for reinforcements; do not infer that position from
surviving unit locations. Handle simultaneous death events idempotently so one
death cannot consume two reserve entries. Actual engine integration is deferred.

## Data and transaction boundaries

The versioned Classic JSON file is authoritative for confirmed configuration.
Unknowns are null and empty catalogs contain no fabricated units. Current
generation emits only confirmed constants. Lane and phase numeric IDs and -1 for
an invalid identity are implementation choices, not observed gameplay values.

A future transaction must validate phase, owner, resolved cost, funds, package,
grid placement, and capacity constraints before committing balances and roster
together. UI and AI call that boundary. Unknown costs must cause rejection.
No free purchase or successful placeholder transaction is exposed now.

JSON definitions are development input, not a promise that Galaxy can read JSON
at runtime. Add deterministic Galaxy tables or Editor GameData generation only
after schemas and dependencies are confirmed. Future community rulesets need
explicit selection and separate data; Classic must not inherit silent overrides.

## Logical formation reference

tools/awdev/formation.py accepts a rectangular row-major grid, synthetic package
definitions, and explicit experimental capacity. It skips holes, expands members,
and returns immutable deployed/reserve tuples without editing the input.
Within-package order follows the supplied member list as a provisional convention.
Reserve tuple order does not establish a runtime reinforcement selection policy.
No coordinates, unit creation, flags, or combat are implemented.

## Map integration and validation boundary

src/galaxy/Bootstrap.galaxy defines the include order and has no engine entry
point. Import the source under virtual AW/ paths in a real Editor-created map.
Preserve the Editor's generated MapScript.galaxy and trigger metadata; don't
replace them with handwritten bootstrap code. Source files use plain Galaxy
constructs (`const int`, `struct`, functions, and `include`), with no native API
calls or C/C++ preprocessing. Every module is explicitly uncompiled.

Python tests establish reference-model invariants only. A successful Modkit
verification, Editor save/validation, and SC2 test run are separate milestones.
Record tool versions, dependencies, and results before claiming runtime support.
