# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirror(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 and node2:
            return False
        elif node1 and not node2:
            return False
        else:
            return node1.val == node2.val and \
                self.isMirror(node1.left, node2.right) and \
                self.isMirror(node1.right, node2.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)