class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 0,0   0,1   0,2   0,3
        # 1,0   1,1   1,2   1,3
        # 2,0   2,1   2,2   2,3
        # 3,0   3,1   3,2   3,3
        # positive diagonal = col - row
        # negative diagonal = col + row

        cols = set()
        p_diags = set()
        n_diags = set()

        result = []
        board = [["."] * n for _ in range(n)]

        def dfs(row):
            # traverse down rows
            if row == n:
                res = ["".join(row) for row in board.copy()]
                result.append(res)
                return

            for col in range(n):
                p_diag = row + col
                n_diag = row - col
                    
                if col in cols or p_diag in p_diags or n_diag in n_diags:
                    continue

                cols.add(col)
                p_diags.add(p_diag)
                n_diags.add(n_diag)
                board[row][col] = "Q"
                
                dfs(row + 1)
                
                cols.remove(col)
                p_diags.remove(p_diag)
                n_diags.remove(n_diag)
                board[row][col] = "."
        
        dfs(0)
        return result
                
                
                
                
                




