# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_l = ListNode(0)
        dummy_r = ListNode(0)
        dummy_l.next = head
        node_l = dummy_l
        node_r = dummy_r
        while node_l.next:
            if node_l.next.val >= x:
                node_r.next = node_l.next
                node_r = node_r.next
                node_l.next = node_l.next.next
            else:
                node_l = node_l.next
        node_r.next = None
        node_l.next = dummy_r.next
        return dummy_l.next