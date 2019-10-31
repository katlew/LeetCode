/*
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
public class TreeMinMax {
    public TreeNode node;
    public int? left;
    public int? right;
    public TreeMinMax(TreeNode node, int? left, int? right) {
        this.node = node;
        this.left = left;
        this.right = right;
    }
}
public class Solution {
    public bool IsValidBST(TreeNode root) {
        if (root == null) return true;

        var stack = new Stack<TreeMinMax>();

        stack.Push(new TreeMinMax(root, null, null));

        while (stack.Count > 0)
        {
            TreeMinMax curr = stack.Pop();
            int? left = curr.left;
            int? right = curr.right;
            TreeNode node = curr.node;

            if (left != null && node.val <= left) return false;
            if (right != null && node.val >= right) return false;

            if (node.left != null) {
                stack.Push(new TreeMinMax(node.left, left, node.val));
            }
            if (node.right != null) {
                stack.Push(new TreeMinMax(node.right, node.val, right));
            }
        }
        return true;
    }
}
/*
Complexity Analysis

Time complexity : O(N) since we visit each node exactly once.
Space complexity : O(N) since we keep up to the entire tree.
*/