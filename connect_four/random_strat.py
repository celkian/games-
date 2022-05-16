import random

class Random_Strat: 
    def open_columns(self, board_copy):
        open_columns = []
        for i in range(7):
            list = [self.board[j][i] for j in range(len(board_copy))]
            if list.count(list[0]) == len(list) and 0 not in list: 
                continue
            open_columns.append(i)
        return open_columns
    
    def choose_move(self): 
        move = 0
        open_columns = self.open_columns(board_copy)
        move = randm.choice(open_columns)
        return move
