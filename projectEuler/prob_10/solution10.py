# Project Euler #10: Summation of primes
# find the sum of all the primes not greater than given N.

from math import sqrt


def primes(n=10 ** 6):
    ''' returns a list of primes less than n'''
    sieve = [True] * n
    p = 2
    while p <= int(sqrt(n)):
        if sieve[p]:
            for i in range(2 * p, n, p):
                sieve[i] = False
        p += 1
    sum_dict = {}
    s = 0
    for k in range(2, n):
        if sieve[k]:
            s += k
            sum_dict[k] = s
        else:
            sum_dict[k] = s

    # p_dict = {k: v for k, v in enumerate(p_list, start=1)}
    return sum_dict

if __name__ == "__main__":
    ans = primes()
    n = [5, 10]
    for N in n:
        print(ans[N])
