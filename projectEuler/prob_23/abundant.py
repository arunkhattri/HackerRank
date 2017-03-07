# Project Euler #23: Non-abundant sums
# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.
# Given N, print YES if it can be expressed as sum of two abundant numbers,
# else print NO.


# Project Euler # 23 Abundant Numbers
from math import ceil, sqrt


def divisors(n):
    ''' Return divisors of n'''
    # 1 is always a divisor
    yield 1
    upper_limit = ceil(sqrt(n))

    # for square numbers
    if upper_limit * upper_limit == n:
        yield upper_limit

    # for others
    for i in range(2, upper_limit):
        if n % i == 0:
            yield i
            yield n // i


def is_abundant(n):
    # smallest abundant number is 12, hence
    if n < 12:
        return False
    return(sum(divisors(n)) > n)

abundants = [i for i in range(1, 28124) if is_abundant(i)]


def sum_of_abundants(n):
    for i in abundants:
        if i > n:
            return False
        if (n - i) in abundants:
            return True
    return True


t = int(input())
N = []
for _ in range(t):
    n = int(input())
    N.append(n)

for n in N:
    if n > 28123:
        print('YES')
    elif sum_of_abundants(n):
        print('YES')
    else:
        print('NO')
