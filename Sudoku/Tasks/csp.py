import numpy as np

class csp():
    def __init__(self, board):
        self.o_board = board
        self.c_board = board
        self.domains = self.original_domains()
        self.solve()
        #self.pprint()

    def empty(self,):
        for row in range(9):
            for col in range(9):
                if(self.c_board[row][col] == 0):
                    return False
        return True

    def solve(self):
        while not self.empty():
            self.check()
            self.check2()
            for row in range(9):
                for col in range(9):
                    if(self.c_board[row][col] == 0):
                        if len(self.domains[f'{row},{col}']) == 1:
                            #print(f'{row},{col}', self.c_board[row][col] ,self.domains[f'{row},{col}'][0])
                            self.c_board[row][col] = self.domains[f'{row},{col}'][0]
            print(self.c_board)
        
    
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
                        if num in self.domains[key]: self.domains[key].remove(num)
                        '''try:
                            self.domains[key].remove(num)
                        except:
                            continue'''

                    rowstart = int(position[0])//3*3
                    colstart = int(position[1])//3*3

                    for r in range(rowstart, rowstart + 3):
                        for c in range(colstart, colstart + 3):
                            if self.c_board[r][c] == num:
                                if num in self.domains[key]: self.domains[key].remove(num)
                                '''try: 
                                    self.domains[key].remove(num)
                                except:
                                    continue'''
    def check2(self):
        boxxes=[['0,0','0,1','0,2','1,0','1,1','1,2','2,0','2,1','2,2'],
                ['0,3','0,4','0,5','1,3','1,4','1,5','2,3','2,4','2,5'],
                ['0,6','0,7','0,8','1,6','1,7','1,8','2,6','2,7','2,8'],
                ['3,0','3,1','3,2','4,0','4,1','4,2','5,0','5,1','5,2'],
                ['3,3','3,4','3,5','4,3','4,4','4,5','5,3','5,4','5,5'],
                ['3,6','3,7','3,8','4,6','4,7','4,8','5,6','5,7','5,8'],
                ['6,0','6,1','6,2','7,0','7,1','7,2','8,0','8,1','8,2'],
                ['6,3','6,4','6,5','7,3','7,4','7,5','8,3','8,4','8,5'],
                ['6,6','6,7','6,8','7,6','7,7','7,8','8,6','8,7','8,8']]
        naked_twins_row = []
        naked_twins_col = []
        naked_twins_box = []
        potential_twins=[]
        for x in self.domains: 
            if len(self.domains[x]) == 2:
                for n in range(9):
                    if x.split(",")[0] == f'{n}':
                        potential_twins.append(x)


        for n in range(9):
            naked_twins_row = []
            naked_twins_col = []
            naked_twins_box = []
            for x in potential_twins:
                if f'{n},' in x:
                    naked_twins_row.append(x)
                if f',{n}' in x:
                    naked_twins_col.append(x)
                #for i in range(9):
                for pt in boxxes[n]:
                    if pt in x:
                        naked_twins_box.append(x)  
            
                
            if len(naked_twins_row) > 1:
                #print(f'Row{n}: ',naked_twins_row)
                test = iter(naked_twins_row)
                f=self.domains[next(test)]
                s=self.domains[next(test)]
                if f==s:
                    for num in range(9):
                        if len(self.domains[f'{n},{num}']) >2:
                            #print(self.domains[f'{n},{num}'])
                            if f[0] in self.domains[f'{n},{num}']: self.domains[f'{n},{num}'].remove(f[0])
                            if f[1] in self.domains[f'{n},{num}']: self.domains[f'{n},{num}'].remove(f[1])
                            return

            if len(naked_twins_col) > 1:
                #print(f'Col{n}: ',naked_twins_col)
                test = iter(naked_twins_col)
                f=self.domains[next(test)]
                s=self.domains[next(test)]
                if f==s:
                    for num in range(9):
                        if len(self.domains[f'{num},{n}']) >2:
                            #print(self.domains[f'{num},{n}'])
                            if f[0] in self.domains[f'{num},{n}']: self.domains[f'{num},{n}'].remove(f[0])
                            if f[1] in self.domains[f'{num},{n}']: self.domains[f'{num},{n}'].remove(f[1])
                            return
            print(f'box {n}: ',naked_twins_box)
            '''if len(naked_twins_box) > 1:
                print(f'box {n}: ',naked_twins_box)
                test = iter(naked_twins_box)
                f=self.domains[next(test)]
                s=self.domains[next(test)]
                if f==s:
                    for num in range(9):
                        if len(self.domains[f'{num},{n}']) >2:
                            print(self.domains[f'{num},{n}'])
                            if f[0] in self.domains[f'{num},{n}']: self.domains[f'{num},{n}'].remove(f[0])
                            if f[1] in self.domains[f'{num},{n}']: self.domains[f'{num},{n}'].remove(f[1])
                            return'''
            
                

            for key in self.domains:
                print(key, "->", self.domains[key])

                
        
        
    def pprint(self):
        count = 0
        for key in self.domains:
            #print(key, "->", self.domains[key])
            if len(self.domains[key]) == 1:
                count =count + 1
        print(count)
        
        print(self.c_board)


    
