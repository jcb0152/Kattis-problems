# Task: Determine if there is an equal number of "|" characters on each side of the "()" characters
# Strategy: Count number of "|" characters before "(" character. Then, compare to amount of "|" characters in the string.
x = input()

lhs = x.index("(")
# See if lhs equals half of the "|" characters in the string
if (len(x) - 2) / 2 != lhs:
    print("fix")
else:
    print("correct")

