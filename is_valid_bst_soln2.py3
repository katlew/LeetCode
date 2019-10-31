"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Approach 2: Iteration
The above recursion could be converted into iteration, with the help of stack.
DFS would be better than BFS since it works faster here.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: 
            return True
        
        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, left, right = stack.pop()
            if not root:
                continue

            val = root.val
            if val <= left or val >= right:
                return False
            stack.append((root.right, val, right))
            stack.append((root.left, left, val))
        return True
"""
Complexity Analysis

Time complexity : O(N) since we visit each node exactly once.
Space complexity : O(N) since we keep up to the entire tree.
"""