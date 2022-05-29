class ChristinePlayer: 
    def choose_move(self,board,snake):
        head = snake[-1]
        if head in [(9,i) for i in range(0,9,2)]:
            return 'd'
        if head in [(1,i) for i in range(1,8,2)]:
            return 'd'
        if head in [(i,0) for i in range(1,9)]:
            return 's'
        if head in [(i,1) for i in range(2,10)]:
            return 'w'
        if head in [(i,2) for i in range(1,9)]:
            return 's'
        if head in [(i,3) for i in range(2,10)]:
            return 'w'
        if head in [(i,4) for i in range(1,9)]:
            return 's'
        if head in [(i,5) for i in range(2,10)]:
            return 'w'
        if head in [(i,6) for i in range(1,9)]:
            return 's'
        if head in [(i,7) for i in range(2,10)]:
            return 'w'
        if head in [(i,8) for i in range(1,9)]:
            return 's'
        if head in [(i,9) for i in range(1,10)]:
            return 'w'
        if head in [(0,i) for i in range(1,10)]:
            return 'a'
        if head == (0,0):
            return 's'
