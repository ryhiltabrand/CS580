from xml.dom.minidom import Element
import numpy as np
import sys
sys.path.insert(0, '15-puzzle-problem/move/move.py')
import move.move as move

class puzzle:
    def __init__(self, number, board):
        self.number = number
        self.board = board

def bfs(board):
    f = open("results", "a")
    print(board)
    moves = ['up', 'down', 'left', 'right']
    goal_board = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]).reshape(4,4)

    queue = [puzzle(0, board)]
    Number = 0
    explored = []
    #print (queue[0])
    
    #found = False
    while queue:
        currentBoard = queue.pop()
        f.write(f"{currentBoard.board}\n")


        if currentBoard.tolist() == goal.board.tolist():
            print('winner winner chicken dinner')
        for x in moves:
            
            possible = move.move(x,currentBoard.board)
            #print(possible)
            
            if possible is not None and possible.tolist() not in explored:
                number =+ 1
                queue.append(puzzle(number, possible))

        explored.append(currentBoard.board.tolist())
            
        #print(len(explored))
        #explored.append(node.tolist())
        #queue.pop(0)
        #node = queue[0]