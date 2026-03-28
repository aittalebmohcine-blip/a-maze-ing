*This project has been created as part of the 42 curriculum by aittalebmohcine-blip.*

#  A-Maze-ing

##  Description

**A-Maze-ing** is a Python project that generates, solves, and visualizes mazes in the terminal.

The objective of this project is to:
- Parse and validate a configuration file
- Generate a maze using a chosen algorithm
- Solve the maze using pathfinding techniques
- Render the maze in ASCII format
- Provide an interactive terminal interface

This project demonstrates strong understanding of **algorithms, data structures, modular design, and input validation**.
instruction:
Installation
Clone the repository and install dependencies:
make install
This installs required packages using pip and the requirements.txt file.

Run the Project
make run
This executes the main script using Python.

Debug Mode
make debug
Runs the program using Python’s built-in debugger (pdb).

Linting
Check code quality and static typing:
make lint
This runs:
flake8
mypy with strict typing flags

Clean Temporary Files
make clean
Removes:
__pycache__
.mypy_cache
ressources:
Documentation
Maze generation algorithms:
https://en.wikipedia.org/wiki/Maze_generation_algorithm
Depth-First Search:
https://en.wikipedia.org/wiki/Depth-first_search
Breadth-First Search:
https://en.wikipedia.org/wiki/Breadth-first_search
Pydantic:
https://docs.pydantic.dev/
Blessed:
https://blessed.readthedocs.io/
AI (ChatGPT) was used for:

Writing and improving docstrings
Structuring the project
Generating documentation (README)
dfs ascci render
Config file structure and format
the config file providing as a key=value format

          # reqire entires 
          WIDTH=width size  
          HEIGHT=height size 
          ENTRY=x, y 
          EXIT=x, y 
          OUTPUT_FILE=output_file 
          PERFECT= boolean is activated, the maze must contain exactly one path between the entry and the exit 
          # optional entries 
          ANIMATE= boolean 
          SEED= integer to get a maze seed 
chosen maze generation algorithm:
Maze Generation and Solving Algorithms
🔹 Maze Generation: Depth-First Search (DFS)

The maze is generated using the Depth-First Search (DFS) algorithm with a recursive backtracking approach.

How it works:
The algorithm starts from the entry cell.
It marks the current cell as visited.
It randomly selects one of the unvisited neighboring cells.
It removes the wall between the current cell and the chosen neighbor.
The process continues recursively.
When a cell has no unvisited neighbors, the algorithm backtracks to the previous cell and continues exploration.
Characteristics:
Produces a perfect maze (a maze with exactly one path between any two points).
Ensures all cells are reachable.
Creates long, winding paths with few dead ends.
🔹 Maze Solving: Breadth-First Search (BFS)

To find the shortest path between the entry and exit, the Breadth-First Search (BFS) algorithm is used.

How it works:
The search starts from the entry cell.
It explores all neighboring cells level by level.
A queue is used to manage the exploration order.
Each visited cell stores its parent to reconstruct the path.
When the exit is reached, the shortest path is rebuilt by backtracking from the exit to the entry.
Characteristics:
Guarantees the shortest path in an unweighted maze.
Systematic and complete exploration.
Efficient for grid-based pathfinding problems.
Your team and project management with:
doha:
cell/drawing/parsing
mohcine:the other parts
Anticipated Planning (Initial Plan)

At the beginning of the project, your planning typically includes:

Objectives
Define what you intended to build (e.g., a maze generator with DFS/BFS, rendering, validation, etc.).
Chosen Approach / Architecture
Maze generation algorithm(s): DFS (backtracking), BFS (for solving or exploration)
Data structures: grid, graph, cells
Input handling: configuration parsing
Output: ASCII rendering or file output
Task Breakdown
Example:
Parse configuration file
Validate inputs (width, height, entry/exit)
Implement maze generation
Implement solving (if required)
Build renderer (ASCII output)
Testing and debugging
Timeline / Milestones
Phase 1: Setup and parsing
Phase 2: Maze generation
Phase 3: Visualization
Phase 4: Testing and refinement
2. Evolution of the Plan (What Changed)

In real projects, the initial plan usually evolves due to challenges or discoveries:

Algorithm Adjustments
You may have started with DFS only, then added BFS for solving or validation.
Optimization or handling edge cases may have required changes.
Design Improvements
Refactoring code into modules (e.g., utils, rendering, parsing)
Introducing classes like Maze, Cell, or AsciiRenderer
Validation Enhancements
Adding stricter input validation using tools like Pydantic
Handling invalid configurations or edge cases
Debugging & Constraints
Fixing recursion issues in DFS
Adjusting memory/performance for large mazes
Handling incorrect entry/exit positions
Feature Additions
Bonus features (e.g., path visualization, special cells, animations, etc.)
Improved ASCII visualization (entry/exit markers, path highlighting)

What worked well:
The parsing component worked reliably. It correctly read and validated the configuration inputs (width, height, entry, exit), which helped prevent errors early and ensured the program ran smoothly.

What could be improved:
The drawing/visualization could be improved in terms of clarity and flexibility. The ASCII output can be made more readable with better formatting, and the rendering logic could be refactored to support enhancements like path highlighting or better scalability for larger mazes.

Tools Used
Python3
Github
Branch-based collaboration
Code merging and review
Makefile
Automated workflow
mypy
Static type checking
flake8
Code style enforcement
pip / build
Packaging and distribution
