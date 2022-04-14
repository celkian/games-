def is_end_copy(board):
    for i in range(0,3):
        if board[3*i + 0] == board[3*i + 1] == board[3*i + 2] != 0:
            return "Player " + str(board[3*i + 0])
        if board[0 + i] == board[3 + i] == board[6 + i] != 0:
            return "Player " + str(board[0+i])

    if board[0] == board[4] == board[8] != 0:
        return "Player " + str(board[0])
    if board[2] == board[4] == board[6] != 0:
        return "Player " + str(board[2])

    if 0 not in board:
        return 'Tie'
    return False

def possible_moves(board):
    empty_spaces = []
    for i in range(0,len(board)):
        if board[i] == 0:
            empty_spaces.append(i)
    return empty_spaces
    
def is_almost_end(board):
    empty_spaces = possible_moves(board)
    p_one = []
    p_two = []
    ends = [p_one,p_two]
    #player 1's turn
    for b in range(1,3):
        for i in empty_spaces:
            tboard = list(board)
            tboard[i] = b
            if is_end_copy(tboard) not in ['Tie',False]:
                ends[b-1].append(i)
    return ends


def jeff(board):
    corners = [0,2,6,8]
    edges = [1,3,5,7]
    middle = [4]
    p_turn = 1 if len(possible_moves(board))%2 == 1 else 2
    if p_turn == 1:
        if len(possible_moves(board)) == 9:
            return 8 #takes corner
    if p_turn == 2 and len(possible_moves(board)) == 8:
        if board[4] == 0:
            return 4
        else:
            return 8
    '''-------------- set = 1 ended ----------------'''
    if p_turn == 1 and len(possible_moves(board)) == 9 - 2:
        i = board.index(p_turn+1)
        if i in middle:
            return 0
        elif i in corners:
            if i + board.index(1) == 8:
                return 2
            else:
                return 8 - i
        elif i in edges:
            return 4
            
    if p_turn == 2 and len(possible_moves(board)) == 9 - 3:
        if len(is_almost_end(board)[0]) == 0:
            for i in possible_moves(board):
                if i in corners:
                    return i
    '''-------------- set = 2 ended ----------------'''
    #print(p_turn)
    if p_turn == 1:
        if len(is_almost_end(board)[0]) != 0:
            return is_almost_end(board)[0][0]
        elif len(is_almost_end(board)[1]) != 0:
            return is_almost_end(board)[1][0]
        for corner in corners:
            if board[corner] == 0:
                return corner
        else:
            return possible_moves(board)[0]
    if p_turn == 2:
        if len(is_almost_end(board)[1]) != 0:
            return is_almost_end(board)[1][0]
        elif len(is_almost_end(board)[0]) != 0:
            return is_almost_end(board)[0][0]
        for corner in corners:
            if board[corner] == 0:
                return corner
        else:
            return possible_moves(board)[0]