# Task: Given a tic-tac-toe board as an octal number, determine the current state of the game (x win, o win, cat's game, in progress)
# Strategy: Parse input, then compare indicies of values in potential winning positions
cases = int(input())

for _ in range(cases):
    # Parsing input
    num = str(bin(int(input(), 8)))[2:]

    num = "0"*(19-len(num)) + num

    num = num[::-1]

    filled = num[0:9]
    x = num[9:18]
    turn = num[18]

    # Array of potential winning positions
    win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

    for tup in win:
        # Check if all values in each winning position are occupied.
        if filled[tup[0]] == "0" or filled[tup[1]] == "0" or filled[tup[2]] == "0":
            continue

        # If values in each winning position are equal, determine winner.
        if x[tup[0]] == x[tup[1]] and x[tup[0]] == x[tup[2]]:
            winner = "X"
            if x[tup[0]] == "0":
                winner = "O"

            print(f"{winner} wins")
            break
    else:
        # If all spaces are filled with no winner, it is a cat's game.
        if sum([int(i) for i in filled]) == 9:
            print("Cat\'s")
        # Otherwise, it is in progress.
        else:
            print("In progress")
