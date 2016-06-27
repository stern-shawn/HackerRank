#!/bin/python3
import sys

t = int(input().strip())
for a0 in range(t):
  n = int(input().strip())
  height = 1
  spring = True

  while n > 0:
    if spring:
      height *= 2
      spring = False
    else:
      height += 1
      spring = True

    n -= 1

  print(height)
