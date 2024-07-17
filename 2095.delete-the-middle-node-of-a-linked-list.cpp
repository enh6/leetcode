/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if (!head->next) {
            return nullptr;
        }
        ListNode* node = head;
        int n = 0;
        while (node) {
            node = node->next;
            n++;
        }
        n = n / 2;
        node = head;
        for (int i = 1; i < n; i++) {
            node = node->next;
        }
        node->next = node->next->next;
        return head;
    }
};