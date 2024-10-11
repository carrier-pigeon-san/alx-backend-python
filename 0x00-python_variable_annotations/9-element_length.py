#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list l of strings as
argument and returns a list of integers representing the lengths of the
strings"""


def element_length(lst: list[str]) -> list[int]:
    """Returns a list of integers representing the lengths of the
    strings in a given list"""
    return [len(x) for x in lst]
