#!/bin/python3

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

# My code below
sums = []
for i in range(4):
    for j in range(4):
        #print(i, j)
        #currSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        #print("---")
        #print(arr[i][j:j+3])
        #print(arr[i+1][j+1])
        #print(arr[i+2][j:j+3])
        currSum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
        #print(currSum)
        sums.append(currSum)

print(sorted(sums).pop())
