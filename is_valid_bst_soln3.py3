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

Approach 3: Inorder traversal
Algorithm

Let's use the order of nodes in the inorder traversal Left -> Node -> Right.
Here the nodes are enumerated in the order you visit them, and you could follow 1-2-3-4-5 to compare different strategies.
Left -> Node -> Right order of inorder traversal means for BST that each element should be smaller than the next one.

Hence the algorithm with O(N) time complexity and O(N) space complexity could be simple:
Compute inorder traversal list inorder.
Check if each element in inorder is smaller than the next one.


Do we need to keep the whole inorder traversal list?
Actually, no. The last added inorder element is enough 
to ensure at each step that the tree is BST (or not). 
Hence one could merge both steps into one and reduce the used space.

Implementation
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
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
"""
Complexity Analysis

Time complexity : O(N) in the worst case when the tree is BST or the "bad" element is a rightmost leaf.
Space complexity : O(N) to keep stack.
"""
