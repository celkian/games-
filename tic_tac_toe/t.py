from player import *
from game import Game
from ben_strat import strat1
from elias_strat import strategy
from jeff_strat import jeff
from player import *
from random_player import *
from strat_player import * 
from cheater_strat import *

my_strat = Player(strategy_function)
random = Player(strategy_function)
outcomes = {'Tie': 0, 'my_strat': 0, 'random': 0}
for i in range(100000):
    if i % 2 == 0:
        game = Game(my_strat,random,log=False)
        player_order = {'Tie': 'Tie', 1: 'my_strat', 2: 'random'}
    else:
        game = Game(random ,my_strat,log=False)
        player_order = {'Tie': 'Tie', 1: 'random', 2: 'my_strat'}

    game.run()
    outcomes[player_order[game.winner]] += 1
    if i % 1000 == 0:
        print(i)
print((outcomes['my_strat'] / 100000) * 100 , '%')
