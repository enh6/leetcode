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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder, int in_left, int post_left, int len) {
        if (len == 0) {
            return NULL;
        }
        int val = postorder[post_left + len - 1];
        TreeNode* root = new TreeNode(val);
        int root_pos;
        for (int i = in_left; i < in_left + len; i++) {
            if (inorder[i] == val) {
                root_pos = i;
                break;
            }
        }
        int left_len = root_pos - in_left;
        root->left = buildTree(inorder, postorder, in_left, post_left, left_len);
        root->right = buildTree(inorder, postorder, root_pos + 1, post_left + left_len, len - left_len - 1);
        return root;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return buildTree(inorder, postorder, 0, 0, inorder.size());
    }
};