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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        vector<TreeNode*> level;
        if (root) {
            level.push_back(root);
        }
        int level_num = 1;
        while (!level.empty()) {
            vector<int> level_vals;
            vector<TreeNode*> next_level;
            for (auto& node : level) {
                level_vals.push_back(node->val);
                if (node->left) {
                    next_level.push_back(node->left);
                }
                if (node->right) {
                    next_level.push_back(node->right);
                }
            }
            if (level_num % 2 == 0) {
                reverse(level_vals.begin(), level_vals.end());
            }
            ans.push_back(level_vals);
            level = next_level;
            level_num++;
        }
        return ans;
    }
};