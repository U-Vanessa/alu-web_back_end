#!/usr/bin/env python3
"""Complex types - functions."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Type-annotated function that returns a function which multiplies a float by a multiplier."""
    def fn(n: float):
        return n * multiplier
    return fn
