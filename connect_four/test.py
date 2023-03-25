from game import ConnectFour
from custom_player import CustomPlayer
from random_player import RandomPlayer
from c4_tree import *
from heuristic_player import *


random = RandomPlayer()
heuristic = HeuristicPlayer(5)


outcomes = {'Tie': 0, 'random': 0, 'heuristic': 0}
amount = 10

for i in range(amount):
    if i % 2 == 0:
        game = ConnectFour(random, heuristic)
        order = {'Tie': 'Tie', 1: 'random', 2: 'heuristic'}
    else:
        game = ConnectFour(heuristic, random)
        order = {'Tie': 'Tie', 1: 'heuristic', 2: 'random'}
    game.run()
    outcomes[order[game.winner]] += 1 
print(outcomes)


win_rate = (outcomes['heuristic'] / amount ) * 100
print(win_rate)