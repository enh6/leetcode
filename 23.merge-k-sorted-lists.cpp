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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return NULL;
        }
        auto cmp = [](ListNode* a, ListNode*b) {
            if (a && b) {
                return a->val > b->val;
            } else if (a) {
                return false;
            } else {
                return true;
            }
        };
        make_heap(lists.begin(), lists.end(), cmp);
        ListNode dummy(0);
        ListNode* node = &dummy;
        while (1) {
            pop_heap(lists.begin(), lists.end(), cmp);
            node->next = *lists.rbegin();
            if (node->next == NULL) {
                break;
            }
            *lists.rbegin() = node->next->next;
            push_heap(lists.begin(), lists.end(), cmp);
            node = node->next;
        }
        return dummy.next;
    }
};