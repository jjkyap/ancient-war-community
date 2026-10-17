# Unknown original mechanics

Do not fill these gaps with conventional autobattler assumptions. Nulls in
data/classic.json deliberately block treating the bootstrap as runtime-ready.

| Area | Questions to resolve |
| --- | --- |
| Lobby | Player count, teams, spectators, disconnects, AI slots? |
| Phases | Buy/deploy timers, ready states, simultaneous transitions, timeouts? |
| Grids | Dimensions, package footprints, rotation, overlap, movement/swap limits? |
| Packages | Factions, composition, heterogeneous member order, upgrades, sale/refund rules? |
| Formation | Capacity per group, unit footprints, facing, geometry, compaction details? |
| Reserves | FIFO or other selection, spawn delay, cap on active reinforcements, reserve deaths? |
| Flags | Boundaries, lane geometry, facing, overlap, locking, whether flags may move in combat? |
| Combat | AI/targeting, convergence condition, ties, time limit, simultaneous deaths? |
| Economy | Starting resources, kill attribution, assists, income, win bonuses, conversion formula? |
| Matchmaking | Opponent rotation, repeat opponents, odd counts/byes, round pairings? |
| Tournament | Seeding, bracket size, elimination, byes, army reset, buying windows, final-unit eligibility? |
| Persistence | Roster changes after elimination, upgrades, disconnect/rejoin ownership? |
| Catalog | SC2 dependencies/patch, original custom units, stats, ability modifications? |

## Observation record template

```text
ID:
Date / observer:
Original map version / SC2 patch:
Source: replay or video path/URL, timestamp, player perspective
Question:
Setup and controlled variables:
Observed action and outcome:
Alternative explanations:
Confidence and repeat count:
Classic rule supported (or still unknown):
Affected configuration, code, and follow-up test:
```

Track conflicting observations rather than selecting a convenient answer. Do not
copy original assets or derive catalog values merely from similarly named ladder
units. Confirm the original map's dependencies and modifications first.
