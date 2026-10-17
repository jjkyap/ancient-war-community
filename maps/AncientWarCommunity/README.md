# Editable map placeholder

No valid SC2 map exists here yet. Follow docs/DEVELOPMENT.md to create one in
Galaxy Editor and save it here as component folders. Keep the editor-generated
ComponentList.SC2Components and other components under version control.
Never rename this README or a ZIP file into a .SC2Map.

src/galaxy is the authoritative hand-written script source. After creating a
real map, stage/import those scripts under the map's `AW/` virtual paths and
validate the include graph in Editor. No import manifest is fabricated here.
