
class ConnectFour: 
    def __init__(self, player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.players = {1: self.player1, 2: self.player2}
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
        for i in range(4):
            for j in range(6):
                if self.board[j][i] == self.board[j][i+1] == self.board[j][i+2] == self.board[j][i+3] != 0:
                    return self.board[j][i]

        #vertical
        for i in range(7):
            for j in range(3):
                if self.board[j][i] == self.board[j+1][i] == self.board[j+2][i] == self.board[j+3][i] != 0:
                    return self.board[j][i]

        #positive diagonals 
        for i in range(4):
            for j in range(3):
                if self.board[j][i] == self.board[j+1][i+1] == self.board[j+2][i+2] == self.board[j+3][i+3] != 0:
                    return self.board[j][i]

        #negative diagonals
        for i in range(4):
            for j in range(3, 6):
                if self.board[j][i] == self.board[j-1][i+1] == self.board[j-2][i+2] == self.board[j-3][i+3] != 0:
                    return self.board[j][i]

       #tie
        flat_list =[]
        for rows in self.board: 
            for i in range(len(rows)): 
                flat_list.append(rows[i])
        
        if 0 not in flat_list: 
            return 'Tie'   
    
    def move_validity(self, move): 
        for i in range(6): 
            if self.board[i][move] == 0: 
                return True 
        return False

    def row_index_of_move(self, move):
        for i in range(6): 
            row = 5-i
            if self.board[row][move] == 0:
                return row 
    
    def run(self, log=False): 
        self.log = log
        self.current_player_num = 1
        while self.winner == None: 
            copy_board = self.copy_board()
            current_player = self.players[self.current_player_num]
            upcoming_column_move = current_player.choose_move(copy_board)
            move_row_index = self.row_index_of_move(upcoming_column_move)

            if self.move_validity(upcoming_column_move) == True: 
                self.board[move_row_index][upcoming_column_move] += self.current_player_num
            
            if self.log == True: 
                print('move coordinates made is',(move_row_index, upcoming_column_move))
                self.print()
            
            if self.current_player_num == 1: 
                self.current_player_num = 2
            elif self.current_player_num == 2: 
                self.current_player_num = 1
            
            self.winner = self.check_win_states()

            if self.winner != None:
                print("final game state")
                self.print()
                print('winner was player', self.winner)
        return self.winner

         

    

 


