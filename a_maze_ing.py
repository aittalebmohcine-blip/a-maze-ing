import os
import time
import sys

try:
    import blessed
    import utils.parsing as parser
    from mazegen import generator
    from utils import file_writer
    import utils.drawing as drawer
except ImportError as e:
    print(f"Import error: {e}")
    exit(1)


def main() -> None:
    """
    Main entry point for the A-Maze-ing application.

    This function:
    1. Reads and validates the configuration file.
    2. Generates a maze using the provided parameters.
    3. Solves the maze using BFS.
    4. Writes the maze and solution to an output file.
    5. Launches an interactive terminal UI to:
        - regenerate the maze
        - show/hide the solution path
        - change display colors
        - quit the program

    Usage:
        python3 a_maze_ing.py config.txt

    Raises:
        SystemExit: If imports fail, file errors occur,
                    or configuration is invalid.
    """
    if len(sys.argv) != 2 or sys.argv[1] != "config.txt":
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    config_file = sys.argv[1]
    try:
        config = parser.parsing_config_file(config_file)
    except Exception as e:
        print(f"Configuration error:\n{e}")
        exit(1)

    width = config.WIDTH
    height = config.HEIGHT
    start = config.ENTRY
    end = config.EXIT
    is_perfect = config.PERFECT
    seed = config.SEED
    output_file = config.OUTPUT_FILE

    maze = generator.MazeGenerator(
        width, height, start, end, is_perfect, seed)
    maze.generate()

    path = maze.bfs_solver()

    try:
        file_writer.file_writer(
            maze.grid,
            start,
            end,
            path,
            output_file,
        )
    except Exception as e:
        print(e)
        exit(1)

    os.system('clear')
    term = blessed.Terminal()

    renderer = drawer.AsciiRenderer(maze, start, end)

    try:
        with open("bonus/intrro.txt", "r") as file:
            for line in file:
                print(term.red(line.strip()))
                time.sleep(0.1)
            os.system('clear')
    except Exception as e:
        print(f"File error: {e}")
        exit(1)

    colors = [
        term.blue,
        term.red,
        term.white,
        term.green,
        term.brown,
    ]

    i = 0
    path = None
    just_pressed = 0

    with term.cbreak():
        while True:
            """
            Interactive loop handling user input and rendering.

            Controls:
                1 -> Generate a new maze
                2 -> Toggle solution path visibility
                3 -> Change maze color
                4 -> Exit program
            """
            if path is None:
                print(colors[i](renderer.render()))
            else:
                print(colors[i](renderer.render(path=path)))

            print(term.white(
                "\n=== A-Maze-ing ===\n",
                "1. Re-generate a new maze\n",
                "2. Show/Hide path\n",
                "3. Rotate maze colors\n",
                "4. Quit\n",
                "Choice? (1-4):"))

            key = term.inkey()

            if key == "3":
                i = (i + 1) % len(colors)

            elif key == "1":
                path = None
                maze.generate()
                just_pressed = 0

            elif key == '2':
                if not just_pressed:
                    path = maze.bfs_solver()
                    just_pressed = 1
                else:
                    path = None
                    just_pressed = 0

            elif key == "4":
                os.system('clear')
                break

            os.system('clear')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Program exit.")
