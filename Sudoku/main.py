import numpy as np
import Tasks.backtracking as dt

def main():
    dif = input("easy, medium, hard, evil: ")
    s_puzzle = puzzle(dif)

    print(s_puzzle)
    dt.backtracking(s_puzzle)

def puzzle(choice):
    if choice == "easy":
        ### Easy Puzzle
        easy = np.array([[0, 3, 0, 0, 8, 0, 0, 0, 6],
                [5, 0, 0, 2, 9, 4, 7, 1, 0],
                [0, 0, 0, 3, 0, 0, 5, 0, 0],
                [0, 0, 5, 0, 1, 0, 8, 0, 4],
                [4, 2, 0, 8, 0, 5, 0, 3, 9],
                [1, 0, 8, 0, 3, 0, 6, 0, 0],
                [0, 0, 3, 0, 0, 7, 0, 0, 0],
                [0, 4, 1, 6, 5, 3, 0, 0, 2],
                [2, 0, 0, 0, 4, 0, 0, 6, 0]])
        return easy
    elif choice == "medium":
        ### Medium puzzle
        medium = np.array([[3, 0, 8, 2, 9, 6, 0, 0, 0],
                [0, 4, 0, 0, 0, 8, 0, 0, 0],
                [5, 0, 2, 1, 0, 0, 0, 8, 7],
                [0, 1, 3, 0, 0, 0, 0, 0, 0],
                [7, 8, 0, 0, 0, 0, 0, 3, 5],
                [0, 0, 0, 0, 0, 0, 4, 1, 0],
                [1, 2, 0, 0, 0, 7, 8, 0, 3],
                [0, 0, 0, 8, 0, 0, 0, 2, 0],
                [0, 0, 0, 5, 4, 2, 1, 0, 6]])
        return medium
    elif choice == "hard":
        ### Hard Puzzle
        hard   = np.array([[7, 0, 0, 0, 0, 0, 0, 0, 0],
                [6, 0, 0, 4, 1, 0, 2, 5, 0],
                [0, 1, 3, 0, 9, 5, 0, 0, 0],
                [8, 6, 0, 0, 0, 0, 0, 0, 0],
                [3, 0, 1, 0, 0, 0, 4, 0, 5],
                [0, 0, 0, 0, 0, 0, 0, 8, 6],
                [0, 0, 0, 8, 4, 0, 5, 3, 0],
                [0, 4, 2, 0, 3, 6, 0, 0, 7],
                [0, 0, 0, 0, 0, 0, 0, 0, 9]])
        return hard
    elif choice == "evil":
        ### EVIL Puzzle
        evil   = np.array([[0, 6, 0, 8, 0, 0, 0, 0, 0],
                [0, 0, 4, 0, 6, 0, 0, 0, 9],
                [1, 0, 0, 0, 4, 3, 0, 6, 0],
                [0, 5, 2, 0, 0, 0, 0, 0, 0],
                [0, 0, 8, 6, 0, 9, 3, 0, 0],
                [0, 0, 0, 0, 0, 0, 5, 7, 0],
                [0, 1, 0, 4, 8, 0, 0, 0, 5],
                [8, 0, 0, 0, 1, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 5, 0, 4, 0]])
        return evil
    else:
        print("No difficulty selected, restart program")
        quit()


if __name__ == "__main__":
    main()