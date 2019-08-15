"""
Non-Divisible Subset
ref: https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""


def non_divisible_subset(s, k):
    """
    Longest subset of array s, meeting the criteria

    Parameters
    ----------
    s: an array of integers
    k: an integer

    Criteria
    --------
    sum of any 2 numbers in subset should not be evenly
    divisible by k.

    Returns
    -------
    an integer, length of longest subset
    """
    d = {x: [] for x in range(k)}
    # remainders after dividing by k
    for i in range(len(s)):
        d[s[i] % k].append(s[i])
    count = 0
    if len(d[0]) > 0:
        count = 1
    S = set([(x, k-x) for x in range(1, k//2+1)])
    for i, j in S:
        if i != j:
            if len(d[i]) > len(d[j]):
                count += len(d[i])
            else:
                count += len(d[j])
        else:
            if len(d[i]) > 0:
                count += 1
    return count


if __name__ == '__main__':
    s = [1, 7, 2, 4]
    k = 3
    res = non_divisible_subset(s, k)
    print(res)
