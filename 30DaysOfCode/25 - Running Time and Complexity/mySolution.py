# Needed for sqrt()
import math

# Figure out how many inputs will be given...
numCases = int(input())

# Determine prime status of each line separately...
for i in range(numCases):
    testValue = int(input())
    isPrime = True

    # A number will only be evenly divisible by a value <= its square root,
    # this reduces the # of loops needed. Truncate down to an int for range()
    limit = int(math.sqrt(testValue))

    # Only loop from 2 and up to avoid dividing by 1
    for i in range(2, limit):
        # Evenly divisible if there is no remainder
        if testValue % i == 0:
            isPrime = False
        break

    # Print result... 1 and 0 are not prime
    if isPrime and testValue > 1:
        print("Prime")
    else:
        print("Not prime")
