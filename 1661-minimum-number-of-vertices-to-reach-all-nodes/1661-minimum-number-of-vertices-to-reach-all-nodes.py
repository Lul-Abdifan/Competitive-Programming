class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        in_vertex = set()
        out_vertex = set()

        for edge in edges:
            u,v = edge


            in_vertex.add(u)   
            out_vertex.add(v)
        res = []

        for v_in in in_vertex:
            if v_in not in out_vertex:
                res.append(v_in)
        return res           


        