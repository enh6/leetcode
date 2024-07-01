# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = -10e8
        self.subPath(root)
        return self.max

    def subPath(self, root):
        if not root:
            return 0
        l = self.subPath(root.left)
        r = self.subPath(root.right)
        if root.val > self.max:
            self.max = root.val
        if l + root.val > self.max:
            self.max = l + root.val
        if root.val + r > self.max:
            self.max = root.val + r
        if l + root.val + r > self.max:
            self.max = l + root.val + r
        return max(l + root.val, r + root.val, root.val)
