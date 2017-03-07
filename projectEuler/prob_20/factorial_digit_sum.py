# Project Euler #20: Factorial digit sum
# Find the sum of the digits in the number N!

from math import factorial


def add_factorial(n):
    fact_l = [int(i) for i in str(factorial(n))]
    return sum(fact_l)

t = int(input())
nums = []
for _ in range(t):
    n = int(input())
    nums.append(n)


for n in nums:
    print(add_factorial(n))
