#!/usr/bin/env python3
"""Type-annotated function safe_first_element"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element of a list if exists, otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
