# Task: Find the number with the greatest fraction of common factors less than the input number
# Strategy: Multiply prime numbers until almost past input number. Compute cototient of this number.
# Definitions: Totient = number of integers less than n coprime with n (count k in [1..n] where gcd(k, n) == 1)
# Cototient = number of integers less than n not coprime with n (count k in [1..n] where gcd(k, n) > 1)
import math

num = int(input())

ans = 1
counter = 1

primes = []

# Multiply prime numbers together, saving previous factors.
while True:
    x = math.gcd(ans, counter)
        
    tmp = ans * counter

    if tmp > num:
        break
    
    if x == 1 and counter != 1:
        ans = tmp
        primes.append(counter)
    counter += 1
   
# Compute totient using product(1-1/i) for each prime factor i
frac = ans
for i in primes:
    frac *= ((i - 1) / i)
    frac = round(frac)

# cototient = num - totient
frac = ans - frac
common = math.gcd(frac, ans)
numer = round(frac / common)
denom = round(ans / common)

print(f"{numer}/{denom}")
