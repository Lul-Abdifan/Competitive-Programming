# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def df(node,left,right):
            if not node:
                return True

            if node.val >= right or node.val <= left:
                return False


            return df(node.left,left,node.val) and df(node.right,node.val,right)
             
        
        return df(root,-float('inf'),float('inf'))     
        