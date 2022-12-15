import random 

class RandomPlayer: 
     def choose_move(self,board):
          avaliable_moves = []
          for i in range(len(board)): 
               if board[i] == 0: 
                    avaliable_moves.append(i) 

          move = random.choice(avaliable_moves)
          return move



