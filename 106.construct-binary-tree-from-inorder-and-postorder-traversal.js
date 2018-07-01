/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    if (inorder.length == 0) {
        return null;
    }
    let val = postorder[postorder.length - 1];
    let root = new TreeNode(val);
    let pos = inorder.indexOf(val);
    root.left = buildTree(inorder.slice(0, pos), postorder.slice(0, pos));
    root.right = buildTree(inorder.slice(pos + 1), postorder.slice(pos, postorder.length - 1));
    return root;
};