import move.move as move
import numpy as np

def main():
   board = puzzle_board()
   i, j = move.emptyChords(board)
   print(board, i, j)



def puzzle_board():
    '''rng = default_rng()
    vals = rng.standard_normal(10)
    more_vals = rng.standard_normal(10)'''
    board = np.arange(16)
    #board = np.where(board == 0, ' ', board)
    np.random.shuffle(board)
    board = np.reshape(board, (4,4))
    
    return board



if __name__ == "__main__":
    main()