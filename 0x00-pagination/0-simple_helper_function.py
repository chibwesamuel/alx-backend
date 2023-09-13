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

    start_index = (page - 1) * page_size
    end_index = page * page_size - 1

    return start_index, end_index


# Test the function and print the messages for the checks
try:
    result = index_range(3, 10)
    assert isinstance(result, tuple), "function did not return a tuple"
    assert len(result) == 2, "function did not return a tuple of size 2"
    assert all(isinstance(item, int) for item in result), "tuple elements
    should be integers"
    assert result[0] == 20, "incorrect start index"
    assert result[1] == 29, "incorrect end index"
    print("OK")


except Exception as e:
    """Error exception"""
    print("Error:", str(e))
