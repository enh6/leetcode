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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder, int pre_left, int in_left, int len) {
        if (len == 0) {
            return NULL;
        }
        int val = preorder[pre_left];
        TreeNode* root = new TreeNode(val);
        int root_pos;
        for (int i = in_left; i < in_left + len; i++) {
            if (inorder[i] == val) {
                root_pos = i;
                break;
            }
        }
        int left_len = root_pos - in_left;
        root->left = buildTree(preorder, inorder, pre_left + 1, in_left, left_len);
        root->right = buildTree(preorder, inorder, pre_left + 1 + left_len, root_pos + 1, len - left_len - 1);
        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buildTree(preorder, inorder, 0, 0, preorder.size());
    }
};