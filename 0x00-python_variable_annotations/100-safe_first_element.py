#!/usr/bin/env python3
"""Annotate a function"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence if it exists"""
    return lst if lst[0] else None
