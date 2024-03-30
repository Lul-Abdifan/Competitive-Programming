class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        self.tmp_matrix = [[0 for i in range(len(mat[0]) + 1)] for i in range(len(mat) + 1)]
        self.output =[]
        
        for i in range(1,len(mat) + 1):
            for j in range(1,len(mat[0]) + 1):
                no_matrix = mat[i - 1][j - 1]
                tmp_rside = self.tmp_matrix[i -1][j]
                tmp_lside = self.tmp_matrix[i][j - 1]
                tmp_upper_left = self.tmp_matrix[i - 1][j - 1]
                self.tmp_matrix[i][j] = no_matrix + tmp_rside + tmp_lside - tmp_upper_left
                
        for i in range(len(mat)):
            tmp_mat = []
            for j in range(len(mat[0])):
                row1 = max(i - k,0)
                col1 = max(j - k,0)
                row2 = min(len(mat) - 1,i + k)
                col2 = min(len(mat[0]) - 1,j + k)
                tmp_mat.append(self.sumRegion(row1,col1,row2,col2))
            self.output.append(tmp_mat)    
                
        return self.output        
                
       
       
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        no_point = self.tmp_matrix[row2 + 1][col2 + 1]
        upper_left = self.tmp_matrix[row1][col1]
        right_top = self.tmp_matrix[row1][col2 + 1]
        left_bottom = self.tmp_matrix[row2 + 1][col1]
        
        return no_point + upper_left - right_top -left_bottom     
       
       
        
        
        
      
      