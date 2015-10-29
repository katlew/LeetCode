class Solution(object):
    def minDepth(self, root):
        count = 0
        if root is None:
        	return 0
        elif root.left is None and root.right is None:
        	return 1		# leaf
        elif root.left is None:
        	return self.minDepth(root.right) + 1
        elif root.right is None:
        	return self.minDepth(root.left) + 1
        else:
        	return min(self.minDepth(root.left),self.minDepth(root.right))+1
