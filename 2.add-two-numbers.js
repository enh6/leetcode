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
var addTwoNumbers = function(l1, l2) {
    let sum = null, current = null;
    let carry = 0;
    while(l1 || l2 || carry) {
        let s = carry;
        if (l1) {
            s += l1.val;
            l1 = l1.next;
        }
        if (l2) {
            s += l2.val;
            l2 = l2.next;
        }
        if (s > 9) {
            s -= 10;
            carry = 1;
        } else {
            carry = 0;
        }
        if (sum === null) {
            current = new ListNode(s);
            sum = current;
        } else {
            current.next = new ListNode(s);
            current = current.next;
        }
    }
    return sum;
};