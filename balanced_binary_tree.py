class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                diff = abs(self.height(root.left) - self.height(root.right))
                return diff <= 1
            else:
                return False

    def height(self, root):
        if root is None:
            return -1
        else:
            return max(self.height(root.left), self.height(root.right)) + 1     # add each node
                