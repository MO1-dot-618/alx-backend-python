#!/usr/bin/env python3
"""Typed function element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes list returns list"""
    return [(i, len(i)) for i in lst]