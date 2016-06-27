#!/bin/python3
import sys

t = int(input().strip())
for a in range(t):
    n = int(input().strip())
    # Tree is planted with inital height 1 always
    height = 1

    # Start at 1 since cycle 0 has no effect. Also skips loop if n is 0
    for i in range(1, n+1):
        # Double height on odd cycles
        if i % 2 != 0:
            height *= 2
        # Increase height by 1 on even cycles
        else:
            height += 1

    print(height)
