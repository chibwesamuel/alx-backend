#!/usr/bin/env python3
"""
Main file
"""

import sys
from typing import Tuple

# Add the current directory to the sys.path
sys.path.append(".")

from simple_helper_function import index_range

res: Tuple[int, int] = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

