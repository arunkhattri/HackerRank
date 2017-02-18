# Project Euler #8: Largest product in a series
# Find the greatest product of K consecutive digits in the N digit number.
# Constraints:
# 1 <= T <= 100
# 1 <= K <= 7
# K <= N <= 1000

from functools import reduce
import operator


def largest_product_in_a_series(n, k, num):
    '''
    num ---> int, digit
    n -----> int, number of digits in num
    k -----> int, consecutive digits
    return greatest product of k consecutive digit in n digit num
    '''
    num_l = [int(i) for i in str(num)]
    sum_l = [reduce(operator.mul, num_l[i:i+k], 1) for i in range(n) if i < (n-(k-1))]
    return(max(sum_l))


if __name__ == "__main__":
    t = 2
    N = [10, 10]
    K = [5, 5]
    Num = [3675356291, 2709360626]
    for i in range(t):
        n, k, num = N[i], K[i], Num[i]
        print(largest_product_in_a_series(n, k, num))
