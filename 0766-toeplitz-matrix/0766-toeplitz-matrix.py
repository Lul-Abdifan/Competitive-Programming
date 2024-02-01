class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(len(matrix) - 1):
            n = len(matrix[i])
            for j in range(n - 1):
                    if matrix[i + 1][j + 1] != matrix[i][j]:
                        return False
        return True            
               
                
        
        