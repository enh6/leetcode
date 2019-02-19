/**
 * Definition for binary tree with next pointer.
 * function TreeLinkNode(val) {
 *     this.val = val;
 *     this.left = this.right = this.next = null;
 * }
 */

/**
 * @param {TreeLinkNode} root
 * @return {void} Do not return anything, modify tree in-place instead.
 */
var connect = function(root) {
    if (!root) {
        return;
    }
    connect(root.left);
    connect(root.right);
    var left = root.left, right = root.right;
    while (left && right) {
        left.next = right;
        left = left.right;
        right = right.left;
    }
};
