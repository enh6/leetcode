# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = []

    def path(self, root, sum, li):
        if not root.left and not root.right:
            if sum == root.val:
                li.append(sum)
                self.ans.append(li)
            return
        if root.left:
            self.path(root.left, sum - root.val, li + [root.val])
        if root.right:
            self.path(root.right, sum - root.val, li + [root.val])

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root:
            self.path(root, sum, [])
        return self.ans;
