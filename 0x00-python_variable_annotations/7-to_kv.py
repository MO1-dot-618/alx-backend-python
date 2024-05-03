#!/usr/bin/env python3
"""Complex type function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes string and int or float returns tuple"""
    return (k, v * v)