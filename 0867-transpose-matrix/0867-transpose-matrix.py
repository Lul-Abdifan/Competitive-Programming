class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix) 
        cols = len(matrix[0]) 
        

        
        tmp_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
        
        for row in range(rows):
            for col in range(cols):
                tmp_matrix[col][row] = matrix[row][col]
                
        
        return tmp_matrix
        
        
        
        
        
        