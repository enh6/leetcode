# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node.next:
            next = node.next
            val = next.val
            if next.next and next.next.val == val:
                next = next.next.next
                while next and next.val == val:
                    next = next.next
                node.next = next
            else:
                node = node.next
        return dummy.next