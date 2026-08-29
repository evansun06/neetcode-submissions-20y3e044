from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        Breath first search from a single island(all nodes)
        - O(n^2)

        - find all 1s in the island 
        - bfs to find entire island and initialize
        - multi-bfs to find the other island
        """
        n = len(grid)
        visited = set()
        q = deque()

        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        for i in range(n):
            initialized = False
            for j in range(n):
                if grid[i][j] == 1:

                    # bfs
                    _q = deque()
                    _q.append((i, j))
                    visited.add((i, j))

                    while _q:
                        row, col = _q.popleft()
                        # initialize future multi-bfs
                        q.append((row, col))

                        for dr, dc in directions:
                            new_row, new_col = row + dr, col + dc

                            if ((new_row, new_col) not in visited
                                and (0 <= new_row < n)
                                and (0 <= new_col < n)
                                and grid[new_row][new_col] == 1
                            ):
                                _q.append((new_row, new_col))
                                visited.add((new_row, new_col))
                    
                    initialized = True
                    break
            
            if initialized:
                break
        
        distance = 0

        while q:
            
            
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if ((new_row, new_col) not in visited
                        and (0 <= new_row < n)
                        and (0 <= new_col < n)
                    ):
                        if grid[new_row][new_col] == 1:
                            return distance
                        else:  
                            q.append((new_row, new_col))
                            visited.add((new_row, new_col))

            distance += 1

        return distance


        

        


        