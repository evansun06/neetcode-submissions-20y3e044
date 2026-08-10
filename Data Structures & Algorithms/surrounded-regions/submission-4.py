class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs():
            for r in range(ROWS):
                for c in range(COLS):
                    if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == 'O' and (r, c):
                        queue.append((r, c))
                    

            while queue:
                r, c = queue.popleft()
                board[r][c] = 'T'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == 'O':
                        queue.append((nr, nc))
        
        bfs()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
                