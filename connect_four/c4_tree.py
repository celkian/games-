import copy

class C4Node:

    def __init__(self, game_state):
        self.game_state = game_state
        self.upcoming_player = self.upcoming_player()
        self.winner = self.check_win_states()
        self.parents = []
        self.children = []
        self.depth = 0

    def upcoming_player(self):
        upcoming_player = 2
        flattened_board = sum(self.game_state, [])
        if flattened_board.count(1) == flattened_board.count(2):
            upcoming_player = 1
        return upcoming_player

    def print(self):
        for i in range(6):
            print(self.game_state[i])

    def check_win_states(self):
        # horizontal
        for i in range(4):
            for j in range(6):
                if self.game_state[j][i] == self.game_state[j][i+1] == self.game_state[j][i+2] == self.game_state[j][i+3] != 0:
                    return self.game_state[j][i]

        # vertical
        for i in range(7):
            for j in range(3):
                if self.game_state[j][i] == self.game_state[j+1][i] == self.game_state[j+2][i] == self.game_state[j+3][i] != 0:
                    return self.game_state[j][i]

        # positive diagonals
        for i in range(4):
            for j in range(3):
                if self.game_state[j][i] == self.game_state[j+1][i+1] == self.game_state[j+2][i+2] == self.game_state[j+3][i+3] != 0:
                    return self.game_state[j][i]

        # negative diagonals
        for i in range(4):
            for j in range(3, 6):
                if self.game_state[j][i] == self.game_state[j-1][i+1] == self.game_state[j-2][i+2] == self.game_state[j-3][i+3] != 0:
                    return self.game_state[j][i]

       # tie
        flat_list = []
        for rows in self.game_state:
            for i in range(len(rows)):
                flat_list.append(rows[i])

        if 0 not in flat_list:
            return 'Tie'

    def remaining_columns(self):
        open_columns = [i for i in range(7)]
        for i in range(7):
            nonzero_column_values = [self.game_state[j][i] for j in range(6) if self.game_state[j][i] != 0]
            if len(nonzero_column_values) == 6:
                open_columns.remove(i)

        return open_columns
    
    def copy_of_copies(self): 
        new_copy = []
        for rows in self.game_state: 
            new_copy.append(rows.copy())
        
        return new_copy


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
    def __init__(self, game_state, ply):
        self.root = C4Node(game_state)
        self.ply = ply
        self.generate_tree()

    def generate_tree(self): 
        self.nodes = {}
        self.nodes[tuple([tuple(self.root.game_state[i]) for i in range(6)])] = self.root

        queue = Queue()
        queue.enqueue(self.root)

        while len(queue.items) != 0:

            current_node = queue.items[0]
            if current_node.depth >= self.ply: 
                break

            if current_node.winner == None: 
                avaliable_columns = current_node.remaining_columns()
                current_board = current_node.game_state

                for column in avaliable_columns: 

                    new_move_board = current_node.copy_of_copies()
                    new_move_row_index = self.row_index_of_move(column, new_move_board)
                    new_move_board[new_move_row_index][column] = current_node.upcoming_player
                    new_move_tuple_board = tuple([tuple(new_move_board[i]) for i in range(6)])
                    
                    if new_move_tuple_board in self.nodes:
                        new_node = self.nodes[new_move_tuple_board]
                        current_node.children.append(new_node)
                        new_node.parents.append(current_node)
                        new_node.depth = current_node.depth + 1
                        continue

                    new_node = C4Node(new_move_board)
                    new_node.depth = current_node.depth + 1
                    new_node.parents.append(current_node)
                    current_node.children.append(new_node)
                    queue.enqueue(new_node)
                    self.nodes[new_move_tuple_board] = new_node
                    
            queue.dequeue() 
        self.num_nodes = len(self.nodes)
    
    def row_index_of_move(self, move, board):
        for i in range(6):
            row = 5-i
            if board[row][move] == 0:
                return row


test = [[0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]

tree = C4HeuristicTree(test,3)

for nodes in tree.nodes: 
        tree.nodes[nodes].print()
        print()

print('num nodes', tree.num_nodes)

