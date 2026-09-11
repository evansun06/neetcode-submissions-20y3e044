class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        staircase search
        - start at [0, len(matrix[0]) - 1]
        - if matrix[row][col] < target -> col -= 1
        - if matrix[row][col] > target -> row += 1
        - if row > len(matrix) or col < 0 -> return False
        """

        rows , cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        return False