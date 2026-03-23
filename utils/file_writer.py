# maze rows (hex)
# empty line
# entry
# exit
# path
from typing import List, Tuple, Optional


def file_writer(
        maze: List[List[int]],
        start: Tuple[int, int],
        end: Tuple[int, int],
        path: Optional[str],
        output_file_path: str,
) -> None:
    try:
        with open(output_file_path, 'w') as file:
            # maze
            for line in maze:
                for num in line:
                    file.write(f"{hex(num)[2:].upper()}")
                file.write('\n')

            # empty line
            file.write('\n')

            # entry / exit
            file.write(f"{start[0]},{start[1]}\n")
            file.write(f"{end[0]},{end[1]}\n")

            # path
            file.write(f"{path}\n")

    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        raise Exception(f"File error: {e}")


# file_writer([[1, 2, 3], [4, 5, 6]], (0, 0), (1, 1), "SEWN", "output_file")
