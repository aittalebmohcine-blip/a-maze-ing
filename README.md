*This project has been created as part of the 42 curriculum by mait-tal, maeev-d.*

# A-Maze-ing - "This is the way"

## Description

**A-Maze-ing** is a Python project that generates, solves, and visualizes mazes in an interactive terminal interface. This project demonstrates expertise in **algorithm design, graph theory, data structures, modular architecture, and input validation**.

### Project Goals

- **Parse & Validate Configuration**: Read and validate a configuration file using a robust validation framework
- **Generate Mazes**: Implement a maze generation algorithm using recursive backtracking (DFS)
- **Solve Mazes**: Find the shortest path between entry and exit points using BFS
- **Render & Visualize**: Display mazes in ASCII format with configurable styling
- **Interactive Experience**: Provide an interactive terminal UI for real-time exploration and customization

### Key Features

- ✨ **Perfect Maze Generation**: Creates mazes with exactly one solution path
- 🎨 **Colored Terminal Output**: Multiple color themes for visual appeal (blue, red, white, green, brown)
- 🔄 **Interactive Controls**: Regenerate mazes, toggle solutions, and change colors in real-time
- 📊 **Solution Visualization**: Display the shortest path overlay on the maze
- 🎯 **Bonus "42 Pattern"**: Special animation and branded maze element
- 🔒 **Strict Validation**: Comprehensive input validation using Pydantic
- 🎮 **Reproducible Generation**: Optional seed parameter for deterministic maze generation

---

## Instructions

### Installation

Install required dependencies:

```bash
make install
```

This command installs all Python packages specified in `requirements.txt`:
- **blessed** (v1.33.0): Terminal styling and color support
- **pydantic** (v2.12.5): Data validation and configuration parsing

### Running the Project

Execute the main application:

```bash
make run
```

This runs `python3 a_maze_ing.py config.txt`

**Prerequisites**: The `config.txt` file must exist in the root directory with proper configuration.

### Interactive Terminal Commands

Once the application starts, use these controls:

- **1** - Regenerate the maze with new random design
- **2** - Show/hide the solution path
- **3** - Cycle through color themes
- **4** - Quit the application

### Configuration File Format

Create a `config.txt` file in the root directory with the following structure:

```plaintext
# Required Entries
WIDTH=15
HEIGHT=10
ENTRY=0,0
EXIT=9,9
OUTPUT_FILE=output.txt
PERFECT=false

# Optional Entries
SEED=-1
```

#### Configuration Parameters

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| `WIDTH` | Integer | 9-100 | Horizontal maze dimension |
| `HEIGHT` | Integer | 6-100 | Vertical maze dimension |
| `ENTRY` | Tuple (x,y) | Valid coordinates within bounds | Starting position (excluded from 42-pattern) |
| `EXIT` | Tuple (x,y) | Valid coordinates within bounds | End position (excluded from 42-pattern) |
| `PERFECT` | Boolean | true/false | If true, maze has exactly one solution |
| `OUTPUT_FILE` | String | Valid file path | Output file for maze data in hex format |
| `SEED` | Integer (Optional) | Any integer | Random seed for reproducible mazes |

#### Validation Rules

- `WIDTH` and `HEIGHT` must be within [9-100] and [6-100] respectively
- `ENTRY` ≠ `EXIT`
- Entry and exit must be within maze bounds
- Entry and exit cannot be inside the center "42 pattern" (protected zone)

### Output File Format

The `output.txt` file (or custom filename) contains the maze data:

```plaintext
[Row 1: Hex values representing bitmask walls]
[Row 2: Hex values representing bitmask walls]
...
[Empty line]
[Entry coordinates: x,y]
[Exit coordinates: x,y]
[Solution path: Direction sequence]
```

**Bitmask Encoding**: Each cell value is a 4-bit integer where:
- Bit 0 (N = 1): North wall present
- Bit 1 (E = 2): East wall present
- Bit 2 (S = 4): South wall present
- Bit 3 (W = 8): West wall present

Example: `F` (15 = 0b1111) = all walls present; `0` = no walls

**Path Encoding**: Directions are represented as string of characters:
- `N` - Move North (up)
- `E` - Move East (right)
- `S` - South (down)
- `W` - West (left)

### Development Commands

#### Debug Mode

Run with Python debugger:

```bash
make debug
```

#### Code Quality & Linting

Check code quality and type safety:

```bash
make lint
```

This runs:
- **flake8**: Code style checking
- **mypy**: Static type analysis with strict flags

#### Clean Temporary Files

Remove cache and compiled files:

```bash
make clean
```

Removes `__pycache__` directories and `.mypy_cache`

---

## Maze Generation Algorithm

### Algorithm: Depth-First Search (DFS) with Recursive Backtracking

The maze is generated using a **recursive backtracking algorithm** based on Depth-First Search principles.

#### How DFS Maze Generation Works

1. **Initialization**: Start from the entry cell, mark it as visited, initialize all walls between cells
2. **Exploration**: From the current cell, randomly select an unvisited neighbor
3. **Carving**: Remove the wall between the current cell and the chosen neighbor
4. **Recursion**: Move to the neighbor and repeat the process recursively
5. **Backtracking**: When a cell has no unvisited neighbors, backtrack to the previous cell
6. **Completion**: Continue until all cells are visited and fully explored

#### Characteristics & Properties

| Property | Value |
|----------|-------|
| **Type** | Perfect maze (exactly one solution path) |
| **Connectivity** | All cells reachable from entry |
| **Path Style** | Long, winding corridors with few dead ends |
| **Bias** | Creates tunnels preferring certain directions early |
| **Memory** | O(width × height) for grid storage |
| **Time** | O(width × height) for generation |
| **Solution Uniqueness** | Guaranteed single solution when PERFECT=true |

### Algorithm: Breadth-First Search (BFS) for Maze Solving

The generated maze is solved using **Breadth-First Search** to find the shortest path from entry to exit.

#### How BFS Maze Solving Works

1. **Initialization**: Create a queue, add entry point with distance 0
2. **Level-by-level exploration**: Dequeue a cell and explore all unvisited neighbors
3. **Parent tracking**: Mark parent cell for each neighbor to enable path reconstruction
4. **Termination**: When exit is reached, backtrack using parent pointers from exit to entry
5. **Path encoding**: Convert cell coordinates into direction strings (N, S, E, W)

#### Why BFS for Solving

- ✅ Guarantees shortest path in unweighted grids
- ✅ Efficient exploration order (level-by-level)
- ✅ Simple to implement and debug
- ✅ Optimal for visual display (demonstrates solution clearly)

---

## Algorithm Selection Rationale

### Why Depth-First Search (DFS) for Generation?

1. **Perfect Maze Guarantee**: DFS with backtracking naturally produces mazes with exactly one path between any two points
2. **Complete Exploration**: Recursive nature ensures every cell is visited
3. **Simplicity**: Elegant recursive implementation without complex state management
4. **Visual Appeal**: Creates long, winding corridors that look natural and challenging
5. **Memory Efficient**: Uses implicit call stack for backtracking (no explicit stack needed)
6. **Reproducible**: With seed parameter, generates identical mazes for testing

### Alternative Algorithms Considered

| Algorithm | Pros | Cons | Decision |
|-----------|------|------|----------|
| **Prim's Algorithm** | Fast, good wall removal | Complexity higher, less intuitive | ❌ Not chosen |
| **Kruskal's Algorithm** | Mathematical elegance, efficient | Requires MST concepts | ❌ Not chosen |
| **Recursive Backtracking** | Perfect mazes, intuitive, efficient | ✅ **CHOSEN** | ✅ Selected |
| **Hunt & Kill** | Fewer backtracking operations | More complex implementation | ❌ Not chosen |
| **Eller's Algorithm** | Memory efficient for large mazes | Harder to understand and implement | ❌ Not chosen |

### Why Breadth-First Search (BFS) for Solving?

- **Shortest Path**: Guaranteed to find optimal solution
- **Simplicity**: Straightforward queue-based implementation
- **Visualization**: Level-by-level exploration creates clear visual representation
- **Time Complexity**: O(width × height), acceptable for project scope

---

## Project Structure & Reusable Components

### Directory Organization

```
a-maze-ing/
├── a_maze_ing.py          # Main entry point and interactive UI
├── config.txt             # Configuration file (user-customizable)
├── output.txt             # Generated maze output
├── requirements.txt       # Python dependencies
├── Makefile               # Build and development commands
├── README.md              # This file
│
├── mazegen/               # Maze generation and solving module
│   ├── __init__.py
│   └── generator.py       # MazeGenerator class (core algorithm)
│
└── utils/                 # Utility modules for support tasks
    ├── __init__.py
    ├── parsing.py        # Configuration validation and parsing
    ├── drawing.py        # ASCII rendering engine
    └── file_writer.py    # Output file generation
```

### Reusable Components

#### 1. **MazeGenerator Class** (`mazegen/generator.py`)

**Reusability Score**: ⭐⭐⭐⭐⭐ (Highly Reusable)

**What it does**: Core maze generation and solving engine

**How to reuse**:
```python
from mazegen.generator import MazeGenerator

# Create generator
gen = MazeGenerator(
    width=20,
    height=15,
    entry=(0, 0),
    exit=(19, 14),
    perfect=True,
    seed=42
)

# Generate maze
gen.generate()

# Solve maze
solution_path = gen.bfs_solver()

# Access grid
maze_grid = gen.grid
```

**Extensibility**: Can be extended to:
- Support different solving algorithms (A*, Dijkstra)
- Add maze optimization techniques
- Implement different generation algorithms
- Export to various formats

#### 2. **Configuration Validation** (`utils/parsing.py`)

**Reusability Score**: ⭐⭐⭐⭐ (Very Reusable)

**What it does**: Robust input validation using Pydantic

**How to reuse**:
```python
from utils.parsing import MazeConfig, parsing_config_file

# Option 1: Parse from file
config = parsing_config_file("config.txt")

# Option 2: Create programmatically
config = MazeConfig(
    WIDTH=20,
    HEIGHT=15,
    ENTRY=(0, 0),
    EXIT=(19, 14),
    PERFECT=True,
    OUTPUT_FILE="maze.txt"
)
```

**Extensibility**: Can be adapted for:
- Other configuration formats (JSON, YAML)
- Additional validation rules
- Different project types

#### 3. **ASCII Renderer** (`utils/drawing.py`)

**Reusability Score**: ⭐⭐⭐⭐ (Very Reusable)

**What it does**: Converts bitmask maze grid to ASCII art

**How to reuse**:
```python
from utils.drawing import AsciiRenderer

renderer = AsciiRenderer(maze_gen, entry, exit)

# Render without solution
plain_maze = renderer.render()

# Render with solution path
solved_maze = renderer.render(path="NNNEEESSS")

# Print to terminal
print(plain_maze)
```

**Features**: 
- Bitmask interpretation (N, E, S, W walls)
- Solution path overlay
- 42-pattern preservation
- Flexible styling

**Extensibility**: Can be extended for:
- Different ASCII characters
- 2D graphics rendering
- Interactive visualization
- Color coding by regions

#### 4. **File Writer** (`utils/file_writer.py`)

**Reusability Score**: ⭐⭐⭐ (Moderately Reusable)

**How to reuse**:
```python
from utils.file_writer import file_writer

file_writer(
    maze_grid,
    start=(0, 0),
    end=(19, 14),
    path="NNNEEESSS",
    output_file_path="output.txt"
)
```

---


## Roles


**Responsibilities**:

**mait-tal**:
- Algorithm implementation (DFS, BFS generation and solving)
- Configuration parsing and validation
- Project packaging and distribution
- Build system (Makefile) development

**maeev-d**:
- ASCII rendering and display logic
- Terminal UI and interactive components
- Configuration parsing and validation (shared)

**Shared**:
- Architecture and design decisions
- Module integration and testing
- Documentation and README

### Project Planning & Evolution

#### Initial Plan

1. ✅ **Phase 1**: Understand maze generation algorithms and choose one
2. ✅ **Phase 2**: Implement basic DFS maze generation
3. ✅ **Phase 3**: Implement BFS maze solving
4. ✅ **Phase 4**: ASCII rendering engine
5. ✅ **Phase 5**: Configuration system with validation
6. ✅ **Phase 6**: Interactive terminal UI
7. ✅ **Phase 7**: Output file generation
8. ✅ **Phase 8**: Testing, optimization, and documentation

#### Plan Evolution & Adjustments

| Original Plan | Actual Implementation | Reason for Change |
|---------------|----------------------|-------------------|
| Basic string config parsing | Pydantic validation framework | Better type safety and error messages |
| Simple output format | Hex bitmask format | More compact, industry-standard |
| Static rendering | Interactive color-changing UI | Enhanced user experience |
| No reproducibility | Seed parameter added | Enables testing and debugging |
| Single color display | Multi-color theme system | Better visual feedback |
| Manual wall carving | Efficient bitwise operations | Performance optimization |

### What Worked Well ✅

1. **Modular Architecture**: Separation into `mazegen` and `utils` packages enabled isolated development and testing
2. **Type Hinting**: Full type annotations caught bugs early and improved code clarity
3. **Pydantic Validation**: Comprehensive validation eliminated invalid configuration edge cases
4. **ASCII Rendering**: Clean abstraction for maze visualization enabled rapid UI iteration
5. **Makefile Automation**: Simplified installation, running, and maintenance tasks
6. **Seed Parameter**: Enabled reproducible testing and debugging
7. **Interactive Terminal**: Real-time color changing and regeneration enhanced user engagement
8. **Documentation**: Well-structured docstrings aided development and maintenance

### What Could Be Improved 🔧

1. **Algorithm Performance**: For very large mazes (100×100), could optimize memory with iterator pattern
2. **Visualization Options**: Could add animated generation and solving sequences
3. **Additional Algorithms**: Could implement Prim's, Kruskal's, or Eller's for comparison
4. **Unit Testing**: Could add pytest suite for comprehensive test coverage
5. **Error Recovery**: Could implement graceful error handling for manual config edits
6. **Maze Export**: Could support additional formats (PNG, ASCII art, SVG)
7. **Performance Profiling**: Could analyze bottlenecks in large maze generation
8. **Solver Visualization**: Could show solution-finding process in real-time

### Tools & Technologies Used 🛠️

| Tool | Purpose | Version |
|------|---------|---------|
| **Python** | Programming language | 3.10+ |
| **Blessed** | Terminal styling and colors | 1.33.0 |
| **Pydantic** | Configuration validation | 2.12.5 |
| **flake8** | Code style checking | Latest |
| **mypy** | Static type checking | Latest |
| **Makefile** | Build automation | GNU Make |
| **Git** | Version control | Latest |
| **Claude AI** | AI assistance (see AI Usage below) | - |

### AI Usage & Assistance 🤖

AI was utilized for specific, targeted tasks to enhance development efficiency:

#### Tasks Where AI Was Used

| Task | Scope | Details |
|------|-------|---------|
| **Docstring Improvement** | Code documentation | Enhanced clarity and completeness of module docstrings |
| **Project Structure** | Architecture planning | Validated modular design approach and package organization |
| **Algorithm Explanation** | Documentation | Clarified DFS/BFS algorithm descriptions for README |
| **Config Validation Logic** | Code review | Suggested Pydantic for robust input validation |
| **Error Messages** | User experience | Crafted clear, actionable error messages |
| **Code Formatting** | Style consistency | Ensured compliance with PEP 8 standards |

#### Tasks Where AI Was NOT Used

- ❌ Core algorithm implementation (DFS, BFS)
- ❌ ASCII rendering logic
- ❌ Testing and debugging
- ❌ Performance optimization
- ❌ Architecture decisions
- ❌ Final code reviews

#### AI Integration Principles

- AI was used as a **reference and clarification tool**, not as code generation
- All AI-assisted code was reviewed, tested, and modified before integration
- Core algorithms and critical logic were implemented manually for understanding

---

## Resources & References

### Documentation & Learning Materials

#### Maze Generation & Algorithms

- [Maze Generation Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
  - Comprehensive overview of all major maze generation techniques
  
- [Depth-First Search (DFS) - Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)
  - Theoretical foundation and applications of DFS
  
- [Breadth-First Search (BFS) - Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
  - BFS algorithm theory and pathfinding applications
  
- [Recursive Backtracking - GeeksforGeeks](https://www.geeksforgeeks.org/maze-generation-using-backtracking/)
  - Detailed explanation with code examples

#### Python Libraries & Frameworks

- [Pydantic Documentation](https://docs.pydantic.dev/)
  - Official documentation for data validation framework
  
- [Blessed Documentation](https://blessed.readthedocs.io/)
  - Terminal styling, color support, and interactive features
  
- [Python Type Hints - Official Docs](https://docs.python.org/3/library/typing.html)
  - Python type annotation system

#### Code Quality Tools

- [flake8 - Style Guide Enforcement](https://flake8.pycqa.org/)
  - PEP 8 compliance checking
  
- [mypy - Static Type Checker](https://www.mypy-lang.org/)
  - Python static type checking documentation

### Related Projects & Inspiration

- Maze visualization projects on GitHub
- Terminal UI projects using Blessed
- Educational resources on graph algorithms from CS curricula

---

## Advanced Features

### Perfect Maze Generation

When `PERFECT=true`, the maze is guaranteed to have exactly one path between any two points. This is a mathematical property of depth-first search with complete backtracking.

### Seed-Based Reproducibility

The `SEED` parameter enables deterministic maze generation:
- Use `SEED=42` to always generate the same maze
- Use `SEED=-1` for random generation each time
- Useful for testing, debugging, and sharing specific mazes

### Multi-Color Themes

The interactive UI provides multiple color options:
- **Blue** - Cool, calming aesthetic
- **Red** - Bold, energetic feel
- **White** - Clean, minimal look
- **Green** - Natural, harmony
- **Brown** - Warm, earthy tone

Cycle through themes using the **C** key during execution.

### Solution Path Visualization

When displayed, the solution path overlays on the maze showing:
- The shortest path from entry to exit
- Clear directional flow
- Optimal route through the maze

---

## Getting Started

### Quick Start (5 minutes)

```bash
# 1. Install dependencies
make install

# 2. Run the project
make run

# 3. Try interactive commands (R, S, C, Q)
```

### Customizing Your Maze

Edit `config.txt`:

```plaintext
WIDTH=25
HEIGHT=20
ENTRY=0,0
EXIT=24,19
PERFECT=true
SEED=12345
OUTPUT_FILE=my_maze.txt
```

Then run:

```bash
make run
```

---

## Conclusion

**A-Maze-ing** demonstrates a complete understanding of maze algorithms, terminal-based UI design, and professional software engineering practices. The project showcases effective use of design patterns, type safety, validation frameworks, and modular architecture—all critical skills in software development.

The combination of elegant algorithm implementation with user-friendly interface creates an engaging, educational tool for exploring graph theory and pathfinding concepts.
