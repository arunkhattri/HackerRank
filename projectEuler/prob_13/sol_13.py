# Project Euler #13: Large sum

# Work out the first ten digits of the sum of N 50 digit numbers.


def sum_50digit(N):
    '''
    N ---> list of 50 digit number
    returns first 10 digits of the final sum
    '''
    S = str(sum(N))
    s = ''
    for i in range(10):
        s += S[i]
    return s


if __name__ == "__main__":
    N = [37107287533902102798797998220837590246510135740250,
         46376937677490009712648124896970078050417018260538,
         74324986199524741059474233309513058123726617309629,
         91942213363574161572522430563301811072406154908250,
         23067588207539346171171980310421047513778063246676]
    ans = 2728190129

    if sum_50digit(N) == str(ans):
        print("Test Pass Successfully")
    else:
        print("come back with your coffee, job yet not finished...")
