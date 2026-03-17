# parsing_config_file(file) -> Config

from utils.drawing import AsciiRenderer
from typing import Tuple, Optional
from pydantic import BaseModel, Field, ValidationError, model_validator


class MazeConfig(BaseModel):
    WIDTH: int = Field(..., ge=9, description="Maze width (>=5)")
    HEIGHT: int = Field(..., ge=6, description="Maze height (>=6)")
    ENTRY: Tuple[int, int] = Field(...)
    EXIT: Tuple[int, int] = Field(...)
    PERFECT: bool = Field(...)
    SEED: int = Field(default=None)
    OUTPUT_FILE: str = Field(...)

    @model_validator(mode="after")
    def validate_entry(self):
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


def parsing_config_file(filepath: str) -> Optional[MazeConfig]:
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
                    config[key] = int(value)

                elif key in {"ENTRY", "EXIT"}:
                    x, y = map(int, value.split(","))
                    config[key] = (x, y)

                elif key == "PERFECT":
                    if value.lower() not in {"true", "false"}:
                        raise ValueError("PERFECT must be True or False")
                    config[key] = value.lower() == "true"

                elif key == "OUTPUT_FILE":
                    config[key] = value

                elif key == "SEED":
                    config[key] = int(value)

                else:
                    raise ValueError(f"Unknown key: {key}")

        return MazeConfig(**config)

    except FileNotFoundError:
        print("Config file not found")
        exit(1)

    except PermissionError:
        print("Permission denied while reading config file")
        exit(1)

    except (ValueError, ValidationError) as e:
        print(f"Configuration error:\n{e}")
        exit(1)
