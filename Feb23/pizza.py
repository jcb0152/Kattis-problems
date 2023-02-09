# Task: Given a list of required and conditional (and/or chains) topping preferences, compute minimum number of toppings to satisfy all preferences.
# Strategy: Create bit string for each condition, where each bit represents one topping. Use bitwise operators to determine if condition is met.
# For or conditions: (condition and toppings) != 0 (at least one condition bit is set in topping list) 
# for and conditions: (condition or not toppings) == -1 (all condition bits are set in topping list)
# Iterate through all conditions until no new toppings are added.
num = int(input())

# Separate input conditions into list of required toppings, or-conditional toppings, and and-conditional toppings
# Also create a set of all toppings used.
required = []
a_cond = []
o_cond = []
toppings = set()
for _ in range(num):
    line = input().split()
    
    if len(line) > 1 and line[2] == "and":
        a_cond.append(tuple(line[1::2]))
        toppings.update(line[1::2])
        continue

    if len(line) > 1 and line[2] == "or":
        o_cond.append(tuple(line[1::2]))
        toppings.update(line[1::2])
        continue

    # If a condition only has one variable (if a then b), treat it as an or condition
    if len(line) > 1 and line[2] == "then":
        o_cond.append(tuple(line[1::2]))
        toppings.update(line[1::2])
        continue

    required.extend(line)
    toppings.update(line)

# Assign a bit to each topping.
top_dict = {x: 2 ** i for (i, x) in enumerate(list(toppings))}
chosen = 0

# Include all required toppings using the |= operator (bitwise or)
for i in required:
    chosen |= top_dict[i]

# Convert conditions into bit strings
a_bits = []
for t_list in a_cond:
    tmp = 0
    for top in t_list[:-1]:
        tmp |= top_dict[top]
    a_bits.append((tmp, t_list[-1]))

o_bits = []
for t_list in o_cond:
    tmp = 0
    for top in t_list[:-1]:
        tmp |= top_dict[top]
    o_bits.append((tmp, t_list[-1]))

# Iterate through conditions until topping choice remains unchanged.
# Ignore conditions that have already been satisfied
prev = 0
ignore = set()
while (prev != chosen):
    prev = chosen
    for tup in o_bits:
        if tup in ignore:
            continue
        # Or-conditions are met when at least one of the toppings has been chosen.
        # So, the bitwise and of the condition with the chosen toppings will be nonzero if any topping in the condition has been chosen.
        if ((tup[0] & chosen) != 0):
            chosen |= top_dict[tup[1]]
            ignore.add(tup)

    for tup in a_bits:
        if tup in ignore:
            continue
        # And-conditions are met when all of the toppings have been chosen.
        # So, the bitwise or of the condition with the inverse (bitwise not) of the chosen toppings will be equal to -1 if all toppings in the condition have been chosen.
        # Note: For signed 2's complement numbers, -1 = "11111..."
        if ((chosen | ~tup[0]) == -1):
            chosen |= top_dict[tup[1]]
            ignore.add(tup)

print(bin(chosen).count("1"))
            
            
