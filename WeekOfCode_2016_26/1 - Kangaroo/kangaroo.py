#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

# Boolean to track if the kangaroos are ever at the same location at the same time
tied = False

# Locations are constrained between 0 and 10,000 so we only ever need to track up to that distance
while x1 < 10000 and x2 < 10000:
    x1 += v1
    x2 += v2

    if x1 == x2:
        print("YES")
        tied = True

        # Also break... just to save some runtime instead of waiting for either value to hit 10k
        break

# Print NO if no success case occured
if not tied:
    print("NO")
