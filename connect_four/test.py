from game import ConnectFour
from custom_strat import CustomPlayer
from random_strat import RandomStrat


random = RandomStrat()
custom = CustomPlayer()



outcomes = {'Tie': 0, 'random': 0, 'custom': 0}
amount = 10000
for i in range(amount):
    if i % 2 == 0:
        game = ConnectFour(random, custom)
        order = {'Tie': 'Tie', 1: 'random', 2: 'custom'}
    else:
        game = ConnectFour(custom, random)
        order = {'Tie': 'Tie', 1: 'custom', 2: 'random'}
    game.run()
    outcomes[order[game.winner]] += 1 
print(outcomes)


win_rate = (outcomes['custom'] / amount ) * 100
print(win_rate)