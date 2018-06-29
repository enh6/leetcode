/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    let dummy = new ListNode(0);
    dummy.next = head;
    let node = dummy;
    while (node.next) {
        let next = node.next;
        let val = next.val;
        if (next.next && next.next.val == val) {
            next = next.next.next;
            while (next && next.val == val) {
                next = next.next;
            }
            node.next = next;
        } else {
            node = node.next;
        }
    }
    return dummy.next;
};