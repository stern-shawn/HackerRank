import sys

class Solution:
    # Write your code here
    # Define two lists to use at the 'stack' and 'queue'
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, c):
        self.stack.append(c)

    def enqueueCharacter(self, c):
        self.queue.append(c)

    # Use pop to return last element in the list, like stack pop
    def popCharacter(self):
        return self.stack.pop()

    # Use pop(0) to return first element in the list, like a queue
    def dequeueCharacter(self):
        return self.stack.pop(0)

# Provided code below...

# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
