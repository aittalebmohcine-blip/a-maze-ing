*This project has been created as part of the 42 curriculum by mait-tal, dez-zahe.*

## Description

A-Maze-ing is a Python-based maze generation and solving application. It generates mazes using an iterative depth-first search algorithm, allows solving them with breadth-first search, and provides an interactive ASCII terminal interface for visualization and regeneration. The project includes a "42" pattern carved into the maze center as a thematic element.

The goal of this project is to create a functional maze generator that demonstrates algorithmic concepts in a practical, interactive way, while adhering to clean code principles and modularity.

## Instructions

### Installation

1. Ensure Python 3.10 or higher is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or use the Makefile:
   ```bash
   make install
   ```

### Execution

Run the application with:
```bash
python3 a_maze_ing.py config.txt
```
Or:
```bash
make run
```

This will generate a maze based on the configuration, solve it, write the output to a file, and launch an interactive terminal UI.

### Interactive Controls

- **1**: Regenerate a new maze
- **2**: Toggle solution path visibility
- **3**: Cycle through color themes
- **4**: Exit the program

## Resources

### References

- [Maze Generation Algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm) - Overview of common maze generation techniques.
- [Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search) - Algorithm used for solving the maze.
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/) - For configuration validation.
- [Blessed Library](https://blessed.readthedocs.io/en/latest/) - For terminal UI interactions.

### AI Usage

AI was used for:
- Code structure suggestions and best practices.
- Debugging assistance and error handling improvements.
- Documentation generation and README drafting.
- Ensuring code modularity and reusability.

## Config File Structure and Format

The configuration file (`config.txt`) uses a simple key-value format with one parameter per line. Lines starting with `#` are comments and are ignored. Blank lines are allowed.

### Required Parameters

- `WIDTH`: Integer, maze width in cells (9-100).
- `HEIGHT`: Integer, maze height in cells (6-100).
- `ENTRY`: Tuple as `x,y`, starting point coordinates.
- `EXIT`: Tuple as `x,y`, ending point coordinates.
- `PERFECT`: Boolean (`true`/`false`), whether the maze has no loops.
- `OUTPUT_FILE`: String, path to the output file for maze data.

### Optional Parameters

- `SEED`: Integer, random seed for reproducible maze generation (-1 for random).

### Example Config

```
WIDTH=15
HEIGHT=10
ENTRY=0,0
EXIT=9,9
OUTPUT_FILE=output.txt
PERFECT=false
SEED=-1
```

## Maze Generation Algorithm

The maze is generated using an iterative depth-first search (DFS) algorithm implemented with a stack. This ensures a perfect maze (no loops) when `PERFECT=true`, with all cells connected and no cycles. For imperfect mazes, additional walls are randomly removed to introduce loops.

### Why This Algorithm?

Iterative DFS was chosen for its simplicity and efficiency in creating spanning tree mazes. It produces aesthetically pleasing, complex mazes with a single solution path in perfect mode. The iterative approach avoids recursion depth limits and is easy to implement and understand.

## Reusable Code Parts

The codebase is designed with modularity in mind:

- **`MazeGenerator` class** (`mazegen/generator.py`): Core maze generation and solving logic. Can be reused in other projects for maze-related functionality.
- **Configuration parsing** (`utils/parsing.py`): Uses Pydantic for robust validation. Reusable for any config file parsing needs.
- **ASCII rendering** (`utils/drawing.py`): Converts maze data to visual representation. Easily adaptable for different output formats.
- **File I/O** (`utils/file_writer.py`): Handles maze data export. Reusable for structured data writing.

## Team and Project Management

### Team Members

### 🧑‍💻 dez-zahe

* Implemented **parsing system** (config file handling & validation)
* Developed **ASCII rendering** (maze drawing logic)
* Worked on **bonus features** (enhancements and visual improvements)

### 🧑‍💻 mait-tal

* Implemented core **maze generation algorithms**:

  * Depth-First Search (DFS)
  * Breadth-First Search (BFS)
* Developed the **MazeGenerator** logic (grid creation and structure)

### Planning and Evolution

Initial planning focused on core requirements: maze generation, solving, and basic output. The project evolved to include interactive UI, configuration validation, and bonus features like the "42" pattern and color themes.

What worked well: Modular design allowed easy addition of features. Iterative development with testing at each step ensured stability.

What could be improved: More extensive testing coverage and user input validation in the interactive mode.

### Tools Used

- **Python 3.10+**: Core language.
- **Pydantic**: Configuration validation.
- **Blessed**: Terminal interactions.
- **Flake8 & MyPy**: Code linting and type checking.
- **Makefile**: Build automation.
- **Git**: Version control.</content>
<parameter name="filePath">/home/mait-tal/Documents/a-maze-ing/README.md
