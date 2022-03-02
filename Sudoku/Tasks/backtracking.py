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
    def __init__(self, board):
        self.o_board = board
        self.c_board = self.o_board
        self.solve()

    def solve(self):
        self.check_row(1, 0)
        self.check_column(1, 0)
        self.check_box()
        '''while True:
            self.check_row(1, 0)
            self.check_column(1, 0)'''
    
    def check_row(self, number_input, row_num):
        print(self.c_board[row_num])
        if number_input in self.c_board[row_num]:
            print(False)
        else:
            print(True)
    
    def check_column(self, number_input, col_num):
        print(self.c_board[:, col_num])
        if number_input in self.c_board[:, col_num]:
            print(False)
        else:
            print(True)

    def check_box(self):
        mats_9x3x3 = np.array(self.c_board)
        print([mats_9x3x3[3*i:3*i+3, 3*j:3*j+3] for i in range(3) for j in range(3)])
        print("check box")
    
    def print_board(self):
        print