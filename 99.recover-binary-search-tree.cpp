/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* first;
    TreeNode* second;
    TreeNode* prev;

    void traversal(TreeNode* root) {
        if (root == NULL) {
            return;
        }
        traversal(root->left);
        if (prev && root->val <= prev->val) {
            if (first == NULL) {
                first = prev;
            }
            second = root;
        }
        prev = root;
        traversal(root->right);
    }

    void recoverTree(TreeNode* root) {
        traversal(root);
        swap(first->val, second->val);
    }
};