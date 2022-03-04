''' 
1. Make a check if puzzle is complete
    Follows all constraints and checks if there are any remaining 0
2. Make a recursive function that inserts number based on constrainsts and exhaist numbers until it is finished
3. Function to check if number in row
4. Function to check if number is in column
5. Fucntion to check if number is in 3x3 block
'''

import numpy as np
    
class backtracking():

    def solve(self, board, count):
        
        print(board, count)
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
                
        
        return False


    def empty(self, board):
        for row in range(9):
            for col in range(9):
                if(board[row][col] == 0):
                    return row,col
        return None,None

    def check(self, board, number_input, row, col):

        print(rowstart, colstart)
        if number_input in board[row]:
            #print(f"In row")
            return(False)

        if number_input in board[:, col]:
            #print("In column")
            return(False)

        rowstart = row//3*3
        colstart = col//3*3

        for r in range(rowstart, rowstart + 3):
            for c in range(colstart, colstart + 3):
                if board[r][c] == number_input:
                    return False

        '''mats_9x3x3 = np.array(board)
        box = mats_9x3x3[3*row:3*row+3, 3*col:3*col+3]
        print(box)
        if number_input in box:
            #print("In Box")
            return (False)'''
       
        
        return (True)

    
"""import numpy as np
    
class backtracking():
    def __init__(self, board):
        self.o_board = board
        self.c_board = self.o_board
        self.x = 0
        self.y = 0
        self.solve()

    def solve(self):
        
        #print(board, count)
        #row, col = self.empty(board)

        '''if row == None:
            return True'''
        self.x = 0
        self.y = 0
        if not self.empty():
            return True

        for value in range(1,10):

            if self.check(value):
                                
                self.c_board[self.x][self.y] = value
                #print(board)
                if self.solve():
                    return True
                                
                self.c_board[self.x][self.y] = 0
                
        
        return False


    def empty(self):
        for row in range(9):
            for col in range(9):
                if(self.c_board[row][col] == 0):
                    self.x = row
                    self.y = col
                    return True
        return False

    def check(self, number_input):
        if number_input in self.c_board[self.x]:
            #print(f"In row")
            return(False)

        if number_input in self.c_board[:, self.y]:
            #print("In column")
            return(False)

        rowstart = self.x//3*3
        colstart = self.y//3*3

        for r in range(rowstart, rowstart + 3):
            for c in range(colstart, colstart + 3):
                if self.c_board[r][c] == number_input:
                    return False

        '''mats_9x3x3 = np.array(board)
        box = mats_9x3x3[3*row:3*row+3, 3*col:3*col+3]
        print(box)
        if number_input in box:
            #print("In Box")
            return (False)'''
        
        return (True)"""