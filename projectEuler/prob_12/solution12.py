# Project Euler #12: Highly divisible triangular number
# What is the value of the first triangle number to have over N divisors?

import time
from math import ceil, sqrt
from collections import Counter
from functools import reduce
import operator


def nth_triangular(n):
    return(int(n * (n + 1) / 2))


# TODO:
# start with prime factorization


def prime_factor(n):
    if n <= 1:
        return []
    # generator expression
    prime = next((x for x in range(2, ceil(sqrt(n))+1)if n % x == 0), n)
    # recursive call
    return([prime] + prime_factor(n//prime))


# TODO:
# collections --> Counter to get freq of factors
# add 1 to freq


def freq_factor(n):
    ''' return list of freq of factors after adding 1'''
    d = Counter(prime_factor(n))
    l = list(d.values())
    new_l = [i + 1 for i in l]
    return new_l


# TODO:
# functools, operator --> reduce, mul
# multiply freq


def total_divisors(n):
    '''input ---> list of freq of factors, returned by freq_factor()
    output ---> int, number of divisors
    '''
    return(reduce(operator.mul, freq_factor(n), 1))


# def dict_td_triangular():
#     '''
#     n ---> int,
#     return dict{total_divisors: [triangular_numbers]}
#     '''
#     n = 10 ** 3
#     d = {}
#     i = 1
#     i_t = nth_triangular(i)
#     i_td = total_divisors(i_t)
#     # print("before while statement \ni:{}, i_t:{}, i_td:{}".format(i, i_t, i_td))
#     while i_td <= n:
#         # print("i:{}, i_t:{}, i_td:{}".format(i, i_t, i_td))
#         # if d.get(i_td, None):
#         #     d[i_td] = [i_t]
#         #     print("if statement d: {}".format(d))
#         # else:
#         l = d.get(i_td, [])
#         l.append(i_t)
#         d[i_td] = l
#         # print("else statement d: {}".format(d))
#         i += 1
#         i_t = nth_triangular(i)
#         i_td = total_divisors(i_t)
#     return d


def dict_keys():
    ''' list of keys in dict_td_triangular()'''
    return(list(index.keys()))


def index_dict():
    id = {}
    n = 1
    i = 1
    i_t = nth_triangular(i)
    d_i = total_divisors(i_t)
    prev_it = i_t
    while n <= 1050:
        # i = 1
        i_t = nth_triangular(i)
        d_i = total_divisors(i_t)
        while d_i <= n:
            i += 1
            i_t = nth_triangular(i)
            d_i = total_divisors(i_t)
            curr_it = i_t
        if prev_it != curr_it:
            id[n] = i_t
            prev_it = curr_it
        # if n % 100 == 0:
            # print(id)
        n += 1
    return id

index = {1: 3, 2: 6, 4: 28, 6: 36, 9: 120, 16: 300, 18: 528, 20: 630, 24: 2016,
         36: 3240, 40: 5460, 48: 25200, 90: 73920, 112: 157080, 128: 437580,
         144: 749700, 162: 1385280, 168: 1493856, 192: 2031120, 240: 2162160,
         320: 17907120, 480: 76576500, 576: 103672800, 648: 236215980, 768: 842161320,
         1024: 3090906000}


def solution(n):
    if n in dict_keys():
        return(index[n])
    n += 1


if __name__ == "__main__":
    N = [1, 2, 3, 4]
    for n in N:
        start = time.time()
        elapsed = (time.time() - start)
        print("result {} returned in {} sec.".format(solution(n), elapsed))
        # if n >= 2 and n % 2 == 0:
        #     print(min(dict_td_triangular()[n + 2]))
        #     print("time: {}".format((time.time() - start)))
        # else:
        #     print(min(dict_td_triangular()[n + 1]))
        #     print("time: {}".format((time.time() - start)))
        # if n + 1 in dict_keys():
        #     print(min(dict_td_triangular()[n + 1]))
        # else:
        #     print(min(dict_td_triangular()[n + 2]))
        # print("n is {}".format(n))
        # i = 1
        # ith_triangular = nth_triangular(i)
        # td_i = total_divisors(ith_triangular)
        # while(td_i <= n):
        #     i += 1
        #     ith_triangular = nth_triangular(i)
        #     td_i = total_divisors(ith_triangular)
        #     # print("i= {} and ans = {}".format(i, td_i))
        # print("result: {} returned in {} sec.".format(nth_triangular(i), elapsed))
