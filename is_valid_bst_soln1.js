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
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root)
{
    return helper(root, null, null);
};

var helper = function(node, left, right)
{
    if (!node) return true;

    if (left !== null && node.val <= left) return false;
    if (right !== null && node.val >= right) return false;

    return helper(node.left, left, node.val) 
        && helper(node.right, node.val, right);
};
/*
Complexity Analysis

Time complexity : O(N) since we visit each node exactly once.
Space complexity : O(N) since we keep up to the entire tree.
*/