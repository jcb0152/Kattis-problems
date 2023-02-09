# Task: Identify number(s) closest to input number with no digits in common
def main():
    num = str(int(input()))
    digits = [str(x) for x in range(10)]
    
    # Identify which digits are not used by input number, sorted from high to low
    uni_digits = set(digits)
    uni_num = set(num)
    
    available = uni_digits.difference(uni_num)
    a_nums = list(available)
    a_nums.sort(reverse=True)
    
    # Early exit if all digits are used by input number
    if len(a_nums) == 0:
        return "Impossible"
        
    # Find closest number less than input number
    # First digit is the largest available number less than the first digit of the input number
    low_ans = ""
    for i in reversed(range(0, int(num[0]))):
        i = str(i)
        if i in available:
            low_ans += i
            break
    # If all digits less than the first digit of the input number are used, 
    # the first digit is a 0, which will be removed in the integer conversion
    else:
        low_ans = "0"
        
    # All remaining digits are the largest digits not used by the input number
    low_ans += a_nums[0] * (len(num) - 1)
    
    # Find closest number greater than input number
    high_ans = ""
    for i in range(int(num[0]), 10):
        i = str(i)
        if i in available:
            high_ans += i
            break
    # If no digits greater than the first digit of the input number are available, 
    # choose the lowest available number. If 0 is available, start with the 2nd-lowest and a 0 (e.g. "10")
    else:
        if a_nums[-1] == "0":
            if len(a_nums) > 1:
                high_ans = a_nums[-2] + a_nums[-1]
            # If only 0 is available, it is impossible to make a number higher than the input number without repeating digits
            else:
                high_ans = -1
        else:
            high_ans = a_nums[-1] * 2
        
    if high_ans != -1:
        high_ans += a_nums[-1] * (len(num) - 1)

    # Determine which of the numbers is closer to the input number
    low_ans = int(low_ans)
    high_ans = int(high_ans)
    num = int(num)
    if high_ans == -1:
        return str(low_ans)
    
    if abs(high_ans - num) > abs(num - low_ans):
        return str(low_ans)

    if abs(high_ans - num) < abs(num - low_ans):
        return str(high_ans)

    return f"{low_ans} {high_ans}"

if __name__ == "__main__":
    print(main())
