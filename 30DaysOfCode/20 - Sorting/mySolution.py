#!/bin/python3

import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

# Everything below here is my code...

# Implement a basic version of Bubble Sort that also tracks the number
# of swaps executed during the process
total_swaps = 0

for i in range(n - 1):
    curr_swaps = 0
    for j in range(n - 1):
        if a[j] > a[j+1]:
            # Swap
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

            curr_swaps += 1
            total_swaps += 1

    # If nothing was swapped on this pass, we can assume it's already sorted
    if curr_swaps == 0:
        break

print("Array is sorted in " + str(total_swaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n-1]))
