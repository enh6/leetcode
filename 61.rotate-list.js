/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    if (head == null) {
        return null;
    }
    let l = 1;
    let tail = head;
    while (tail.next) {
        tail = tail.next;
        l++;
    }
    k = k % l;
    if (k == 0) {
        return head;
    }
    k = l - k;
    tail.next = head;
    while (--k) {
        head = head.next;
    }
    let new_head = head.next;
    head.next = null;
    return new_head;
};