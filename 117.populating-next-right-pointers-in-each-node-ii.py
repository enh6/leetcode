"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        head = tail = None
        while node:
            if node.left:
                if tail:
                    tail.next = node.left
                    tail = tail.next
                else:
                    head = tail = node.left
            if node.right:
                if tail:
                    tail.next = node.right
                    tail = tail.next
                else:
                    head = tail = node.right
            if node.next:
                node = node.next
            else:
                node = head
                head = tail = None
        return root
