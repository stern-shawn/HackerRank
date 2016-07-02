import sys

class Node:
  def __init__(self,data):
    self.right=self.left=None
    self.data = data

class Solution:
  def insert(self,root,data):
    if root==None:
        return Node(data)
    else:
      if data<=root.data:
        cur=self.insert(root.left,data)
        root.left=cur
      else:
        cur=self.insert(root.right,data)
        root.right=cur
    return root

  def levelOrder(self,root):
    #Write your code here
    # Perform a level-order traversal of the given root node
    if root is not None:
      # Establish a 'queue' starting with root
      queue = [root]
      while(queue):
        # 'De-queue' first element
        curr = queue.pop(0)

        # Print the current node on the same line using the 'end' argument to print
        print(curr.data, end=" ")

        # Enqueue any left/right children in order
        if (curr.left is not None):
          queue.append(curr.left)
        if (curr.right is not None):
          queue.append(curr.right)

# Remainder of provided code below
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
