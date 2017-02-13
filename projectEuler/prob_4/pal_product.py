# Project Euler #4: Largest palindrome product
# Find the largest palindrome made from the product of two 3-digit
# numbers which is less than N.
# NOTE: working solution


def is_pal(n):
    '''
    Assumes n is an int,
    returns True is n is palindrome; False otherwise
    '''
    if str(n) == str(n)[::-1]:
        return True
    return False


def largest_pal(n):
    '''
    n ---> int, inclusive upper limit
    '''
    # pals = []
    pals = (i for i in range(n, 99999, -1) if is_pal(i))
    x = next(pals)
    while True:
        for i in range(100, 1000):
            if x % i == 0 and x // i < 1000:
                return x
        x = next(pals)
    # for i in range(n, 99999, -1):
    #    if is_pal(i):
    #        pals.append(i)

if __name__ == "__main__":
    n = [101110, 800000]
    for N in n:
        print("for {} largest palindrome is: {}".format(N, largest_pal(N)))
