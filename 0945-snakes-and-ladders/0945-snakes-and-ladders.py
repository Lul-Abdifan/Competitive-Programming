class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def index_to_coordinates(index: int) -> (int, int):
            row = n - 1 - (index // n)
            col = index % n
            if (n - 1 - row) % 2 == 1:
                col = n - 1 - col
            return (row, col)
        
        visited = set()
        queue = deque([(1, 0)])
        
        while queue:
            current, moves = queue.popleft()
            
            if current == n * n:
                return moves
            
            for next_square in range(current + 1, min(current + 6, n * n) + 1):
                r, c = index_to_coordinates(next_square - 1)
                
                if board[r][c] != -1:
                    next_square = board[r][c]
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        return -1