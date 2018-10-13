/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

var depth = function(root) {
    if (!root) {
        return 0;
    }
    var left = depth(root.left);
    var right = depth(root.right);
    if (left === -1 || right === -1 || left - right > 1 || right - left > 1) {
        return -1;
    }
    return Math.max(left, right) + 1;
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    return depth(root) !== -1;
};
