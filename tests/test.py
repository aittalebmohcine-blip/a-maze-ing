import os
import time
from mazegen.generator import MazeGenerator
from utils.drawing import AsciiRenderer
from utils.parsing import parsing_config_file
from blessed import Terminal

# Load maze configuration
config = parsing_config_file("config.txt")

width = config.WIDTH
height = config.HEIGHT
entry = config.ENTRY
exit_ = config.EXIT
perfect = config.PERFECT

# Initialize terminal
term = Terminal()

# Initialize maze generator
maze = MazeGenerator(width, height, entry, exit_, perfect)
maze.generate()  # Apply the DFS maze generation

# Optional: solve maze for path (if needed)
path = maze.bfs_solver()

# Initialize renderer
renderer = AsciiRenderer(maze, entry, exit_)
config = parsing_config_file("config.txt")
os.system('clear')
filename = open("bonus/intrro.txt", "r")
col = [
    term.blue,
    term.red,
    term.white,
    term.green,
    term.brown
]
i = 0
for line in filename:
    print(term.red(line.strip()))
    time.sleep(0.1)
os.system('clear')
with term.cbreak():
    while True:
        print(col[i](renderer.render(path=path)))
        key = term.inkey()
        if key == "q":
            os.system('clear')
            break
        elif key == "d":
            i = (i + 1) % len(col)
            os.system('clear')
