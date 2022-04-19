
from player import *
from game import Game
from ben_strat import strat1
from elias_strat import strategy
from jeff_strat import jeff
from player import *
from random_player import *
from strat_player import * 
from cheater_strat import *
from old_me_strat import *
from christine_strat import *

player1 = Player(my_strat)
player2 = Player(random_strategy_function)



outcomes = {'Tie': 0, 'player1': 0, 'player2': 0}
amount = 100000
for i in range(amount):
    if i % 2 == 0:
        game = Game(player1, player2,log=False)
        order = {'Tie': 'Tie', 1: 'player1', 2: 'player2'}
    else:
        game = Game(player2, player1,log=False)
        order = {'Tie': 'Tie', 1: 'player2', 2: 'player1'}
    game.run()
    outcomes[order[game.winner]] += 1 
print(outcomes)


win_rate = (outcomes['player1'] / amount ) * 100
print(win_rate)