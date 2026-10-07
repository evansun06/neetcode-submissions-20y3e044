class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        # n x m
        transpose = [[0] * m for _ in range(n)]

        for row in range(m):
            for col in range(n):
                transpose[col][row] = matrix[row][col]
        
        return transpose