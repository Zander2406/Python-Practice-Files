"""
Step 1: Take input from user

Step 2: Generate random move for computer
Part A: Define the possible moves
Part B: Let the computer choose a move

Step 3: Print the winner
Part A: Determine the winner
Part B: Print the result
"""
import random
"""
Step 1
"""

your_move = input("Enter your move (R/P/S): ")


"""
Step 2
"""

"""
Step 2 Part A
"""

possible_moves = ["R", "P", "S"]

"""
Step 2 Part B
"""

computer_move = possible_moves[random.randint(0, 2)]

"""
Step 3
"""

"""
Step 3 Part A
"""

result = None

if your_move == "R" and computer_move == "P":
    result = "Computer"
elif your_move == "R" and computer_move == "S":
    result = "You"
elif your_move == "P" and computer_move == "R":
    result = "You"
elif your_move == "P" and computer_move == "S":
    result = "Computer"
elif your_move == "S" and computer_move == "R":
    result = "Computer"
elif your_move == "S" and computer_move == "P":
    result = "You"


"""
Step 3 Part B
"""

if result:
    print(f"{result} Win(s)!")
else:
    print("Draw!")



















