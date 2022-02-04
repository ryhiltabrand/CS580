from xml.dom.minidom import Element
import numpy as np
#import sys
#sys.path.insert(0, '15-puzzle-problem/move/move.py')
import move.move as move
import timeit
import tracemalloc

class puzzle:
    def __init__(self, number, board):
        self.number = number
        self.board = board

def dfs(board):
    start = timeit.default_timer()
    tracemalloc.start()
    ListMoves = ""
    Printed_Board = open("results/dfs/Boards", "a")
    Results = open("results/dfs/Results", "a")
    print(board)

    moves = ['up', 'down', 'left', 'right']
    goal_board = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]).reshape(4,4)
    queue = [puzzle(0, board)]
    Number = 0
    explored = []
    
    while queue:
        currentBoard = queue.pop()
        #Printed_Board.write(f"{currentBoard.board}\n")


        if currentBoard.board.tolist() == goal_board.tolist():
            break
        for x in moves:
            
            #print(move.move(x,currentBoard.board))
            possible, m = move.move(x,currentBoard.board)
            
            
            if possible is not "None" and possible.tolist() not in explored:
                #print(m)
                Printed_Board.write(f"{possible}\n")

                ListMoves = ListMoves + m
                number =+ 1
                queue.append(puzzle(number, possible))
                if possible.tolist() == goal_board.tolist():
                    break

        explored.append(currentBoard.board.tolist())
    stop = timeit.default_timer()
    total_Memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    execucation_time = stop - start
    Results.write(f"Moves: {ListMoves}\nTime: {execucation_time}\nNodes explored: {len(explored)}\nMemory Used: {total_Memory}" )
