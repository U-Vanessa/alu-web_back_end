#!/usr/bin/env python3
"""Complex types - string and int/float to tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Type-annotated function that returns a tuple with a string and the square of a number."""
    return (k, v * v)
