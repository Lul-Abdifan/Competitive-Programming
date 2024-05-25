# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

       

        def df(node,cur):
            if not node:
               return 0
            
            cur = cur*10 + node.val

            if not node.left and not node.right:
                return cur
            else:
                return df(node.left,cur) + df(node.right,cur)

        return df(root,0)                
        