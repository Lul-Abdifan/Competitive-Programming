from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.list = []


    def inOrder(self, root: Optional[TreeNode]):
        if root is None:
            return

        self.inOrder(root.left)
        self.list.append(root.val)
        self.inOrder(root.right)

    def BST(self, start: int, end: int) -> Optional[TreeNode]:
        if start > end:
            return None

        mid = start + (end - start) // 2

        root = TreeNode(self.list[mid])
        root.left = self.BST(start, mid - 1)
        root.right = self.BST(mid + 1, end)

        return root

    # Drive code
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inOrder(root)
        return self.BST(0, len(self.list) - 1)
