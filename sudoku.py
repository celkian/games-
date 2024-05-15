class Sudoku: 

    def __init__(self): 
        self.board = [[1,2,3,4,5,6,7,8,9] for i in range(9)]

        self.columns = [[self.board[i][j] for i in range(9)] for j in range(9)]

        self.squares = self.create_squares()
    
    def print(self, board): 
        for i in range(9): 
            print(board[i])


    def create_squares(self): 
        board = [[] for i in range(9)]
        for k in range(0,7): 
            if k in [1,2,4,5,7]: 
                continue
            for i in range(0,3): 
                    for j in range(0, 3): 
                        board[k].append(self.board[i+k][j+k]) 

        self.print(self.board)

        print('')

        self.print(board)



s = Sudoku()
#00 01 02  03 04 05 
#10 11 12  13 14 15
#20 21 22  23 24 25

#30 31 32
#40 41 42
#50 51 42