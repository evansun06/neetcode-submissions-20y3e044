class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        self.prefix_sum = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):

                total = matrix[r][c]

                if r - 1 >= 0:
                    total += self.prefix_sum[r-1][c]
                if c - 1 >= 0:
                    total += self.prefix_sum[r][c-1]
                if r - 1 >= 0 and c - 1 >= 0:
                    total -= self.prefix_sum[r-1][c-1]
                
                self.prefix_sum[r][c] = total
       
        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r_i, c_i = row2, col1 - 1
        r_j, c_j = row1-1, col2
        r_k, c_k = row1-1, col1-1

        i = self.prefix_sum[r_i][c_i] if c_i >= 0 else 0
        j = self.prefix_sum[r_j][c_j] if r_j >= 0 else 0
        k = self.prefix_sum[r_k][c_k] if r_k >= 0 and c_k >= 0 else 0

        return self.prefix_sum[row2][col2] - i - j + k
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)