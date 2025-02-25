import matplotlib

import matplotlib.pyplot as plt


import time
import random


# Traditional Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Binary Insertion Sort
def binary_search(arr, val, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid
    return start

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        pos = binary_search(arr, val, 0, i)
        arr[pos+1:i+1] = arr[pos:i]
        arr[pos] = val

# Experiment Setup
sizes = [100, 500, 1000, 5000, 10000]
insertion_times = []
binary_insertion_times = []

for size in sizes:
    test_data = [random.randint(1, 10000) for _ in range(size)]
    
    # Measure traditional insertion sort
    arr_copy = test_data[:]
    start_time = time.time()
    insertion_sort(arr_copy)
    insertion_times.append(time.time() - start_time)
    
    # Measure binary insertion sort
    arr_copy = test_data[:]
    start_time = time.time()
    binary_insertion_sort(arr_copy)
    binary_insertion_times.append(time.time() - start_time)

# Plot results
plt.plot(sizes, insertion_times, label="Traditional Insertion Sort", marker='o')
plt.plot(sizes, binary_insertion_times, label="Binary Insertion Sort", marker='s')
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Performance")
plt.legend()
plt.savefig('output_plot.png')
plt.show()

'''
4. The binary insertion sort is far faster than the traditonal insertion sort, the reason for this is due to the complexity of each alorithm.
We can see in the traditional insertion sort, that we have an average case complexity of O(n^2), aa quadratic cmplexity, the root of this is due to the nested loops in the function
which can result in a qudratic number of operations in terms of complexity for average and worst case scenarios due to the quadratic number of operations done. Speicifcally, the average case complexity is desrived from [n^2 + 5n - 6] / 4 = O(n^2).
However, the binary insertion sort has a compelxity of O(nlogn) regardless of best, worst, and average cases. Since the binary search function itself splits the array into half until there are single or no element arrrays, the binary search function has a complexity of logn, and the 
binary_insertion_sort function itself only requires a iteration throughout each array n times upon each recursive call from binary search, we find that the overall complexity of the algoirthm is O(nlog(n)) we reduces the number of operatiosn significantly.   
'''