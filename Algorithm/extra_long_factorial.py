"""
Extra Long Factorials
ref: https://www.hackerrank.com/challenges/extra-long-factorials/problem
"""

import math
import argparse


def arguments():
    ap = argparse.ArgumentParser("Factorial of integer n")
    ap.add_argument("-n", "--integer_n", type=int, required=True,
                    help="integer of which factorial is to be calculated.")
    args = ap.parse_args()
    return args


def extra_long_factorials():
    n = args.integer_n
    return math.factorial(n)


if __name__ == '__main__':
    args = arguments()
    f = extra_long_factorials()
    print(f"Factorial:\n{f}")
    
