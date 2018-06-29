# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = None
        current = None
        carry = 0
        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            if s > 9:
                s -= 10
                carry = 1
            else:
                carry = 0
            if sum:
                current.next = ListNode(s)
                current = current.next
            else:
                sum = ListNode(s)
                current = sum
        return sum
