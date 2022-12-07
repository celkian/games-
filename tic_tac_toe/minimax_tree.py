from ttt_recombing_tree import *

class MiniMaxNode(Node):
    def __init__(self, game_state,perspective_player):
        super().__init__(game_state)
        self.minimax_value = None
        self.perspective_player = perspective_player
    

class MiniMaxTree(TicTacToeRecombiningTree): 
    def __init__(self, initial_board_state, perspective_player): 
        super().__init__()
        self.perspective_player = perspective_player
        self.initial_node = MiniMaxNode(initial_board_state, self.perspective_player)
    
    def generate_tree_from_state(self): 
    

        self.nodes[tuple(self.initial_node.game_state)] = self.initial_node
        queue = Queue()
        queue.enqueue(self.initial_node)
    
        while len(queue.items) != 0:

            current_node = queue.items[0]

            if current_node.winner == None: 
                avaliable_moves = current_node.remaining_moves()
                current_board = current_node.game_state

                for move in avaliable_moves: 
                    new_move_board = current_board.copy()
                    new_move_board[move] = current_node.upcoming_player
                    new_node = MiniMaxNode(new_move_board, self.perspective_player)
                    
                    if tuple(new_node.game_state) in self.nodes:
                        current_node.children.append(new_node)
                        continue
                    queue.enqueue(new_node)
                    new_node.parents = current_node
                    current_node.children.append(new_node)
                    self.nodes[tuple(new_node.game_state)] = new_node
                    
            queue.dequeue() 
        
        self.num_nodes = len(self.nodes)
   
    def terminal_states(self, node):
        if node.winner == node.perspective_player: 
            node.minimax_value = 1 
        elif node.winner == 'Tie': 
            node.minimax_value = 0
        else: 
            node.minimax_value = -1
        return
    
    def minimax_from_children(self, node, min_or_max): 

        children_minimax_values = []
        if node.children == []: 
            return
        for child in node.children: 
            self.assign_minimax_values(child)
            value = child.minimax_value
            children_minimax_values.append(value)
        return min_or_max(children_minimax_values)
    
    def assign_minimax_values(self, node):

        if node.children == []: 
            self.terminal_states(node)
            
        else: 
            if node.perspective_player == node.upcoming_player: 
                    node.minimax_value = self.minimax_from_children(node, max)
            else: 
                    node.minimax_value = self.minimax_from_children(node, min)



        


        
tree = MiniMaxTree([0, 0, 0, 0, 0, 0, 0, 0, 0], 1)

tree.generate_tree_from_state()
tree.assign_minimax_values(tree.initial_node)
for nodes in tree.nodes: 
    print(tree.nodes[nodes].print())
    print('minimax_value', tree.nodes[nodes].minimax_value)
