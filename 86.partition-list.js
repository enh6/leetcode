/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    let dummy_l = new ListNode(0);
    let dummy_r = new ListNode(0);
    dummy_l.next = head;
    let node_l = dummy_l;
    let node_r = dummy_r;
    while (node_l.next) {
        if (node_l.next.val >= x) {
            node_r.next = node_l.next;
            node_r = node_r.next;
            node_l.next = node_l.next.next;
        } else {
            node_l = node_l.next;
        }
    }
    node_r.next = null;
    node_l.next = dummy_r.next;
    return dummy_l.next;
};