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
var reverseKGroup = function(head, k) {
    if (k == 1) {
        return head;
    }
    let dummy = new ListNode(0);
    let node = dummy;
    while (head) {
        let begin = head;
        let end = begin;
        head = head.next;
        for (let i = 1; i < k; i++) {
            if (!head) {
                end.next = null;
                let n = begin.next;
                begin.next = null;
                while (n) {
                    let new_n = n.next;
                    n.next = begin;
                    begin = n;
                    n = new_n;
                }
                node.next = begin;
                return dummy.next;
            }
            let new_head = head.next;
            head.next = begin;
            begin = head;
            head = new_head;
        }
        node.next = begin;
        node = end;
    }
    node.next = null;
    return dummy.next;
};