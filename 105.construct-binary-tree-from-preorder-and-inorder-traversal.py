# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:pos + 1], inorder[:pos])
        root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])
        return root