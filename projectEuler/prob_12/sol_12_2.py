import time


def num_divisors(n):
    if n % 2 == 0:
        n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors


def triangular_index(limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n+1)
    while lnum * rnum < limit:
        n += 1
        lnum, rnum = rnum, num_divisors(n+1)
    return n


if __name__ == "__main__":
    N = [1, 2, 3, 4]
    for n in N:
        start = time.time()
        index = triangular_index(n + 1)
        triangle = int((index * (index + 1)) / 2)
        elapsed = (time.time() - start)
        print("result {} returned in {} seconds.".format(triangle, elapsed))
