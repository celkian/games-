from game import Snake
from custom_player import CustomPlayer
from ben_player import BenPlayer
from elias_player import EliasPlayer
from christine_player import ChristinePlayer

total_score = 0
total_moves = 0

num_games = 100
for i in range(num_games): 
    p1 = ChristinePlayer()
    snake = Snake(p1)
    snake.run()
    total_score += snake.score
    total_moves += snake.num_player_moves

average_score = total_score / num_games
average_num_moves = total_moves / num_games

print('average score is', average_score)
print('average num of moves is', average_num_moves)