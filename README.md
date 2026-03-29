*This project has been created as part of the 42 curriculum by mait-tal, maeev-d.*

# Description

A-Maze-ing is a Python command-line maze generator and solver. The goal is to provide a reliable, reproducible maze tool that produces a solvable grid and outputs an ASCII map with a discovered shortest path. It supports configurable width/height, entry/exit points, optional perfect/non-perfect mazes, and deterministic results via seed control.

# Instructions

1. Install dependencies
   - `make install` (reads `requirements.txt`)
2. Run program
   - `make run` (equivalent to `python3 a_maze_ing.py config.txt`)
3. Optional commands
   - `make debug` (extra logging / verbose checks)
   - `make lint` (static checks)
   - `make clean` (remove generated files and caches)

# Config file structure

`config.txt` must include:

- `WIDTH` (int 9-100)
- `HEIGHT` (int 6-100)
- `ENTRY` (x,y inside bounds)
- `EXIT` (x,y inside bounds, not equal to ENTRY)
- `OUTPUT_FILE` (path)
- `PERFECT` (`true`/`false`)
- `SEED` (optional integer)

Example:

```
WIDTH=30
HEIGHT=20
ENTRY=0,0
EXIT=29,19
OUTPUT_FILE=out/maze.txt
PERFECT=true
SEED=42
```

# Maze generation algorithm

- Generation: iterative Depth First Search using an explicit stack and cell visitation; carve passages and backtrack using the stack when dead ends are reached.
- Solver: Breadth First Search (BFS) for shortest path discovery in the generated grid.

# Why this algorithm

- Iterative DFS with stack avoids recursion while giving a complete traversal and perfect maze behavior when `PERFECT=true`.
- BFS gives guaranteed shortest path in grid graph.
- This approach is simple, robust, and fits the 42 project requirement for clear pathfinding behavior.

# Reusable code

- `mazegen/generator.py`: maze grid representation, generator and solver routines. Can be reused as `from mazegen.generator import MazeGenerator`.
- `utils/parsing.py`: config parser + validator, supports reuse in other CLI tools.
- `utils/drawing.py`: ASCII map render + path overlay for text output.
- `utils/file_writer.py`: framing output to files.

# Team and project management

- Roles:
  - `mait-tal`: project lead, core implementation, module structure.
  - `maeev-d`: validation, code review, documentation.

- Planning evolution:
  1. Start with config parser and validation in `utils/parsing.py`.
  2. Build generator and solver in `mazegen/generator.py`.
  3. Add CLI and output module support (`a_maze_ing.py`, `utils/file_writer.py`).
  4. Add optional config options and robust style checks (make targets).

- What worked:
  - Modular architecture split by responsibility.
  - Clear algorithm design with deterministic seeding.

- What could be improved:
  - Add automated tests (`unittest`/`pytest`) and CI.
  - Increase interactive user feedback and dynamic visual mode.

- Tools used:
  - Python 3, Make, Git, `pydantic` (input validation), `flake8`/`black` for linting.
  - Optional: `blessed` for terminal enhancements (if added later).

# Advanced features

- `PERFECT=false` supports mazes with loops (non-perfect) by not strictly forcing one-way connections.
- `SEED` enables deterministic maze repeatability.

# Resources

- Python docs: https://docs.python.org/3/
- DFS maze generation: https://en.wikipedia.org/wiki/Maze_generation_algorithm
- BFS shortest path: https://en.wikipedia.org/wiki/Breadth-first_search
- AI usage: ChatGPT (Raptor mini) assisted in README editing, content clarity, and project requirement alignment.

