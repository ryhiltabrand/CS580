import numpy as np

class backtracking():
    """
    A class used to compute regluar backtracking

    """
    def __init__(self):
        """
        Constructer
        """
        self.recure = 0

    def solve(self, board, count):
        """
        Conducts the naive backtracking to solve the puzzle.

        Parameters
        ----------
        board : numpy array
            The puzzle board which gets updated

        Returns
        -------
        bool
            True the board is solved, false does backtraking
        """
        
        print(board)
        print("Number of Backtracks: ", self.recure)
        r, c = self.empty(board)

        if r == None:
            return True

        for value in range(1,10):

            if self.check(board, value, r, c):
                                
                board[r][c] = value
                count += 1
                if self.solve(board, count):
                    return True
                                
                board[r][c] = 0
                self.recure +=1
                
        
        return False


    def empty(self, board):
        """
        Finds the next empty spot
        
        Parameters
        ----------
        board : numpy array
            The puzzle board which gets updated
        
        Returns
        -------
        row, col : int
            The row and colunm the empty space resides on 
        """
        for row in range(9):
            for col in range(9):
                if(board[row][col] == 0):
                    return row,col
        return None,None

    def check(self, board, number_input, row, col):
        """
        Applies the constraints to the backtracking to make sure the CSP is not violated

        Parameters
        ----------
        board : numpy array
            The puzzle board which gets updated
        number_input : int
            Value that is being tested(1-9)
        row : int
            row the check is occuring on
        col : int
            column the check is occuring on
        Returns
        -------
        Bool
            If True there is no duplicates, False there is a duplicate
        """

        if number_input in board[row]:
            return(False)

        if number_input in board[:, col]:
            return(False)

        rowstart = row//3*3
        colstart = col//3*3

        for r in range(rowstart, rowstart + 3):
            for c in range(colstart, colstart + 3):
                if board[r][c] == number_input:
                    return False

        
        return (True)

