from collections import deque

class Solution:
    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        def count_adjacent_mines(row, col):
            count = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    count += 1
            return count
        
       
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        # BFS
        queue = deque([(click[0], click[1])])
        
        while queue:
            row, col = queue.popleft()
            
          
            mines_count = count_adjacent_mines(row, col)
            
            if mines_count > 0:
                
                board[row][col] = str(mines_count)
            else:
              
                board[row][col] = 'B'
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'E':
                        queue.append((nr, nc))
                        board[nr][nc] = 'B'  
        
        return board


board = [["E","E","E","E","E"],
         ["E","E","M","E","E"],
         ["E","E","E","E","E"],
         ["E","E","E","E","E"]]
click = [3, 0]

solution = Solution()
updated_board = solution.updateBoard(board, click)
print(updated_board)
