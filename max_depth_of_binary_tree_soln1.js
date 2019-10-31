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
    if (!root) {
        return 0;
    }  
    var leftMax = maxDepth(root.left);
    var rightMax = maxDepth(root.right);
    return Math.max(leftMax, rightMax) + 1;
};
/*
Complexity

Time Complexity: O(N)
Space Complexity: O(N) 
*/