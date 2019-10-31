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

Breadth First Search: Iterative Version
Traverse level by level and keep a counter to track level count
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
       int maxLevel = 0
       Stack<Tuple> stack = new Stack<Tuple>();
       if (root != null)
       {
           stack.enqueue(new Tuple<TreeNode, int>(root, 1));
       }
       while (stack.Count > 0)
       {
           
       }
    }
}

/*
Complexity

Time Complexity: O(N)
Space Complexity: O(N) 
*/