from enum import Enum

class BoardState(Enum):
    EMPTY = 0,
    X = 1,
    O = 2

class TicTacToe:

    def __init__(self, n: int):
        self.board = [[BoardState.EMPTY] * n for _ in range(n)]
        self.size = n
        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if self._isWinningMove(row, col, player):
            return player
        else:
            return 0
    
    def _isWinningMove(self, row:int, col:int, player:int) -> bool:
        horizontal_win = True
        vertical_win = True
        pos_diag_win = True
        neg_diag_win = True

        for i in range(self.size):
            if self.board[row][i] != player:
                horizontal_win = False
            if self.board[i][col] != player:
                vertical_win = False
        
        # move placed on negative center diagonal
        if row - col == 0:
            for i in range(self.size):
                if self.board[i][i] != player:
                    neg_diag_win = False
        else:
            neg_diag_win = False
        
        # move placed on positive center diagonal
        if row + col == self.size - 1:
            for i in range(self.size):
                if self.board[i][self.size - 1 - i] != player:
                    pos_diag_win = False
        else:
            pos_diag_win = False

        return (horizontal_win
            or vertical_win
            or neg_diag_win
            or pos_diag_win
        )
    

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
