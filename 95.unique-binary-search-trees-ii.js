/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number} n
 * @return {TreeNode[]}
 */
var generateTrees = function(n) {
    let genTrees = function(start, end) {
        let trees = [];
        if (start > end) {
            trees.push(null);
            return trees;
        }
        for (let i = start; i <= end; i++) {
            let left_trees = genTrees(start, i - 1);
            let right_trees = genTrees(i + 1, end);
            for (let j = 0; j < left_trees.length; j++) {
                for (let k = 0; k < right_trees.length; k++) {
                    let tree = new TreeNode(i);
                    tree.left = left_trees[j];
                    tree.right = right_trees[k];
                    trees.push(tree);
                }
            }
        }
        return trees;
    };
    return genTrees(1, n);
};