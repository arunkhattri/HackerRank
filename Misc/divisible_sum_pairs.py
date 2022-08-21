# -*- coding: utf-8 -*-, #!/bin/python3
"""
Created on Wed May 25 00:11:47 2016
@author: Arun Kr. Khattri
Problem:
n, k ---> Nos. of element, divisor (space seperated integers)
a ------>n space seperated integers
Print the number of(i,j) pairs where i < j  and a_i + a_j is evenly
divisible by k .
"""


def divisible_sum_pairs(n, k, a):
    res = []
    initial_value = 0
    while initial_value < len(a):
        elem = initial_value + 1
        for j in range(elem, len(a)):
            if (a[initial_value] + a[j]) % k == 0:
                res.append((initial_value, j))
        initial_value += 1
    return (len(res))

if __name__ == "__main__":
    n, k = input("\nEnter n and k space-separated integers: "). \
           strip().split(' ')
    n, k = [int(n), int(k)]
    a = [int(a_temp) for a_temp in input("\nEnter n space-separated int: ").
         strip().split(' ')]
    print("Total Divisible Sum Pairs: {}".format(divisible_sum_pairs(n, k, a)))
