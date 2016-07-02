# We can use map(int, input...) to iteratively apply the int function to the
# result of splitting the input
# Date when Accepted
aDay, aMonth, aYear = map(int, input().split())
#aDay, aMonth, aYear = [int(aDay), int(aMonth), int(aYear)]

# Date when Due
dDay, dMonth, dYear = map(int, input().split())
#dDay, dMonth, dYear = [int(dDay), int(dMonth), int(dYear)]

# By default, there is no fine
fine = 0

# 10k fine if year accepted is greater than the due year
if (aYear > dYear):
    fine = 10000
# 500 * months late fee if year is the same but returned on a later month
elif (aMonth > dMonth and aYear == dYear):
    fine = (aMonth - dMonth) * 500
# 15 * days late fee if year and month are fine but returned on a later day
elif (aDay > dDay and aMonth == dMonth and aYear == dYear):
    fine = (aDay - dDay) * 15

print(int(fine))
