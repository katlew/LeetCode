"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

Breadth First Search: Iterative Version
Traverse level by level and keep a counter to track level count
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack, max_level = [], 0
        if root:
            stack.append((root, 1))
        while stack:
            x, level = stack.pop()
            max_level = max(max_level, level)
            if x.left:
                stack.append((x.left, level+1))
            if x.right:
                stack.append((x.right, level+1))
        return max_level

"""
Complexity

Time Complexity: O(N)
Space Complexity: O(N)
"""