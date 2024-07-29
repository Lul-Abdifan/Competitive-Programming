class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        dead = set(deadends)
        q = deque([("0000", 0)])
        vis = set("0000")
        
        while q:
            cur, t = q.popleft()
            
            if cur == target:
                return t
            
            for i in range(4):
                for d in [-1, 1]:
                    n = (int(cur[i]) + d) % 10
                    nxt = cur[:i] + str(n) + cur[i+1:]
                    
                    if nxt not in vis and nxt not in dead:
                        vis.add(nxt)
                        q.append((nxt, t + 1))
        
        return -1
