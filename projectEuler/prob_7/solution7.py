# Project Euler #7: 10001st prime
# What is the Nth prime number?


from math import sqrt


def find_prime(n, primes):
    x = primes[len(primes) - 1]
    while len(primes) < n:
        x += 2
        y = int(sqrt(x))
        count = 0
        for i in primes:
            if i > y:
                count = 0
                break
            if x % i == 0:
                count = 1
                break
        if count == 0:
            primes.append(x)
    return primes


if __name__ == "__main__":
    primes = [2, 3]
    n = [3, 5]
    for i in n:
        if len(primes) < i:
            primes = find_prime(i, primes)
        print(primes[i-1])
