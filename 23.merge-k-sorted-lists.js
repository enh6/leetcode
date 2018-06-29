/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    let array = [];
    for (let i = 0; i < lists.length; i++) {
        let node = lists[i];
        while (node !== null) {
            array.push(node.val);
            node = node.next;
        }
    }
    array.sort(function(a, b) {
        return a - b;
    })
    let dummy = new ListNode(0);
    let node = dummy;
    for (let i = 0; i < array.length; i++) {
        node.next = new ListNode(array[i]);
        node = node.next;
    }
    return dummy.next;
};