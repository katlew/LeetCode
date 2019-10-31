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

Depth First Search: Pre Order

Perform pre-order traversal and pass a variable to track the level
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q, depth = collections.deque(), 0
        if root:
            q.append(root)
        while len(q):
            depth += 1
            for _ in range(len(q)):
                x = q.popleft()
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return depth

"""
Complexity

Time Complexity: O(N)
Space Complexity: O(N)
"""