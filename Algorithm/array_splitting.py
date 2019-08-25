from itertools import accumulate
import operator
from collections import Counter


def play_game(arr):
    res = list(accumulate(arr, operator.add))
    return score(0, res[-1], Counter(res))


def score(lo,hi,ct):
    if (lo + hi) & 1:
        return 0
    elif lo == hi:
        return ct[lo] - 1
    else:
        av = (lo + hi) // 2
        if av in ct:
            return 1 + max(score(lo, av, ct), score(av, hi, ct))
        else:
            return 0


if __name__ == "__main__":
    arr = [1, 2, 3, 6]
    res = play_game(arr)
    print(res)
    arr = [4, 1, 0, 1, 1, 0, 1]
    res = play_game(arr)
    print(res)