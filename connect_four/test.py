from game import ConnectFour
from custom_player import CustomPlayer
from random_player import RandomPlayer
from c4_tree import *
from heuristic_player import *
from manual_player import *
from elias_player import *
from jeff_player import *


random = RandomPlayer()
manual = ManualPlayer()
elias = HeuristicMinimaxStrategy(5, True)
heuristic_5= HeuristicPlayer(5)

jeff = minimaxHeuristic(1,4)

game = ConnectFour(jeff, elias)
game.run(log=True)


#outcomes = {'Tie': 0, 'elias': 0, 'heuristic_5': 0}
#amount = 4

#for i in range(amount):
#    if i % 2 == 0:
#        game = ConnectFour(elias, heuristic_5)
#        order = {'Tie': 'Tie', 1: 'elias', 2: 'heuristic_5'}
#    else:
#       game = ConnectFour(heuristic_5, elias)
#       order = {'Tie': 'Tie', 1: 'heuristic_5', 2: 'elias'}
#    game.run()
#    outcomes[order[game.winner]] += 1 
#print(outcomes)


#win_rate = (outcomes['heuristic'] / amount ) * 100
#print(win_rate)