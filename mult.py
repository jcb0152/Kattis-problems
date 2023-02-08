num = int(input())

first = 0
change = True
for _ in range(num):
    tmp = int(input())

    if change:
        change = False
        first = tmp
        continue

    if tmp % first == 0:
        print(tmp)
        change = True
