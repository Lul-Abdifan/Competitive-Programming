class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        pre_product = 1
        
        forth_prefix = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        back_prefix = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        prefix = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                forth_prefix[row][col] = pre_product
                pre_product = (pre_product * grid[row][col])%12345
                
        pre_product = 1        
        for row in range(len(grid) - 1,-1,-1):
            for col in range(len(grid[0]) - 1,-1,-1):
                back_prefix[row][col] = pre_product
                pre_product = (pre_product * grid[row][col])%12345
       
    
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                prefix[row][col] = (forth_prefix[row][col] * back_prefix[row][col])%12345
      
    
        
        return prefix
        