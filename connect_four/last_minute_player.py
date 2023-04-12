class LastMinutePlayer: 
    def choose_move(self, board): 
        return
    
    def check_win_states(self, board):
        # horizontal
        for i in range(4):
            for j in range(6):
                if board[j][i] == board[j][i+1] == board[j][i+2] == board[j][i+3] != 0:
                    return board[j][i]

        # vertical
        for i in range(7):
            for j in range(3):
                if board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i] != 0:
                    return board[j][i]

        # positive diagonals
        for i in range(4):
            for j in range(3):
                if board[j][i] == board[j+1][i+1] == board[j+2][i+2] == board[j+3][i+3] != 0:
                    return board[j][i]

        # negative diagonals
        for i in range(4):
            for j in range(3, 6):
                if board[j][i] == board[j-1][i+1] == board[j-2][i+2] == board[j-3][i+3] != 0:
                    return board[j][i]

       # tie
        flat_list = []
        for rows in board:
            for i in range(len(rows)):
                flat_list.append(rows[i])

        if 0 not in flat_list:
            return 'Tie'