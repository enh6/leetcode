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
    vector<TreeNode*> genTrees(int start, int end) {
        vector<TreeNode*> trees;
        if (start > end) {
            trees.push_back(NULL);
            return trees;
        }
        for (int i = start; i <= end; i++) {
            auto left_trees = genTrees(start, i - 1);
            auto right_trees = genTrees(i + 1, end);
            for (auto left_tree : left_trees) {
                for (auto right_tree : right_trees) {
                    TreeNode* tree = new TreeNode(i);
                    tree->left = left_tree;
                    tree->right = right_tree;
                    trees.push_back(tree);
                }
            }
        }
        return trees;
    }
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) {
            return {};
        }
        return genTrees(1, n);
    }
};