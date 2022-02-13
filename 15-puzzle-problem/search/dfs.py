import numpy as np
import move.move as move
import timeit
import tracemalloc

class puzzle:
    """
    A class used to represent each node of the puzzle
    """

    def __init__(self, number, board):
        """
        Parameters
        ----------
        number : int
            Identifier based on increment of node
        board : numpy array
            Current position of the board
        """

        self.number = number
        self.board = board

def dfs(board):
    """
    Gets starting board and loops till it finds the goal board using depth first search which
    continually explores one branch until it has no moves left
    
    Parameters
    ----------
    board : numpy array
        starting node (either random or set board from assignment)
    """

    #starting incrementation and writing files
    start = timeit.default_timer()
    tracemalloc.start()
    ListMoves = ""
    Printed_Board = open("results/dfs/Boards", "a")
    Results = open("results/dfs/Results", "a")

    print(board)

    moves = ['up', 'down', 'left', 'right']
    goal_board = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]).reshape(4,4)
    
    Number = 0
    queue = [puzzle(Number, board)]
    

    explored = []
    exploredDict = {}
    while queue:
        currentBoard = queue.pop()
        """
        Will run until stack is empty or if goal state is found where it will break
        """

        if currentBoard.board.tolist() == goal_board.tolist():
            break

        for x in moves:
            """
            Tests moving empty puzzle slot up, down, left, right. If it has already been expolored it is skiped
            """

            possible, m = move.move(x,currentBoard.board)
            
            #if possible is not None and possible.tolist() not in explored:
            if possible is not None and possible.tobytes() not in exploredDict:
                Printed_Board.write(f"{possible}\n")

                ListMoves = ListMoves + m
                Number += 1
                
                #add to the current puzzle object to the stack
                queue.append(puzzle(Number, possible))

                #if the goal is found break out for loop, and then break out while loop
                if possible.tolist() == goal_board.tolist():
                    break

        #add to explored list of boards seen
        #explored.append(currentBoard.board.tolist())
        exploredDict[currentBoard.board.tobytes()] = Number

    stop = timeit.default_timer()
    total_Memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    execucation_time = stop - start
    Results.write(f"Moves: {ListMoves}\nTime: {execucation_time}\nNodes explored: {len(explored)}\nMemory Used: {total_Memory}" )
