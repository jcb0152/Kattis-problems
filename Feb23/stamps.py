# Task: Given a list of integers, determine if an input number can be reached by adding numbers from either end of the list.
# Strategy: Compute two arrays storing the sum of all numbers to the left or right of each number.
# For each input number n, iterate over the left-sum array, checking if (n - k) is in the right-sum array.

# Function to determine if a number can be reached.
# Note: Arrays given as dictionaries mapping sums to indicies for faster lookup time.
def check(case, arr1, arr2):
    # Iterate over left-sum array
    for (i, val) in enumerate(arr1):
        i += 1
        # Check if input number is in left-sum array
        if ((case - val) == 0):
            return True
        # Check if (input number - val) is in first (len - i) chars of right-sum array for each val in the left-sum array
        if ((case - val) in arr2 and arr2[(case - val)] < (len(arr2) - i)):
            return True
        # Early exit: If the number in the left-sum array is greater than the input number, it is not in either array.
        if (case - val < 0):
            return False
    return False

(clusters, cases) = input().split()
clusters = int(clusters)
cases = int(cases)

nums = [int(i) for i in input().split()]

# Compute left-sum and right-sum arrays as dictionaries.
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

    # Trivial case
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
