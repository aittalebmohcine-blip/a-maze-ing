from generator import MazeGenerator

maze = MazeGenerator(8, 8, (0, 0), (1, 1))
maze.generate()

path = maze.bfs_solver(maze.grid, maze.entry, maze.exit)
maze.draw_maze_with_path(maze.grid, path)
