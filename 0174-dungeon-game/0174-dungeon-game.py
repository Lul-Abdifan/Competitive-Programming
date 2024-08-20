class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        test = [[0] * m for _ in range(n)]
        
        y = -dungeon[n-1][m-1] + 1
        test[n-1][m-1] = 1 if y <= 0 else y
        
        for i in range(m-2, -1, -1):
            x = test[n-1][i+1] - dungeon[n-1][i]
            test[n-1][i] = 1 if x <= 0 else x
        
        for i in range(n-2, -1, -1):
            x = test[i+1][m-1] - dungeon[i][m-1]
            test[i][m-1] = 1 if x <= 0 else x
        
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                curr = dungeon[i][j]
                right = test[i][j+1]
                down = test[i+1][j]
                x = min(right, down) - curr
                test[i][j] = 1 if x <= 0 else x
        
        return test[0][0]
        