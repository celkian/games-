import random

class LastMinutePlayer: 
    def choose_move(self, board): 

        self.rows = [board[i] for i in range(len(board))]
        self.columns = [[rows[i] for rows in board] for i in range(7)]

        move = self.check_win_or_block_states(board)

        if move != None: 
            return move

        else: 
            open_columns = self.open_columns(board)
            move = random.choice(open_columns)
            return move

    def check_win_or_block_states(self, board): 
        is_move_posible = False
        
        for horizontal in self.rows: 
            for i in range(4): 
                #2220
                if horizontal[0 + i] == horizontal[1 + i] == horizontal[2+i] != 0 and horizontal[3+i] == 0: 
                    is_move_posible = True
                    move = 3 + i 
                    return move

                #0222
                elif horizontal[0 + i] == 0 and horizontal[1 + i] == horizontal[2 + i] == horizontal[3 + i] != 0: 
                    is_move_posible = True
                    move = 0 + i 
                    return move
                #2202
                elif horizontal[0 + i] == horizontal[1 + i] == horizontal[3 + i] != 0 and  horizontal[2 + i] == 0: 
                    is_move_posible = True
                    move = 2 + i 
                    return move
                
                #2022
                elif horizontal[0 + i] == horizontal[2 + i] == horizontal[3 + i] != 0 and  horizontal[1 + i] == 0: 
                    is_move_posible = True
                    move = 1 + i 
                    return move

        
        for vertical in self.columns: 
            for i in range(3): 
                #0222
                if vertical[0 + i] == 0 and vertical[1 + i] == vertical[2 + i] == vertical[3 + i] != 0: 
                    is_move_posible = True
                    move = self.columns.index(vertical)
                    return move

        return None

    def open_columns(self, board_copy):
        open_columns = []
        for i in range(7):
            list = [board_copy[j][i] for j in range(len(board_copy))]
            if list.count(list[0]) == len(list) and 0 not in list: 
                continue
            open_columns.append(i)
        return open_columns