import numpy as np

class csp():
    def __init__(self, board):
        self.o_board = board
        self.c_board = board
        self.domains = self.original_domains()
        self.solve()
        self.pprint()

    def solve(self):
        self.check()
        for row in range(9):
            for col in range(9):
                if(self.c_board[row][col] == 0):
                    if len(self.domains[f'{row},{col}']) == 1:
                        self.c_board[row][col] = self.domains[f'{row},{col}'][0]
        
    
    def original_domains(self):
        domains = {}
        for row in range(9):
            for col in range(9):
                if self.o_board[row][col] > 0:
                    domains[f'{row},{col}'] = [self.o_board[row][col]]
                elif self.o_board[row][col] == 0:
                    domains[f'{row},{col}'] = [1,2,3,4,5,6,7,8,9]
        return domains

    def check(self):
        for key in self.domains:
            #print(self.domains[key])
            if len(self.domains[key]) > 1:
                position = key.split(",")
                #print(position)
                for num in range(1,10):
                    if num in self.c_board[int(position[0])] or num in self.c_board[:, int(position[1])]:
                        self.domains[key].remove(num)

                    '''if num in self.c_board[:, int(position[1])]:
                        try: 
                            self.domains[key].remove(num)
                        except:
                            continue'''

                    rowstart = int(position[0])//3*3
                    colstart = int(position[1])//3*3

                    for r in range(rowstart, rowstart + 3):
                        for c in range(colstart, colstart + 3):
                            if self.c_board[r][c] == num:
                                try: 
                                    self.domains[key].remove(num)
                                except:
                                    continue
            

    def eliminate(self):
        print("elim")
    
    def pprint(self):
        count = 0
        for key in self.domains:
            print(key, "->", self.domains[key])
            if len(self.domains[key]) == 1:
                count =count + 1
        print(count)
        print(self.o_board)
        print(self.c_board)


    
