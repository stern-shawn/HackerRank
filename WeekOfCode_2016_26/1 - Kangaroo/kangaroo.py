#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

# Solve the equation x1 + v1 * t = x2 + v2 * t, and make sure we have a
# positive integer result
if ((x2 - x1) / (v1 - v2)).is_integer() and (x2 - x1) / (v1 - v2) >= 0:
    print("YES")
else:
    print("NO")
