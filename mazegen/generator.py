import random
from random import Random
from typing import Tuple, List, Generator, Dict, Optional

N = 1 << 0
E = 1 << 1
S = 1 << 2
W = 1 << 3

DIRS = {
    "N": (0, -1, 1),
    "E": (1, 0, 2),
    "S": (0, 1, 4),
    "W": (-1, 0, 8),
}


class MazeGenerator:
    """
    Generates and solves a maze using depth-first search (DFS)
    and breadth-first search (BFS).

    The maze is represented as a grid where each cell contains
    bitwise flags indicating the presence of walls.
    """

    def __init__(
        self,
        width: int,
        height: int,
        entry: Tuple[int, int],
        exit: Tuple[int, int],
        perfect: bool = True,
        seed: int | None = None,
    ):
        """
        Initialize the maze generator.

        Args:
            width (int): Width of the maze (>= 9).
            height (int): Height of the maze (>= 6).
            entry (Tuple[int, int]): Entry point (x, y).
            exit (Tuple[int, int]): Exit point (x, y).
            perfect (bool): If True, generates a perfect maze (no loops).
            seed (int | None): Seed for random generator (for reproducibility).

        Raises:
            TypeError: If inputs are not of correct types.
            ValueError: If dimensions or coordinates are invalid.
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("[ERROR]: width and height must be integers.")

        if (
            not isinstance(entry, tuple)
            or not isinstance(exit, tuple)
            or len(entry) != 2
            or len(exit) != 2
        ):
            raise TypeError("[ERROR]: entry and exit must be tuples (x, y).")

        if not all(isinstance(v, int) for v in (*entry, *exit)):
            raise TypeError(
                "[ERROR]: entry and exit coordinates must be integers.")

        if width < 9 or height < 6:
            raise ValueError("[ERROR]: Maze dimensions too small.")

        if entry == exit:
            raise ValueError(
                "[ERROR]: entry and exit should not be the same point."
            )

        if not self._is_inside_static(width, height, *entry):
            raise ValueError("[ERROR]: Invalid entry point.")

        if not self._is_inside_static(width, height, *exit):
            raise ValueError("[ERROR]: Invalid exit point.")

        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect

        self._rng: Random = random.Random(seed)

        self.grid: list[list[int]] = [
            [0b1111 for _ in range(width)]
            for _ in range(height)
        ]

    @staticmethod
    def _is_inside_static(
        width: int, height: int, x: int, y: int
    ) -> bool:
        """
        Check if a coordinate is inside maze boundaries.

        Args:
            width (int): Maze width.
            height (int): Maze height.
            x (int): X coordinate.
            y (int): Y coordinate.

        Returns:
            bool: True if inside bounds, False otherwise.
        """
        return 0 <= x < width and 0 <= y < height

    def generate(self) -> None:
        """
        Generate the maze using depth-first search (DFS).

        If `perfect` is False, additional walls are randomly removed
        to create loops.
        """
        self.grid = [
            [0b1111 for _ in range(self.width)]
            for _ in range(self.height)
        ]

        visited: list[list[bool]] = [
            [False for _ in range(self.width)]
            for _ in range(self.height)
        ]

        for cell in self.cells_of_42(self.width, self.height):
            x, y = cell
            visited[y][x] = True

        stack: list[tuple[int, int]] = []
        curent: tuple[int, int] = self.entry
        x, y = curent
        visited[y][x] = True
        stack.append(curent)

        while len(stack):
            curent = stack.pop()
            neighbors: list[tuple[int, int]
                            ] = self._get_unvisited_neighbors(*curent, visited)

            if neighbors:
                stack.append(curent)
                nx, ny = self._rng.choice(neighbors)
                self._remove_wall(*curent, nx, ny)
                visited[ny][nx] = True
                stack.append((nx, ny))

        if not self.perfect:
            self._make_imperfect()

    def _make_imperfect(self) -> None:
        """
        Introduce randomness into the maze by removing additional walls.

        This creates multiple possible paths (non-perfect maze).
        """
        proba: float = 0.15

        visited: list[list[bool]] = [
            [False for _ in range(self.width)]
            for _ in range(self.height)
        ]

        for cell in self.cells_of_42(self.width, self.height):
            x, y = cell
            visited[y][x] = True

        stack: list[tuple[int, int]] = []
        curent: tuple[int, int] = self.entry
        x, y = curent
        visited[y][x] = True
        stack.append(curent)

        while len(stack):
            curent = stack.pop()
            neighbors: list[tuple[int, int]
                            ] = self._get_unvisited_neighbors(*curent, visited)

            if neighbors:
                stack.append(curent)
                nx, ny = self._rng.choice(neighbors)

                if self._rng.random() < proba:
                    self._remove_wall(*curent, nx, ny)

                visited[ny][nx] = True
                stack.append((nx, ny))

    @staticmethod
    def cells_of_42(wd: int, ht: int) -> List[Tuple[int, int]]:
        """
        Return predefined "42 pattern" cells around the center.

        These cells are marked as already visited to create
        a recognizable shape in the maze.

        Args:
            wd (int): Width of the maze.
            ht (int): Height of the maze.

        Returns:
            List[Tuple[int, int]]: Valid coordinates of the pattern.
        """
        cx: int = wd // 2
        cy: int = ht // 2

        cells: list[tuple[int, int]] = [
            (cx + 2, cy - 2), (cx + 1, cy - 2), (cx + 3, cy - 2),
            (cx + 3, cy - 1), (cx + 3, cy), (cx + 2, cy),
            (cx + 1, cy), (cx + 1, cy + 1), (cx + 1, cy + 2),
            (cx + 2, cy + 2), (cx + 3, cy + 2),

            (cx - 3, cy - 2), (cx - 3, cy - 1), (cx - 3, cy),
            (cx - 2, cy), (cx - 1, cy),
            (cx - 1, cy + 1), (cx - 1, cy + 2)
        ]

        return [(x, y) for x, y in cells if 0 <= x < wd and 0 <= y < ht]

    @staticmethod
    def _get_unvisited_neighbors(
        x: int,
        y: int,
        visited: list[list[bool]]
    ) -> list[tuple[int, int]]:
        """
        Get all unvisited neighboring cells.

        Args:
            x (int): Current x position.
            y (int): Current y position.
            visited (list[list[bool]]): Visited grid.

        Returns:
            list[tuple[int, int]]: List of valid neighbors.
        """
        width: int = len(visited[0])
        height: int = len(visited)
        neighbors: list[tuple[int, int]] = []

        if x + 1 < width and not visited[y][x + 1]:
            neighbors.append((x + 1, y))

        if x - 1 >= 0 and not visited[y][x - 1]:
            neighbors.append((x - 1, y))

        if y + 1 < height and not visited[y + 1][x]:
            neighbors.append((x, y + 1))

        if y - 1 >= 0 and not visited[y - 1][x]:
            neighbors.append((x, y - 1))

        return neighbors

    def _remove_wall(
        self,
        x: int,
        y: int,
        nx: int,
        ny: int
    ) -> None:
        """
        Remove the wall between two adjacent cells.

        Args:
            x (int): Current cell x.
            y (int): Current cell y.
            nx (int): Neighbor cell x.
            ny (int): Neighbor cell y.
        """
        if nx == x and ny == y - 1:
            self.grid[y][x] &= ~N
            self.grid[ny][nx] &= ~S

        elif nx == x + 1 and ny == y:
            self.grid[y][x] &= ~E
            self.grid[ny][nx] &= ~W

        elif nx == x and ny == y + 1:
            self.grid[y][x] &= ~S
            self.grid[ny][nx] &= ~N

        elif nx == x - 1 and ny == y:
            self.grid[y][x] &= ~W
            self.grid[ny][nx] &= ~E

    def bfs_solver(self) -> Optional[str]:
        """
        Solve the maze using Breadth-First Search (BFS).

        Returns:
            str: Path from entry to exit as a sequence of directions.
        """
        stack: list[tuple[int, int]] = [self.entry]
        parent: dict[tuple[int, int], tuple[tuple[int, int], str]] = {}

        visited: list[list[bool]] = [
            [False for _ in range(self.width)]
            for _ in range(self.height)
        ]

        x, y = self.entry
        visited[y][x] = True

        while stack:
            curent: tuple[int, int] = stack.pop(0)

            if curent == self.exit:
                break

            for d, nx, ny in self._neighbors(self.grid, *curent):
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    parent[(nx, ny)] = (curent, d)
                    stack.append((nx, ny))

        return self._build_path(self.entry, self.exit, parent)

    @staticmethod
    def _neighbors(
        maze: list[list[int]],
        x: int,
        y: int
    ) -> Generator[tuple[str, int, int], None, None]:
        """
        Yield accessible neighboring cells (no wall between).

        Args:
            maze (list[list[int]]): Maze grid.
            x (int): Current x.
            y (int): Current y.

        Yields:
            Generator[tuple[str, int, int]]: Direction and neighbor coords.
        """
        w: int = len(maze[0])
        h: int = len(maze)

        for d, (dx, dy, bit) in DIRS.items():
            if not (maze[y][x] & bit):
                ny: int = y + dy
                nx: int = x + dx
                if 0 <= ny < h and 0 <= nx < w:
                    yield d, nx, ny

    @staticmethod
    def _build_path(
        entry: tuple[int, int],
        exit: tuple[int, int],
        parent: Dict[tuple[int, int], tuple[tuple[int, int], str]]
    ) -> str:
        """
        Reconstruct the path from BFS parent mapping.

        Args:
            entry (tuple[int, int]): Start point.
            exit (tuple[int, int]): End point.
            parent (dict): Parent mapping.

        Returns:
            str: Path as sequence of directions.
        """
        path: list[str] = []
        curent: tuple[int, int] = exit

        while curent != entry:
            prev, d = parent[curent]
            path.append(d)
            curent = prev

        return "".join((reversed(path)))
