import search.bfs as BFS
import search.dfs as DFS
import search.heuristics as HS
import sys

import search.bfs8 as bfs8
import search.dfs8 as dfs8
import search.heuristics8 as h8

import numpy as np

def main():
    """
    Asks for which type of search you want to use to solve the puzzle and puts it into the runner
    """
    puzzle = input("Do you want to run 8 or 15 puzzle (Enter 8 or 15): ")
    print("What type of search do you want to perform on the puzzle?")
    searchType = input("Choose one: B (bfs), D (dfs), H (heurisitics)\n")
    runner(puzzle, searchType)

def runner(p, choice):
    """
    Takes in the search choice and calls corresponding function.

    Parameters
    ----------
    choice : str
        The choice of search (B, b, D, d, H, h)
    """

    #To have random board uncomment below commented code and comment declared board
    if p == '15':
        board = puzzle_board(p)
        #board = np.array([1,2,3,4,5,6,7,8,9,10,11,12,0,13,15,14]).reshape(4,4)
        if choice == "B" or choice == "b":
            BFS.bfs(board)
        elif choice == "D" or choice == "d":
            DFS.dfs(board)
        elif choice == "H" or choice == "h":
            HS.hs(board)
        else:
            print("Run program again and select a proper type.")
            exit()
    elif p == '8':
        board = puzzle_board(p)
        if choice == "B" or choice == "b":
            bfs8.bfs(board)
        elif choice == "D" or choice == "d":
            dfs8.dfs(board)
        elif choice == "H" or choice == "h":
            h8.hs(board)
        else:
            print("Run program again and select a proper type.")
            exit()

def puzzle_board(p):
    """
    Creates a random 4 by 4 board using numpy shuffle
    """
    if p == '15':
        board = np.arange(16)
        np.random.shuffle(board)
        board = np.reshape(board, (4,4))
        return board
    else:
        board = np.arange(9)
        np.random.shuffle(board)
        board = np.reshape(board, (3,3))
        return board



if __name__ == "__main__":
    main()