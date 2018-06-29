# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        array = []
        for list in lists:
            while list:
                array.append(list.val)
                list = list.next
        array.sort()
        dummy = ListNode(0)
        node = dummy
        for val in array:
            node.next = ListNode(val)
            node = node.next
        return dummy.next