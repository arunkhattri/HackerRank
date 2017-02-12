# Project Euler #3: Largest prime factor
# What is the largest prime factor of a given number ?
# NOTE: working solution
from math import ceil, sqrt

def factor(n):
    # Sundaram sieve
    # https://plus.maths.org/content/os/issue50/features/havil/index
    if n <= 1:
        return []
    # generator expression
    prime = next((x for x in range(2, ceil(sqrt(n))+1)if n % x == 0), n)
    # recursive call
    return([prime] + factor(n//prime))

def largest_prime_factor(n):
    return(max(factor(n)))


if __name__ == "__main__":
    n = [10, 17, 24, 25, 27, 13195]
    for N in n:
        print("Largest Prime Factor of {} is: {}".format(N, largest_prime_factor(N)))
