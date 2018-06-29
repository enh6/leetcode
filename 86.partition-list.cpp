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
    ListNode* partition(ListNode* head, int x) {
        ListNode dummy_l(0);
        ListNode dummy_r(0);
        dummy_l.next = head;
        ListNode* node_l = &dummy_l;
        ListNode* node_r = &dummy_r;
        while (node_l->next) {
            if (node_l->next->val >= x) {
                node_r->next = node_l->next;
                node_r = node_r->next;
                node_l->next = node_l->next->next;
            } else {
                node_l = node_l->next;
            }
        }
        node_r->next = NULL;
        node_l->next = dummy_r.next;
        return dummy_l.next;
    }
};