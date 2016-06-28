numContests, maxLoss = input().strip().split(' ')
numContests, maxLoss = [int(numContests), int(maxLoss)]

# Storage for contests which can/can't be skipped and total luck value
unimp = []
imp = []
totalLuck = 0

# Add each contest to the appropriate list
for i in range(numContests):
    luck, importance = input().strip().split(' ')
    luck, importance = [int(luck), int(importance)]

    if importance == 1:
        imp.append(luck)
    else:
        unimp.append(luck)

# Sort the lists so we can target the contests with the smallest luck penalty
unimp = sorted(unimp)
imp = sorted(imp)

# print(imp)
# print(unimp)

# She has to win enough to not exceed the max limit on failed important
# contests... each win counts AGAINST her luck. Contests in the front of the
# list have the smallest impact, so they should be won first
while (len(imp) > maxLoss):
    currLoss = imp.pop(0)
    totalLuck -= currLoss

# Add the remaining important contests luck values...
for i in range(len(imp)):
    totalLuck += imp[i]

# ... and add the luck values for all unimportant contests
for j in range(len(unimp)):
    totalLuck += unimp[j]

print(totalLuck)
