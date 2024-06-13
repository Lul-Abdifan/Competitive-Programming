class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_vertex = defaultdict(int)
        out_vertex = defaultdict(int)



        for edge in trust:
            u,v = edge
            in_vertex[u] +=1   
            out_vertex[v] +=1
        print(in_vertex)
        print(out_vertex)    
        ans = -1
        for i in range(1,n + 1):
            if in_vertex[i] == 0 and out_vertex[i] == n - 1:
                ans = i
        
        return ans 


        