
from typing import Tuple, Optional, List

N = 1
E = 2
S = 4
W = 8


class AsciiRenderer:
    """
    Render a maze in ASCII format.

    This class takes a maze generated using a bitmask grid and
    converts it into a visual ASCII representation. It also supports:
    - displaying entry and exit points
    - overlaying a solution path
    - preserving a fixed "42 pattern" as blocked cells
    """

    def __init__(self, maze, entry: Tuple[int, int], exit: Tuple[int, int]):
        """
        Initialize the renderer.

        Args:
            maze: MazeGenerator instance containing the grid.
            entry (Tuple[int, int]): Entry point (x, y).
            exit (Tuple[int, int]): Exit point (x, y).
        """
        self.maze = maze
        self.entry = entry
        self.exit = exit

    @staticmethod
    def cells_of_42(wd: int, ht: int) -> List[Tuple[int, int]]:
        """
        Return coordinates forming the "42 pattern" in the maze center.

        These cells are always rendered as fully blocked.

        Args:
            wd (int): Maze width.
            ht (int): Maze height.

        Returns:
            List[Tuple[int, int]]: Valid coordinates of the pattern.
        """
        cx = wd // 2
        cy = ht // 2

        cells = [
            (cx + 2, cy - 2), (cx + 1, cy - 2), (cx + 3, cy - 2),
            (cx + 3, cy - 1), (cx + 3, cy), (cx + 2, cy),
            (cx + 1, cy), (cx + 1, cy + 1), (cx + 1, cy + 2),
            (cx + 2, cy + 2), (cx + 3, cy + 2),

            (cx - 3, cy - 2), (cx - 3, cy - 1), (cx - 3, cy),
            (cx - 2, cy), (cx - 1, cy),
            (cx - 1, cy + 1), (cx - 1, cy + 2)
        ]

        return [(x, y) for x, y in cells if 0 <= x < wd and 0 <= y < ht]

    def render(
        self,
        player_pos: Optional[Tuple[int, int]] = None,
        visited_trail: Optional[List] = None,
        path: Optional[List[Tuple[int, int]]] = None,
        show: bool = True
    ) -> str:
        """
        Render the maze as an ASCII string.

        Supports optional overlays such as player position,
        visited cells, and solution path.

        Args:
            player_pos (Optional[Tuple[int, int]]): Current player position.
            visited_trail (Optional[List]): List of visited cells.
            path (Optional[List[Tuple[int, int]]]): Path as sequence of directions.
            show (bool): If True, intended for display (not used internally).

        Returns:
            str: The rendered ASCII maze.
        """
        BLOCK = "█"
        width = self.maze.width
        height = self.maze.height
        grid = self.maze.grid
        h_seg = BLOCK * 3

        x, y = self.entry
        path_cells = {(x, y)}

        moves = {
            "N": (0, -1),
            "E": (1, 0),
            "S": (0, 1),
            "W": (-1, 0),
        }

        if path is not None:
            for step in path:
                dx, dy = moves[step]
                x += dx
                y += dy
                path_cells.add((x, y))

        output = ""

        output += BLOCK + (h_seg + BLOCK) * (width - 1) + h_seg + BLOCK + "\n"

        cell42 = set(self.cells_of_42(width, height))

        for y in range(height):

            row_str = BLOCK

            for x in range(width):

                cell = grid[y][x]

                if (x, y) in cell42:
                    cell |= N | E | S | W

                if (x, y) == self.entry:
                    body = " 🐹"
                elif (x, y) == self.exit:
                    body = " 🚪"
                elif (x, y) in cell42:
                    body = " 🔥"
                elif path and (x, y) in path_cells:
                    body = " x "
                else:
                    body = "   "

                wall_char = BLOCK if (cell & E) != 0 or x == width - 1 else " "
                row_str += body + wall_char

            output += row_str + "\n"

            if y < height - 1:
                row_str = BLOCK

                for x in range(width):
                    cell = grid[y][x]

                    if (x, y) in cell42:
                        cell |= N | E | S | W

                    wall = h_seg if (cell & S) != 0 else "   "
                    row_str += wall + BLOCK

                output += row_str + "\n"

        output += BLOCK + (h_seg + BLOCK) * (width - 1) + h_seg + BLOCK + "\n"

        return output
