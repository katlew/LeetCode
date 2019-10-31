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

Depth First Search: Pre Order

Perform pre-order traversal and pass a variable to track the level

TODO: This does not work for this test case
Input: 
[0,2,4,1,null,3,-1,5,1,null,6,null,8]
Output: 5
Expected 4

*/
public class Solution {
    public int MaxDepth(TreeNode root) {
        Queue q = new Queue<TreeNode>();
        int depth = 0;
        if (root != null) {
            q.Enqueue(root);
        }

        while(q.Count > 0)
        {
            depth += 1;
            for(var i = 0; i < q.Count; ++i)
            {
                x = q.Dequeue();
                if (x.left != null)
                {
                    q.Enqueue(x.left);
                }
                if (x.right != null) 
                {
                    q.Enqueue(x.right);
                }
            }
        }
        return depth;
    }
}

/*
Complexity

Time Complexity: O(N)
Space Complexity: O(N)
*/