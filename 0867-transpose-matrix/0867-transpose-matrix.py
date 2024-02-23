class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix) 
        cols = len(matrix[0]) 
        
        tmp_matrix = [[matrix[row][col] for row in range(rows)] for col in range(cols)]
    
        
        return tmp_matrix
        
        
        
          
        
        
        
        
