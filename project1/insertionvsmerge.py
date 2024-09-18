'''
This script is used to find the threshold at which Insertion Sort becomes slower than Merge Sort for sorting random arrays of integers.
This is done by comparing the average time taken by both algorithms to sort arrays of increasing sizes (up to n).
Each size is tested multiple times to get a more accurate average time.
'''

import random
import timeit
import statistics

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def time_sort(sort_func, arr):
    setup_code = f"from __main__ import {sort_func.__name__}, generate_random_array; arr = generate_random_array({len(arr)})"
    stmt = f"{sort_func.__name__}(arr.copy())"
    return timeit.timeit(stmt, setup=setup_code, number=1000)

def find_threshold(max_size=200, runs_per_size=1, consecutive_checks=10):
    threshold_count = 0
    for size in range(1, max_size + 1):
        insertion_times = []
        merge_times = []
        
        for _ in range(runs_per_size):
            arr = generate_random_array(size)
            insertion_times.append(time_sort(insertion_sort, arr))
            merge_times.append(time_sort(merge_sort, arr))
        
        insertion_avg = statistics.mean(insertion_times)
        merge_avg = statistics.mean(merge_times)
        
        print(f"Size: {size}, Insertion: {insertion_avg:.6f}, Merge: {merge_avg:.6f}")
        
        if merge_avg < insertion_avg:
            threshold_count += 1
            if threshold_count >= consecutive_checks:
                print(f"\nThreshold found at array size: {size - consecutive_checks + 1}")
                return size - consecutive_checks + 1
        else:
            threshold_count = 0
    
    print("Threshold not found within the given range")
    return None

if __name__ == "__main__":
    threshold = find_threshold()
    if threshold:
        print(f"For arrays smaller than {threshold} elements, Insertion Sort is faster.")
        print(f"For arrays with {threshold} or more elements, Merge Sort is faster.")