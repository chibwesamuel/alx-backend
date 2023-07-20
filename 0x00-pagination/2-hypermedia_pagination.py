#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same arguments as get_page
Returns a dictionary with key-pair values
"""

import csv
import math
from typing import List, Dict

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end indexes for a given page and page_size."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index

class Server:
    """Server class to paginate a database of popular baby names."""
    
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset based on pagination parameters.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list containing the rows for the given page and page_size.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page_size must be a positive integer."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return hypermedia pagination details for the given page and page_size.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing hypermedia pagination details.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page_size must be a positive integer."

        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

