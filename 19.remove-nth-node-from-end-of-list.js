/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let n1 = head, n2 = head;
    while (--n) {
        n1 = n1.next;
    }
    if (n1.next == undefined) {
        return n2.next;
    }
    n1 = n1.next;
    while (n1.next) {
        n1 = n1.next;
        n2 = n2.next;
    }
    n2.next = n2.next.next;
    return head;
};