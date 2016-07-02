#!/bin/python3

import sys

x1,v1,x2,v2 = map(int, input().strip().split(' '))

# Solve the equation x1 + v1 * t = x2 + v2 * t, and make sure we have a
# positive integer result since kangaroos can't travel in partial jumps...
if ((x2 - x1) / (v1 - v2)).is_integer() and (x2 - x1) / (v1 - v2) >= 0:
    print("YES")
else:
    print("NO")
