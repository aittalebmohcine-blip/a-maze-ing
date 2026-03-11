from generator import MazeGenerator

maze = MazeGenerator(3, 3, (0, 0), (2, 2))
maze.generate()

path = maze.bfs_solver(maze.grid, maze.entry, maze.exit)
print(path)
maze.draw_maze_with_path(maze.grid, path, maze.entry)
