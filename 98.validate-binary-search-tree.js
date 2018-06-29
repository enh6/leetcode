/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    let ans = [];
    let s = [];
    let cur = root;
    while (cur || s.length > 0) {
        while (cur) {
            s.push(cur);
            cur = cur.left;
        }
        cur = s.pop();
        ans.push(cur.val);
        cur = cur.right;
    }
    return ans;
};

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    let values = inorderTraversal(root);
    for (let i = 1; i < values.length; i++) {
        if (values[i] <= values[i - 1]) {
            return false;
        }
    }
    return true;
};