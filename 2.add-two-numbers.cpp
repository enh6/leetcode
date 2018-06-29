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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* sum = nullptr;
        ListNode* current = nullptr;
        int carry = 0;
        while(l1 || l2 || carry) {
            int s = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
            if (s > 9) {
                s -= 10;
                carry = 1;
            } else {
                carry = 0;
            }
            if (current == nullptr) {
                current = new ListNode(s);
                sum = current;
            } else {
                current->next = new ListNode(s);
                current = current->next;
            }
            if (l1) {
                l1 = l1->next;
            }
            if (l2) {
                l2 = l2->next;
            }
        }
        return sum;
    }
};