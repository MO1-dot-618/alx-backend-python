#!/usr/bin/env python3
"""Typed function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes float and returns float"""
    def multiplier_function(x: float) -> float:
        """Multiplies the input by the given multiplier"""
        return x * multiplier

    return multiplier_function