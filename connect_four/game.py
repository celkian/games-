class Game: 
    def __init__(self, player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[0,0,0,0,0,0,0] for i in range(6)]

    def print(self):
        for i in range(6):
            print(self.board[i])

    def copy_board(self):
        copy_board =[]
        for rows in self.board: 
            copy_board.append(rows.copy())
        return copy_board
    
    def check_win_states(self): 
        



player1=0
player2 = 0
c4 = Game(player1,player2)
c4.print()
