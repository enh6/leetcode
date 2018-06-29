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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* n1 = head, *n2 = head;
        while (--n) {
            n1 = n1->next;
        }
        if (n1->next == NULL) {
            return n2->next;
        }
        n1 = n1->next;
        while (n1->next) {
            n1 = n1->next;
            n2 = n2->next;
        }
        n2->next = n2->next->next;
        return head;
    }
};