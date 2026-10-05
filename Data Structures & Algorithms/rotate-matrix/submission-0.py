class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        n = len(matrix)
        (n+1)//2

        [1, 2, 3]
        [4, 5, 6]   
        [7, 8, 9]
        (0,0) -> (0,2) -> (2,2) -> (2,0)
        (0,1) -> (1,2) -> (2,1) -> (1,2)
        r = old_col
        c = n - 1 - old_row

        1 0
        0 1

        0  1
        -1 0
        """

        n = len(matrix)

        for i in range(n//2):
            for j in range(i, n - 1 - i):
                row, col = i, j
                prev = matrix[row][col]
                for _ in range(4):
                    new_row = col
                    new_col = n - 1 - row
                    temp = matrix[new_row][new_col]
                    matrix[new_row][new_col] = prev
                    prev = temp
                    row = new_row
                    col = new_col
