# read config
# generate maze
# solve maze
# write output file
# display maze

import blessed

import os
import time
import sys

import utils.parsing as parser
import mazegen.generator as generator
from utils import file_writer
import utils.drawing as drawer


def main() -> None:
    # read config
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    config_file = sys.argv[1]
    config = parser.parsing_config_file(config_file)

    # generate maze
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

    # solve maze
    path = maze.bfs_solver()

    # write output file
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

    # display maze:

    # - Initialize terminal
    os.system('clear')
    term = blessed.Terminal()

    renderer = drawer.AsciiRenderer(maze, start, end)

    # print(blessed.Terminal().blue(drawer.AsciiRenderer().render()))

    # print the intro logo
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
    main()
