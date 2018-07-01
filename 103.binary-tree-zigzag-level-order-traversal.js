/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
    let ans = [];
    let level = [];
    if (root) {
        level.push(root);
    }
    level_num = 1;
    while (level.length > 0) {
        let level_vals = [];
        let next_level = [];
        for (let i = 0; i < level.length; i++) {
            level_vals.push(level[i].val);
            if (level[i].left) {
                next_level.push(level[i].left);
            }
            if (level[i].right) {
                next_level.push(level[i].right);
            }
        }
        if (level_num % 2 == 0) {
            level_vals.reverse();
        }
        ans.push(level_vals);
        level = next_level;
        level_num++;
    }
    return ans;
};