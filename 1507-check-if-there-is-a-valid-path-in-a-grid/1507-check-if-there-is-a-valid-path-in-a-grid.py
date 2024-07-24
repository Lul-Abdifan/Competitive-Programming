class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if not grid or not grid[0]:
            return False

        numRows, numCols = len(grid), len(grid[0])
        
        streetDirections = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        def isValidConnection(currentX, currentY, nextX, nextY):
            if not (0 <= nextX < numRows and 0 <= nextY < numCols):
                return False
            for dirX, dirY in streetDirections[grid[nextX][nextY]]:
                if nextX + dirX == currentX and nextY + dirY == currentY:
                    return True
            return False

        bfsQueue = deque([(0, 0)])
        visitedCells = set((0, 0))

        while bfsQueue:
            currentX, currentY = bfsQueue.popleft()
            if (currentX, currentY) == (numRows - 1, numCols - 1):
                return True
            for dirX, dirY in streetDirections[grid[currentX][currentY]]:
                nextX, nextY = currentX + dirX, currentY + dirY
                if (0 <= nextX < numRows and 0 <= nextY < numCols and 
                    (nextX, nextY) not in visitedCells and 
                    isValidConnection(currentX, currentY, nextX, nextY)):
                    visitedCells.add((nextX, nextY))
                    bfsQueue.append((nextX, nextY))

        return False