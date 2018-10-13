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
    vector<vector<int>> ans;
    void pathSum(TreeNode* root, int sum, vector<int> path) {
        if (!root->left && !root->right) {
            if (sum == root->val) {
                path.push_back(sum);
                ans.push_back(path);
            }
            return;
        }
        path.push_back(root->val);
        if (root->left) {
            pathSum(root->left, sum - root->val, path);
        }
        if (root->right) {
            pathSum(root->right, sum - root->val, path);
        }
    }

    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        if (root) {
            pathSum(root, sum, vector<int>());
        }
        return ans;
    }
};
