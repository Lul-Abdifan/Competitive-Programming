class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        cols = len(mat[0])
        rows = len(mat)
        queue = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        is_bounded = lambda x,y:(0<= x< rows) and (0<= y < cols)

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    mat[i][j] = float('inf')
                if mat[i][j] == 0:
                    queue.append((i,j))
        while queue:
            r,c = queue.popleft()
            dist = mat[r][c]
            for x,y in directions:
                new_x = x + r
                new_y = y + c

                if is_bounded(new_x,new_y):
                    if mat[new_x][new_y] > dist + 1:
                        mat[new_x][new_y] = dist + 1
                        queue.append((new_x,new_y))
        return mat                






        