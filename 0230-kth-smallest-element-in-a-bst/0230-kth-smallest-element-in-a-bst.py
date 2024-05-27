# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        store = []

        def df(node):
            if not node:
                return 

            df(node.left)
            store.append(node.val)
            df(node.right)

        df(root)

        return store[k - 1]        
        