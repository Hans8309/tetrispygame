## Purpose
This file guides AI coding agents (and contributors) to be immediately productive in the `tetrispygame` repository. It documents the project's structure, important patterns, run/debug workflows, and safe edit guidelines derived from the actual code.

## Big picture
- Single-player Tetris implemented with `pygame` in a single main script: `TetrisPygame.py`.
- Game state is stored in a 20x10 grid (list of 20 rows, each a list of 10 RGB tuples). `grid[y][x]` is the canonical view.
- Falling blocks are `Piece` objects. Per-block locked cells are stored in `locked_positions` as keys `(x, y)` -> color.
- Audio and visuals are loaded/played via `pygame.mixer` and `pygame.display` respectively; assets are expected at repository root (e.g. `music.ogg`, `settle.ogg`).

## Key files to read first
- `TetrisPygame.py` — canonical, current playable game (start here).
- `Tetris.py` / `TetrisTkinter*.py` — historical/alternate implementations (tkinter variants exist).
- `build/` — pyinstaller output; useful to see how an exe was packaged.
- `README.md` — author notes and background (mentions pygame→tkinter fallback).

## Important implementation details & patterns
- Grid vs locked positions: `grid` is derived each frame from `locked_positions` by `create_grid(locked_positions)`; modify `locked_positions` to change the world.
- Coordinate conventions: `locked_positions` keys are `(x, y)` but `grid` is indexed as `grid[y][x]`.
- Shape representation: `shapes` is a list of 5x5 string matrices. A shape's rotation index selects which 5x5 pattern to use. To add a shape, append the 5x5 rotation variants to `shapes` and a color to `shape_colors` at the same index.
- Top-level execution: the script instantiates the `pygame` window and runs `main_menu()` at import-time (no `if __name__ == '__main__'` guard). If you refactor to import this module, preserve or intentionally change that behavior.
- Globals: Many configuration values are module-level globals (e.g. `s_width`, `play_width`, `top_left_x`, `scores`). Small edits to these affect layout and scoring globally.
- Sounds: audio files are loaded at import-time with `pygame.mixer.Sound(...)`. Missing files will raise at import — check for files before changing runtime behavior.

## Run / debug workflows (Windows / PowerShell)
- Quick run: `python TetrisPygame.py` from repository root (ensure running in the folder containing audio files).
- When editing, run with verbose prints or use a debugger. Because the script opens a `pygame` window at import-time, prefer running the file directly rather than importing it in tests.

## Common change examples
- Add a new tetromino shape:
  1. Add the shape patterns to `shapes` (5x5 patterns for each rotation).
  2. Add a corresponding RGB tuple to `shape_colors` at the same index.
  3. Verify spawn position and `valid_space()` behavior.

- Change window size or block pixel size:
  - Update `s_width`, `s_height`, `play_width`, `play_height` and `block_size` together; recompute `top_left_x` / `top_left_y` if needed.

## Project-specific gotchas and safety notes for agents
- The code relies on side effects at import-time (window setup, audio loading, `main_menu()` call). If you refactor to make functions import-safe, keep an explicit entrypoint for running the game.
- `scores` is a global mutated in `clear_rows()`; editing that code should preserve how/when `scores` increments. The current logic increments `scores` inside a try/except while deleting locked cells — be cautious when changing row-clear logic.
- `clear_rows()` plays `sound_clear.play()`; audio side effects are mixed with game logic.
- Many helper functions assume 10x20 grid; avoid arbitrary re-sizing without changing related constants and drawing code.
- Several modules in the repo are experimental copies (`TetrisPygame200.py`, `TetrisPygame201.py`, ...). Prefer editing `TetrisPygame.py` unless you intentionally want to modify an alternate variant.

## Integration & packaging
- Packaging has been done with PyInstaller (see `build/`), so to create an exe use a PyInstaller spec similar to whatever produced `build/TetrisPygame`. Validate audio file inclusion when packaging.

## What to do if something is missing
- If runtime fails due to missing audio files, either add placeholder files with the same names or guard loading with file-exists checks before calling `pygame.mixer.Sound(...)`.

## How an AI agent should proceed
- Read `TetrisPygame.py` top-to-bottom to understand flow: initialization → `main_menu()` → `main()` → game loop.
- When changing gameplay logic (rotation, collision, scoring), run the game locally to validate behavior. Small changes can have outsized stateful effects.
- Preserve user-facing layout and controls unless the task explicitly intends to change them (controls are standard arrow keys + space).

If anything here is unclear or you'd like me to expand any section (for example, a short example patch that adds a new shape or an import-safe refactor), tell me which part and I'll iterate.
