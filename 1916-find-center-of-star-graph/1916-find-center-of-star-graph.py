class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjacent_list = {vertex:[] for vertex in range(1,len(edges) + 2)}
       

        for edge in edges:
            u,v = edge
            adjacent_list[u].append(v)
            adjacent_list[v].append(u)

        for l in adjacent_list:
            if len(adjacent_list[l]) == len(edges):
                return l
                



        