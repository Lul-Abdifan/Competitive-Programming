# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
         def df(node,val):
            if not node:
                return False
            val = val + node.val    
            if not node.left and not node.right:
                
                if val == targetSum:
                    return True
                
            

            
            return df(node.left,val) + df(node.right,val)   
         return df(root,0) 