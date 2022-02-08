from asyncio import futures
from xml.dom.minidom import Element
import numpy as np
#import sys
#sys.path.insert(0, '15-puzzle-problem/move/move.py')
import move.move as move
import timeit
import tracemalloc

class puzzle:
    def __init__(self, number, board, manhat, displaced):
        self.number = number
        self.board = board
        self.manhatten = manhat
        self.displaced = displaced

def hs(board):
    goal_board = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]).reshape(4,4)
    #print(board, goal_board)
    #board1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,0,15]).reshape(4,4)
    man_score1 = manhattan(board, goal_board)
    dis_score1 = displacement(board, goal_board)

    start = timeit.default_timer()
    tracemalloc.start()
    ListMoves = ""
    Printed_Board = open("results/h/Boards", "a")
    Results = open("results/h/Results", "a")
    print(board)

    moves = ['up', 'down', 'left', 'right']
    queue = [puzzle(0, board, man_score1, dis_score1)]
    Number = 0
    explored = []
    current_exploration = []
    all = []
    #print(queue)
    while queue:
        print(all)
        #print(queue)
        currentBoard = queue.pop(0)
        #Printed_Board.write(f"{currentBoard.board}\n")


        if currentBoard.board.tolist() == goal_board.tolist():
            break
        for x in moves:

            possible, m = move.move(x,currentBoard.board)
             
            if possible is not "None" and possible.tolist() not in explored:

                Printed_Board.write(f"{possible}\n")

                ListMoves = ListMoves + m
                number =+ 1

                man_score = manhattan(possible, goal_board)
                dis_score = displacement(possible, goal_board)
                if possible.tolist() not in all:
                    current_exploration.append(puzzle(number, possible, man_score, dis_score))
                    all.append(possible.tolist())
                if possible.tolist() == goal_board.tolist():
                    break
                
            #print(current_exploration)

        sortedL = sorted(current_exploration, key=lambda x: x.manhatten)     
        
        
        explored.append(currentBoard.board.tolist())
        queue[:0] = sortedL

        #print(sortedL)
        sortedL.clear()
        #print(sortedL)

        


    stop = timeit.default_timer()
    total_Memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    execucation_time = stop - start
    Results.write(f"Moves: {ListMoves}\nTime: {execucation_time}\nNodes explored: {len(explored)}\nMemory Used: {total_Memory}" )

def manhattan(current, goal):
    distance = 0
    for x in goal.flatten().tolist():
        goals = np.where(goal == x)
        currents = np.where(current == x)
        distance += abs(currents[0][0] - goals[0][0])
        distance += abs(currents[1][0] - goals[1][0])
    return(distance)

def displacement(current, goal):
    displaced = 0
    for x in goal.flatten().tolist():
        goals = np.where(goal == x)
        currents = np.where(current == x)
        if goals[0][0] != currents[0][0] or goals[1][0] != currents[1][0]:
            displaced += 1
    return(displaced)
