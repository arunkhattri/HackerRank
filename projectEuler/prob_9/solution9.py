# Project Euler #9: Special Pythagorean triplet
# Given N, check if there exists any pythagorean triplet for which
# a + b + c = N
# find maximum possible value of abc among all such pythagorean triplets,
# if there is no such pythagorean triplet print -1


def possible_comb(N):
    '''
    a < b < c
    a ** a + b ** b == c ** c
    a + b + c = N
    '''
    comb = []
    nums = [i for i in range(1, int(N/2) + 1)]
    for i in nums:
        a = int(i)
        c = int((2 * N * a - (2 * a * a) - (N * N)) / (2 * (a - N)))
        b = int(N - c - a)
        A = a * a
        B = b * b
        C = c * c
        if a < b and b < c and (a + b + c == N) and (A + B == C):
            comb.append((a * b * c))
    return comb


if __name__ == "__main__":
    N = [12, 4]
    for n in N:
        ans = possible_comb(n)
        if ans == []:
            print(-1)
        else:
            print(max(ans))
