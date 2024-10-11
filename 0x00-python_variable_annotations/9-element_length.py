#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list l of strings as
argument and returns a list of integers representing the lengths of the
strings"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of integers representing the lengths of the
    strings in a given list"""
    return [(i, len(i)) for i in lst]
