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
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0);
        ListNode* node = &dummy;
        while (head && head->next) {
            ListNode* new_head = head->next->next;
            node->next = head->next;
            node = node->next;
            node->next = head;
            node = node->next;
            head = new_head;
        }
        if (head) {
            node->next = head;
        } else {
            node->next = NULL;
        }
        return dummy.next;
    }
};