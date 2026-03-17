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
    file_writer.file_writer(
        maze.grid,
        start,
        end,
        path,
        output_file,
    )

    # display maze:

    # - Initialize terminal
    os.system('clear')
    term = blessed.Terminal()

    renderer = drawer.AsciiRenderer(maze, start, end)

    # print(blessed.Terminal().blue(drawer.AsciiRenderer().render()))

    # print the intro logo
    with open("bonus/intrro.txt", "r") as file:
        for line in file:
            print(term.red(line.strip()))
            time.sleep(0.1)
        os.system('clear')

    colors = [
        term.blue,
        term.red,
        term.white,
        term.green,
        term.brown,
    ]

    i = 0
    with term.cbreak():
        while True:
            print(colors[i](renderer.render()))
            key = term.inkey()
            if key == "d":
                i = (i + 1) % len(colors)
                os.system('clear')
            elif key == "g":
                os.system('clear')
                maze.generate()
            elif key == "q":
                os.system('clear')
                break
            else:
                os.system('clear')


if __name__ == "__main__":
    main()
