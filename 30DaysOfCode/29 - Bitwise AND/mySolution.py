#!/bin/python3

import sys

# Grab the number of test cases
t = int(input().strip())
for a0 in range(t):
    # Grab current test's set limit (n) and integer limit (k)
    n,k = map(int, input().strip().split(' '))

    # Loop over all combinations of a&b and print the largest value under k
    currMax = 0
    for a in range(1, n):
        for b in range (a + 1, n + 1):
            if a & b > currMax and a & b < k:
                currMax = a & b
            # print("A: " + str(a) + " B: " + str(b) + " A&B: " + str(a&b))
    print(str(currMax))

    # O(1) solution which takes advantage of the fact that we want to
    # always try to get a value of k-1 or k-2 as the result.
    # Very fast, but not very readable or maintainable...
    # a = k - 1
    # b = (~a) & -(~a)
    #
    # if (a | b) > n:
    #     print (str(a - 1))
    # else:
    #     print (str(a))
