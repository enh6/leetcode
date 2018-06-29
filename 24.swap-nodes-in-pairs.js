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
var swapPairs = function(head) {
    let dummy = new ListNode(0);
    let node = dummy;
    while (head && head.next) {
        let new_head = head.next.next;
        node.next = head.next;
        node = node.next;
        node.next = head;
        node = node.next;
        head = new_head;
    }
    if (head) {
        node.next = head;
    } else {
        node.next = null;
    }
    return dummy.next;
};