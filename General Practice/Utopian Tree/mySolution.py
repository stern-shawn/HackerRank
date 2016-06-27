#!/bin/python3
import sys

t = int(input().strip())
for a in range(t):
    n = int(input().strip())
    height = 1

    for i in range(1, n+1):
        if i % 2 != 0:
            height *= 2
        elif i % 2== 0:
            height += 1

    print(height)
