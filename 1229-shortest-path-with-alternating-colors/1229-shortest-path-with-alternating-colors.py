class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        r_adj = defaultdict(list)  
        b_adj = defaultdict(list)  
        
        for u, v in redEdges:
            r_adj[u].append(v)
        
        for u, v in blueEdges:
            b_adj[u].append(v)

        dist = [-1] * n  
        dist[0] = 0
        
        q = deque([(0, 0, 'R'), (0, 0, 'B')])  
        
        vis = {'R': set(), 'B': set()}  
        
        while q:
            node, length, clr = q.popleft()
            if clr == 'R':
                nxt_adj = b_adj
                nxt_clr = 'B'
            else:
                nxt_adj = r_adj
                nxt_clr = 'R'
            
            for nei in nxt_adj[node]:
                if (nei, nxt_clr) not in vis[nxt_clr]:
                    vis[nxt_clr].add((nei, nxt_clr))
                    q.append((nei, length + 1, nxt_clr))
                    if dist[nei] == -1:
                        dist[nei] = length + 1
        
        return dist