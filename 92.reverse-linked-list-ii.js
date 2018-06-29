/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function(head, m, n) {
    if (m == n) {
        return head;
    }
    n = n - m;
    let node = head;
    let left_tail = null;
    while (--m) {
        left_tail = node;
        node = node.next;
    }
    let mid_tail = node;
    let right_head = node.next;
    while (n--) {
        let last_node = node;
        node = right_head;
        right_head = right_head.next;
        node.next = last_node;
    }
    mid_tail.next = right_head;
    if (!left_tail) {
        return node;
    }
    left_tail.next = node;
    return head;
};