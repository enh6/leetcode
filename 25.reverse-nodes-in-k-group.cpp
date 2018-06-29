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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (k == 1) {
            return head;
        }
        ListNode dummy(0);
        ListNode* node = &dummy;
        while (head) {
            ListNode* begin = head;
            ListNode* end = begin;
            head = head->next;
            for (int i = 1; i < k; i++) {
                if (!head) {
                    end->next = NULL;
                    ListNode* n = begin->next;
                    begin->next = NULL;
                    while (n) {
                        ListNode* new_n = n->next;
                        n->next = begin;
                        begin = n;
                        n = new_n;
                    }
                    node->next = begin;
                    return dummy.next;
                }
                ListNode* new_head = head->next;
                head->next = begin;
                begin = head;
                head = new_head;
            }
            node->next = begin;
            node = end;
        }
        node->next = NULL;
        return dummy.next;
    }
};