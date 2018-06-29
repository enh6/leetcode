# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traversal(self, root):
        if not root:
            return
        self.traversal(root.left)
        if self.prev and root.val <= self.prev.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.traversal(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None
        self.traversal(root)
        tmp = self.first.val
        self.first.val = self.second.val
        self.second.val = tmp