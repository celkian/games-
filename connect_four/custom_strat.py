class CustomPlayer: 

    def __init__(self): 
        self.player_num = None
        self.opposition = None
        self.open_columns = None
    
    def all_open_columns(self, board_copy):
        open_columns = []
        for i in range(7):
            list = [board_copy[j][i] for j in range(len(board_copy))]
            if list.count(list[0]) == len(list) and 0 not in list: 
                continue
            open_columns.append(i)
        self.open_columns = open_columns
    
    def determine_player_num(self, board):
        one_count = sum(x.count(1) for x in board)
        two_count = sum(x.count(2) for x in board) 
        if one_count == two_count: 
            self.player_num = 1 
        else: 
            self.player_num = 2
