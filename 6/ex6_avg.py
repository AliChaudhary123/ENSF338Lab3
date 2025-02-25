# ENSF 338
#Lab3
# Exercise 6

import sys
import timeit
import numpy as np
import matplotlib.pyplot as plt
import random
import faulthandler

sys.setrecursionlimit(200000)
faulthandler.enable()

# Linear search:
def linear_search(item, data):
    for i in range(0, len(data)):
        if data[i] == item:
            return i
    return -1


# Binary search:
def binary_search(item, data):
    lower = 0
    upper = len(data) - 1

    while lower <= upper:
        mid = lower + (upper - lower) // 2

        if data[mid] == item:
            return mid
        elif data[mid] > item:
            upper = mid - 1
        else:
            lower = mid + 1

    return -1


def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        # Partition
        while left <= right and arr[left] < pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        # Swap
        if right < left:
            done = True
        else:
            arr[right], arr[left] = arr[left], arr[right]

    # Partitioning is complete
    # New pivot is the element at the highest index of the left sub-array
    arr[low], arr[right] = arr[right], arr[low]
    # Return highest index of left sub-array
    return right


def quick_sort(arr, low, high):

    if low < high:
        pivot_index = partition(arr, low, high)
        # For left sub-array
        quick_sort(arr, low, pivot_index)
        # For right sub-array
        quick_sort(arr, pivot_index + 1, high)

        
def sorted_bin_search(item, arr, low, high):
    quick_sort(arr, low, high)
    return binary_search(item, arr)


list_lengths = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
avg_times_lin = []
avg_times_bin = []
item = 7

for length in list_lengths:
    print(length)
    avg_lin = 0
    avg_bin = 0

    for i in range(100):
        task = []
        for i in range(length):
            task.append(random.randint(0, length - 1))

        avg_lin += timeit.timeit(lambda: linear_search(7, task), number=1)
        avg_bin += timeit.timeit(lambda: sorted_bin_search(7, task, 0, length - 1), number=1)

    avg_lin /= 100
    avg_bin /= 100
    
    avg_times_lin.append(avg_lin)
    avg_times_bin.append(avg_bin)


plt.plot(list_lengths, avg_times_lin, label="Linear Search")
plt.plot(list_lengths, avg_times_bin, label="Binary Search")
plt.legend(loc="upper left")
plt.show()

# Discussion
# From the plot it is clear that linear search is faster than sorting the array with quick sort and then using binary search.
# This result makes sense as the time complexity for quick sort itself is O(nlogn) which is already greater than linear serach
# which has a time complexity of O(n).
