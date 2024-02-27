class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        n = len(matrix)
        for i in range(n):
            for j in range(len(matrix[0])):
                row_set[i].add(matrix[i][j])
                col_set[j].add(matrix[i][j])
        
        for i in range(len(matrix)):
            if len(row_set[i]) != n or len(col_set[i]) != n:
                return False
                
        
        
        return True
        
        