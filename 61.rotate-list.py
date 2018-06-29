# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        l = 1
        tail = head
        while tail.next != None:
            tail = tail.next
            l += 1
        k = k % l
        if k == 0:
            return head
        k = l - k
        tail.next = head
        for _ in range(1, k):
            head = head.next
        new_head = head.next
        head.next = None
        return new_head