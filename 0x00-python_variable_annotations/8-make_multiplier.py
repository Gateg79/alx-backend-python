#!/usr/bin/env python3
"""A type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """TAkes a float and returns a function"""
    return lambda x: x * multiplier
