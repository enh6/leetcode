/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

var path = function(root, sum, li, ans) {
    li = li.slice();
    li.push(root.val);
    if (!root.left && !root.right) {
        if (sum === root.val) {
            ans.push(li);
        }
        return;
    }
    sum = sum - root.val;
    if (root.left) {
        path(root.left, sum, li, ans);
    }
    if (root.right) {
        path(root.right, sum, li, ans);
    }
};

/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number[][]}
 */
var pathSum = function(root, sum) {
    var ans = []
    if (root) {
        path(root, sum, [], ans);
    }
    return ans;
};
