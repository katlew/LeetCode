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

Depth First Search: Iterative Version
Traverse level by level and keep a counter to track level count

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
   let maxLevel = 0;
   let stack = [];
   if (root) {
       stack.push([root, 1])
   }

   while (stack.length > 0) {
       let currStackItem = stack.pop();
       let currNode = currStackItem[0];
       let currLevel = currStackItem[1];

       maxLevel = Math.max(maxLevel, currLevel);

       if (currNode.left) {
           stack.push([currNode.left, currLevel+1]);
       }
       if (currNode.right) {
           stack.push([currNode.right, currLevel+1]);
       }
   }

   return maxLevel;
};
/*
Complexity

Time Complexity: O(N)
Space Complexity: O(N)
*/