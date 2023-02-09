# Task: Determine first number in a sequence that is a multiple of the starting number. Start a new sequence after a multiple is found.
# Strategy: Calculate (modulo n) for each integer in the sequence. Use new n after multiple is found.
num = int(input())

# Store modulo base in first. Set change flag if the next number will change the modulo base.
first = 0
change = True
for _ in range(num):
    tmp = int(input())

    if change:
        change = False
        first = tmp
        continue

    # When a multiple is found, print it and indicate that a new sequence is starting.
    if tmp % first == 0:
        print(tmp)
        change = True
