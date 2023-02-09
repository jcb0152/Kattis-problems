num = int(input())

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

    if len(line) > 1 and line[2] == "then":
        o_cond.append(tuple(line[1::2]))
        toppings.update(line[1::2])
        continue

    required.extend(line)
    toppings.update(line)

top_dict = {x: 2 ** i for (i, x) in enumerate(list(toppings))}
chosen = 0

for i in required:
    chosen |= top_dict[i]

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

prev = 0
ignore = set()
while (prev != chosen):
    prev = chosen
    for tup in o_bits:
        if tup in ignore:
            continue
        if ((tup[0] & chosen) != 0):
            chosen |= top_dict[tup[1]]
            ignore.add(tup)

    for tup in a_bits:
        if tup in ignore:
            continue
        if ((chosen | ~tup[0]) == -1):
            chosen |= top_dict[tup[1]]
            ignore.add(tup)

print(bin(chosen).count("1"))
            
            
