from typing import Tuple, Optional, Dict, Any, List
from pydantic import BaseModel, Field, ValidationError, model_validator
from utils.drawing import AsciiRenderer


# -------------------------
# Helpers
# -------------------------

def parse_int(value: str, key: str) -> int:
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"{key} must be an integer (got '{value}')")


def parse_bool(value: str, key: str) -> bool:
    v: str = value.lower()
    if v in {"true", "1"}:
        return True
    if v in {"false", "0"}:
        return False
    raise ValueError(f"{key} must be True/False (got '{value}')")


def parse_tuple(value: str, key: str) -> Tuple[int, int]:
    parts: list[str] = value.split(",")
    if len(parts) != 2:
        raise ValueError(f"{key} must be in format x,y (got '{value}')")

    x: int = parse_int(parts[0].strip(), key)
    y: int = parse_int(parts[1].strip(), key)
    return (x, y)


# -------------------------
# Model
# -------------------------

class MazeConfig(BaseModel):
    WIDTH: int = Field(..., ge=9, le=100)
    HEIGHT: int = Field(..., ge=6, le=100)
    ENTRY: Tuple[int, int]
    EXIT: Tuple[int, int]
    PERFECT: bool
    OUTPUT_FILE: str
    SEED: Optional[int] = None

    @model_validator(mode="after")
    def validate_all(self) -> "MazeConfig":
        w: int = self.WIDTH
        h: int = self.HEIGHT

        def in_bounds(p: Tuple[int, int], name: str) -> None:
            x: int
            y: int
            x, y = p
            if not (0 <= x < w and 0 <= y < h):
                raise ValueError(
                    f"{name} {p} is outside maze bounds ({w}x{h})"
                )

        in_bounds(self.ENTRY, "ENTRY")
        in_bounds(self.EXIT, "EXIT")

        if self.ENTRY == self.EXIT:
            raise ValueError("ENTRY and EXIT must be different")

        blocked: set[Tuple[int, int]] = set(AsciiRenderer.cells_of_42(w, h))

        if self.ENTRY in blocked:
            raise ValueError(f"ENTRY {self.ENTRY} is inside the 42-block")

        if self.EXIT in blocked:
            raise ValueError(f"EXIT {self.EXIT} is inside the 42-block")

        return self


# -------------------------
# Parser
# -------------------------

ALLOWED_KEYS: set[str] = {
    "WIDTH", "HEIGHT", "ENTRY", "EXIT",
    "PERFECT", "OUTPUT_FILE", "SEED"
}

REQUIRED_KEYS: set[str] = {
    "WIDTH", "HEIGHT", "ENTRY", "EXIT",
    "PERFECT", "OUTPUT_FILE"
}


def parsing_config_file(filepath: str) -> MazeConfig:
    raw: Dict[str, Any] = {}
    errors: List[str] = []

    try:
        with open(filepath, "r") as f:
            lineno: int
            line: str
            for lineno, line in enumerate(f, 1):
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if "=" not in line:
                    errors.append(f"Line {lineno}: missing '='")
                    continue

                key: str
                value: str
                key, value = map(str.strip, line.split("=", 1))
                key = key.upper()

                if key not in ALLOWED_KEYS:
                    errors.append(f"Line {lineno}: unknown key '{key}'")
                    continue

                if key in raw:
                    errors.append(f"Line {lineno}: duplicate key '{key}'")
                    continue

                try:
                    if key in {"WIDTH", "HEIGHT", "SEED"}:
                        raw[key] = parse_int(value, key)

                    elif key in {"ENTRY", "EXIT"}:
                        raw[key] = parse_tuple(value, key)

                    elif key == "PERFECT":
                        raw[key] = parse_bool(value, key)

                    elif key == "OUTPUT_FILE":
                        if not value:
                            raise ValueError("OUTPUT_FILE cannot be empty")
                        raw[key] = value

                except ValueError as e:
                    errors.append(f"Line {lineno}: {e}")

        missing: set[str] = REQUIRED_KEYS - raw.keys()
        if missing:
            errors.append(
                f"Missing required keys: {', '.join(sorted(missing))}"
            )

        if errors:
            raise ValueError("\n".join(errors))

        return MazeConfig(**raw)

    except FileNotFoundError:
        raise RuntimeError("Config file not found")

    except PermissionError:
        raise RuntimeError("Permission denied while reading config file")

    except ValidationError as e:
        msgs: List[str] = []
        for err in e.errors():
            field: str = ".".join(map(str, err["loc"]))
            msgs.append(f"{field}: {err['msg']}")
        raise ValueError("\n".join(msgs))
