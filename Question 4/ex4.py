import matplotlib.pyplot as plt
import numpy as np
import timeit




def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right + - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[low]
        arr[low], arr[right] = arr[right], arr[low]
        return right

def time_measure(size):
    arr = np.random.randint(0, 10000, size)
    return timeit.timeit(lambda: quicksort(arr, 0, len(arr) - 1), number = 1)

sizes = [10, 100, 1000, 10000, 100000]
time = []

for i in sizes:
    time.append(time_measure(i))

plt.figure(figsize = (10, 6))
plt.plot(sizes, time, label = "QuickSort Complexity", marker = 'o')
plt.xlabel("Input size")
plt.ylabel("Time")
plt.title("QuickSort vs Time")
plt.show()    


    
    