cases = int(input())
nums = input().split()

inst = []
extra = 0
for num in nums[::-1]:
    tmp = "{0:b}".format(int(num) + extra)
    tmp = "1" + tmp[1:].replace("0", "d+").replace("1", "d+1+")
    inst.append(tmp)
    extra += tmp.count("+")

ans = "".join(inst[::-1])
print(ans)
