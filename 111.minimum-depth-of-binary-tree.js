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
var minDepth = function(root) {
    if (!root) {
        return 0;
    }
    var left = minDepth(root.left);
    var right = minDepth(root.right);
    if (left === 0) {
        return right + 1;
    }
    if (right === 0) {
        return left + 1;
    }
    return Math.min(left, right) + 1;
};
