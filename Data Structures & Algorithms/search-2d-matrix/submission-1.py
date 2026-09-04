class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Brute force iteration O(m + n)

        Binary Search O(log(m + n))
        - matrix = m x n

        func(i) -> row, col
         col = i mod n
         row = i // n

        10 -> 2,2 
        """
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1
        mid = (left + right) // 2

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False

