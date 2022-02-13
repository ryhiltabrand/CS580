import search.bfs as BFS
import search.dfs as DFS
import search.heuristics as HS
import numpy as np

def main():
    """
    Asks for which type of search you want to use to solve the puzzle and puts it into the runner
    """

    print("What type of search do you want to perform on the puzzle?")
    searchType = input("Choose one: B (bfs), D (dfs), H (heurisitics)\n")
    runner(searchType)

def runner(choice):
    """
    Takes in the search choice and calls corresponding function.

    Parameters
    ----------
    choice : str
        The choice of search (B, b, D, d, H, h)
    """

    #To have random board uncomment below commented code and comment declared board
    #board = puzzle_board()
    board = np.array([1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(4,4)

    if choice == "B" or choice == "b":
        BFS.bfs(board)
    elif choice == "D" or choice == "d":
        DFS.dfs(board)
    elif choice == "H" or choice == "h":
        HS.hs(board)
    else:
        print("Run program again and select a proper type.")
        exit()

def puzzle_board():
    """
    Creates a random 4 by 4 board using numpy shuffle
    """
    board = np.arange(16)
    np.random.shuffle(board)
    board = np.reshape(board, (4,4))
    
    return board



if __name__ == "__main__":
    main()