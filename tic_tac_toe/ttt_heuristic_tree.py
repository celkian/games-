
class HeuristicNode:

    def __init__(self, game_state): 
        self.game_state = game_state
        self.upcoming_player = self.upcoming_player()
        self.winner = self.check_win_states()
        self.parents = []
        self.children = []
        self.heuristic_value = None
        self.depth = 0 
    
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
    
    def calc_heuristic_value(self): 
        board = self.game_state
        all_rows = [[self.game_state[0 + 3*i], self.game_state[1 + 3*i], self.game_state[2 + 3*i]] for i in range(0,3)]
        all_columns = [[self.game_state[0 + i], self.game_state[3 + i], self.game_state[6 + i]] for i in range(0,3)]
        all_diagonals = [[self.game_state[2], self.game_state[4], self.game_state[6]], [self.game_state[0],self.game_state[4],self.game_state[8]]]

        all_states = all_rows + all_columns + all_diagonals

        winner_counter = 0
        opponent_counter = 0

        for states in all_states: 
            state_value = self.check_if_state(states)
            if state_value == self.upcoming_player: 
                winner_counter += 1 
            elif state_value == False: 
               1 + 1 
            else: 
                opponent_counter += 1 

        return ((winner_counter - opponent_counter) / 8)
        
    
    def check_if_state(self, state): 
        if state[0] == state[1] != 0 and state[2] == 0: 
            return state[0]
        elif state[0] == state[2] != 0 and state[1] == 0: 
            return state[0]
        elif state[1] == state[2] != 0 and state[0] == 0: 
            return state[1]
        else: 
            return False

    def remaining_moves(self): 
    
        avaliable_moves = []
        for i in range(9):
            if self.game_state[i] == 0:
                avaliable_moves.append(i)
        return avaliable_moves

class Queue:
    def __init__(self):
        self.items = [] 

    def print(self):
        print(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

class TicTacToeHeuristicTree: 
    def __init__(self,game_state,ply): 
        self.ply = ply
        self.root = HeuristicNode(game_state)
        self.generate_tree()
        self.assign_heuristic_values(self.root)
    
    def generate_tree(self): 
        self.nodes = {}
        self.nodes[tuple(self.root.game_state)] = self.root

        queue = Queue()
        queue.enqueue(self.root)

        while len(queue.items) != 0:

            current_node = queue.items[0]
            if current_node.depth >= self.ply: 
                break

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
                        new_node.depth = current_node.depth + 1
                        continue

                    new_node = HeuristicNode(new_move_board)
                    new_node.depth = current_node.depth + 1
                    new_node.parents.append(current_node)
                    current_node.children.append(new_node)
                    queue.enqueue(new_node)
                    self.nodes[tuple(new_node.game_state)] = new_node
                    
            queue.dequeue() 
        self.num_nodes = len(self.nodes)
    
        
    def assign_heuristic_values(self, node):
        
        if node.children == []: 
            if node.winner == 1:
                node.heuristic_value = 1
            elif node.winner == 2:
                node.heuristic_value = -1
            elif node.winner == 'Tie':
                node.heuristic_value = 0
            else: 
                node.heuristic_value = node.calc_heuristic_value()
                
        
        else:
            children_heuristic_values = []

            for child in node.children:
                self.assign_heuristic_values(child)
                children_heuristic_values.append(child.heuristic_value)


            if node.upcoming_player == 1:
                node.heuristic_value = max(children_heuristic_values)
            else:
                node.heuristic_value = min(children_heuristic_values)
        
        return node.heuristic_value


tree = TicTacToeHeuristicTree([0,0,0,0,0,0,0,0], 1)

for nodes in tree.nodes: 
    print(tree.nodes[nodes].game_state)
    
        
