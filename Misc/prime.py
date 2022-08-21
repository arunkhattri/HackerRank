# generating prime numbers


import itertools


def erastosthenes_sieve():
    '''
    Yields the sequence of prime numbers via the Sieve of Erastosthenes.
    '''
    # map each composite integer to its first found prime factor
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, 10000, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x & 1):
                x += p
            D[x] = p


ans = {k: v for k, v in list(enumerate(erastosthenes_sieve(), start=1))}
if __name__ == "__main__":
    n = [3, 5]
    for N in n:
        print(ans[N])
