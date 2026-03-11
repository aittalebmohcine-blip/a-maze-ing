from generator import MazeGenerator

maze = MazeGenerator(15, 15, (0, 0), (12, 12))
maze.generate()

path = maze.bfs_solver(maze.grid, maze.entry, maze.exit)
print(path)
maze.draw_maze_with_path(maze.grid, path, maze.entry)
