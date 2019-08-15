"""
Sherlock and Square
ref: https://www.hackerrank.com/challenges/sherlock-and-squares/problem
"""

import math

def squares(lower_range, upper_range):
    """
    Determine square integers within the range, inclusive of endpoints
    Parameters
    ----------
    lower_range: an integer, the lower range boundary
    upper_range: an integer, the upper range boundary
    Returns
    -------
    integer, number of square integers in the inclusive range a to b and
    list of those square integers
    """
    res = []
    l = range(lower_range, upper_range + 1)
    a = math.ceil(math.sqrt(lower_range))
    b = math.floor(math.sqrt(upper_range))
    for n in range(a, b + 1):
        if n * n in l:
            res.append(n * n)
    return res


if __name__ == '__main__':
    lower_range = [24, 3, 17]
    upper_range = [49, 9, 24]
    for i in range(len(lower_range)):
        sq = squares(lower_range[i], upper_range[i])
        print(f"Total Square Integer: {len(sq)}\n{sq}")
        
