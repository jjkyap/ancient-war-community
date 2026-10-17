# Local development

## Inspected environment (2026-10-17)

| Tool | Observation |
| --- | --- |
| OS | Fedora Linux 44 Workstation, x86_64 |
| Shell | Bash; SHELL=/bin/bash |
| Git | 2.56.0, /usr/bin/git |
| Python | 3.14.8 via pyenv; /usr/bin/python3 also reports 3.14.8 |
| Node / npm | Commands available; not required by project checks |
| VS Code | /usr/bin/code; Python and Pylance extensions detected |
| SC2 / Editor / Wine | No executables or installations found in inspected common paths |
| Galaxy Toolkit / Modkit | talv.sc2galaxy not in installed extension list |
| Galaxy validator / server | No relevant executable found on PATH |
| GitHub CLI | Initially absent; user installed gh 2.102.0 and authenticated via keyring |
| Git identity | Existing effective author name jjkyap; no identity settings changed |
| GitHub owner | jjkyap, user-confirmed and verified via gh api user after authentication |

Detection was limited to PATH, VS Code extensions, /opt, /usr/local/bin,
~/.local/bin, project files, and common game installation locations. Undetected
software may exist elsewhere. VS Code's extension listing returned installed IDs
alongside a sandbox log-directory error. Shell startup also printed pyenv shim
rehash warnings; Python itself ran successfully. No global environment was changed.

The initially empty folder contained a sandbox-protected empty .git directory.
`git init -b main` succeeded through an approved elevated command after the
sandboxed attempt failed. Do not create an alternative hidden Git directory to
work around permissions. Further .git writes may also need command approval.

## Dependency-free checks

Use Python 3.11+; no packages or virtual environment are required:

```sh
python3 tools/validate_data.py
python3 tools/generate.py --check
python3 tools/check.py
python3 tools/generate.py
```

Run from the repository root. Entry points locate inputs using their own paths;
the combined runner sets the subprocess working directory itself. An optional
explicit definition file can be passed to validate_data.py.

- Schema validation rejects missing/extra fields, duplicate JSON keys/IDs,
  invalid integers (including booleans), and broken catalog references.
- Null values are valid research placeholders, not defaults or runtime approval.
- The constant check compares committed Galaxy constants against confirmed data.
- Tests use synthetic catalogs, dimensions, and capacity. They verify logical
  ordering, overflow/conservation, stable purchase IDs, and input immutability.
- Generation writes build/AW/core/Constants.galaxy deterministically. Unknown
  economy, dimensions, stats, and catalog tables are deliberately not emitted.
  Review the generated output before updating src/galaxy/core/Constants.galaxy.

These checks do not parse/compile Galaxy, open a map, validate Editor imports,
or exercise SC2. No portable SC2 build command has been established. Exports
belong in ignored build/; actual map components remain tracked.

## Galaxy tooling

The current [Modkit Marketplace documentation](https://marketplace.visualstudio.com/items?itemName=talv.sc2galaxy)
identifies talv.sc2galaxy as its extension ID, offers Modkit on the prerelease
channel, and describes bundled Galaxy language support and the **Modkit: Verify
Galaxy Script** command. It is alpha tooling. Install through VS Code Extensions,
select the prerelease channel if using Modkit, and record the chosen version.
On Linux its documentation requires configuring modkit.sources for the actual
SC2 installation; do not commit someone else's absolute installation path.

The [Toolkit repository](https://github.com/sc2-arcade-watcher/sc2-galaxy-toolkit)
also provides project history. The similarly named galaxyproject language server
targets a different, scientific Galaxy product and is not an SC2 validator.

No engine native is called by the bootstrap. Before adding one, inspect the
matching installed game's TriggerLibs declaration (and required dependency),
record the API source, and validate against that version. No compilation is
claimed merely because a file has a .galaxy extension.

## Manual Galaxy Editor setup (required)

Use a machine where StarCraft II and Galaxy Editor actually run. No supported
native Linux Editor was detected here; this bootstrap does not establish Wine
compatibility. Keep game and Editor installations outside the repository.

1. Launch Galaxy Editor. Choose **File > New**, select a map, and create a blank
   terrain. Use temporary terrain settings only for the integration smoke test;
   they are not claims about Ancient War 2's original layout.
2. Open **File > Dependencies** and record the Editor/game version and exact
   selected dependencies below. Do not guess original dependencies or download
   original map assets to make the skeleton work.
3. Choose **File > Save As**. Select **StarCraft II Component Folders
   (*.SC2Components)** as the save type. Save the component output under
   maps/AncientWarCommunity/. If Editor creates an additional named directory,
   use that directory as the component root and document the actual path here.
4. Confirm that Editor created a real **ComponentList.SC2Components** with the
   map's associated components. Close and reopen that file in Editor. Do not
   manufacture a manifest or rename an empty directory to a .SC2Map archive.
   Keep the placeholder README outside Editor-owned components if needed.
5. Open the **Import** module (F9). Import all files from src/galaxy preserving
   subdirectories beneath virtual **AW/**. For example,
   src/galaxy/core/Constants.galaxy becomes AW/core/Constants.galaxy, and
   src/galaxy/Bootstrap.galaxy becomes AW/Bootstrap.galaxy. Save the map. Imported
   copies are staged output; src/galaxy remains the authoritative source.
6. Open the **Trigger** module (F6). Add a **Custom Script** object at global
   scope with `include "AW/Bootstrap"` as its script. This is a declaration
   include, not a trigger action. Include it only once. Use the script view to
   confirm it appears at global scope in the Editor-generated script. Do not
   replace MapScript.galaxy or put declarations inside an action function.
7. Save and inspect Editor's errors. If Modkit is available, verify the integrated
   script with resolved dependencies as an additional check. Fix imports or
   syntax based on actual diagnostics, then update each module's validation note.
   The include/module workflow has not been exercised in this environment yet.
8. Use **File > Test Document** (Ctrl+F9) for a minimal load test. There is no
   gameplay to exercise yet. Record success/failure, versions, dependencies, and
   errors below. Export a packaged .SC2Map to build/ only after a real map exists.
9. Review the complete component diff, including trigger metadata and required
   binary terrain components, before committing. Never globally ignore .SC2Map,
   .SC2Data, or .SC2Components source. Do not overwrite unrelated map projects.

Component-folder saving is described in the
[Editor tutorial on exporting assets](https://s2editor-guides.readthedocs.io/New_Tutorials/07_Lessons/083_Export_Game_Assets/);
the [GalaxyScript tutorial](https://s2editor-guides.readthedocs.io/New_Tutorials/03_Trigger_Editor/058_GalaxyScript/)
describes script inclusion. UI labels/shortcuts should be checked against the
installed Editor version. No generated map integration is certified yet.

### Integration record

```text
Editor and SC2 version: not yet available
Dependencies: not yet selected/observed
Component root and manifest: not created
Modkit version and verification: not installed / not run
Editor save and script validation: not run
SC2 Test Document: not run
```

## Git and GitHub handoff

The user approved the public repository and initial commit/push, installed GitHub
CLI, and authenticated. Both gh auth status and gh api user verified the active
account as jjkyap. The sandbox initially could not reach api.github.com and
misreported invalid authentication; verification succeeded with approved network
access. No agent changes were made to global Git identity or authentication.

The owner is **jjkyap**. Repository:
**ancient-war-community**, visibility **Public**, remote
**https://github.com/jjkyap/ancient-war-community.git**, default branch **main**.
The repository was created after checking that the name was available. Use this
URL as origin and track origin/main. Do not overwrite another repository.

For a new machine, install GitHub CLI using the
[official installation instructions](https://github.com/cli/cli#installation),
then authenticate with the same GitHub account used in VS Code:

```sh
gh auth login --hostname github.com --git-protocol https --web
gh auth status --hostname github.com
gh api user --jq .login
```

Login is a user-run setup step; account verification was executed by the agent.
In the browser, explicitly choose jjkyap. Do not run login against a different
account or change global identity/authentication settings on the user's behalf.
The [official auth documentation](https://cli.github.com/manual/gh_auth_login)
describes this browser flow. If multiple accounts are present, inspect the active
one and agree on any change before altering authentication. Never print tokens.

Before creation or pushing, verify CLI authentication is jjkyap and obtain the
user's confirmation of the exact owner, repository, visibility, and URL. If the
user has already approved this exact proposal conditional on that verification,
honor that approval without asking again. Any owner or visibility change needs
a fresh review.
After approval: check the name is available, create the public repository,
review and stage only this project's files, make the initial commit, configure
origin, and push main with upstream tracking. Do not force-push or overwrite an
existing unrelated repository. If credentials cannot push, resolve that with the
user instead of assuming VS Code's session grants permission.

## Next implementation task

Create the real map and validate these Galaxy interfaces before gameplay work.
In parallel with future research, collect original grid dimensions, deployment
capacity, and package-order evidence using docs/UNKNOWN_MECHANICS.md. Those
observations unlock the first small Galaxy roster/grid/formation milestone.
