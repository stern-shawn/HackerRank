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

    def getHeight(self,root):
        #Write your code here
        curr = root
        # Root case where we're at the bottom of a path. Return 0 since we're
        # tracking edges instead of number of nodes as depth
        if curr.left is None and curr.right is None:
            return 0
        # Case where only one child exists for this node, get that child's
        # height and increment by the edge that exists between this and the
        # child
        elif curr.left is None and curr.right is not None:
            return 1 + self.getHeight(curr.right)
        # Same case as above for child on other side
        elif curr.left is not None and curr.right is None:
            return 1 + self.getHeight(curr.left)
        # Case where current node has two children, return the largest
        # plus the edge that exists between the child and his node
        else:
            return 1 + max(self.getHeight(curr.left), self.getHeight(curr.right))

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
