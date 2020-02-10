class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.board = [[0]*n for i in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 2:
            player = -1
        self.board[row][col] = player

        # check rows
        for r in range(self.n):
            sum_row = 0
            for c in range(self.n):
                sum_row += self.board[r][c]
            if (sum_row == player*self.n):
                if sum_row < 0:
                    return 2
                else:
                    return 1

        # check columns
        for c in range(self.n):
            sum_col = 0
            for r in range(self.n):
                sum_col += self.board[r][c]
            if (sum_col == player*self.n):
                if sum_col < 0:
                    return 2
                else:
                    return 1

        # check diags
        sum_diag = 0
        for i in range(self.n):
            sum_diag += self.board[i][i]
        if sum_diag == player*self.n:
            if sum_diag < 0:
                return 2
            else:
                return 1

        sum_diag_rev = 0
        i = self.n-1
        while(i >= 0):
            sum_diag_rev += self.board[self.n-1-i][i]
            i -= 1
        if sum_diag_rev == player*self.n:
            if sum_diag_rev < 0:
                return 2
            else:
                return 1

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
