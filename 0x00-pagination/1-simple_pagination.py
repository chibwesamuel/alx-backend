#!/usr/bin/env python3

"""
Implement a method named get_page that takes two integer arguments page
with default value 1 and page_size with default value 10.
"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The CSV file containing the dataset.
        __dataset (List[List[str]]): Cached dataset loaded from the CSV file.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server class."""
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset.

        Returns:
            List[List[str]]: The dataset loaded from the CSV file,
            excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Get a page of the dataset based on page number and page size.

        Args:
            page (int, optional): Page number (default is 1).
            page_size (int, optional): Number of items per page
            (default is 10).

        Returns:
            List[List[str]]: A list of rows representing the page data.
        """
        assert isinstance(page, int), "Page must be an integer"
        assert page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int), "Page size must be an integer"
        assert page_size > 0, "Page size must be a positive integer"

        total_pages = math.ceil(len(self.__dataset) / page_size)
        if page > total_pages or page < 1:
            return []

        index_range = self.index_range(page, page_size)
        return self.__dataset[index_range[0]:index_range[1]]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Return a tuple of start and end indexes for the given page
        and page size.

        Args:
            page (int): Page number.
            page_size (int): Number of items per page.

        Returns:
            Tuple[int, int]: A tuple (start_index, end_index) representing
            the index range for the page.
        """
        start_index = (page - 1) * page_size
        end_index = page * page_size
        return start_index, end_index

if __name__ == "__main__":
    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_page(2, 'Bob')
    except AssertionError:
        print("AssertionError raised when page and/or
                page_size are not ints")

    print(server.get_page(1, 3))
    print(server.get_page(3, 2))
    print(server.get_page(3000, 100))

