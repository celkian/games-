from ttt_heuristic_tree import *
from game import *
from random_player import RandomPlayer

class HeuristicPlayer:
    def __init__(self,ply): 
        self.ply = ply

    def choose_move(self, board):
        tree = TicTacToeHeuristicTree(board, self.ply)
        board_node = tree.root

        children_heuristic_values_dict = {tuple(children.game_state) : children.heuristic_value for children in board_node.children}

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
