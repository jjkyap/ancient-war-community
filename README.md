# Ancient War 2: Community Edition

A community recreation of the abandoned StarCraft II Arcade autobattler Ancient
War 2. Original source is unavailable. We will observe gameplay, document evidence,
and implement it incrementally, preserving Classic behavior before adding optional
quality-of-life features or separate community balance rules.

**Status: development foundation only.** No playable map, combat, UI, matchmaking,
or tournament exists yet. Galaxy files have not been compiled or run in SC2.

Players build three persistent army groups across seven regular rounds, then
enter a knockout tournament. Purchase grids persist; battlefield units do not.
Unknown statistics and mechanics remain unknown rather than guessed.

## Start locally

Python 3.11+ and Git are sufficient for the dependency-free development checks:

```sh
python3 tools/check.py
python3 tools/generate.py
```

The first command validates Classic data, checks constants for drift, and runs
unit tests for the development models. The second generates confirmed Galaxy
constants into ignored build/AW/core/Constants.galaxy. Neither builds a map or
compiles Galaxy. No pip install is required. VS Code's default test task runs
the same local checks.

For editor validation and playtesting, create a real component-folder map in
Galaxy Editor using [the development workflow](docs/DEVELOPMENT.md). Optional
[Modkit / SC2 Galaxy Toolkit](https://marketplace.visualstudio.com/items?itemName=talv.sc2galaxy)
uses extension ID `talv.sc2galaxy`; its current Modkit offering is on the prerelease
channel. It was not installed in the inspected environment.

## Layout

```text
maps/AncientWarCommunity/  Placeholder for Editor-created component map
src/galaxy/
  core/                  Confirmed constants and internal phase IDs
  state/                 Persistent player and army-group records
  economy/               Affordability predicate and transaction boundary notes
  army/                  Definition, grid, roster, and formation contracts
data/                    Classic configuration and format documentation
tools/awdev/             Python schema and logical formation reference
tools/                   Validation, constant generation, local check entry points
tests/                   Synthetic data and formation invariant tests
docs/                    Mechanics, unknowns, architecture, roadmap, workflow
.vscode/                 Shared tasks, settings, extension recommendations
```

## Project documents

- [Mechanics](docs/MECHANICS.md): supplied gameplay specification and evidence status.
- [Unknown mechanics](docs/UNKNOWN_MECHANICS.md): research questions and observation template.
- [Architecture](docs/ARCHITECTURE.md): module ownership and persistence boundaries.
- [Roadmap](docs/ROADMAP.md): incremental milestones and acceptance criteria.
- [Development](docs/DEVELOPMENT.md): environment, manual Editor setup, checks, and GitHub setup.
- [Agent conventions](AGENTS.md): instructions for future coding work.
- [Data format](data/README.md): executable schema contract and null semantics.

The public repository is [jjkyap/ancient-war-community](https://github.com/jjkyap/ancient-war-community),
with `main` as its default branch. No license is selected yet; choose one with
the project owner before inviting outside contributions. This repository contains
no copied original map or Blizzard assets.
