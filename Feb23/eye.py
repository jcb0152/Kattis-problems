x = input()

lhs = x.index("(")
if (len(x) - 2) / 2 != lhs:
    print("fix")
else:
    print("correct")

