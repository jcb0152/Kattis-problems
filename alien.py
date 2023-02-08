def main():
    num = str(int(input()))
    digits = [str(x) for x in range(10)]
    
    uni_digits = set(digits)
    uni_num = set(num)
    
    available = uni_digits.difference(uni_num)
    a_nums = list(available)
    a_nums.sort(reverse=True)
    
    if len(a_nums) == 0:
        return "Impossible"
        
    low_ans = ""
    for i in reversed(range(0, int(num[0]))):
        i = str(i)
        if i in available:
            low_ans += i
            break
    else:
        low_ans = "0"
        
    low_ans += a_nums[0] * (len(num) - 1)
    
    high_ans = ""
    for i in range(int(num[0]), 10):
        i = str(i)
        if i in available:
            high_ans += i
            break
    else:
        if a_nums[-1] == "0":
            if len(a_nums) > 1:
                high_ans = a_nums[-2] + a_nums[-1]
            else:
                high_ans = -1
        else:
            high_ans = a_nums[-1] * 2
        
    if high_ans != -1:
        high_ans += a_nums[-1] * (len(num) - 1)

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
