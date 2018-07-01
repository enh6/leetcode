# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        level = []
        if root:
            level.append(root)
        while level:
            level_vals = []
            next_level = []
            for node in level:
                level_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            ans.append(level_vals)
            level = next_level
        ans.reverse()
        return ans