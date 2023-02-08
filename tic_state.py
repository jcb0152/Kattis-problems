cases = int(input())

for _ in range(cases):
    num = str(bin(int(input(), 8)))[2:]

    num = "0"*(19-len(num)) + num

    num = num[::-1]

    filled = num[0:9]
    x = num[9:18]
    turn = num[18]

    win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

    for tup in win:
        if filled[tup[0]] == "0" or filled[tup[1]] == "0" or filled[tup[2]] == "0":
            continue

        if x[tup[0]] == x[tup[1]] and x[tup[0]] == x[tup[2]]:
            winner = "X"
            if x[tup[0]] == "0":
                winner = "O"

            print(f"{winner} wins")
            break
    else:
        if sum([int(i) for i in filled]) == 9:
            print("Cat\'s")
        else:
            print("In progress")
