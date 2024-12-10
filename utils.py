from typing import TypeVar

Number = TypeVar("Number", int, float)


def pattern_match(find, pattern: object) -> bool | Exception:
    return next(value for key, value in pattern.items() if find in key)
