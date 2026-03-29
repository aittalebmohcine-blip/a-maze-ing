from typing import List, Tuple, Optional


def file_writer(
        maze: List[List[int]],
        start: Tuple[int, int],
        end: Tuple[int, int],
        path: Optional[str],
        output_file_path: str,
) -> None:
    """
    Write the maze, entry/exit points, and solution path to a file.

    The file format is structured as follows:
        1. Maze grid (each row as hexadecimal values without '0x')
        2. Empty line
        3. Entry coordinates (x,y)
        4. Exit coordinates (x,y)
        5. Path as a string of directions (e.g., "NESW")

    Args:
        maze (List[List[int]]): 2D maze grid where each cell is a bitmask.
        start (Tuple[int, int]): Entry point (x, y).
        end (Tuple[int, int]): Exit point (x, y).
        path (Optional[str]): Path from entry to exit as a sequence of directions (may be None).
        output_file_path (str): Path to the output file.

    Raises:
        Exception: If a file-related error occurs
        (permission, invalid path, etc.).
    """
    try:
        with open(output_file_path, 'w') as file:
            for line in maze:
                for num in line:
                    file.write(f"{hex(num)[2:].upper()}")
                file.write('\n')

            file.write('\n')

            file.write(f"{start[0]},{start[1]}\n")
            file.write(f"{end[0]},{end[1]}\n")

            file.write(f"{path}\n")

    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        raise Exception(f"File error: {e}")
