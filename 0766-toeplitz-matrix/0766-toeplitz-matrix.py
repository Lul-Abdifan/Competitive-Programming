class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(len(matrix)):
            n = len(matrix[i])
            for j in range(n):
                if j + 1 < n and i + 1 < len(matrix): 
                    if matrix[i + 1][j + 1] != matrix[i][j]:
                        return False
        return True            
               
                
        
        