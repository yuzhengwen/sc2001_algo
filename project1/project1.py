import random
import timeit

s = 100 # threshold value for switching to insertion sort
data_list = []

def generate_input_data():
    for i in range(1000, 2000):
        data_list.append(generate_list(i, 0, 1000))

def generate_list(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]

def hybrid_merge_sort(arr):
    def merge(arr, left, right):
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy the remaining elements from the leftover subarrays
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def insertion_sort(arr):
        for i in range(1, len(arr)): 
            # start from 2nd element as 1st element is considered sorted
            key = arr[i]

            # j holds index of the last element in the sorted subarray (left of key)
            j = i - 1 

            # find the correct position for key in the sorted subarray
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j] # shift arr[j] to the right if it is greater than key
                j -= 1

            # insert key into the correct position (right of j)
            arr[j + 1] = key

    def sort(arr):
        if len(arr) > 1:
            if len(arr) < s:
                insertion_sort(arr)
            else:
                mid = len(arr) // 2
                (left, right) = (arr[:mid], arr[mid:])

                # Sort the left and right halves recursively
                sort(left)
                sort(right)

                # Merge the sorted halves
                merge(arr, left, right) # arr modified in place

    sort(arr)

def benchmark():
    for arr in data_list:
        hybrid_merge_sort(arr)
    return 0

generate_input_data()
# benchmark the task
result = timeit.timeit('benchmark()', setup='from __main__ import benchmark', number=3)
# calculate the average
average_result = result / 3
# report the result
print(f'Average time: {average_result:.3f} seconds')