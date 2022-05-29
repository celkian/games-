import random
from custom_player import CustomPlayer

class Snake: 

    def __init__(self, player): 
        self.board = [[' ' for i in range(10)] for i in range(10)]
        self.score = 0
        self.snake = [(4,1), (4,2), (4,3)] 
        self.berry_location = None 
        self.player = player
        self.game_over = False
        self.num_player_moves = 0

    def print_board(self): 
        for i in range(10):
            print(self.board[i])
    
    def random_berry_location(self):
        open_spaces = []
        for i in range(10): 
            for j in range(10): 
                if self.board[i][j] == ' ': 
                    open_spaces.append((i,j))

        random_space = random.choice(open_spaces)
        self.berry_location = random_space
    
    def generate_berry(self): 
        self.random_berry_location()
        i = self.berry_location[0]
        j = self.berry_location[1]
        self.board[i][j] = 'b'
    
    def generate_snake(self):
        for part in self.snake[:-1]:
                self.board[part[0]][part[1]] = "o"
        self.board[self.snake[-1][0]][self.snake[-1][1]] = "e"

    def check_collision(self):
        if len(list(set(self.snake))) != len(self.snake):
            return True
        elif self.snake[-1][0] not in range(0, 10):
            return True
        elif self.snake[-1][1] not in range(0, 10):
            return True
        return False
    
    
    def run(self,log=False): 
        self.generate_berry()
        self.generate_snake()
        if log == True: 
            self.print_board()

        while self.game_over == False:
            head = self.snake[-1]
            tail = self.snake[0]
        
            move = self.player.choose_move(self.board,self.snake)
            self.num_player_moves += 1
            new_segment = None 
            if move == 'w':
                new_segment = (self.snake[-1][0] - 1, self.snake[-1][1])
            elif move == 's':
                new_segment = (self.snake[-1][0] + 1, self.snake[-1][1])
            elif move == 'a':
                new_segment = (self.snake[-1][0], self.snake[-1][1] - 1)
            elif move == 'd':
                new_segment = (self.snake[-1][0], self.snake[-1][1] + 1)
            
            self.snake.append(new_segment)

            if self.check_collision() == True: 
                if log == True: 
                    print(self.score)
                return self.score
            
            self.snake.remove(tail)
            self.board[tail[0]][tail[1]] = ' '

            if head == self.berry_location: 
                self.score += 1 
                self.generate_berry()
                self.snake.insert(0, tail)

            self.generate_snake()
            if log == True:
                self.print_board()