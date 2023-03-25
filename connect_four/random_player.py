import random

class RandomPlayer: 
    def open_columns(self, board_copy):
        open_columns = []
        for i in range(7):
            list = [board_copy[j][i] for j in range(len(board_copy))]
            if list.count(list[0]) == len(list) and 0 not in list: 
                continue
            open_columns.append(i)
        return open_columns
    
    def choose_move(self,board_copy): 
        move = 0
        open_columns = self.open_columns(board_copy)
        move = random.choice(open_columns)
        return move
