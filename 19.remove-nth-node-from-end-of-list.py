# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        n1 = head
        n2 = head
        while n > 1:
            n1 = n1.next
            n -= 1
        if not n1.next:
            return n2.next
        n1 = n1.next
        while n1.next:
            n1 = n1.next
            n2 = n2.next
        n2.next = n2.next.next
        return head