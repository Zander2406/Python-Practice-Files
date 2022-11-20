"""
Step 1: Identify an empty square

Step 2: Place a number

Step 3: Check if that number is repeated

Step 4: Proceed if the number is not repeated

Step 5: Check next square
"""

"""
Flow of the program

We check for an empty square

We loop through all possible answers

Check if the answer is valid for that square for the time being

If the answer is valid we place it in the square

And move on to the next square until we find a solution or hit an invalid placement

If an invalid solution is reached we reset our position until we find the place where the problem arised

If no answer can be placed we move back until we run out of a place to move where we can say there is no solution
"""

def display_board(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            print(board[row][col], end=" ")
        print()


def is_valid(board, row, col, number):
    for i in range(len(board)):
        if board[i][col] == number:
            return False

        if board[row][i] == number:
            return False

        if board[3 * int(row / 3) + int(i / 3)][3 * int(col / 3) + int(i % 3)] == number:
            return False
    
    return True


def solve(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                for number in range(1, 10):
                    if is_valid(board, row, col, number):
                        board[row][col] = number
                        if solve(board):
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True


if __name__=='__main__':
    board_1 = [
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 7, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 8, 0, 0, 4, 0, 0, 1, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 8, 0],
        [5, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0]
    ]

    board_2 = [
        [0, 0, 7, 0, 4, 0, 0, 3, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 6, 0, 0, 0],
        [0, 2, 0, 6, 0, 0, 1, 0, 0],
        [0, 3, 0, 9, 0, 0, 0, 0, 5],
        [4, 0, 0, 0, 0, 0, 0, 8, 6],
        [0, 5, 0, 0, 2, 1, 0, 0, 8],
        [7, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0]
    ]

    board = board_2

    print("Initial Board: ")
    display_board(board)
    solve(board)
    print("Solved Board: ")
    display_board(board)









































