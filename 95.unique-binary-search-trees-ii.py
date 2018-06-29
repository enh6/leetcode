# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        def genTrees(start, end):
            trees = []
            if start > end:
                trees.append(None)
                return trees
            for i in range(start, end + 1):
                left_trees = genTrees(start, i - 1)
                right_trees = genTrees(i + 1, end)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        tree = TreeNode(i)
                        tree.left = left_tree
                        tree.right = right_tree
                        trees.append(tree)
            return trees
        return genTrees(1, n)