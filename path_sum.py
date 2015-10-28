# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None:
        	return False
        elif root.left is None and root.right is None:
        	return sum == root.val
        elif root.left is None:
        	return self.hasPathSum(root.right, sum - root.val)
        elif root.right is None:
        	return self.hasPathSum(root.left, sum - root.val)
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum-root.val)