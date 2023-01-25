from game import Game
from heuristic_player import HeuristicPlayer
from minimax_player import MiniMaxPlayer
from random_player import RandomPlayer
from manual_player import ManualPlayer
from ttt_heuristic_tree import *
from ttt_recombing_tree import *

#random_nine =  {'Tie': 0, 'heuristic_9': 0, 'random': 0}
#random_two =  {'Tie': 0, 'heuristic_2': 0, 'random': 0}
two_nine =  {'Tie': 0, 'heuristic_9': 0, 'heuristic_2': 0}
amount = 10
for i in range(amount):
    if i % 2 == 0:
        #game = Game(HeuristicPlayer(9), RandomPlayer(),False)
        #order = {'Tie': 'Tie', 1: 'heuristic_9', 2: 'random'}

        #game = Game(HeuristicPlayer(2), RandomPlayer(),False)
        #order = {'Tie': 'Tie', 1: 'heuristic_2', 2: 'random'}

        game = Game(HeuristicPlayer(2), HeuristicPlayer(9),False)
        order = {'Tie': 'Tie', 1: 'heuristic_2', 2: 'heuristic_9'}
    
    else:
        #game = Game(RandomPlayer(), HeuristicPlayer(9), False)
        #order = {'Tie': 'Tie', 1: 'random', 2: 'heuristic_9'}

        #game = Game(RandomPlayer(), HeuristicPlayer(2), False)
        #order = {'Tie': 'Tie', 1: 'random', 2: 'heuristic_2'}

        game = Game(HeuristicPlayer(9), HeuristicPlayer(2), False)
        order = {'Tie': 'Tie', 1: 'heuristic_9', 2: 'heuristic_2'}


    game.run()
    #random_nine[order[game.winner]] += 1 
    #random_two[order[game.winner]] += 1 
    two_nine[order[game.winner]] += 1 
print(two_nine)
