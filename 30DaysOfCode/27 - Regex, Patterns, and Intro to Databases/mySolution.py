#!/bin/python3

import sys
import re

# Storage for first names which are connected to a gmail address
names = []

N = int(input().strip())
for entry in range(N):
    firstName, emailID = map(str, input().strip().split(' '))

    # Check email for '@gmail.com' suffix and add to the list of names if so
    match = re.search('@gmail\.com$', emailID)
    if match:
        names.append(firstName)

# Print each name on a separate line, in alphabetical order
for name in sorted(names):
    print(name)
