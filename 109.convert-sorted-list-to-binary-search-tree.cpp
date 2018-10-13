/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode* sortedArrayToBST(vector<int>::const_iterator begin, vector<int>::const_iterator end) {
        if (begin == end) {
            return nullptr;
        }
        auto it = begin + (end - begin) / 2;
        TreeNode* root = new TreeNode(*it);
        root->left = sortedArrayToBST(begin, it);
        if (it + 1 != end) {
            root->right = sortedArrayToBST(it + 1, end);
        }
        return root;
    }
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> nums;
        while (head) {
            nums.push_back(head->val);
            head = head->next;
        }
        return sortedArrayToBST(nums.begin(), nums.end());
    }
};
