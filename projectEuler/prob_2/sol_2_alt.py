# Project Euler #2: Even fibonacci Sequence
# t ---> nos of test cased
# n ---> list of N (inclusive upper limit for fibonacci Sequence)


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    # constraint is 10 <= N <= 4 * (10 ** 16)
    # N is the inclusive upper limit of an fiboncci seq
    fib_seq = [1, 2]
    total = 2
    ans = []
    while(fib_seq[-1] + fib_seq[-2] <= n):
            fib_seq.append(fib_seq[-2] + fib_seq[-1])
            if fib_seq[-1] % 2 == 0:
                total += fib_seq[-1]
    print(total)
