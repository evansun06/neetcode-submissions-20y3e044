# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        let m and n be the rows and cols of the matrix

        Simplest/Bruteforce: O(m*n)
        - obtain dimensions
        - iterate left to right via columns
        - return the column index when a 1 is hit

        Optimized Search via binary search per row. O(m * log(n))
        - if 1 is found at index 0 return
    
        """

        rows, cols = binaryMatrix.dimensions()

        result = float('inf')

        for row in range(rows):
            left, right = 0, cols - 1

            while left <= right:

                mid = (left + right) // 2

                candidate = binaryMatrix.get(row, mid)
                binaryMatrix.get(row, mid - 1)

                if candidate == 1:
                    if mid == 0:
                        return 0
                    elif binaryMatrix.get(row, mid - 1) == 0:
                        result = min(result, mid)
                        break
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
        
        return result if result != float('inf') else -1


    

