
# Quicksort Algorithm Variants

This Python script demonstrates two variants of the Quicksort sorting algorithm: deterministic Quicksort and randomized Quicksort. Both methods aim to sort an array of integers, with the randomized version using a random element as the pivot to improve performance in certain scenarios.

## Features

- **Deterministic Quicksort**: Uses the last element as the pivot.
- **Randomized Quicksort**: Selects a random element as the pivot.
- **Performance Analysis**: Measures and prints the execution time of each sort on different types of input arrays (random, sorted, reverse sorted).

## Requirements

- Python 3.6 or higher

## Installation

No additional libraries are required to run this script. Ensure that Python is correctly installed on your system. You can download Python from [python.org](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

## Usage

To run this script, navigate to the directory containing the script and run the following command in the terminal:

```bash
python Ass_5.py
```

This will execute the script and print the execution times for both deterministic and randomized Quicksort on three different array types:
- Random array
- Already sorted array
- Reverse sorted array

The results provide insights into how each algorithm performs under various conditions, illustrating the potential advantages of randomized pivoting in Quicksort.

## Functionality

- **partition(arr, low, high)**: Helper function for deterministic Quicksort that partitions the array around the last element as the pivot.
- **deterministic_quicksort(arr, low, high)**: Implements the deterministic Quicksort algorithm.
- **randomized_partition(arr, low, high)**: Randomizes the pivot selection for Quicksort.
- **randomized_quicksort(arr, low, high)**: Implements the Quicksort algorithm using a randomized pivot.
- **measure_time(sort_function, arr)**: Measures and returns the execution time of a sorting function.

## Performance Analysis

The script measures and compares the execution times of both sorting algorithms on different types of arrays to help understand their efficiency and behavior in various scenarios. This analysis can help in choosing the right sorting strategy based on the input data characteristics.

