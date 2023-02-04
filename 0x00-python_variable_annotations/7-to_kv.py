#!/usr/bin/env python3
"""A type-annotated function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string and an int OR float & returns a tuple"""
    return (k, (v**2))
