#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        # Verify that index is in a valid range
        assert index is None or 0 <= index < len(self.indexed_dataset()), "Invalid index range"

        # If index is None, set it to 0
        if index is None:
            index = 0

        # Get the dataset
        dataset = self.indexed_dataset()

        # Calculate the next index to query
        next_index = index + page_size

        # Find the last valid index for the current page
        last_index = next_index
        while last_index >= index and last_index not in dataset:
            last_index -= 1

        # Retrieve the data for the current page
        data = [dataset[i] for i in range(index, last_index + 1)]

        return {
            'index': index,
            'next_index': last_index + 1,
            'page_size': page_size,
            'data': data
        }

