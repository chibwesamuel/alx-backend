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
