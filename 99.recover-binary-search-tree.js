/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var recoverTree = function(root) {
    let first = null;
    let second = null;
    let prev = null;
    let traversal = function(root) {
        if (root == null) {
            return;
        }
        traversal(root.left);
        if (prev && root.val <= prev.val) {
            if (first == null) {
                first = prev;
            }
            second = root;
        }
        prev = root;
        traversal(root.right);
    }
    traversal(root);
    let tmp = first.val;
    first.val = second.val;
    second.val = tmp;
};