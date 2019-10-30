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

Approach 1: Recursion
The idea above could be implemented as a recursion. 
One compares the node value with its upper and lower limits 
if they are available. 
Then one repeats the same step recursively for left and right subtrees.

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
    public bool IsValidBST(TreeNode root) 
    {
        return helper(root, null, null);
    }

    public bool helper(TreeNode node, int left, int right)
    {
        if (node == null) { return true; }

        int val = node.val;
        if (left != null && val <= left) {
            return false;
        }
        if (right != null && val >= right){
            return false;
        }

        if (helper(node.right, val, right) == false) {
            return false;            
        }
        if (helper(node.left, left, val) == false) {
            return false;
        }
        return true;
    }
}