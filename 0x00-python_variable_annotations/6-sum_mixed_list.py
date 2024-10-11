#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list that computes the sum of a list of
integers and floats
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Computes the sum of a list of integers and floats"""
    total: float = 0.00
    for item in mxd_list:
        total += item
    return total
