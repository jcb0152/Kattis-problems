# Task: Given a list of numbers, compute a sequence of stack operations to product the list.
# Stack operations are: '1': push 1 onto stack; 'd': duplicate top of stack; '+': add top two numbers on stack; decrement all others by 1
# Strategy: Create stack from top to bottom (right to left). For each number, convert the binary string into stack operations.
# start with "1". Then, "d+" is equal to shifting the string left, or doubling the number. "1+" is equal to adding 1 to the number.
# Keep track of "+" operations, and add the number of them to lower numbers on the stack.
cases = int(input())
nums = input().split()

inst = []
extra = 0
for num in nums[::-1]:
    # Compute the binary representation of the current number plus the "+" operations used on numbers above is in the stack.
    tmp = "{0:b}".format(int(num) + extra)
    # Start with 1. For 0s: double the number. For 1s: double the number and add 1
    tmp = "1" + tmp[1:].replace("0", "d+").replace("1", "d+1+")
    inst.append(tmp)
    # Count the number of "+" characters added to form this number.
    extra += tmp.count("+")

# Print the stack operations in the correct order (bottom to top)
ans = "".join(inst[::-1])
print(ans)
