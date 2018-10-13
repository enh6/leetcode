/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST2 = function(nums) {
    if (nums.length === 0) {
        return null;
    }
    var middle = nums.length >> 1;
    var root = new TreeNode(nums[middle]);
    root.left = sortedArrayToBST2(nums.slice(0, middle));
    root.right = sortedArrayToBST2(nums.slice(middle + 1));
    return root;
};

/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    var nums = [];
    while (head) {
        nums.push(head.val);
        head = head.next;
    }
    return sortedArrayToBST2(nums);
};
