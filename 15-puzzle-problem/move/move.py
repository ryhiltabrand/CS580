import numpy as np

def emptyChords(board):
    i, j = np.where(board == 0)
    i = int(i)
    j = int(j)
    return (i,j)

def up(board):
    print("up", board)
    i,j = emptyChords(board)
    moveup = i - 1
    tempBoard = d

    
def down(board):
    print("down", board)

def left(board):
    print("left", board)

def right(board):
    print("right", board)

def move(where, board):
    if where == 'up':
        return up(board)
    elif where == 'down':
        return down(board)
    elif where == 'left':
        return left(board)
    elif where == 'right':
        return right(board)
    else:
        print("move went wrong")
        return None