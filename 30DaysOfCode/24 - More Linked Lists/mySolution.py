class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class Solution:
  def insert(self,head,data):
    p = Node(data)
    if head==None:
      head=p
    elif head.next==None:
      head.next=p
    else:
      start=head
      while(start.next!=None):
        start=start.next
      start.next=p
    return head
  def display(self,head):
    current = head
    while current:
      print(current.data,end=' ')
      current = current.next

  def removeDuplicates(self,head):
    #Write your code here
    # Make a copy of head to iterate over and so we keep a reference to head available
    curr = head
    # Only iterate if next is not null
    while curr.next:
      # If this data and the next element are a match, 'delete' the element by linking
      # this node to the following node
      if curr.data == curr.next.data:
        curr.next = curr.next.next
      # Otherwise, keep iterating to the next node
      else:
        curr = curr.next

    # Return the original head pointer
    return head

# Remaining provided code below...
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);
