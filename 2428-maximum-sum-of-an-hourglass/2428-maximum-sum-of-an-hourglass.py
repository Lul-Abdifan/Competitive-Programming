class Solution:
        def maxSum(self, grid: List[List[int]]) -> int:
            cols = len(grid[0])
            rows = len(grid)
            max_hours_glass = float('-inf') 
            
            for i in range(rows - 2): 
                for j in range(cols - 2):  
                    tmp_max = 0

                    for k in range(i, i + 3):
                        for l in range(j, j + 3):
                            if k == i + 1 and (l == j or l == j + 2): 
                                continue
                            tmp_max += grid[k][l]

                    max_hours_glass = max(max_hours_glass, tmp_max)

            return max_hours_glass

