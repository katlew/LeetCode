/*
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
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
    public int MinDepth(TreeNode root) {
        if (root == null)
        {
            return 0;
        }
        
        if (root.right == null && root.left == null)
        {
            return 1;
        }
        
        int level = 1;
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        while (queue.Count > 0)
        {
            int count = queue.Count;
            for(int i = 0; i < count; ++i)
            {
                TreeNode node = queue.Dequeue();

                if (node.left == null && node.right == null)
                {
                    return level;
                }

                if (node.left != null)
                {
                    queue.Enqueue(node.left);
                }
                if (node.right != null)
                {
                    queue.Enqueue(node.right);
                }
            }
            
            level++;

        }
        
        return level;
    }
}

/*
Complexity:
Time Complexity: O(n)
Space Complexity: O(n) 
*/