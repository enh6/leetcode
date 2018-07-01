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
    bool isSymmetric(TreeNode* node1, TreeNode* node2) {
        if (!node1 && !node2) {
            return true;
        } else if (!node1 && node2) {
            return false;
        } else if (node1 && !node2) {
            return false;
        } else {
            return node1->val == node2->val &&
                isSymmetric(node1->left, node2->right) &&
                isSymmetric(node1->right, node2->left);
        }
    }

    bool isSymmetric(TreeNode* root) {
        if (!root) {
            return true;
        }
        return isSymmetric(root->left, root->right);
    }
};