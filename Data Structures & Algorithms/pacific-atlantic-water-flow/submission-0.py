from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        def bfs(starts):
            q = deque(starts)
            visited = set(starts)

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    
                    new_row = row + dr
                    new_col = col + dc

                    if (
                        0 <= new_row < len(heights)
                        and 0 <= new_col < len(heights[0])
                        and (new_row, new_col) not in visited
                        and heights[new_row][new_col] >= heights[row][col]
                    ):
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))
            
            return visited
    
        pacific_border = []
        atlantic_border = []

        for row in range(len(heights)):
            pacific_border.append((row, 0))
            atlantic_border.append((row, len(heights[0]) - 1))

        for col in range(len(heights[0])):
            pacific_border.append((0, col))
            atlantic_border.append(((len(heights) - 1), col))
        
        pacific = bfs(pacific_border)
        atlantic = bfs(atlantic_border)

        return [list(cell) for cell in pacific & atlantic]
            


        