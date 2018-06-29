/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* node = &dummy;
        while (node->next) {
            ListNode* next = node->next;
            int val = next->val;
            if (next->next && next->next->val == val) {
                next = next->next->next;
                while (next && next->val == val) {
                    next = next->next;
                }
                node->next = next;
            } else {
                node = node->next;
            }
        }
        return dummy.next;
    }
};