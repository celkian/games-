import random 
from tic_tac_toe import Game

class Player: 
     
     def __init__(self, strategy): 
          self.strategy = strategy

     def choose_move(self, board): 
          return self.strategy(board)
     
def is_board_empty(board): 
     return board.count(board[0]) == len(board)


def random_strategy_function(board):
     move = random.randint(0,8)
     return move


def strategy_function(board):

     empty = is_board_empty(board)
     move = 0

    #4
     if board[3] == board[5] != 0 and board[4] == 0:
          move = 4
     elif board[1] == board[7] != 0 and board[4] == 0:
          move = 4
     elif board[2] == board[6] != 0 and board[4] == 0: 
          move = 4
     #0
     elif board[1] == board[2] != 0 and board[0] == 0: 
          move = 0 
     elif board[3] == board[6] != 0 and board[0] == 0: 
          move = 0 
     elif board[4] == board[8] != 0 and board[0] == 0: 
          move = 0 
     elif board[4] == board[6] != 0 and board[0] == 0: 
          move = 0 
     #2
     elif board[0] == board[1] != 0 and board[2] == 0:
          move = 2
     elif board[5] == board[8] != 0 and board[2] == 0: 
          move = 2
     #6
     elif board[7] == board[8] != 0 and board[6] == 0: 
          move = 6
     elif board[0] == board[3] != 0 and board[6] == 0:
          move = 6
     elif board[2] == board[4] != 0 and board[6] == 0: 
          move = 6
     #8
     elif board[6] == board[7] != 0 and board[8] == 0:
          move = 8
     elif board[2] == board[5] != 0 and board[8] == 0:
          move = 8
     elif board[0] == board[4] != 0 and board[8] == 0: 
          move = 8
     #1
     elif board[0] == board[2] != 0 and board[1] == 0:
          move = 1
     elif board[4] == board[7] != 0 and board[1] == 0: 
          move = 1
     #3
     elif board[4] == board[5] != 0 and board[3] == 0:
          move = 3
     elif board[0] == board[6] != 0 and board[3] == 0: 
          move = 3
     #5
     elif board[3] == board[4] != 0 and board[5] == 0:
          move = 5
     elif board[2] == board[8] != 0 and board[5] == 0: 
          move = 5
     #7
     elif board[6] == board[8] != 0 and board[7] == 0:
          move = 7
     elif board[4] == board[1] != 0 and board[7] == 0: 
          move = 7
     
     elif board[4] == 0: 
          move = 4
     elif board[0] == 0: 
          move = 0
     elif board[2] == 0: 
          move = 2
     elif board[6] == 0: 
          move = 6
     elif board[8] == 0: 
          move = 8
     elif board[1] == 0: 
          move = 1
     elif board[3] == 0: 
          move = 3
     elif board[5] == 0: 
          move = 5
     elif board[7] == 0: 
          move = 7
     return move

def or_function(board):
     empty = is_board_empty(board)
     move = 0

    #4
     if board[3] == board[5] != 0 or board[1] == board[7] != 0 or board[2] == board[6] != 0 and board[4] == 0:
          move = 4
        
     elif board[1] == board[2] != 0 or board[3] == board[6] != 0 or board[4] == board[8] != 0 or board[4] == board[6] != 0 and board[0] == 0: 
          move = 0 
     #2
     elif board[0] == board[1] != 0 or board[5] == board[8] != 0 and board[2] == 0:
          move = 2
     #6
     elif board[7] == board[8] != 0 or board[0] == board[3] != 0 or board[2] == board[4] != 0  and board[6] == 0: 
          move = 6
     #8
     elif board[6] == board[7] != 0 or board[2] == board[5] != 0 or board[0] == board[4] != 0  and board[8] == 0:
          move = 8
     #1
     elif board[0] == board[2] != 0 or board[4] == board[7] != 0  and board[1] == 0:
          move = 1
     #3
     elif board[4] == board[5] != 0 or board[0] == board[6] != 0 and board[3] == 0:
          move = 3
     #5
     elif board[3] == board[4] != 0 or board[2] == board[8] != 0  and board[5] == 0:
          move = 5
     #7
     elif board[6] == board[8] != 0 or board[4] == board[1] != 0 and board[7] == 0:
          move = 7

     elif board[4] == 0: 
          move = 4
     elif board[0] == 0: 
          move = 0
     elif board[2] == 0: 
          move = 2
     elif board[6] == 0: 
          move = 6
     elif board[8] == 0: 
          move = 8
     elif board[1] == 0: 
          move = 1
     elif board[3] == 0: 
          move = 3
     elif board[5] == 0: 
          move = 5
     elif board[7] == 0: 
          move = 7
     return move


Player1 = Player(random_strategy_function)
Player2 = Player(or_function)


game = Game(Player1, Player2, log=True)
game.run()
print(game.winner)    