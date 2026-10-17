# Incremental roadmap

## 0. Development foundation (this bootstrap)

- Component-map placeholder, modular Galaxy contracts, known/unknown documentation.
- Strict Classic data validation and deterministic confirmed-constant generation.
- Synthetic tests for scan ordering, expansion, capacity, reserves, identity,
  input preservation, and malformed data.
- Local Git on main and an approved public GitHub repository under jjkyap.

Acceptance: Python checks pass; unknowns and Galaxy validation limits are explicit.

## 1. Real map and tooling integration

Create the component map in Galaxy Editor, record dependencies and editor/game
versions, import AW/ sources, and validate includes/types. Run a minimal map smoke
test with no gameplay. Record repeatable manual steps before adding automation.

Acceptance: checked-in valid component source opens, validates, and runs in SC2;
Galaxy module validation status updated with actual evidence.

## 2. Observe and implement army layout

Observe purchase-grid dimensions, package footprints/member order, formation
capacity, and deployment geometry. Add a few verified definitions. Implement
roster storage and grid move/swap plus formation generation in Galaxy, using the
Python model for logical comparisons. Keep persistent purchases immutable during
battle construction.

Acceptance: observed fixtures reproduce ordering/overflow and survive rebuilding
a battle without losing purchases. No full combat or economy needed yet.

## 3. Economy and deployment

Confirm costs, resource flows, conversion, placement boundaries, and flag locking.
Implement atomic transactions and flag validation with a minimal interaction UI.
Acceptance: invalid actions change no resources/roster; all three groups obey lane limits.

## 4. Battle lifecycle and reinforcement

Observe AI, death events, reserve order/timing, central convergence, and teardown.
Implement temporary instances and reinforcement with deterministic event handling.
Acceptance: one eligible death releases one reserve at the original flag; rounds
reconstruct from the same owned roster.

## 5. Full regular match

Confirm matchmaking, ties, timers, rewards, and disconnect rules. Integrate seven
rounds and UI. Add AI actions through the same validated interfaces.
Acceptance: a reproducible seven-round match preserves state and awards observed rewards.

## 6. Tournament and fidelity review

Observe and implement final-unit access, bracket/seeding/byes, and elimination.
Acceptance: replay comparisons demonstrate Classic behavior and a final champion.

## 7. Optional community improvements

Add opt-in conveniences and separately configured balance changes after Classic
acceptance. Obtain license/contribution decisions before an external contribution
process. Keep observable Classic behavior covered by regression fixtures.
