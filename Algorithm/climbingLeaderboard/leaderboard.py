"""
Climbing the Leaderboard
ref: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""


def climbing_leaderboard(scores, alice):
    """
    Assign ranking after each score of alice

    Parameters
    ----------
    scores: list of sorted scores, in descending order
    alice: list of alice scores, in ascending order

    Returns
    -------
    """
    res = []
    scores = sorted(list(set(scores)))
    index = 0
    n = len(scores)

    for i in alice:
        while(n > index and i >= scores[index]):
            index += 1
        res.append(n + 1 - index)

    return res


if __name__ == "__main__":
    scores = [100, 100, 50, 40, 40, 20, 10]
    alice = [5, 25, 50, 120]
    ranks = climbing_leaderboard(scores, alice)
    print(f"Ranks: {ranks}")
    scores = [100, 90, 90, 80, 75, 60]
    alice = [50, 65, 77, 90, 102]
    ranks = climbing_leaderboard(scores, alice)
    print(f"Ranks: {ranks}")
