from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        queue = deque()
        distance = float('inf')
        queue.append((entrance[0], entrance[1], 0))
        visited = set()
        visited.add((entrance[0], entrance[1]))
        is_bounded = lambda x, y: (0 <= x <= rows - 1) and (0 <= y <= cols - 1)
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        while queue:
            x, y, dist = queue.popleft()

            for rx, ry in directions:
                new_x, new_y = x + rx, y + ry
                if is_bounded(new_x, new_y) and maze[new_x][new_y] == '.' and (new_x, new_y) not in visited:
                    if (new_x == 0 or new_x == rows - 1 or new_y == 0 or new_y == cols - 1) and (new_x, new_y) != (entrance[0], entrance[1]):
                        return dist + 1
                    queue.append((new_x, new_y, dist + 1))
                    visited.add((new_x, new_y))

        return -1
