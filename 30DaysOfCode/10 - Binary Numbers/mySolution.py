#!/bin/python3

import sys
n = int(input().strip())

# My code below
# Convert to binary and skip the '0b' at the beginning
output = bin(n)[2:]

# return the length of the longest element after we split the result by 0s
output = len(max(output.split('0')))

print(output)
