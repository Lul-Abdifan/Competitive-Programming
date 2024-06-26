# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root and root.val > val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left,val)
        elif root and root.val < val:
                if root.right == None:
                    root.right = TreeNode(val)
                else:
                    self.insertIntoBST(root.right,val)
        if not root:
            root =  TreeNode(val)
        return root               






        