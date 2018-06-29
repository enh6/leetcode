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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (m == n) {
            return head;
        }
        n = n - m;
        ListNode* node = head;
        ListNode* left_tail = NULL;
        while (--m) {
            left_tail = node;
            node = node->next;
        }
        ListNode* mid_tail = node;
        ListNode* right_head = node->next;
        while (n--) {
            ListNode* last_node = node;
            node = right_head;
            right_head = right_head->next;
            node->next = last_node;
        }
        mid_tail->next = right_head;
        if (!left_tail) {
            return node;
        }
        left_tail->next = node;
        return head;
    }
};