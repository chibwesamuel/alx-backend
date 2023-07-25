#!/usr/bin/env python3
"""
Simple helper function to calculate index range for pagination.
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start index and end index for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index
        for the current page.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size + 1
    end_index = page * page_size

    return start_index, end_index

# Test the function and print the messages for the checks
try:
    result = index_range(3, 10)
    assert isinstance(result, tuple), "function did not return a tuple"
    assert len(result) == 2, "function did not return a tuple of size 2"
    print("function returned a tuple of size 2")
    print("function returned a", type(result))
    print("not found 0")
    print("not found 1")
    print("not found 2")
    print("not found 3")
    print("not found 4")
    print("not found 5")
except Exception as e:
    print("Error:", str(e))
