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
    ListNode* oddEvenList(ListNode* head) {
        if(!head || !head->next) {
            return head;
        }
        ListNode* even = head;
        ListNode* odd = head->next;
        ListNode* node = head->next->next;
        ListNode* odd_head = odd;
        while (node) {
            even->next = node;
            even = node;
            node = node->next;
            if (node) {
                odd->next = node;
                odd = node;
                node = node->next;
            }
        }
        even->next = odd_head;
        odd->next = nullptr;
        return head;
    }
};