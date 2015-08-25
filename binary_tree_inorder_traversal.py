# Definition for a binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    array = []
    def iot(self, root):
        if root == None:
            return
        else:
            self.iot(root.left)
            self.array.append(root.val)
            self.iot(root.right)
            
    def inorderTraversal(self, root):
        self.array = []     # reset the result list
        self.iot(root)
        return self.array
