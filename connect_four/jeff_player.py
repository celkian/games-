import random as rng
import numpy as np
import time
class minimaxHeuristic:
    def __init__(self,player,depth):
        self.player = player
        self.depth = depth
        self.generate_new_tree(depth)

    #helper functions
    def generate_new_tree(self,depth):
        self.tree = CFourTree()
        self.tree.recursion_recombining_node_tree(depth)
        self.nodes_by_id = self.tree.nodes_by_id
        self.nodes_by_state = self.tree.nodes_by_state

    def sort_node_by_depth(self,nodes_by_id):
        max_depth = 0
        #finds max depth
        for node in nodes_by_id:
            if max(nodes_by_id[node].depth,max_depth) != max_depth:
                max_depth = nodes_by_id[node].depth
        #sorting
        nodes_by_depth = [[] for _ in range(max_depth + 1)]
        for node in nodes_by_id:
            node_depth = nodes_by_id[node].depth
            nodes_by_depth[node_depth].append(node)
        return nodes_by_depth
    
    def score_heuristic(self,board):
        #score stuff
        scores = [0,1,7,15,np.inf]
        total_points = 0
        #scores vertical
        if len(board) > 4:
            for i in range(0,len(board) - 3):
                for j in range(0,len(board[0])):
                    subboard = []
                    for a in range(4):
                        subboard.append(board[i+a][j])
                    total_points += scores[subboard.count(1)] * [1,-1][0]
                    total_points += scores[subboard.count(2)] * [1,-1][1] 
        #scores horizontal
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                subboard = board[i][j:j+4]
                total_points += scores[subboard.count(1)] * [1,-1][0]
                total_points += scores[subboard.count(2)] * [1,-1][1]
        #scores left diagonal 
        if len(board) > 4:
            for i in range(0,len(board) - 4):
                for j in range(0,len(board[0]) - 4):
                    subboard = []
                    for a in range(4):
                        subboard.append(board[i+a][j+a])
                    
                    total_points += scores[subboard.count(1)] * [1,-1][0]
                    total_points += scores[subboard.count(2)] * [1,-1][1]
        #scores right diagonal
        if len(board) > 4:
           for row in range(5,2,-1):
                for col in range(0,4):
                    subboard = [board[row][col],board[row-1][col+1], board[row-2][col+2], board[row-3][col+3]]
                    total_points += scores[subboard.count(1)] * [1,-1][0]
                    total_points += scores[subboard.count(2)] * [1,-1][1]
         
        return total_points 

    def add_new_layer(self,starting_node_id):
        self.nodes_by_depth = self.sort_node_by_depth(self.nodes_by_id)
        max_depth = len(self.nodes_by_depth)
        terminal_children = []
        all_children = []
        queue = [starting_node_id]
        #gets terminal children
        while len(queue) != 0:
            if self.nodes_by_id[queue[0]].children == []:
                terminal_children.append(queue[0])
            else:
                for child in self.nodes_by_id[queue[0]].children:
                    if child not in all_children:
                        all_children.append(child)
                        queue.append(child)
            queue.pop(0)
        #all terminal children found
        for child in terminal_children:
            if Game.is_end(self,self.tree.nodes_by_id[child].board) == False:
                last_move = self.tree.nodes_by_id[child].board
                node = self.tree.nodes_by_id[child]
                for i in Game.find_possible_moves(self,last_move):
                    turn = CFourTree.find_player_turn(self,last_move)
                    new_board = copy.deepcopy(last_move)
                    new_board = Game.update_board(self,new_board,i,turn)
                    if str(new_board) in self.tree.nodes_by_state:
                        duplicate_node_id = self.tree.nodes_by_state[str(new_board)]
                        self.tree.nodes_by_id[duplicate_node_id].parents.append(child)
                        node.children.append(duplicate_node_id)
                    else:
                        #finds max new node id
                        new_node_id = len(self.nodes_by_state)
                        #fits new node
                        self.tree.nodes_by_id[new_node_id] = Node(new_node_id,new_board,node.depth + 1)
                        self.tree.nodes_by_state[str(new_board)] = new_node_id
                        self.tree.nodes_by_id[new_node_id].parents.append(child)
                        node.children.append(new_node_id)

    def prune_tree(self,starting_id):
        pruned_tree = {}
        queue = [starting_id]
        while len(queue) != 0:
            pruned_tree[queue[0]] = self.tree.nodes_by_id[queue[0]]
            for child in self.tree.nodes_by_id[queue[0]].children:
                queue.append(child)
            queue.pop(0)
        self.tree.nodes_by_id = pruned_tree

    def find_last_move(self,board1,board2):
        for i in range(0,len(board1)):
            if board1[i] != board2[i]:
                for j in range(len(board1[i])):
                    if board1[i][j] != board2[i][j]:
                        return j


    #actual functions
    def fit(self):
        self.nodes_by_id = self.tree.nodes_by_id
        self.nodes_by_state = self.tree.nodes_by_state
        nodes_by_depth = self.sort_node_by_depth(self.nodes_by_id)
        #all heuristic values are appended here
        for state_id in nodes_by_depth[-1]:
            state = self.nodes_by_id[state_id]
            state_board = state.board
            current_node = self.nodes_by_id[self.nodes_by_state[str(state.board)]]
            turn = CFourTree.find_player_turn(self,state_board)
            current_node.value = self.score_heuristic(current_node.board) 
        for depth in range(len(nodes_by_depth)-2,-1,-1):
            for state_id in nodes_by_depth[depth]:
                state_node = self.nodes_by_id[state_id]
                if len(state_node.children) == 0:
                    turn = CFourTree.find_player_turn(self,state_node.board)
                    state_node.value = self.score_heuristic(state_node.board) 
                else:
                    #all minimax-values are appended here
                    turn = CFourTree.find_player_turn(self,state_node.board)
                    children_worth = []

                    for child in state_node.children:
                        children_worth.append(self.nodes_by_id[child].value)
                    state_node.value = max(children_worth) if turn == 1 else min(children_worth)

    def choose_move(self,current_state):
        #adds layer
        node_id = self.nodes_by_state[str(current_state)]
        if node_id != 0:
            self.add_new_layer(node_id)
            self.add_new_layer(node_id)
            self.prune_tree(node_id)
        self.fit()
        #gets children
        children = []
        children_value = []
        for child_id in self.nodes_by_id[node_id].children:
            children.append(child_id)
            if self.find_last_move(current_state,self.nodes_by_id[child_id].board) == 3:
                children_value.append(self.nodes_by_id[child_id].value)
            else:
                children_value.append(self.nodes_by_id[child_id].value)

        # for child in range(len(children_value)):
        #     print("-----")
        #     print("child is ", children[child])
        #     print("child has " + str(len(self.nodes_by_id[children[child]].children)) + " children")
        #     print("board is ", self.nodes_by_id[children[child]].board)
        #     print("heuristic value is ", children_value[child])
            

        #     print("-----")

        best_move = max(children_value) if self.player == 1 else min(children_value)
        move = children_value.index(best_move)
        best_node_id = self.nodes_by_id[node_id].children[move]
        last_move = self.find_last_move(current_state,self.nodes_by_id[best_node_id].board) 
        return last_move


#tests


import copy
"""
README FOR FORMATTING: 
    boards are stored as a 6 7 entry array
    children and parents are stored in ID's
    for recombining, nodes are in order of DFS
"""


class CFourTree:

    def find_player_turn(self,board):
        #index 0 is p1, index 1 is p2
        moves_by_player = [0,0]
        for row in board:
            for index in row:
                if index == 1:
                    moves_by_player[0] += 1
                elif index == 2:
                    moves_by_player[1] += 1
        return 1 if moves_by_player[0] == moves_by_player[1] else 2
        
    def recursion_recombining_node_tree(self, remaining_depth = 6, node_id = 0):
        if node_id == 0:
            self.nodes_by_id = {}
            self.nodes_by_id[0] = Node(0,[[0 for i in range(7)] for i in range(6)])
            self.nodes_by_state = {}
            self.nodes_by_state[str([[0 for i in range(7)] for i in range(6)])] = 0
        board = copy.deepcopy(self.nodes_by_id[node_id].board)
        if remaining_depth != 0 and Game.is_end(self,board) == False:
            #setup stuff
            node = self.nodes_by_id[node_id]
            last_state = copy.copy(node.board)
            player_to_move = self.find_player_turn(last_state)
            #children
            for possible_move in Game.find_possible_moves(self,last_state):
                possible_state = Game.update_board(self,copy.deepcopy(last_state),possible_move,player_to_move)
                if str(possible_state) not in self.nodes_by_state:
                    new_id = len(self.nodes_by_id) 
                    self.nodes_by_id[new_id] = Node(new_id,possible_state,node.depth + 1)
                    self.nodes_by_state[str(possible_state)] = new_id
                    self.nodes_by_id[new_id].parents.append(node_id)
                    self.nodes_by_id[node_id].children.append(new_id)
                    self.recursion_recombining_node_tree(remaining_depth-1,new_id)

                else:
                    #deal with all of the parent remapping here
                    duplicate_id = self.nodes_by_state[str(possible_state)]
                    self.nodes_by_id[duplicate_id].parents.append(node_id)
                    node.children.append(duplicate_id)


class Node:
    def __init__(self,node_id,board,depth = 0):
        self.id = node_id
        self.board = board
        self.parents = []
        self.children = []
        self.depth = depth


"""
copy is used just for copy nest, instead of copy_nest function
time is used for debugging purposes
"""
import copy
import time

class Game:

    def __init__(self,player_one, player_two):
        self.players = [player_one,player_two]
        self.turn = 0
        self.board = [[0 for i in range(7)] for i in range(6)]

    def print_board(self):
        for row in self.board:
            print(row)
        print('')
    

    def update_board(self,board,col,turn):
        for row in range(5,-1,-1):
            if board[row][col] == 0:
                board[row][col] = turn
                return board
        
        self.print_board()
        print("invalid move, turn skipped")
        print("player is ",self.turn)
        print('move was made by ',self.players)
        return board


    def make_move(self):
        self.turn = self.turn %2 + 1
        player = self.players[self.turn - 1]
        board_copy = copy.copy(self.board)
        player_move = player.choose_move(board_copy)
        self.board = self.update_board(board_copy,player_move,int(self.turn))

    def find_possible_moves(self,board):
        possible_moves = []
        for i in range(len(board[0])):
            if board[0][i] == 0:
                possible_moves.append(i)
        return possible_moves
                

    def is_end(self,board):
        #horizontal
        for row in range(0,6):
            for col in range(0,4):
                last_piece = board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row][col+1] == board[row][col+2] == board[row][col+3]:
                    return str(last_piece)
        #vertical
        for row in range(0,3):
            for col in range(0,7):
                last_piece = board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row+1][col] == board[row+2][col] == board[row+3][col]:
                    return str(last_piece)
        #diagonal (\)
        for row in range(0,3):
            for col in range(0,4):
                last_piece = board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]:
                    return str(last_piece)
        #diagonal (/)
        for row in range(5,2,-1):
            for col in range(0,4):
                last_piece = board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]:
                    return str(last_piece)
        for row in board:
            if 0 in row:
                return False
        return 'Tie'

    def game(self,log = False):
        while True:
            if log == True:
                print(self.turn)
                self.print_board()
            start = time.time()
            if self.is_end(copy.copy(self.board)) != False:
                return self.is_end(copy.copy(self.board))
            self.make_move()
            elapsed = time.time() - start
            if elapsed > 1:
                print('player ', self.turn, " took ",elapsed ,"seconds")
        
            