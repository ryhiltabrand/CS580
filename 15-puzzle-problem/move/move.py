import numpy as np

def emptyChords(board):
    i, j = np.where(board == 0)
    i = int(i)
    j = int(j)
    return (i,j)

def up(board):
    i,j = emptyChords(board)
    if i > 0:
        movingElement = board[i-1][j]
        temp = np.where(board == movingElement, 17, board)
        temp2 = np.where(temp == 0, movingElement, temp)
        board = (np.where(temp2 == 17, 0, temp2))

        return (board, "U")
        
    else: return "None", "N"
    
def down(board):
    i,j = emptyChords(board)
    if i < 3:
        movingElement = board[i+1][j]
        temp = np.where(board == movingElement, 17, board)
        temp2 = np.where(temp == 0, movingElement, temp)
        board = (np.where(temp2 == 17, 0, temp2))
    
        return (board, "D")

    else: return "None", "N"

def left(board):
    i,j = emptyChords(board)
    if j > 0:
        movingElement = board[i][j-1]
        temp = np.where(board == movingElement, 17, board)
        temp2 = np.where(temp == 0, movingElement, temp)
        board = (np.where(temp2 == 17, 0, temp2))
    
        return (board, "L")
    else: return "None", "N"

def right(board):
    i,j = emptyChords(board)
    if j < 3:
        movingElement = board[i][j+1]
        temp = np.where(board == movingElement, 17, board)
        temp2 = np.where(temp == 0, movingElement, temp)
        board = (np.where(temp2 == 17, 0, temp2))
    
        return (board, "R")
    else: return "None", "None"

def move(where, board):
    if where == 'up':
        #(print(up(board)))
        b, m = (up(board))
        return(b,m)
        #return (up(board))
    elif where == 'down':
        return (down(board))
    elif where == 'left':
        return (left(board))
    elif where == 'right':
        return (right(board))
    else:
        print("move went wrong")
        return ("None", "None")