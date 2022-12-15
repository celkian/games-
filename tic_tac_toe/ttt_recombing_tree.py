
class Node:

    def __init__(self, game_state): 
        self.game_state = game_state
        self.upcoming_player = self.upcoming_player()
        self.winner = self.check_win_states()
        self.parents = []
        self.children = []
        self.minimax_value = None
    
    def upcoming_player(self): 
        upcoming_player = 2
        if self.game_state.count(1) == self.game_state.count(2):
            upcoming_player = 1
        return upcoming_player 
    
    def print(self): 
         print(f'{self.game_state[0]} {self.game_state[1]} {self.game_state[2]}\n{self.game_state[3]} {self.game_state[4]} {self.game_state[5]}\n{self.game_state[6]} {self.game_state[7]} {self.game_state[8]}')

    def check_win_states(self):
    
        #rows
        if self.game_state[0] == self.game_state[1] == self.game_state[2] != 0: 
            return self.game_state[0]
        elif self.game_state[3] == self.game_state[4] == self.game_state[5] != 0: 
            return self.game_state[3]
        elif self.game_state[6] == self.game_state[7] == self.game_state[8] != 0: 
            return self.game_state[6]
        #columns
        elif self.game_state[0] == self.game_state[3] == self.game_state[6] != 0: 
            return self.game_state[0]
        elif self.game_state[1] == self.game_state[4] == self.game_state[7] != 0: 
            return self.game_state[1]
        elif self.game_state[2] == self.game_state[5] == self.game_state[8] != 0: 
            return self.game_state[2]
        #diagonals
        elif self.game_state[0] == self.game_state[4] == self.game_state[8] != 0: 
            return self.game_state[0]
        elif self.game_state[2] == self.game_state[4] == self.game_state[6] != 0: 
            return self.game_state[2]
        #cats_cradle
        elif 0 not in self.game_state: 
            return 'Tie'
        
        return None
    
    def remaining_moves(self): 
    
        avaliable_moves = []
        for i in range(9):
            if self.game_state[i] == 0:
                avaliable_moves.append(i)
        return avaliable_moves

    def assign_minimax_values(self): 
        if self.children == []:
            if self.winner == 1: 
                self.minimax_value = 1
            elif self.winner == 2: 
                self.minimax_value = -1 
            elif self.winner == 'Tie': 
                self.minimax_value = 0
        
        else: 
            children_minimax_values = []
            for children in self.children:

                value = self.assign_minimax_values(children)
                children_minimax_values.append(value)

            if self.upcoming_player == 1: 
                    self.minimax_value = max(children_minimax_values)
            else: 
                self.minimax_value = min(children_minimax_values)
class Queue:
    def __init__(self):
        self.items = [] 

    def print(self):
        print(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)


class TicTacToeRecombiningTree: 
    def __init__(self): 
        self.generate_tree()
        self.assign_minimax_values(self.root)
    
    def generate_tree(self): 
        self.nodes = {}
        empty_board = Node([0 for i in range(9)])
        self.root = empty_board
        self.nodes[tuple(empty_board.game_state)] = empty_board

        queue = Queue()
        queue.enqueue(empty_board)
    
        while len(queue.items) != 0:

            current_node = queue.items[0]

            if current_node.winner == None: 
                avaliable_moves = current_node.remaining_moves()
                current_board = current_node.game_state

                for move in avaliable_moves: 
                    new_move_board = current_board.copy()
                    new_move_board[move] = current_node.upcoming_player
                    #new_node = Node(new_move_board)
                    
                    if tuple(new_move_board) in self.nodes:
                        new_node = self.nodes[tuple(new_move_board)]
                        current_node.children.append(new_node)
                        new_node.parents.append(current_node)
                        continue
                    
                    new_node = Node(new_move_board)
                    new_node.parents.append(current_node)
                    current_node.children.append(new_node)
                    queue.enqueue(new_node)
                    self.nodes[tuple(new_node.game_state)] = new_node
                    
            queue.dequeue() 
        self.num_nodes = len(self.nodes)
    
    def assign_minimax_values(self, node):
        
        if node.children == []: 
            if node.winner == 1:
                node.minimax_value = 1
            elif node.winner == 2:
                node.minimax_value = -1
            elif node.winner == 'Tie':
                node.minimax_value = 0
        
        else:
            children_minimax_values = []
            #print("a" + str(len(node.children)))

            for child in node.children:
                self.assign_minimax_values(child)
                children_minimax_values.append(child.minimax_value)

            if node.upcoming_player == 1:
                node.minimax_value = max(children_minimax_values)
            else:
                node.minimax_value = min(children_minimax_values)
        
        return node.minimax_value



        
        
            

        

tree = TicTacToeRecombiningTree()

