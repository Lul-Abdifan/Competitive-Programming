class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.tmp_matrix = [[0 for i in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        
            
        
        for i in range(1,len(matrix) + 1):
            for j in range(1,len(matrix[0]) + 1):
                no_matrix = matrix[i - 1][j - 1]
                tmp_rside = self.tmp_matrix[i -1][j]
                tmp_lside = self.tmp_matrix[i][j - 1]
                tmp_upper_left = self.tmp_matrix[i - 1][j - 1]
                self.tmp_matrix[i][j] = no_matrix + tmp_rside + tmp_lside - tmp_upper_left
        print(self.tmp_matrix)                                                 
                
                
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        no_point = self.tmp_matrix[row2 + 1][col2 + 1]
        upper_left = self.tmp_matrix[row1][col1]
        right_top = self.tmp_matrix[row1][col2 + 1]
        left_bottom = self.tmp_matrix[row2 + 1][col1]

        return no_point + upper_left - right_top - left_bottom

