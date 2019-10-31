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
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    let depth = 0;
    let q = [];

    if (root !== null)
    {
        q.push(root);
    }
    while (q.length != 0)
    {
        depth += 1;
        for(var i = 0; i < q.length; ++i)
        {
            x = q.pop();
            if (x.left)
            {
                q.push(x.left);
            }
            if (x.right)
            {
                q.push(x.right);
            }
        }
    }
    return depth;
}
/*
Complexity

Time Complexity: O(N)
Space Complexity: O(N)
*/