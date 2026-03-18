# project structure:
a-maze-ing/
│
├── a_maze_ing.py        # main program
├── config.txt           # default config
├── maze.txt             # generated output
│
├── generator/
│   └── maze_generator.py
│
├── utils/
│   ├── config_parser.py
│   ├── file_writer.py
│   ├── path_converter.py
│   └── renderer.py
│
├── tests/               # optional test scripts
│
├── README.md
├── Makefile
└── .gitignore

--------

git commit naming:
- feat: new feature
- fix: bug fix
- refactor: improve code
- docs: README

---

# Tasks

- [ ] unperfect maze.
- [ ] error msgs.
- [ ] impossible maze params.
  - [ ] impossible dimentions
- [ ] maze dim too small for 42 pattern.
  - valid maze , just without the 42 pattern.
- [ ] Re-generate a new maze and display it.
- [ ] Show/Hide a valid shortest path.
- [ ] Change maze wall colours.
- [ ] Optional: set specific colours to display the “42” pattern.
- [ ] 

---------

## A-Maze-ing — Complete To-Do List

### 1. Project Setup

* [x] Create Git repository.
* [x] Create project structure.
* [x] Create `.gitignore` for Python artifacts.
* [ ] Setup virtual environment (recommended). 
* [x] Add `requirements.txt` if dependencies are used.

---

# 2. Main Program

### `a_maze_ing.py`

* [ ] Implement CLI entry point.
* [x] Accept exactly **one argument: config file**. 
* [ ] Handle missing/extra arguments.
* [ ] Handle all runtime errors gracefully.

Subtasks:

* [x] Load configuration.
* [x] Generate maze.
* [x] Solve maze.
* [x] Write output file.
* [x] Launch visual representation.

---

# 3. Configuration System

### Config parser

* [x] Read config file.
* [x] Ignore comments (`#`). 
* [x] Parse `KEY=VALUE` pairs.
* [x] Validate syntax.
* [x] Handle invalid lines.

### Required keys

* [x] `WIDTH`
* [x] `HEIGHT`
* [x] `ENTRY`
* [x] `EXIT`
* [x] `OUTPUT_FILE`
* [x] `PERFECT` 

### Optional keys

* [x] `SEED`
* [ ] `ALGORITHM`
* [ ] `DISPLAY_MODE`
* [ ] Other custom options.

### Validation

* [x] Width/height > 0.
* [x] Entry inside bounds.
* [x] Exit inside bounds.
* [x] Entry ≠ Exit.
* [x] Output file valid.
* [x] Perfect flag boolean.

### Repository requirement

* [x] Provide **default config file**. 

---

# 4. Maze Data Model

* [ ] Represent maze grid.
* [ ] Represent walls (N,E,S,W).
* [ ] Store entry cell.
* [ ] Store exit cell.
* [ ] Ensure neighbour wall consistency.

Subtasks:

* [ ] Define cell structure.
* [ ] Define wall encoding.
* [ ] Provide neighbour access utilities.

---

# 5. Maze Generation

* [x] Implement random maze generation. 
* [x] Support reproducibility using seed.

Subtasks:

* [ ] Initialize RNG with seed.
* [x] Generate full maze structure.
* [x] Ensure connectivity.
* [x] Ensure no isolated cells.

### PERFECT mode

* [ ] If `PERFECT=True`:

  * [ ] Ensure exactly **one path** between entry and exit. 

### Structural constraints

* [x] Maze borders must have walls.
* [x] Prevent inconsistent walls between neighbours.
* [ ] Prevent **3×3 open areas**.
* [ ] Corridors max width = 2.

---

# 6. “42” Pattern

* [x] Embed visible **“42” pattern** using closed cells. 
* [x] Validate maze size allows it.

Subtasks:

* [x] Detect if maze too small.
* [ ] If too small:

  * [ ] Print error message.
  * [ ] Continue maze generation without pattern.

---

# 7. Maze Solver

* [x] Implement shortest path solver.

Subtasks:

* [x] Use BFS or equivalent.
* [x] Compute path from entry → exit.
* [x] Convert path to `N,E,S,W` directions.
* [x] Store path.

---

# 8. Output File Writer

* [x] Write maze to output file.

Subtasks:

* [x] Encode each cell as **hexadecimal wall value**. 
* [x] Write rows line by line.
* [x] Add newline after each row.

After maze:

* [x] Add empty line.
* [x] Write entry coordinates.
* [x] Write exit coordinates.
* [x] Write shortest path.

---

# 9. Visual Representation

* [ ] Terminal ASCII rendering

### Visual features

* [x] Show maze walls.
* [x] Show entry.
* [x] Show exit.
* [x] Show solution path.

### User interactions

* [x] Regenerate maze.
* [x] Toggle shortest path display.
* [x] Change wall colors.
* [ ] (Optional) color the “42” pattern.

---

# 10. Reusable Maze Generator Module

Create reusable module.

Subtasks:

* [x] Implement `MazeGenerator` class. 
* [x] Provide maze generation API.
* [x] Provide solution access.
* [ ] Expose maze structure.

### Packaging

* [ ] Package module as `mazegen-*`.
* [ ] Single installable package file.

Allowed formats:

* [ ] `.whl`
* [ ] `.tar.gz` 

### Repository requirements

* [ ] Include files needed to build package.

---

# 11. Documentation for Reusable Module

Provide documentation explaining:

* [ ] How to install package.
* [ ] How to instantiate generator.
* [ ] How to pass parameters (size, seed).
* [ ] How to access maze structure.
* [ ] How to access solution path.

---

# 12. Code Quality Requirements

* [ ] Python ≥ 3.10. 
* [ ] Follow `flake8`.
* [ ] Pass `mypy`.
* [ ] Use type hints.
* [ ] Write docstrings (PEP257).
* [ ] Handle exceptions properly.
* [ ] Use context managers.

---

# 13. Makefile

Create Makefile with rules:

* [ ] `install`
* [ ] `run`
* [ ] `debug`
* [ ] `clean`
* [ ] `lint`
* [ ] `lint-strict` (optional) 

---

# 14. Testing (recommended)

* [ ] Create test programs.
* [ ] Test edge cases.
* [ ] Use `pytest` or `unittest`.

(Not submitted but recommended.)

---

# 15. README.md

Include sections:

### Required sections

* [ ] First line with project attribution. 
* [ ] Description.
* [ ] Instructions.
* [ ] Resources.

### Project explanation

* [ ] Config file structure.
* [ ] Maze generation algorithm.
* [ ] Reason for algorithm choice.
* [ ] Reusable code explanation.

### Team section

* [ ] Member roles.
* [ ] Planning evolution.
* [ ] What worked / improvements.
* [ ] Tools used.

---

# 16. Bonuses (Optional)

* [ ] Multiple generation algorithms.
* [ ] Maze generation animation. 
