#!/usr/bin/env python3
"""
Main file
"""

from typing import Tuple
from index_range import index_range

res: Tuple[int, int] = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

