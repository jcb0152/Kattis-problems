import math

num = int(input())

ans = 1
counter = 1

primes = []

while True:
    x = math.gcd(ans, counter)
        
    tmp = ans * counter

    if tmp > num:
        break
    
    if x == 1 and counter != 1:
        ans = tmp
        primes.append(counter)
    counter += 1
    
frac = ans
for i in primes:
    frac *= ((i - 1) / i)
    frac = round(frac)

frac = ans - frac
common = math.gcd(frac, ans)
numer = round(frac / common)
denom = round(ans / common)

print(f"{numer}/{denom}")
