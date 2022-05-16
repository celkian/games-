class Game: 
    def __init__(self, player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.players = {1: self.player_1, 2: self.player_2}
        self.board = [[0,0,0,0,0,0,0] for i in range(6)]
        self.winner = None


    def print(self):
        for i in range(6):
            print(self.board[i])

    def copy_board(self):
        copy_board =[]
        for rows in self.board: 
            copy_board.append(rows.copy())
        return copy_board
    
    def check_win_states(self): 
        #horizontal
        for i in range(6): 
            for j in range(4):
                if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] != 0: 
                    return self.board[i][j]

        #vertical
        for i in range(4): 
            for j in range(7):
                if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] != 0:
                    return self.board[i][j]

        
        #positive diagonals
        for i in range(4):
            for j in range(3, 6):
                if self.board[i][j] == self.board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] != 0:
                    return self.board[i][j]

        #negative diagonals
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] != 0:
                    return self.board[i][j]

       #tie
        flat_list =[]
        for rows in self.board: 
            for i in range(len(rows)): 
                flat_list.append(rows[i])
        
        if 0 not in flat_list: 
            return 'Tie'
        
        return False
    
    def colum_index_of_move(self,colum):
         

        







p1= 0
p2= 0
c4 = Game(p1,p2)
print(c4.open_columns())
        


