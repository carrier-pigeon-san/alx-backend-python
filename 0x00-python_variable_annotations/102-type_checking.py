#!/usr/bin/env python3
"""Type Checking"""
from typing import Tuple, Union, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Creates a new list where each element of the input tuple is repeated
    'factor' times.

    Args:
        lst (Tuple): The input tuple whose elements are to be repeated.
        factor (int, optional): The number of times each element in the tuple
        should be repeated. Defaults to 2.

    Returns:
        List: A list containing the elements of the input tuple, each repeated
        'factor' times.
    """
    """"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
