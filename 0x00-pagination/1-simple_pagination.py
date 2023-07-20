#!/usr/bin/env python3
"""
Implement a method named get_page that takes two integer arguments page
with default value 1 and page_size with default value 10.
"""

import csv
from typing import List

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
        """Return the appropriate page of the dataset based on pagination
        parameters.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list containing the rows for the given
            page and page_size.
        """
        assert isinstance(page, int) and page > 0, "Page must be a
        positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page_size must
        be a positive integer."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []

        return (dataset[start_index:end_index])

