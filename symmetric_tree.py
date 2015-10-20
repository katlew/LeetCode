# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
        	return True
        else:
        	return self.symmetric(root.left, root.right)
    def symmetric(self, left, right):
    	if left is None and right is None:
    		return True
    	elif left is None or right is None:
    		return False
    	elif left.val != right.val:
    		return False
    	else:
    		return self.symmetric(left.left, right.right) and self.symmetric(left.right, right.left)