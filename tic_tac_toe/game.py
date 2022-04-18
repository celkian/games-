import random

class Game: 
    def __init__(self, player_1, player_2, log): 
        self.player_1 = player_1
        self.player_2 = player_2
        self.players = {1: self.player_1, 2: self.player_2}
        self.board = [0 for i in range(9)]
        self.winner = None 
        self.log = log

    def print(self): 
         print(f'{self.board[0]} {self.board[1]} {self.board[2]}\n{self.board[3]} {self.board[4]} {self.board[5]}\n{self.board[6]} {self.board[7]} {self.board[8]}')
    
    def move_validity(self, move):
        if self.board[move] != 0: 
            return False
        else: 
            return True

    def win_states_check(self):
        #rows
        if self.board[0] == self.board[1] == self.board[2] != 0: 
            return self.board[0]
        elif self.board[3] == self.board[4] == self.board[5] != 0: 
            return self.board[3]
        elif self.board[6] == self.board[7] == self.board[8] != 0: 
            return self.board[6]
        #columns
        elif self.board[0] == self.board[3] == self.board[6] != 0: 
            return self.board[0]
        elif self.board[1] == self.board[4] == self.board[7] != 0: 
            return self.board[1]
        elif self.board[2] == self.board[5] == self.board[8] != 0: 
            return self.board[2]
        #diagonals
        elif self.board[0] == self.board[4] == self.board[8] != 0: 
            return self.board[0]
        elif self.board[2] == self.board[4] == self.board[6] != 0: 
            return self.board[2]
        #cats_cradle
        elif 0 not in self.board: 
            return 'Tie'
    
    def run(self):

        self.current_player_num = 1
        print(self.current_player_num)

        while self.winner == None: 
            board_copy = self.board.copy()
            current_player = self.players[self.current_player_num]
            upcoming_move = current_player.choose_move(board_copy)

            if isinstance(upcoming_move, tuple):
                upcoming_move = upcoming_move[0] * 3 + upcoming_move[1]

        

            move_validity = self.move_validity(upcoming_move)
            if move_validity == True:
                self.board[upcoming_move] += self.current_player_num

            if self.log == True: 
                print("player moving is player", self.current_player_num)
                print("move made is to spot ",upcoming_move )
                self.print()
            
            if self.current_player_num == 1: 
                self.current_player_num = 2
            elif self.current_player_num == 2: 
                self.current_player_num = 1
            
            self.winner = self.win_states_check()
            
        
        print("final game state")
        self.print()
    
        return self.winner


