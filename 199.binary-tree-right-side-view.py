# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        nodes = [root]
        while nodes:
            result.append(nodes[0].val)
            next_layer = []
            for n in nodes:
                if n.right:
                    next_layer.append(n.right)
                if n.left:
                    next_layer.append(n.left)
            nodes = next_layer
        return result
