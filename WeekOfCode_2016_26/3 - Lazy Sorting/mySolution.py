import math

numIn = int(input())

# Grab the inputs and convert to a list of ints
elements = input().split()
elements = [int(i) for i in elements]

# To calculate the number of permutations, we'll need the number of elements!
# as a numerator and the product of all counts of each unique element! as the
# denominator
# ie the solution to the input [5, 2] would be 2! / (1! * 1!) as there are two
# values and each occurs once
#
# Refer to: https://en.wikipedia.org/wiki/Permutation#Permutations_of_multisets

# Use a dictionary to count the number of occurences of each unique int
elementCounts = {}
for element in elements:
    if element in elementCounts:
        elementCounts[element] += 1
    else:
        elementCounts[element] = 1

# Take the factorial of each count and multiply them all together
denominator = 1
for key in elementCounts.keys():
    denominator *= math.factorial(elementCounts[key])

# print(elementCounts)

# Take the factorial of how many elements are in the list
n = math.factorial(numIn)
# print(n)
# print(denominator)

result = n / denominator
# User requests 'accuracy' of 6 decimal places
print('%.6f' % result)
