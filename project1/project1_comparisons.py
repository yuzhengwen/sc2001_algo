import random
import timeit

def hybrid_merge_sort(arr, s=10):
    def insertion_sort(sub_arr):
        comparisons = 0
        for i in range(1, len(sub_arr)):
            key = sub_arr[i]
            j = i - 1
            while j >= 0 and sub_arr[j] > key:
                comparisons += 1
                sub_arr[j + 1] = sub_arr[j]
                j -= 1
            sub_arr[j + 1] = key
        return comparisons

    def merge(arr, left, right):
        comparisons = 0
        i = j = k = 0
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

        return comparisons

    def sort(arr):
        comparisons = 0
        if len(arr) > 1:
            if len(arr) <= s:
                comparisons += insertion_sort(arr)
            else:
                mid = len(arr) // 2
                (left, right) = (arr[:mid], arr[mid:])

                comparisons += sort(left)
                comparisons += sort(right)
                comparisons += merge(arr, left, right)

        return comparisons

    return sort(arr)

def generate_list(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]

data_list = generate_list(1000, 0, 1000)
def benchmark():
    new_list = data_list.copy()
    print(hybrid_merge_sort(new_list))

# benchmark the task
result = timeit.timeit('benchmark()', setup='from __main__ import benchmark', number=3)
# calculate the average
average_result = result / 3
# report the result
print(f'Average time: {average_result:.5f} seconds')