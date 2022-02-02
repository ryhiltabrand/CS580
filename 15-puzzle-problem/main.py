import search.bfs as BFS
import search.dfs as DFS
import search.heuristics as HS
import numpy as np

def main():
    print("What type of search do you want to perform on the puzzle?")
    searchType = input("Choose one: B (bfs), D (dfs), H (heurisitics)\n")
    runner(searchType)

def runner(choice):
    board = puzzle_board()
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
    board = np.arange(16)
    np.random.shuffle(board)
    board = np.reshape(board, (4,4))
    
    return board



if __name__ == "__main__":
    main()