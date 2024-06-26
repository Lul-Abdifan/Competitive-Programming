class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if not grid:
            return 0

        def dfs(i,j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] != '1':
                   return
            grid[i][j] = '2'       
 

            dfs(i,j + 1)  
            dfs(i,j - 1)  
            dfs(i + 1,j)
            dfs(i - 1,j) 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    islands +=1
        return islands                
        