
import time
import pickle


class HeuristicMinimaxStrategy:
    def __init__(self, n: int, save_heuristic_values: bool):
        # self.generate_tree([[0 for _ in range(7)] for _ in range(6)], n)
        self.get_pickled_cache()
        # self.time = self.propagate_minimax_values()
        self.n = n
        self.save_heuristic_values = save_heuristic_values

    def get_pickled_cache(self):
        try:
            with open('heuristic_values.pickle', 'rb') as f:
                self.calculated_heuristic_values = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.calculated_heuristic_values = {}

        self.need_to_update_pickle = False

    def generate_tree(self, board_state, n):
        if (not hasattr(self, "tree")) or board_state == [[0 for _ in range(7)] for _ in range(6)]\
              or sum([row.count(1) for row in board_state]) == 1 != sum([row.count(2) for row in board_state])\
              or self.n == 1:
            self.tree = ConnectFourRecombiningTreeCustomDepth(board_state, n)
        else:
            self.tree.generate_tree_using_cache(board_state)
        self.node_dict = self.tree.node_dict
        self.terminal_nodes = self.tree.terminal_nodes
        # this fixes 3-ply sucking; old minimax values were being retained for some reason, so the new ones weren't being propagated to all nodes
        # i should probably figure out a better way to implement this, but it works for now
        for state in self.node_dict:
            if state not in self.terminal_nodes and hasattr(self.node_dict[state], "minimax_value"):
                del self.node_dict[state].minimax_value

    def propagate_minimax_values(self):
        start = time.time()
        game_states_to_propagate = Queue()
        for node in self.terminal_nodes:
            node.minimax_value = {
                1: 9999, 2: -9999, 'Tie': 0}[node.winner] if node.winner is not None else self.assign_heuristic_value(node.state)
            if self.tree.deeptuple(node.state) not in self.calculated_heuristic_values and self.save_heuristic_values:
                print('updating cache dict')
                self.need_to_update_pickle = True
                self.calculated_heuristic_values[self.tree.deeptuple(node.state)] = node.minimax_value
                print(len(self.calculated_heuristic_values))
            for parent_node in node.parents:
                game_states_to_propagate.enqueue(parent_node.state)

        while game_states_to_propagate.contents != []:
            # tuple because the keys in self.node_dict can't be lists
            game_state_to_propagate = self.tree.deeptuple(
                game_states_to_propagate.dequeue())
            current_node = self.node_dict[game_state_to_propagate]
            if hasattr(current_node, 'minimax_value'):
                continue
            children_all_have_values = True
            minimax_values_of_children = []
            for child_node in current_node.children:
                if not hasattr(child_node, 'minimax_value'):
                    children_all_have_values = False
                    break
                minimax_values_of_children.append(child_node.minimax_value)
            if children_all_have_values is False:
                continue
            if current_node.turn == 1:
                current_node.minimax_value = max(minimax_values_of_children)
            else:
                current_node.minimax_value = min(minimax_values_of_children)

            for parent_node in current_node.parents:
                if hasattr(parent_node, 'minimax_value'):
                    continue
                game_states_to_propagate.enqueue(parent_node.state)
        end = time.time()
        return end - start

    def choose_move(self, board):
        start = time.time()

        board = board[::-1]

        self.current_board_state = board
        self.generate_tree(board, self.n)
        propagation_time = self.propagate_minimax_values()
        print('after propagation: cache dict length is', len(self.calculated_heuristic_values))

        if board == [[0 for _ in range(7)] for _ in range(6)]:
            self.player = 1
            return 3
        elif sum([row.count(1) for row in board]) == 1 != sum([row.count(2) for row in board]):
            self.player = 2
            return 2

        # in order to look up in self.node_dict; lists aren't hashable
        board = self.tree.deeptuple(board)
        current_node = self.node_dict[board]
        if self.player == 1:
            goal_node = max(current_node.children,
                            key=lambda node: node.minimax_value)
        else:
            goal_node = min(current_node.children,
                            key=lambda node: node.minimax_value)

        if goal_node.winner is not None and  self.save_heuristic_values:
            with open('heuristic_values.pickle', 'wb') as f:
                print('updating pickle')
                print(len(self.calculated_heuristic_values))
                pickle.dump(self.calculated_heuristic_values,
                            f, pickle.HIGHEST_PROTOCOL)

        for j in range(7):  # check for which column was changed i.e. i want to move in
            if [board[i][j] for i in range(6)] != [goal_node.state[i][j] for i in range(6)]:
                end = time.time()
                if end - start >= 1:
                    print(end - start)
                    print('propagation', propagation_time)
                return j

    def assign_heuristic_value(self, board):
        tuple_of_board = self.tree.deeptuple(board)
        if tuple_of_board in self.calculated_heuristic_values:
            return self.calculated_heuristic_values[tuple_of_board]
        print('encountered new game state, calculating heuristic value')
        return self.calculate_heuristic_value(board)

    def calculate_heuristic_value(self, board):
        heuristic_value = 0
        for i in range(6):
            for j in range(4):
                horizontal = board[i][j:j + 4]
                if (horizontal.count(1) == 3 or horizontal.count(2) == 3) and horizontal.count(0) == 1:
                    heuristic_value += {3: 0.9, 0: -0.9}[horizontal.count(1)]
                elif (horizontal.count(1) == 2 or horizontal.count(2) == 2) and horizontal.count(0) == 2:
                    heuristic_value += {2: 0.3, 0: -0.3}[horizontal.count(1)]
                elif (horizontal.count(1) == 1 or horizontal.count(2) == 1) and horizontal.count(0) == 3:
                    heuristic_value += {1: 0.1, 0: -0.1}[horizontal.count(1)]
        for j in range(7):
            for i in range(3):
                vertical = [board[i + k][j] for k in range(4)]
                if (vertical.count(1) == 3 or vertical.count(2) == 3) and vertical[-1] == 0:
                    heuristic_value += {3: 0.9, 0: -0.9}[vertical.count(1)]
                elif (vertical.count(1) == 2 or vertical.count(2) == 2) and vertical[-2] == 0:
                    heuristic_value += {2: 0.3, 0: -0.3}[vertical.count(1)]
                elif (vertical.count(1) == 1 or vertical.count(2) == 1) and vertical[-3] == 0:
                    heuristic_value += {1: 0.1, 0: -0.1}[vertical.count(1)]
        for i in range(0, 3):
            for j in range(0, 4):
                positive_diagonal = [board[i + k][j + k] for k in range(4)]
                negative_diagonal = [board[5 - (i + k)][j + k] for k in range(4)]
                if positive_diagonal.count(0) == 0 and (positive_diagonal.count(1) == 0 or positive_diagonal.count(2) == 0):
                    heuristic_value += {True: [0, 0.1, 0.3, 0.9][positive_diagonal.count(1)], False: [0, -0.1, -0.3, -0.9][positive_diagonal.count(2)]}[
                        positive_diagonal.count(2) == 0]  # what is wrong with me
                if negative_diagonal.count(0) == 0 and (negative_diagonal.count(1) == 0 or negative_diagonal.count(2) == 0):
                    heuristic_value += {True: [0, 0.1, 0.3, 0.9][negative_diagonal.count(1)], False: [0, -0.1, -0.3, -0.9][negative_diagonal.count(2)]}[
                        negative_diagonal.count(2) == 0]  # what is wrong with me
        return heuristic_value


import time


class Queue:

    def __init__(self, contents=None):

        if contents is None:
            self.contents = []

        else:
            self.contents = contents

    def print(self):

        for item in self.contents:

            print(item)

    def enqueue(self, item_to_queue):

        self.contents.append(item_to_queue)

    def dequeue(self):

        return self.contents.pop(0)


class Node:
    def __init__(self, board_state):
        self.state = board_state
        self.winner = self.determine_winner()
        if self.winner is None:
            self.turn = 1 if sum(row.count(1) for row in self.state) == sum(row.count(2) for row in self.state) else 2
        else:
            self.turn = None
        self.children = []
        self.parents = []
        self.possible_moves = self.find_possible_moves()
        self.is_terminal_node = False  # false by default, gets set to true during tree generation

    def determine_winner(self):
        if self.state == [[0 for _ in range(7)] for _ in range(6)]:
            return None

        for i in range(0, 6):
            for j in range(0, 4):
                if self.state[i][j] == self.state[i][j + 1] == self.state[i][j + 2] == self.state[i][j + 3] != 0:
                    return self.state[i][j]

        for i in range(0, 3):
            for j in range(0, 7):
                if self.state[i][j] == self.state[i + 1][j] == self.state[i + 2][j] == self.state[i + 3][j] != 0:
                    return self.state[i][j]

        for i in range(0, 3):
            for j in range(0, 4):
                if self.state[i][j] == self.state[i + 1][j + 1] == self.state[i + 2][j + 2] == self.state[i + 3][j + 3] != 0:
                    return self.state[i][j]

                elif self.state[5 - i][j] == self.state[5 - (i + 1)][j + 1] == self.state[5 - (i + 2)][j + 2] == self.state[5 - (i + 3)][j + 3] != 0:
                    return self.state[5 - i][j]

        if any(0 in row for row in self.state):
            pass
        else:
            return 'Tie'

        return None

    def check_move_validity(self, move):
        for row in self.state:
            if row[move] == 0:
                return True
        return False

    def find_possible_moves(self):
        possible_moves = []
        for i in range(7):
            if self.check_move_validity(i):
                possible_moves.append(i)
        return possible_moves


class ConnectFourRecombiningTreeCustomDepth:
    def __init__(self, first_game_state, n):
        self.generate_tree(first_game_state, n)

    def generate_tree(self, first_game_state, n):
        start_time = time.time()
        first_node = Node(first_game_state)
        first_node.depth = 0
        created_game_states = {self.deeptuple(first_game_state): first_node}
        terminal_nodes = []

        queue = Queue([first_node])

        while queue.contents != []:

            dequeued_node = queue.dequeue()

            if dequeued_node.depth == n:
                terminal_nodes.append(dequeued_node)
                dequeued_node.is_terminal_node = True
                continue

            if dequeued_node.winner is not None and dequeued_node.is_terminal_node is False:
                terminal_nodes.append(dequeued_node)
                dequeued_node.is_terminal_node = True
                continue

            dequeued_node_board_state = dequeued_node.state
            next_player = dequeued_node.turn
            possible_moves = dequeued_node.possible_moves

            for move in possible_moves:
                new_board_state = self.deeplist(dequeued_node_board_state)
                new_board_state = self.drop_token(next_player, new_board_state, move)

                if self.deeptuple(new_board_state) in created_game_states:
                    new_node = created_game_states[self.deeptuple(new_board_state)]
                    new_node.parents.append(dequeued_node)
                    dequeued_node.children.append(new_node)
                    continue

                # continue seems to be slightly faster than the regular if/else, not sure if its a fluke
                # else:
                new_node = Node(new_board_state)
                new_node.depth = dequeued_node.depth + 1
                new_node.parents.append(dequeued_node)
                dequeued_node.children.append(new_node)
                queue.enqueue(new_node)
                created_game_states[self.deeptuple(new_board_state)] = new_node

        end_time = time.time()
        # print(end_time - start_time)
        self.root = first_node
        self.node_dict = created_game_states
        self.terminal_nodes = terminal_nodes

    def generate_tree_using_cache(self, starting_game_state):
        self.prune_tree(starting_game_state)
        node_dict = self.node_dict
        bottom_layer_nodes = self.bottom_layer_nodes
        terminal_nodes = []
        for terminal_node in self.terminal_nodes:
            if terminal_node.winner is not None:  # if the game is over
                terminal_nodes.append(terminal_node)
        new_layer_nodes = self.create_new_layer(bottom_layer_nodes)
        for current_node in new_layer_nodes:
            if current_node.winner is not None:
                terminal_nodes.append(current_node)
        second_new_layer_nodes = self.create_new_layer(new_layer_nodes)
        terminal_nodes += second_new_layer_nodes
        self.terminal_nodes = terminal_nodes
        self.root = node_dict[self.deeptuple(starting_game_state)]
        self.node_dict = node_dict
        self.previous_game_state = starting_game_state  # to help debug

    def prune_tree(self, template_state):
        template_node = self.node_dict[self.deeptuple(template_state)]
        node_dict = {self.deeptuple(template_state): template_node}
        queue = Queue([template_node])
        terminal_nodes = []
        bottom_layer_nodes = []

        while queue.contents != []:
            dequeued_node = queue.dequeue()
            if dequeued_node.is_terminal_node:
                terminal_nodes.append(dequeued_node)
                if dequeued_node.winner is None:
                    bottom_layer_nodes.append(dequeued_node)  # excludes nodes that have already finished the game

            for child_node in dequeued_node.children:
                child_node_state = child_node.state
                tuple_of_child_node_state = self.deeptuple(child_node_state)
                if tuple_of_child_node_state not in node_dict:
                    node_dict[tuple_of_child_node_state] = child_node
                    queue.enqueue(child_node)

                node_dict[tuple_of_child_node_state].parents = [parent for parent in node_dict[tuple_of_child_node_state].parents if self.deeptuple(parent.state) in node_dict]

        self.node_dict = node_dict
        self.terminal_nodes = terminal_nodes
        self.bottom_layer_nodes = bottom_layer_nodes

    def create_new_layer(self, layer):
        new_layer_nodes = []
        for current_node in layer:
            if current_node.winner is not None:
                continue
            current_board_state = current_node.state
            possible_moves = current_node.possible_moves
            for move in possible_moves:
                new_board_state = self.deeplist(current_board_state)
                new_board_state = self.drop_token(current_node.turn, new_board_state, move)

                if self.deeptuple(new_board_state) in self.node_dict:
                    new_node = self.node_dict[self.deeptuple(new_board_state)]
                    new_node.parents.append(current_node)
                    new_node.depth = current_node.depth
                    current_node.children.append(new_node)
                else:
                    new_node = Node(new_board_state)
                    new_node.is_terminal_node = True
                    new_node.parents.append(current_node)
                    new_node.depth = current_node.depth
                    current_node.children.append(new_node)
                    current_node.is_terminal_node = False
                    self.node_dict[self.deeptuple(new_board_state)] = new_node
                    new_layer_nodes.append(new_node)

        return new_layer_nodes

    def find_possible_moves(self):
        possible_moves = []
        for i in range(7):
            if self.check_move_validity(i):
                possible_moves.append(i)
        return possible_moves

    def drop_token(self, player, board, column):
        for row in range(6):
            if board[row][column] == 0:
                board[row][column] = player
                break
        return board

    def deeptuple(self, board):
        return tuple(tuple(row) for row in board)

    def find_filled_in_spaces(self, board):
        filled_in_spaces = []
        for i in range(6):
            for j in range(7):
                if board[i][j] != 0:
                    filled_in_spaces.append((i, j))
        return filled_in_spaces

    def deeplist(self, board):
        return list(list(row) for row in board)