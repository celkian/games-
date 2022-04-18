
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

player1 = Player(jeff)
player2 = Player(christine_strat)



outcomes = {'Tie': 0, 'player1': 0, 'player2': 0}
amount = 100

for i in range(amount):
    game = Game(player1, player2,log=False)
    player_order = {'Tie': 'Tie', 1: 'player1', 2: 'player2'}

    game.run()
    outcomes[player_order[game.winner]] += 1
print(outcomes)