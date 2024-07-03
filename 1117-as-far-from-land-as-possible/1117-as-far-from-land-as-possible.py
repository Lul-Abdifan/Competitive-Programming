class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    queue.append((i,j))
        if not queue or len(queue) == rows * cols:
            return -1            
        directions = [[0,-1],[0,1],[1,0],[-1,0]]
        is_bounded = lambda r,c : (0 <= r < rows) and (0 <= c < cols)
        while queue:
            row,col = queue.popleft()
            dis = grid[row][col]
            for x,y in directions:
                x_r,y_r = x + row,y + col
                
                if is_bounded(x_r,y_r) and grid[x_r][y_r] == 0:
                    queue.append((x_r,y_r))
                    grid[x_r][y_r] = dis + 1
        return dis - 1








        