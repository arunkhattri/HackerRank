# Project Euler #4: Largest palindrome product 
# Find the largest palindrome made from the product of two 3-digit numbers
# which is less than N.


def is_pal(n):
    '''
    Assumes n is an int
    Returns True if n is a Palindrome; False otherwise
    '''
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


def pal_number(n):
    if is_pal(n):
        for i in range(100, 1000):
            if n % i == 0 and len(n // i) == 3:
                return(n)
            else:
                continue
    else:
        n -= 1

if __name__ == "__main__":
    n = [101110, 800000]
    for N in n:
        print("largest palindrome: {}".format(pal_number(N)))
