# Project Euler #2: Even fibonacci Sequence
# t ---> nos of test cased
# n ---> list of N (inclusive upper limit for fibonacci Sequence)
#===========================
# NOTE: failing test case: 3
#===========================

import math

def even_fibonacci_numbers(t, n):
    # http://www.python-course.eu/python3_memoization.php

    def memoize(f):
        memo = {}
        def helper(x):
            if x not in memo:
                memo[x] = f(x)
            return memo[x]
        return helper

    @memoize
    def fib(n):
        golden_ratio = (1 + math.sqrt(5)) / 2
        fib_seq = (golden_ratio ** n - (1 - golden_ratio) ** n) / math.sqrt(5)
        return int(fib_seq)


    ans = []
    i = 2
    for N in n:
        i = 2
        total = 0
        temp_count = fib(i)
        while temp_count <= N:
            if fib(i) % 2 == 0:
                total += (fib(i))
            i += 1
            temp_count = fib(i)
        ans.append(total)
    return ans


if __name__ == "__main__":
    t = 2
    n = [10, 100]
    ans = even_fibonacci_numbers(t, n)
    for a in ans:
        print(a)
