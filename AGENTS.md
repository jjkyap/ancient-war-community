# Agent conventions

This repository bootstraps Ancient War 2: Community Edition, an SC2 Arcade
recreation. Keep work incremental. Do not implement the whole game at once.

- Read docs/MECHANICS.md and docs/UNKNOWN_MECHANICS.md before gameplay changes.
- The user's supplied specification is our current evidence, not independently
  observed original behavior. Record observations with replay/video/time markers.
- Never invent original prices, stats, dimensions, capacities, or reward formulas.
  Use null for unknown configuration; runtime code must refuse unresolved values.
- Keep Classic separate from future opt-in community rules. No silent balance edits.
- Galaxy lives in src/galaxy; AW-prefixed symbols, explicit include order, no C/C++
  preprocessor features. Cite the native declaration before adding an engine API.
- Persistent purchases and temporary battle handles must remain separate.
- tools/awdev is dependency-free Python 3.11+. Its formation model is a development
  reference, not an SC2 runtime. Test behavioral invariants and invalid inputs.
- Run python3 tools/check.py after data/tool changes. Passing it does not compile
  Galaxy, validate an SC2 map, or verify in-game behavior. Report those separately.
- Keep editor-owned map components in maps/AncientWarCommunity/. Do not fabricate
  ComponentList.SC2Components, MapScript.galaxy, or a packaged .SC2Map archive.
- Never hand-edit generated build/ files. Do not commit secrets, game installations,
  caches, or original copyrighted map assets without appropriate permission.
- Do not change global Git identity or auth. Remote creation and pushing require
  the user's confirmation of verified owner, name, visibility, and remote URL.
  Use main. The bootstrap remote and initial push were approved for
  jjkyap/ancient-war-community (Public); do not infer approval for future pushes.
