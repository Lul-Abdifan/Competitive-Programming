# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        q = deque([root])

        while q:
            dequed = q.popleft()
            if dequed.right:
                q.append(dequed.right)
            if dequed.left:    
                q.append(dequed.left)
        return dequed.val        
        # stack = [[root,1]]
        # leftMost = [0,root.left]

        # while stack:
        #     node,d = stack.pop(0)
        #     if d > leftMost[1]:
        #             leftMost[0] = node.val
        #             leftMost[1] = d

        #     if node.left:
        #        stack.append([node.left,d + 1])
               

                  
        #     if node.right:
        #         stack.append([node.right,d + 1])   
        # return leftMost[0]        
               
        