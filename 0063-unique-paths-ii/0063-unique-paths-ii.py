class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        M, N = len(grid), len(grid[0])
        dp = [0] * N
        dp[N-1] = 1
        for r in range(M-1, -1, -1):
            for c in range(N-1, -1, -1):
                if grid[r][c] == 1: 
                    dp[c] = 0
                elif c < N - 1:
                    dp[c] = dp[c] + dp[c + 1]
                
        return dp[0]