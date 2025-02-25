# ENSF 338
# Lab 2
# Exercise 2

import sys
import timeit
import matplotlib.pyplot as plt
import faulthandler
import random
#import threading
sys.setrecursionlimit(200000)
#threading.stack_size(2 ** 27)
faulthandler.enable()

def bubble_sort(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp


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
    #print("LR: ", left, right)
    arr[low], arr[right] = arr[right], arr[low]
    # Return highest index of left sub-array
    return right


def quick_sort(arr, low, high):
    #print(low, high)
    #print(arr)

    if low < high:
        pivot_index = partition(arr, low, high)
        # For left sub-array
        quick_sort(arr, low, pivot_index)
        # For right sub-array
        quick_sort(arr, pivot_index + 1, high)


def populate(arr, low, high):
    mid = (high - low) // 2
    print(low, high, mid)
    
    arr[low] = mid
    arr[mid] = mid - 1
    arr[high] = high

    return mid


def pop_best_case(arr, low, high):
    mid = (high - low) // 2
    arr[mid] = 
    
    if low < highs - 2:
        mid = populate(arr, low, high)
        pop_best_case(arr, low + 1, mid - 1)
        pop_best_case(arr, low + mid, high - 1)


# Worst case for this implementation of quick sort is if array is in reverse order
# Best case is when partition results in equal sub-arrays everytime
# Average case is randomized order

# Bubble sort:
# Worst case: reverse order O(n^2)
# Average case: O(n^2)
# Best case: no index update

avg_times_b = []
avg_times_q = []
list_lengths = []


[7, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
arr = [3, 6, 2, 4, 4]
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1, 0]
arr3 = [2, 1, 2, 0, 0, 0]
arr5 = [5, 4, 3, 2, 1, 10 ,9 ,8 ,7 ,6]
[1, 4, 3, 2, 5, 10, 9, 8, 7, 6]
arr4 = [None] * 90
pop_best_case(arr4, 0, 89)
print(arr4)


"""


# Worst case scenario plots
for i in range(1, 21):
    arr_b = []
    arr_q = []
    size = int(i ** 2.5)
    list_lengths.append(size)
    for j in reversed(range(size)):
        arr_b.append(j)
        arr_q.append(j)
    
    avg_times_b.append(timeit.timeit(lambda: bubble_sort(arr_b), number = 1))
    avg_times_q.append(timeit.timeit(lambda: quick_sort(arr_q, 0, size - 1), number = 1))

#print(list_lengths)
plt.scatter(list_lengths, avg_times_b, label="bubble sort")
plt.scatter(list_lengths, avg_times_q, label="quick sort")
plt.legend(loc="upper left")
plt.savefig("WorstCase.png")



# Average case scenario plots
avg_times_b = []
avg_times_q = []
for i in range(1, 21):
    arr_b = []
    arr_q = []
    size = int(i ** 2.5)
    for j in range(size):
        arr_b.append(random.randint(0, size - 1))
        arr_q.append(random.randint(0, size - 1))
    
    avg_times_b.append(timeit.timeit(lambda: bubble_sort(arr_b), number = 1))
    avg_times_q.append(timeit.timeit(lambda: quick_sort(arr_q, 0, size - 1), number = 1))

#print(arr_q)

plt.clf()
plt.scatter(list_lengths, avg_times_b, label="bubble sort")
plt.scatter(list_lengths, avg_times_q, label="quick sort")
plt.legend(loc="upper left")
plt.savefig("AverageCase.png")




# Best case scenario plots

# Bubble sort
avg_times_b = []
for i in range(1, 21):
    arr_b = []
    size = int(i ** 2.5)
    for j in range(size):
        arr_b.append(j)
    
    avg_times_b.append(timeit.timeit(lambda: bubble_sort(arr_b), number=1))
    #avg_times_q.append(timeit.timeit(lambda: quick_sort(arr, 0, size - 1), number = 100))

plt.clf()
plt.scatter(list_lengths, avg_times_b, label="Bubble sort")
plt.savefig("BestCase.png")
"""

# Quick sort
avg_times_q = []
for i in range(1, 21):
    arr_q = []
    size = int(i ** 2.5)
    for j in range(size):
        arr_q.append(j)
    

    
    #avg_times_q.append(timeit.timeit(lambda: quick_sort(arr, 0, size - 1), number = 100))

