# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root):
        def helper(node, p, gp):
            if not node:
                return 0

            s = 0
            if gp is not None and gp % 2 == 0:
                s += node.val

            s += helper(node.left, node.val, p)
            s += helper(node.right, node.val, p)

            return s

        return helper(root, None, None)
