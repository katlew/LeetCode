# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        rootToLeafPaths, currentPath = [], []
        self.preorderTraversal(root, currentPath, rootToLeafPaths)
        return rootToLeafPaths

    def preorderTraversal(self, root, currentPath, rootToLeafPaths):
        if root == None:
            return

        # last child, go through parents and append -> to string
        if root.left is root.right is None:
            string = ""
            for node in currentPath:
                string += (str(node.val) + "->")
            # append last one
            rootToLeafPaths.append(string + str(root.val))

        # if left node exists, append current node
        if root.left:
            currentPath.append(root)
            # DFS
            self.preorderTraversal(root.left, currentPath, rootToLeafPaths)
            currentPath.pop()

        if root.right:
            currentPath.append(root)
            self.preorderTraversal(root.right, currentPath, rootToLeafPaths)
            currentPath.pop()
