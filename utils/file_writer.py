# maze rows (hex)
# empty line
# entry
# exit
# path
from typing import List, Tuple


def file_writer(
        maze: List[List[int]],
        start: Tuple[int, int],
        end: Tuple[int, int],
        path: str,
        output_file_path: str,
) -> None:
    with open(output_file_path, 'w') as file:
        for line in maze:
            for num in line:
                file.write(f"{hex(num)[2:]}")
            file.write('\n')

        file.write('\n')

        x, y = start
        file.write(f"{x},{y}\n")
        x, y = end
        file.write(f"{x},{y}\n")

        file.write(path)


# file_writer([[1, 2, 3], [4, 5, 6]], (0, 0), (1, 1), "SEWN", "output_file")
