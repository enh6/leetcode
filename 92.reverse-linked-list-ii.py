class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        n = n - m
        node = head
        left_tail = None
        for _ in range(m - 1):
            left_tail = node
            node = node.next
        mid_tail = node
        right_head = node.next
        for _ in range(n):
            last_node = node
            node = right_head
            right_head = right_head.next
            node.next = last_node
        mid_tail.next = right_head
        if not left_tail:
            return node
        left_tail.next = node
        return head