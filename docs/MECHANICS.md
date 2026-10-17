# Known gameplay rules

Evidence status: supplied project specification, 2026-10-17. These rules have not
yet been independently confirmed against original gameplay. Keep observation
evidence separate from implementation assumptions.

## Match and phases

A match has seven regular army-building rounds followed by a final knockout
tournament. Each regular round proceeds through buy, deployment, automated combat,
and results/rewards/progression. Timing and exact transition triggers are unknown.

## Persistent armies and formations

Every player owns three persistent army groups. Gold buys packages containing
one or more individual units. Each group has its own purchase grid, supports
intentional holes and later repositioning/swapping, and persists between rounds.

Scan purchase cells front-to-back, left-to-right; skip empty cells. Expand packages
into individual units and compact them into a separate finite deployment formation.
Units beyond that capacity become reserves. This process does not compact or
rewrite the purchase grid. Grid dimensions, within-package order, and physical
formation geometry are not confirmed.

A deployed unit's death causes one reserve unit from its group to spawn at that
group's original deployment flag and advance automatically toward combat.
Reserve selection, timing, and repeated reinforcement behavior need observation.

Battle deaths never remove persistent purchases. Every later round reconstructs
temporary battlefield instances from the purchased rosters.

## Deployment and combat

Players freely position three flags within valid boundaries in two connected
lanes: upper/uphill and lower/downhill. Each lane supports at most two flags,
so groups are allocated two in one lane and one in the other.

Combat is automated with no direct unit micro. Head-to-head fights eventually
converge toward a central battlefield; surviving forces determine the round winner.
Exact topology, navigation, and convergence triggers remain unknown.

## Economy and endgame

Gold buys regular units. Kills and round victories earn wood. Wood can be converted
to gold or saved for special final-round units. No starting balances, conversion
rates, prices, stats, or reward formulas are confirmed.

After the seventh regular round, a knockout tournament determines the match winner.
Bracket details and interactions with persistent armies are not yet confirmed.

## Ruleset policy

Classic is the default. Proposed conveniences and community balancing must be
explicitly documented and separately configurable, never backfilled as original
behavior. Synthetic test fixtures and internal phase IDs are engineering choices,
not observed mechanics.
