from game import Game
from heuristic_player import HeuristicPlayer
from minimax_player import MiniMaxPlayer
from random_player import RandomPlayer
from manual_player import ManualPlayer
from ttt_heuristic_tree import *
from ttt_recombing_tree import *

game = Game(ManualPlayer(), MiniMaxPlayer(), log=True)
game.run()

random_nine =  {'Tie': 0, 'heuristic_9': 0, 'random': 0}
random_two =  {'Tie': 0, 'heuristic_2': 0, 'random': 0}
two_nine =  {'Tie': 0, 'heuristic_9': 0, 'heuristic_2': 0}
amount = 100
for i in range(amount):
    if i % 2 == 0:
        random_nine_game = Game(HeuristicPlayer(9), RandomPlayer(),False)
        random_nine_order = {'Tie': 'Tie', 1: 'heuristic_9', 2: 'random'}

        random_two_game = Game(HeuristicPlayer(2), RandomPlayer(),False)
        random_two_order = {'Tie': 'Tie', 1: 'heuristic_2', 2: 'random'}

        two_nine_game = Game(HeuristicPlayer(2), HeuristicPlayer(9),False)
        two_nine_order = {'Tie': 'Tie', 1: 'heuristic_2', 2: 'heuristic_9'}
    
    else:
        random_nine_game = Game(RandomPlayer(), HeuristicPlayer(9), False)
        random_nine_order = {'Tie': 'Tie', 1: 'random', 2: 'heuristic_9'}

        random_two_game = Game(RandomPlayer(), HeuristicPlayer(2), False)
        random_two_order = {'Tie': 'Tie', 1: 'random', 2: 'heuristic_2'}

        two_nine_game = Game(HeuristicPlayer(9), HeuristicPlayer(2), False)
        two_nine_order = {'Tie': 'Tie', 1: 'heuristic_9', 2: 'heuristic_2'}

    random_nine_game.run()
    random_two_game.run()
    two_nine_game.run()

    random_nine[random_nine_order[random_nine_game.winner]] += 1 
    random_two[random_two_order[random_two_game.winner]] += 1 
    two_nine[two_nine_order[two_nine_game.winner]] += 1 

print(random_nine)
print(random_two)
print(two_nine)