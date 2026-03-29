from typing import Tuple, Optional, List, Dict
from mazegen.generator import MazeGenerator

N: int = 1
E: int = 2
S: int = 4
W: int = 8


class AsciiRenderer:
    """
    Render a maze in ASCII format.

    This class takes a maze generated using a bitmask grid and
    converts it into a visual ASCII representation. It also supports:
    - displaying entry and exit points
    - overlaying a solution path
    - preserving a fixed "42 pattern" as blocked cells
    """

    def __init__(
        self,
        maze: MazeGenerator,
        entry: Tuple[int, int],
        exit: Tuple[int, int]
    ):
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
        cx: int = wd // 2
        cy: int = ht // 2

        cells: List[Tuple[int, int]] = [
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
        path: Optional[str] = None,
        # player_pos: Optional[Tuple[int, int]] = None,
        # visited_trail: Optional[List] = None,
        # show: bool = True
    ) -> str:
        """Return an ASCII representation of the maze.

        Optional path overlay highlights the solution route from entry
        to exit.

        Args:
            path: Optional direction sequence composed of 'N', 'E', 'S', 'W'.

        Returns:
            str: Multiline ASCII maze string including borders, entry/exit
            and optional solution path markers.
        """
        BLOCK: str = "█"
        width: int = self.maze.width
        height: int = self.maze.height
        grid: list[list[int]] = self.maze.grid
        h_seg: str = BLOCK * 3

        x, y = self.entry
        path_cells: set[tuple[int, int]] = {(x, y)}

        moves: Dict[str, tuple[int, int]] = {
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

        output: str = ""

        output += BLOCK + (h_seg + BLOCK) * (width - 1) + h_seg + BLOCK + "\n"

        cell42: set[Tuple[int, int]] = set(
            self.cells_of_42(width, height))

        for y in range(height):

            row_str: str = BLOCK

            for x in range(width):

                cell: int = grid[y][x]

                if (x, y) in cell42:
                    cell |= N | E | S | W

                if (x, y) == self.entry:
                    body: str = " 🐹"
                elif (x, y) == self.exit:
                    body = " 🚪"
                elif (x, y) in cell42:
                    body = " 🔥"
                elif path and (x, y) in path_cells:
                    body = " x "
                else:
                    body = "   "

                wall_char: str = BLOCK if (
                    cell & E) != 0 or x == width - 1 else " "
                row_str += body + wall_char

            output += row_str + "\n"

            if y < height - 1:
                row_str = BLOCK

                for x in range(width):
                    cell = grid[y][x]

                    if (x, y) in cell42:
                        cell |= N | E | S | W

                    wall: str = h_seg if (cell & S) != 0 else "   "
                    row_str += wall + BLOCK

                output += row_str + "\n"

        output += BLOCK + (h_seg + BLOCK) * (width - 1) + h_seg + BLOCK + "\n"

        return output
