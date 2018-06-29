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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL) {
            return NULL;
        }
        int l = 1;
        ListNode* tail = head;
        while (tail->next) {
            tail = tail->next;
            l++;
        }
        k = k % l;
        if (k == 0) {
            return head;
        }
        k = l - k;
        tail->next = head;
        while (--k) {
            head = head->next;
        }
        ListNode* new_head = head->next;
        head->next = NULL;
        return new_head;
    }
};