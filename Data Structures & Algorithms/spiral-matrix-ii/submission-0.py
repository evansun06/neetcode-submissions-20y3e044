class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        [1,  2, 3, 4]
        [12,13,14, 5]
        [11,16,15, 6]
        [10 ,9, 8, 7]

        0,0,0,0,1,2,3,3,3,3,2,1
        1,1,2,2
        """
        matrix = [[0] * n for _ in range(n)]
        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]
        count = 1
        for i in range((n+1)//2):
        
            row, col = i,i
            print(i)
            if i == ((n+1)//2 - 1):
                matrix[row][col] = n*n
            
            for dr, dc in directions:
                for _ in range(n - 1 - i*2):
                    matrix[row][col] = count
                    row,col = row+dr, col+dc
                    count += 1
        return matrix

                    

            


