'''
this file compares the performance of merge_sort and hybrid_merge_sort
the algorithms includes the number of comparisons made
both algorithms can be tested on size n and repeated r times to find average time/comparisons
'''

import random
import timeit

def get_list(size):
    def read_array_from_file(file_path):
        with open(file_path, 'r') as file:
            # Read all lines, strip whitespace, and convert to integers
            array = [int(line.strip()) for line in file]
        return array
    file_path = f'arrays/array_{size}.txt'
    return read_array_from_file(file_path)

def hybrid_merge_sort(arr, s=58):
    comparisons = 0

    def merge(arr, left, right):
        nonlocal comparisons
        i = j = k = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def insertion_sort(arr):
        nonlocal comparisons
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                comparisons += 1
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            if j >= 0:
                comparisons += 1  # Count the last comparison that caused the while loop to exit

    def sort(arr):
        if len(arr) > 1:
            if len(arr) <= s:
                insertion_sort(arr)
            else:
                mid = len(arr) // 2
                left, right = arr[:mid], arr[mid:]

                sort(left)
                sort(right)

                merge(arr, left, right)

    sort(arr)
    return comparisons

def merge_sort(arr):
    def merge(start, mid, end):
        nonlocal comparisons
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]
        i, j, k = 0, 0, start

        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def sort(start, end):
        if start < end:
            mid = (start + end) // 2
            sort(start, mid)
            sort(mid + 1, end)
            merge(start, mid, end)

    comparisons = 0
    sort(0, len(arr) - 1)
    return comparisons

def benchmark_single_run(sort_func, data):
    output = sort_func(data)
    if output is not None:
        print(output)

def run_benchmarks(sort_func, num_runs=1, list_size=10000000):
    total_time = 0
    for _ in range(num_runs):
        # Generate a new list outside of the timed portion
        data = get_list(list_size)
        random.shuffle(data)
        
        # Time only the sorting operation
        time = timeit.timeit(lambda: benchmark_single_run(sort_func, data), 
                             number=1)
        total_time += time
    
    average_time = total_time / num_runs
    print(f'Average time for {sort_func.__name__} over {num_runs} runs: {average_time:.5f} seconds')

# Run benchmarks for each sorting algorithm
print("merge_sort")
run_benchmarks(merge_sort)
print("hybrid_merge_sort")
run_benchmarks(hybrid_merge_sort)
#print("insertion_sort")
#run_benchmarks(insertion_sort)