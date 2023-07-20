## Pagination in Back-End

In this project, I implemented pagination in a back-end environment. Pagination is a common technique used to break down large datasets into smaller, more manageable chunks for better performance and user experience.

### Task 0: Simple Helper Function

In the first task, I created a Python function called `index_range` that takes two integer arguments: `page` and `page_size`. This function returns a tuple containing the start and end indexes corresponding to the range of indexes to return in a list for those specific pagination parameters.

### Task 1: Simple Pagination

In the second task, I implemented a `Server` class that handles pagination of a database containing popular baby names. The `Server` class has a method called `get_page`, which takes two integer arguments: `page` and `page_size`. It uses the `index_range` function from Task 0 to find the correct indexes to paginate the dataset and returns the appropriate page of data. If the input arguments are out of range for the dataset, an empty list is returned.

### Task 2: Hypermedia Pagination

In the third task, I expanded on the previous `Server` class to include a new method called `get_hyper`, which provides hypermedia metadata in addition to the paginated data. The `get_hyper` method returns a dictionary containing information such as `page_size`, `page`, `data`, `next_page`, `prev_page`, and `total_pages`. This metadata helps users navigate through the paginated dataset more easily.

### Task 3: Deletion-Resilient Hypermedia Pagination

The final task involved creating a new method in the `Server` class called `get_hyper_index`. This method behaves similar to `get_hyper`, but it ensures that if certain rows are removed from the dataset between queries, users do not miss items when changing pages. The `get_hyper_index` method returns a dictionary with information about the current start index, next index, page size, and data, making it resilient to data deletions.

## Usage

To test the pagination functionality, you can use the provided main files for each task:

- `0-main.py` for Task 0
- `1-main.py` for Task 1
- `2-main.py` for Task 2
- `3-main.py` for Task 3

Each main file showcases examples of using the implemented functions and classes to perform pagination on the dataset of popular baby names.

### Running the Examples

To run the examples, execute the corresponding main file using Python:

```bash
python3 0-main.py
python3 1-main.py
python3 2-main.py
python3 3-main.py
```

## Repository Structure

- `0-simple_helper_function.py`: Implementation of Task 0's `index_range` function.
- `1-simple_pagination.py`: Implementation of Task 1's `Server` class with `get_page` method.
- `2-hypermedia_pagination.py`: Implementation of Task 2's `get_hyper` method in the `Server` class.
- `3-hypermedia_del_pagination.py`: Implementation of Task 3's `get_hyper_index` method in the `Server` class.
- `0-main.py`, `1-main.py`, `2-main.py`, `3-main.py`: Main files for testing the pagination functionality in each task.
- `Popular_Baby_Names.csv`: Sample dataset used for testing.

## Conclusion

In this project, I demonstrated how to implement pagination in a back-end environment. By breaking down large datasets into smaller pages and providing hypermedia metadata, users can navigate through the data efficiently and in a deletion-resilient manner. Proper pagination improves performance and enhances the user experience when dealing with large datasets.
