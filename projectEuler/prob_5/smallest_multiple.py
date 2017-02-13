# Project Euler #5: Smallest multiple
# What is the smallest positive number that is evenly divisible(divisible
# with no remainder) by all of the numbers from 1 to N ?


def multiple(m, n):
    '''
    m ---> int
    n ---> inclusive upper limit for range
    if m is divisible by n returns True; False otherwise
    '''
    checklist = [i for i in range(1, n+1) if m % i == 0]
    if len(checklist) == n:
        return True
    return False


def smallest_multiple(n):
    m = n
    while True:
        if multiple(m, n):
            return m
        m += 1

if __name__ == "__main__":
    n = [3, 10]
    for N in n:
        print(smallest_multiple(N))
