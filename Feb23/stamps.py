def check(case, arr1, arr2):
    for (i, val) in enumerate(arr1):
        i += 1
        if ((case - val) == 0):
            return True
        if ((case - val) in arr2 and arr2[(case - val)] < (len(arr2) - i)):
            return True
        if (case - val < 0):
            return False
    return False

(clusters, cases) = input().split()
clusters = int(clusters)
cases = int(cases)

nums = [int(i) for i in input().split()]

lsum = {nums[0]: 0}
total = nums[0]
for (i, val) in enumerate(nums[1:]):
    lsum[(val + total)] = (i + 1)
    total += val

rsum = {nums[-1]: 0}
total = nums[-1]
for (i, val) in enumerate(nums[::-1][1:]):
    rsum[(val + total)] = (i + 1)
    total += val

for _ in range(cases):
    case = int(input())

    if case == 0:
        print("Yes")
        continue
    
    if check(case, lsum, rsum):
        print("Yes")
        continue

    if check(case, rsum, lsum):
        print("Yes")
        continue

    print("No")
