# ENSF 338
# Lab3
# Exercise 7

import json
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Binary search:
def interpolation_search(item, data, init_mid):
    lower = 0
    upper = len(data) - 1

    if data[init_mid] == item:
        return init_mid
    elif data[init_mid] > item:
        upper = init_mid - 1
    else:
        lower = init_mid + 1

    while lower <= upper:
        mid = lower + (upper - lower) // 2

        if data[mid] == item:
            return mid
        elif data[mid] > item:
            upper = mid - 1
        else:
            lower = mid + 1

    return -1

with open("./ex7tasks.json", "r") as f:
    tasks = json.load(f)
 
with open("./ex7data.json", "r") as f:
    data = json.load(f)

increment = len(data) // 50
best_mids = []
midpoints = []
for task in tasks:
    times = []
    for midpoint in range(0, len(data) - 1, increment):
        midpoints.append(midpoint)
        times.append(timeit.timeit(lambda: interpolation_search(task, data, midpoint), number=30))
    
    best_mids.append(np.argmin(times) * increment)

plt.scatter(tasks, best_mids)
plt.show()

# The initial midpoint choice seems to affect the performance
# The scatter plot implies that the closer the initial midpoint was to the task, the faster
# the midpoint was found. This is because the scatter plot seems to form a y = x trend, implying
# that the best midpoints were the ones that were closest to the task.
