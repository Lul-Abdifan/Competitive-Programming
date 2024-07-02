# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adjList = defaultdict(list)
        visited = set()
        visited.add(target.val)
        queue = deque([(target.val,0)])
        def preorder(node,parent):
            if parent:
                adjList[node.val].append(parent.val)
                adjList[parent.val].append(node.val)
            if node.left:
                preorder(node.left,node)
            if node.right:
                preorder(node.right,node) 
        preorder(root,None)            
        print(adjList) 
        ans = []

        while queue:
            popped,dis = queue.popleft()
            if dis == k:
                ans.append(popped)
            
            for nm in adjList[popped]:
                    if nm not in visited:
                       visited.add(nm)
                       queue.append((nm,dis + 1))
        return ans               
                    
            