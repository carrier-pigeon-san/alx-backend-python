#!/usr/bin/env python3
"""
Type-annotated function sum_list that returns the sum of floats in a list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    total: float = 0.00
    for item in input_list:
        total += item
    return total
