#!/usr/bin/env python3
"""Type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier.
    """
    def multiply(x: float) -> float:
        """Type-annotated function multiply that takes a float x as argument
        and returns the product of x and multiplier."""
        return x * multiplier
    return multiply
