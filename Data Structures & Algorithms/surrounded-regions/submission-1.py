from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def bfs(coord):
            # returns:
            #  - wether the region is surrounded
            #  - the set of all coordinates in the region

            directions = [
                (0, 1), # right
                (1, 0), # down
                (0, -1),# left
                (-1, 0) # up
            ]

            visited = set([coord])
            q = deque([coord])

            while q:

                row, col = q.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (board[new_row][new_col] == "X") or (new_row, new_col) in visited:
                        continue

                    if (0 < new_row < len(board) - 1) and (0 < new_col < len(board[0]) - 1):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
                    else:
                        return False, None
            
            return True, visited
            
            


        
        for row in range(1, len(board) - 1):
            for col in range(1, len(board[0]) - 1):
                if board[row][col] == "O":
                    
                    isSurrounded, region = bfs((row, col))

                    if isSurrounded:
                        for i, j in region:
                            board[i][j] = "X"
                    
                    