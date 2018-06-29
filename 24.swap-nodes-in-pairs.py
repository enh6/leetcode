# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        node = dummy
        while head and head.next:
            new_head = head.next.next
            node.next = head.next
            node = node.next
            node.next = head
            node = node.next
            head = new_head
        if head:
            node.next = head
        else:
            node.next = None
        return dummy.next