from c4_tree import *
from game import *
from random_strat import *
import random

class HeuristicPlayer:
    def __init__(self,ply): 
        self.ply = ply
        self.tree = C4HeuristicTree(ply)
        self.nodes = self.tree.nodes
        self.prune_depth = 0
        self.add_depth = ply

    def choose_move(self, board):
        board_node = self.nodes[tuple([tuple(board[i]) for i in range(6)])]

        if board == [[0,0,0,0,0,0,0] for i in range(6)]: 
            return 3
       
        self.tree.assign_heuristic_values(board_node)

        children_heuristic_values_dict = {tuple([tuple(children.game_state[i]) for i in range(6)]) : children.heuristic_value for children in board_node.children}
        
        if len(children_heuristic_values_dict) == 0: 
            return random.choice(board_node.remaining_columns())

        if board_node.upcoming_player == 1: 
            best_move_board = list(max(children_heuristic_values_dict, key=children_heuristic_values_dict.get))
        else: 
            best_move_board = list(min(children_heuristic_values_dict, key=children_heuristic_values_dict.get))
        
        current_board = board_node.game_state

        best_move_index = 0
        for i in range(9): 
            if current_board[i] != best_move_board[i]: 
                best_move_index = i 
                return best_move_index
        
        #self.tree.prune_layer(self.prune_depth)
        self.tree.add_layer(self.add_depth)
        #self.prune_depth += 1
        self.add_depth += 1



game = ConnectFour(HeuristicPlayer(6), RandomStrat())
game.run(True)

#don't think its updating the nodes correctly 