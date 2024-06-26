# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def bfs():
            visited = set()
            
            queue = deque([root])
            
            node_val = root.val
            while queue:
                
                node = queue.popleft()

                if node.val != node_val:
                        return False

                if node not in visited:
                    visited.add(node)
                

                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right) 
            return True
        return bfs()    




                 



        