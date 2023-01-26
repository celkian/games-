class C4Node:

    def __init__(self, game_state): 
        self.game_state = game_state
        self.upcoming_player = self.upcoming_player()
        self.winner = self.check_win_states()
        self.parents = []
        self.children = []
    
    def upcoming_player(self): 
        upcoming_player = 2
        if self.game_state.count(1) == self.game_state.count(2):
            upcoming_player = 1
        return upcoming_player 
    
    def print(self):
        for i in range(6):
            print(self.game_state[i])

    def check_win_states(self): 
        #horizontal
        for i in range(4):
            for j in range(6):
                if self.game_state[j][i] == self.game_state[j][i+1] == self.game_state[j][i+2] == self.game_state[j][i+3] != 0:
                    return self.game_state[j][i]

        #vertical
        for i in range(7):
            for j in range(3):
                if self.game_state[j][i] == self.game_state[j+1][i] == self.game_state[j+2][i] == self.game_state[j+3][i] != 0:
                    return self.game_state[j][i]

        #positive diagonals 
        for i in range(4):
            for j in range(3):
                if self.game_state[j][i] == self.game_state[j+1][i+1] == self.game_state[j+2][i+2] == self.game_state[j+3][i+3] != 0:
                    return self.game_state[j][i]

        #negative diagonals
        for i in range(4):
            for j in range(3, 6):
                if self.game_state[j][i] == self.game_state[j-1][i+1] == self.game_state[j-2][i+2] == self.game_state[j-3][i+3] != 0:
                    return self.game_state[j][i]

       #tie
        flat_list =[]
        for rows in self.game_state: 
            for i in range(len(rows)): 
                flat_list.append(rows[i])
        
        if 0 not in flat_list: 
            return 'Tie'   

    def remaining_columns(self): 
        open_columns = []
        for i in range(7): 
            nonzero_column_values = [self.game_state[j][i] for j in range(6) if self.game_state[j][i] != 0]
            if len(nonzero_column_values) < 


class Queue:
    def __init__(self):
        self.items = [] 

    def print(self):
        print(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)


class C4HeuristicTree: 
    def __init__(self,game_state,ply):
        self.game_state = game_state
        self.ply = ply

    #def generate_tree(self): 

