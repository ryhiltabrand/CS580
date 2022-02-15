import numpy as np
import move.move as move
import timeit
import tracemalloc

class puzzle:
    """
    A class used to represent each node of the puzzle
    """
    
    def __init__(self, number, board, manhat, displaced):
        """
        Parameters
        ----------
        number : int
            Identifier based on increment of node
        board : numpy array
            Current position of the board
        Manhatten : int
            The score of manhatten distance of the current board
        displaced : int
            The sum of pieces in the wrong position on board
        """

        self.number = number
        self.board = board
        self.manhatten = manhat
        self.displaced = displaced

def hs(board):
    """
    Gets starting board and loops till it finds the goal board using 
    informed search by using heuristics based on manhatten distance and amount of puzzle pieces in the worng location
    
    Parameters
    ----------
    board : numpy array
        starting node (either random or set board from assignment)
    """

    #the board which we want to end with
    goal_board = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]).reshape(4,4)

    #manhatten and displacement scores of the first node
    man_score1 = manhattan(board, goal_board)
    dis_score1 = displacement(board, goal_board)

    #starting incrementation and writing files
    start = timeit.default_timer()
    tracemalloc.start()
    ListMoves = ""
    Printed_Board = open("results/h/Boards", "a")
    Results = open("results/h/Results", "a")
    #queue = [puzzle(0, board, man_score1, dis_score1)]
    Number = 0
    queue = {Number: puzzle(0, board, man_score1, dis_score1)}
    explored = []
    exploredDict = {}

    moves = ['up', 'down', 'left', 'right']
    
    while queue:
        """
        Will run until  queue is empty or if goal state is found where it will break
        """
        
        #Take lead of queue as it will have the lowest score
        #currentBoard = queue.pop(0)
        min_value = min(queue.keys())
        currentBoard = queue.pop(min_value)
        
        
        #breaks loop if we find goal state
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

                man_score = manhattan(possible, goal_board)
                dis_score = displacement(possible, goal_board)

                #add the current puzzle to the queue
                #queue.append(puzzle(Number, possible, man_score, dis_score))
                queue[man_score+dis_score]=puzzle(Number, possible, man_score, dis_score)

                #if it the goal is found break out for loop, and then break out while loop
                if possible.tolist() == goal_board.tolist():
                    break
                
        #add to explored list of boards seen
        #explored.append(currentBoard.board.tolist())
        exploredDict[currentBoard.board.tobytes()] = Number
        #sort the quese with the lowest manhatten and displaced score at the front

        #queue.sort(key=lambda x: x.manhatten + x.displaced)
           

    #end incrementation and print output
    stop = timeit.default_timer()
    total_Memory = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    execucation_time = stop - start
    Results.write(f"Moves: {ListMoves}\nTime: {execucation_time}\nNodes explored: {len(explored)}\nMemory Used: {total_Memory}" )

def manhattan(current, goal):
    """
    Takes the current and goal board and finds the manhatten distance

    Parameters
    ----------
    current : numpy array
        The current puzzle node
    goal : numpy array
        The goal puzzle node

    Returns
    -------
    int
        Manhattan distance between the current node and the goal node
    """

    distance = 0

    for x in goal.flatten().tolist():
        """
        Iterates through list of the goal array and finds the absolute value of the x and y component of each puzzle piece
        """
        goals = np.where(goal == x)
        currents = np.where(current == x)
        distance += abs(currents[0][0] - goals[0][0])
        distance += abs(currents[1][0] - goals[1][0])

    return(distance)

def displacement(current, goal):
    """
    Takes the current and goal board and finds the manhatten distance

    Parameters
    ----------
    current : numpy array
        The current puzzle node
    goal : numpy array
        The goal puzzle node

    Returns
    -------
    int
        number of puzzle pieces in the wrong position
    """
    
    displaced = 0
    for x in goal.flatten().tolist():
        """
        Iterates through list of the goal array and adds to the sum if the position does not match the goal state
        """
        goals = np.where(goal == x)
        currents = np.where(current == x)
        if goals[0][0] != currents[0][0] or goals[1][0] != currents[1][0]:
            displaced += 1
    return(displaced)
