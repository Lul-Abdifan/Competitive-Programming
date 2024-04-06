class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        cols = len(matrix[0])
        rows = len(matrix)
        
        prefix_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                top = prefix_matrix[i - 1][j] if i > 0 else 0
                left = prefix_matrix[i][j - 1] if j > 0 else 0
                top_left = prefix_matrix[i - 1][j - 1] if i > 0 and j > 0 else 0
                prefix_matrix[i][j] = top + left - top_left + matrix[i][j]
                
        no_of_numSubmatrix = 0
        
        for row1 in range(rows):
            for row2 in range(row1, rows):
                initial_state = defaultdict(int)
                initial_state[0] = 1
                
                for col in range(cols):
                    current_sum = prefix_matrix[row2][col] - (prefix_matrix[row1 - 1][col] if row1 > 0 else 0)
                    no_of_numSubmatrix += initial_state[current_sum - target]
                    initial_state[current_sum] += 1
        
        return no_of_numSubmatrix