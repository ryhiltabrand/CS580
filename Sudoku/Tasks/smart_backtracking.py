from copy import deepcopy
import numpy as np
import time
    
class smart_backtracking():

    def __init__(self, board):
            
            self.o_domains = self.original_domains(board)
            self.zeros = board.size - np.count_nonzero(board)
            self.recure = 0

            self.solve(board, self.o_domains)
           
    def next_empty(self, board):
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

    def empty(self,board):
        for row in range(9):
            for col in range(9):
                if(board[row][col] == 0):
                    return False
        return True    

    
    def MRV(self, board, domains):
        """
        Finds the minimum remaining value. The value with the least remaining in the domian

        Parameters
        ----------
        board : numpy array
            The puzzle board which gets updated
        domains : dictionary
            The domains of the board.

        Returns
        -------
        list  
            Contains the position and domain of the mrv
        """  

        mrvDict = {}
        for x in domains:
            pos = x.split(',')
            if len(domains[x]) == 1 and domains[x] != 0 and board[int(pos[0])][int(pos[1])] == 0:
                return([x,domains[x]])
            if len(domains[x]) > 1:
                mrvDict[x] = len(domains[x])

        if mrvDict:
            minval = min(mrvDict.values())
            res = [k for k, v in mrvDict.items() if v==minval]
            print(res)
            return [res[0], domains[res[0]]]
        


        

    def solve(self, board, domains):
        """
        Conducts the forward checking, MRV with backtracking to solve the puzzle.

        Parameters
        ----------
        board : numpy array
            The puzzle board which gets updated
        domains : dictionary
            The domains of the board.

        Returns
        -------
        bool
            True the board is solved, false there is no solution
        """

        domains = self.forward_check(board, domains)
        
        print(board)
        print("Number of Backtracks: ", self.recure)

        mrv = self.MRV(board, domains)
        
        if mrv == None:
            return True

        pos = mrv[0].split(',')
        r = int(pos[0])
        c = int(pos[1]) 
        val = mrv[1]

        
        tempDomain = domains[f'{r},{c}']
        for value in val:
            
            if self.check(board, value, r, c):
                                
                board[r][c] = value
                domains[f'{r},{c}'] = [value]  
                if self.solve(board, domains):
                    return True
                                
                board[r][c] = 0
                domains[f'{r},{c}'] = tempDomain
                self.recure +=1
                   
        return False

    def original_domains(self, board):
        """
        Gets the origal domains of the board. Domains are 1-9

        Parameters
        ----------
        board : numpy array
            The puzzle board which gets updated

        Returns
        -------
        domains : dictionary
            The domains of the board. Will be in the form of {Position: [domain]} or {Position: [1,2,3,...,9]}
        """

        domains = {}
        for row in range(9):
            for col in range(9):
                if board[row][col] > 0:
                    domains[f'{row},{col}'] = [board[row][col]]
                elif board[row][col] == 0:
                    domains[f'{row},{col}'] = [1,2,3,4,5,6,7,8,9]
        return domains

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

    def forward_check(self,board, domains):
        """
        Checks the current state of the domain and board and checks if it can remove any thing from the domain
        Parameters
        ----------
        board : numpy array
            The puzzle board which gets updated
        domains : dictionary
            The domains of the board.

        Returns
        -------
        domains : dictionary
            The domains of the board. Will be in the form of {Position: [domain]} or {Position: [1,2,3,...,9]}
        """
        domainsCopy = deepcopy(domains)
        for key in domains:
            
            if len(domains[key]) > 1:
                position = key.split(",")
                #print(position)
                for num in range(1,10):
                    if num in board[int(position[0])] or num in board[:, int(position[1])]:
                        if num in domainsCopy[key]: domainsCopy[key].remove(num)
                        

                    rowstart = int(position[0])//3*3
                    colstart = int(position[1])//3*3

                    for r in range(rowstart, rowstart + 3):
                        for c in range(colstart, colstart + 3):
                            if board[r][c] == num:
                                if num in domainsCopy[key]: domainsCopy[key].remove(num)
        return domainsCopy