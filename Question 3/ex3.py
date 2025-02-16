import random
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swaps += 1


    return arr, comparisons, swaps

input_size = range(1, 21)
swaps_data = []
comp_data = []

for size in input_size:
    arr = np.random.randint(100, size = size)
    sorted_arr, swaps, comparisons = bubble_sort(arr)
    swaps_data.append(swaps)
    comp_data.append(comparisons)

    



plt.figure(figsize = (10, 5))

plt.subplot(1, 2, 1)
plt.plot(input_size, swaps_data, marker = 'o', linestyle = '-', color = 'blue')
plt.title("Swaps Graph")
plt.xlabel("Input Size")
plt.ylabel("# of Swaps")

plt.subplot(1, 2, 2)
plt.plot(input_size, comp_data, marker = 'o', linestyle = '-', color = 'red')
plt.title("Comparisons Graph")
plt.xlabel("Input size")
plt.ylabel("Number of Comps")

plt.tight_layout()
plt.show()
