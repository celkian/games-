from game import ConnectFour
from custom_player import CustomPlayer
from random_player import RandomPlayer
from c4_tree import *
from heuristic_player import *
from manual_player import *
from elias_player import *
from jeff_player import *
from last_minute_player import LastMinutePlayer


random = RandomPlayer()
manual = ManualPlayer()
elias = HeuristicMinimaxStrategy(5, True)
heuristic_5= HeuristicPlayer(5)
jeff = minimaxHeuristic(1,4)
last_minute_player = LastMinutePlayer()


game = ConnectFour(heuristic_5, manual)
game.run(log=True)




outcomes = {'Tie': 0, 'last_minute': 0, 'heuristic_5': 0}
amount = 0

for i in range(amount):
    if i % 2 == 0:
        game = ConnectFour(last_minute_player, heuristic_5)
        order = {'Tie': 'Tie', 1: 'last_minute', 2: 'heuristic_5'}
    else:
       game = ConnectFour(heuristic_5, last_minute_player)
       order = {'Tie': 'Tie', 1: 'heuristic_5', 2: 'last_minute'}
    game.run()
    outcomes[order[game.winner]] += 1 


print(outcomes)


#win_rate = (outcomes['heuristic'] / amount ) * 100
#print(win_rate)