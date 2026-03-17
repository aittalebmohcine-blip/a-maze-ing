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
* [ ] Accept exactly **one argument: config file**. 
* [ ] Handle missing/extra arguments.
* [ ] Handle all runtime errors gracefully.

Subtasks:

* [ ] Load configuration.
* [ ] Generate maze.
* [ ] Solve maze.
* [ ] Write output file.
* [ ] Launch visual representation.

---

# 3. Configuration System

### Config parser

* [ ] Read config file.
* [ ] Ignore comments (`#`). 
* [ ] Parse `KEY=VALUE` pairs.
* [ ] Validate syntax.
* [ ] Handle invalid lines.

### Required keys

* [ ] `WIDTH`
* [ ] `HEIGHT`
* [ ] `ENTRY`
* [ ] `EXIT`
* [ ] `OUTPUT_FILE`
* [ ] `PERFECT` 

### Optional keys

* [ ] `SEED`
* [ ] `ALGORITHM`
* [ ] `DISPLAY_MODE`
* [ ] Other custom options.

### Validation

* [ ] Width/height > 0.
* [ ] Entry inside bounds.
* [ ] Exit inside bounds.
* [ ] Entry ≠ Exit.
* [ ] Output file valid.
* [ ] Perfect flag boolean.

### Repository requirement

* [ ] Provide **default config file**. 

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

* [ ] Implement random maze generation. 
* [ ] Support reproducibility using seed.

Subtasks:

* [ ] Initialize RNG with seed.
* [ ] Generate full maze structure.
* [ ] Ensure connectivity.
* [ ] Ensure no isolated cells.

### PERFECT mode

* [ ] If `PERFECT=True`:

  * [ ] Ensure exactly **one path** between entry and exit. 

### Structural constraints

* [ ] Maze borders must have walls.
* [ ] Prevent inconsistent walls between neighbours.
* [ ] Prevent **3×3 open areas**.
* [ ] Corridors max width = 2.

---

# 6. “42” Pattern

* [ ] Embed visible **“42” pattern** using closed cells. 
* [ ] Validate maze size allows it.

Subtasks:

* [ ] Detect if maze too small.
* [ ] If too small:

  * [ ] Print error message.
  * [ ] Continue maze generation without pattern.

---

# 7. Maze Solver

* [ ] Implement shortest path solver.

Subtasks:

* [ ] Use BFS or equivalent.
* [ ] Compute path from entry → exit.
* [ ] Convert path to `N,E,S,W` directions.
* [ ] Store path.

---

# 8. Output File Writer

* [ ] Write maze to output file.

Subtasks:

* [ ] Encode each cell as **hexadecimal wall value**. 
* [ ] Write rows line by line.
* [ ] Add newline after each row.

After maze:

* [ ] Add empty line.
* [ ] Write entry coordinates.
* [ ] Write exit coordinates.
* [ ] Write shortest path.

---

# 9. Visual Representation

* [ ] Terminal ASCII rendering

### Visual features

* [ ] Show maze walls.
* [ ] Show entry.
* [ ] Show exit.
* [ ] Show solution path.

### User interactions

* [ ] Regenerate maze.
* [ ] Toggle shortest path display.
* [ ] Change wall colors.
* [ ] (Optional) color the “42” pattern.

---

# 10. Reusable Maze Generator Module

Create reusable module.

Subtasks:

* [ ] Implement `MazeGenerator` class. 
* [ ] Provide maze generation API.
* [ ] Provide solution access.
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
