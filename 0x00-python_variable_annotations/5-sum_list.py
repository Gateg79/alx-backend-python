#!/usr/bin/env python3
"""A type-annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list and returns the sum of the elements in float"""
    return float(sum(input_list))
