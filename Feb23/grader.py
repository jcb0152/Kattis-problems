from collections import deque

(lines, err) = input().split()
lines = int(lines)
err = int(err)

err_num = deque([int(x) for x in input().split()])

errors = []
while (len(err_num) > 0):
    prev = err_num.popleft()
    start = prev
    while(len(err_num) > 0 and err_num[0] == prev + 1):
        prev = err_num.popleft()
    end = prev

    errors.append((start, end))

correct = []
format_err = []
prev = 1

for group in errors:
    if ((group[0] - 1) > 0):
        correct.append((prev, group[0] - 1))
    prev = group[1] + 1

    if group[0] == group[1]:
        format_err.append(f"{group[0]}")

    else:
        format_err.append(f"{group[0]}-{group[1]}")

if (prev != lines + 1):
    correct.append((prev, lines))

format_cor = []
for group in correct:
    if group[0] == group[1]:
        format_cor.append(f"{group[0]}")

    else:
        format_cor.append(f"{group[0]}-{group[1]}")
    
err_str = "Errors: "
if len(format_err) == 1:
    err_str += format_err[0]
else:
    err_str += ", ".join(x for x in format_err[:-1])
    err_str += f" and {format_err[-1]}"
    
cor_str = "Correct: "
if len(format_cor) == 1:
    cor_str += format_cor[0]
else:
    cor_str += ", ".join(x for x in format_cor[:-1])
    cor_str += f" and {format_cor[-1]}"

print(err_str)
print(cor_str)

