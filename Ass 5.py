import random
import time

# A function to perform partitioning of the array
def partition(arr, low, high):
    # Choose the last element as the pivot
    pivot = arr[high]
    i = low - 1  # Index of the smaller element

    # Traverse the array and swap elements that are smaller than the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Place the pivot element in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partition index

# Deterministic Quicksort using last element as pivot
def deterministic_quicksort(arr, low, high):
    if low < high:
        # Partition the array
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)

# Randomized partitioning
def randomized_partition(arr, low, high):
    # Pick a random pivot element from the array
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]  # Swap with the last element
    return partition(arr, low, high)

# Randomized Quicksort using random pivot selection
def randomized_quicksort(arr, low, high):
    if low < high:
        # Get the partition index using randomized pivot selection
        pi = randomized_partition(arr, low, high)

        # Recursively sort elements before and after partition
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Measure execution time for the sorting algorithms
def measure_time(sort_function, arr):
    start = time.time()  # Record start time
    sort_function(arr, 0, len(arr) - 1)  # Execute the sorting function
    end = time.time()  # Record end time
    return end - start  # Return the execution time

# Test arrays for performance analysis
random_array = [random.randint(0, 10000) for _ in range(1000)]
sorted_array = sorted(random_array)
reverse_sorted_array = sorted(random_array, reverse=True)

# Execute performance analysis for deterministic Quicksort (v2)
print("Deterministic Quicksort (Random array):", measure_time(deterministic_quicksort, random_array.copy()))
print("Deterministic Quicksort (Sorted array):", measure_time(deterministic_quicksort, sorted_array.copy()))
print("Deterministic Quicksort (Reverse sorted array):", measure_time(deterministic_quicksort, reverse_sorted_array.copy()))

# Execute performance analysis for randomized Quicksort (v2)
print("Randomized Quicksort (Random array):", measure_time(randomized_quicksort, random_array.copy()))
print("Randomized Quicksort (Sorted array):", measure_time(randomized_quicksort, sorted_array.copy()))
print("Randomized Quicksort (Reverse sorted array):", measure_time(randomized_quicksort, reverse_sorted_array.copy()))
