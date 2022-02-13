import numpy as np

def emptyChords(board):
    """
    Finds cordinates of the o puzzle piece on the current nodes board

    Parameters
    ----------
    board : numpy array
        current nodes puzzle board

    Returns
    -------
    int
        The x cordintate of 0
    int 
        The y cordinate of 0
    """
    i, j = np.where(board == 0)
    i = int(i)
    j = int(j)
    return (i,j)

def up(board):
    """
    Swaps 0 and puzzle piece above it

    Parameters
    ----------
    board : numpy array
        current nodes puzzle board

    Returns
    -------
    numpy array
        New nodes board after swap
    str 
        U
    """
    i,j = emptyChords(board)
    if i > 0:
        movingElement = board[i-1][j]
        temp = np.where(board == movingElement, 17, board)
        temp2 = np.where(temp == 0, movingElement, temp)
        board = (np.where(temp2 == 17, 0, temp2))

        return (board, "U")
        
    else: return None, "N"
    
def down(board):
    """
    Swaps 0 and puzzle piece below it

    Parameters
    ----------
    board : numpy array
        current nodes puzzle board

    Returns
    -------
    numpy array
        New nodes board after swap
    str 
        D
    """
    i,j = emptyChords(board)
    if i < 3:
        movingElement = board[i+1][j]
        temp = np.where(board == movingElement, 17, board)
        temp2 = np.where(temp == 0, movingElement, temp)
        board = (np.where(temp2 == 17, 0, temp2))
    
        return (board, "D")

    else: return None, "N"

def left(board):
    """
    Swaps 0 and puzzle piece to the left of it

    Parameters
    ----------
    board : numpy array
        current nodes puzzle board

    Returns
    -------
    numpy array
        New nodes board after swap
    str 
        L
    """
    i,j = emptyChords(board)
    if j > 0:
        movingElement = board[i][j-1]
        temp = np.where(board == movingElement, 17, board)
        temp2 = np.where(temp == 0, movingElement, temp)
        board = (np.where(temp2 == 17, 0, temp2))
    
        return (board, "L")
    else: return None, "N"

def right(board):
    """
    Swaps 0 and puzzle piece to the right of it

    Parameters
    ----------
    board : numpy array
        current nodes puzzle board

    Returns
    -------
    numpy array
        New nodes board after swap
    str 
        U
    """
    i,j = emptyChords(board)
    if j < 3:
        movingElement = board[i][j+1]
        temp = np.where(board == movingElement, 17, board)
        temp2 = np.where(temp == 0, movingElement, temp)
        board = (np.where(temp2 == 17, 0, temp2))
    
        return (board, "R")
    else: return None, "N"

def move(where, board):
    """
    Calls proper move function

    Parameters
    ----------
    where : str
        The move it wants to conduct (up, down, left, right)
    board : numpy array
        current nodes puzzle board

    Returns
    -------
    Nested return
        The updated board after the move and the string associated with the move to append to list
    """
    if where == 'up':
        b, m = (up(board))
        return(b,m)
    elif where == 'down':
        return (down(board))
    elif where == 'left':
        return (left(board))
    elif where == 'right':
        return (right(board))
    else:
        print("move went wrong")
        return (None, "None")