from utils.drawing import AsciiRenderer
from typing import Tuple, Optional, Dict, Any
from pydantic import BaseModel, Field, ValidationError, model_validator


class MazeConfig(BaseModel):
    """
    Configuration model for maze generation.

    This class validates all parameters required to generate a maze,
    including dimensions, entry/exit points, and output settings.
    """

    WIDTH: int = Field(..., ge=9, le=100)
    HEIGHT: int = Field(..., ge=6, le=100)
    ENTRY: Tuple[int, int] = Field(...)
    EXIT: Tuple[int, int] = Field(...)
    PERFECT: bool = Field(...)
    OUTPUT_FILE: str = Field(...)

    SEED: Optional[int] = None

    @model_validator(mode="after")
    def validate_entry_exit(self) -> "MazeConfig":
        """
        Validate entry and exit positions.

        Ensures that:
        - ENTRY and EXIT are inside maze bounds
        - ENTRY and EXIT are not inside the 42-block area
        - ENTRY and EXIT are different

        Returns:
            MazeConfig: The validated configuration instance.

        Raises:
            ValueError: If any constraint is violated.
        """
        x, y = self.ENTRY
        w = self.WIDTH
        h = self.HEIGHT

        if not 0 <= x < w or not 0 <= y < h:
            raise ValueError("ENTRY point must be inside the maze")

        x, y = self.EXIT
        if not 0 <= x < w or not 0 <= y < h:
            raise ValueError("EXIT point must be inside the maze")

        if self.ENTRY in AsciiRenderer.cells_of_42(w, h):
            raise ValueError("ENTRY cannot be in the 42-block")

        if self.EXIT in AsciiRenderer.cells_of_42(w, h):
            raise ValueError("EXIT cannot be in the 42-block")

        if self.EXIT == self.ENTRY:
            raise ValueError("ENTRY and EXIT must be different")

        return self


def parsing_config_file(filepath: str) -> MazeConfig:
    config: Dict[Any, Any] = {}
    """
    Parse a configuration file and return a validated MazeConfig object.

    The configuration file must follow a key=value format.
    Supported keys:
        - WIDTH (int)
        - HEIGHT (int)
        - ENTRY (x,y)
        - EXIT (x,y)
        - PERFECT (True/False)
        - OUTPUT_FILE (str)
        - SEED (int, optional)

    Lines starting with '#' or empty lines are ignored.

    Args:
        filepath (str): Path to the configuration file.

    Returns:
        MazeConfig: A validated MazeConfig object if parsing succeeds.

    Raises:
        SystemExit: If the file cannot be read or validation fails.
    """
    config: dict = {}

    try:
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if "=" not in line:
                    raise ValueError(f"Invalid line: {line}")

                key, value = map(str.strip, line.split("=", 1))
                key = key.upper()

                if key in config:
                    raise ValueError(f"A key must be entred only once ({key})")

                if key in {"WIDTH", "HEIGHT"}:
                    config[key] = value

                elif key in {"ENTRY", "EXIT"}:
                    config[key] = tuple(value.split(","))

                elif key == "PERFECT":
                    if value.lower() not in {"true", "false"}:
                        raise ValueError("PERFECT must be True or False")
                    config[key] = value.lower() == "true"

                elif key == "OUTPUT_FILE":
                    config[key] = value

                elif key == "SEED":
                    config[key] = value

                else:
                    raise ValueError(f"Unknown key: {key}")

        return MazeConfig(**config)

    except FileNotFoundError:
        print("Config file not found")
        exit(1)

    except PermissionError:
        print("Permission denied while reading config file")
        exit(1)

    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}: {error['loc'][0]}")
        exit(1)

    except ValueError as e:
        print(f"Configuration error:\n{e}")
        exit(1)
