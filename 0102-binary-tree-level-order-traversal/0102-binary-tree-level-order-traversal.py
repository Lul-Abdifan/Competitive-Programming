

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        

            
            results = []
            if not root:
                return results
            queue = deque()
            queue.append(root)
            

            while queue:
                res = []
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node:
                        res.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                if res:
                    results.append(res)
            return results

                    
                    







            
            