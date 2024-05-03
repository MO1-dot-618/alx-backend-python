#!/usr/bin/env python3
"""Typed function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Takes float and int list returns float"""
    sum: float = 0
    for e in mxd_list:
        sum += e
    return sum