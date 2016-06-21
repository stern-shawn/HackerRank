class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
    #Complete this method
        # Root case, we're given an empty list at the beginning...
        if not head:
            head = Node(data)
        else:
            current = head
            # We're at the end when .next field is null...
            while current.next:
                current = current.next
            current.next = Node(data)

        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
