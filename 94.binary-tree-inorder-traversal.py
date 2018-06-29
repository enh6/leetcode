# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        s = []
        cur = root
        while cur or len(s) > 0:
            while cur:
                s.append(cur)
                cur = cur.left
            cur = s.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans