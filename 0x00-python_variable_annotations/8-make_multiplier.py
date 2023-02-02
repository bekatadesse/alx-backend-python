#!/usr/bin/env python3
"""
Module 8-make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float and  multiplies"""
    def multiplier_fn(number: float) -> float:
        """Multiplies a float by multiplier"""
        return number * multiplier

    return multiplier_fn
