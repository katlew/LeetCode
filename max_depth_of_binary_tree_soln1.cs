/*
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

Depth First Search: Post Order

Empty tree i.e. root is None: Depth = 0
maxDepth(root) = max(maxDepth(root.left), maxDepth(root.right)) + 1 
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int MaxDepth(TreeNode root) {
        if (root == null)
        {
            return 0;
        }
        int leftMax = MaxDepth(root.left);
        int rightMax = MaxDepth(root.right);
        return Math.Max(leftMax, rightMax) + 1;
    }
}

/*
Complexity

Time Complexity: O(N)
Space Complexity: O(N) 
*/