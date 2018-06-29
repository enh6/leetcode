# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        return p.val == q.val \
            and self.isSameTree(p.left, q.left) \
            and self.isSameTree(p.right, q.right)