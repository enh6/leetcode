/**
 * // Definition for a Node.
 * function Node(val,left,right,next) {
 *    this.val = val;
 *    this.left = left;
 *    this.right = right;
 *    this.next = next;
 * };
 */
/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function(root) {
    var node = root;
    var head = null, tail = null;
    while (node) {
        if (node.left) {
            if (tail) {
                tail.next = node.left;
                tail = tail.next;
            } else {
                head = tail = node.left;
            }
        }
        if (node.right) {
            if (tail) {
                tail.next = node.right;
                tail = tail.next;
            } else {
                head = tail = node.right;
            }
        }
        if (node.next) {
            node = node.next;
        } else {
            node = head;
            head = tail = null;
        }
    }
    return root;
};
