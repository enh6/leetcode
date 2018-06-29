# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        dummy = ListNode(0)
        node = dummy
        while head:
            begin = head
            end = begin
            head = head.next
            for _ in range(1, k):
                if not head:
                    end.next = None
                    n = begin.next
                    begin.next = None
                    while n:
                        new_n = n.next
                        n.next = begin
                        begin = n
                        n = new_n
                    node.next = begin
                    return dummy.next
                new_head = head.next
                head.next = begin
                begin = head
                head = new_head
            node.next = begin
            node = end
        node.next = None
        return dummy.next