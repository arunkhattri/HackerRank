# Project Euler #3: Largest prime factor
# What is the largest prime factor of a given number ?
# NOTE: test case # 3,4 and 5 terminated due to timeout

def largest_prime_factor(n):
    prime = []

    # Memoization
    def memoize(f):
        memo = {}

        def helper(x):
            if x not in memo:
                memo[x] = f(x)
            return memo[x]
        return helper

    # prime test

    @memoize
    def is_prime(x):
        '''
        Assumes x is a non-negative int
        Returns True if x is a prime: False otherwise
        '''
        if x <= 1:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    for i in range(2, n+1):
        if is_prime(i) and n % i == 0:
            prime.append(i)
        else:
            continue
    return(max(prime))

if __name__ == "__main__":
    n = [10, 17]
    for i in n:
        ans = largest_prime_factor(i)
        print("Largest Prime factors of {}: \n{}".format(i, ans))
