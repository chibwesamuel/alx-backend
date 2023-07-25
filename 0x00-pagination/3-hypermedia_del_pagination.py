#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict

class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return hypermedia pagination details for the given index and page_size.

        Args:
            index (int, optional): The starting index for pagination (default is None).
            page_size (int, optional): The number of items per page (default is 10).

        Returns:
            Dict: A dictionary containing hypermedia pagination details.
        """
        assert index is None or 0 <= index < len(self.indexed_dataset()), "Invalid index range"

        if index is None:
            index = 0

        dataset = self.indexed_dataset()
        next_index = index + page_size

        last_index = next_index
        while last_index >= index and last_index not in dataset:
            last_index -= 1

        data = [dataset[i] for i in range(index, last_index + 1)]

        return {
            'index': index,
            'next_index': last_index + 1,
            'page_size': page_size,
            'data': data
        }


if __name__ == "__main__":
    server = Server()

    try:
        should_err = server.get_hyper_index(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_hyper_index(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_hyper_index(2, 'Bob')
    except AssertionError:
        print("AssertionError raised when index and/or page_size are not ints")

    print(server.get_hyper_index(1, 3))
    print(server.get_hyper_index(3, 2))
    print(server.get_hyper_index(3000, 100))

