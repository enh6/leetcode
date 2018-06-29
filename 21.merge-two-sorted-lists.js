/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    let dummy = new ListNode(0);
    let l = dummy;
    while (l1 && l2) {
        if (l1.val < l2.val) {
            l.next = l1;
            l1 = l1.next;
        } else {
            l.next = l2;
            l2 = l2.next;
        }
        l = l.next;
    }
    while (l1) {
        l.next = l1;
        l1 = l1.next;
        l = l.next;
    }
    while (l2) {
        l.next = l2;
        l2 = l2.next;
        l = l.next;
    }
    return dummy.next;
};