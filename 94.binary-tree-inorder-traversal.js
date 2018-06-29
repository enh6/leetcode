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