#!/bin/python3
import sys

S = input().strip()

# Attempt to print the given input. If the input is not valid as an integer,
# handle the exception by priting "Bad String"
try:
    print(int(S))
# Use type ValueError for conversion failures
except ValueError:
    print("Bad String")
