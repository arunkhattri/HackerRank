"""
Ref: https://www.hackerrank.com/challenges/kangaroo/problem
"""


def meeting_possibility(x_1, v_1, x_2, v_2):
    """
    Find the possibility of meeting at same point after same number of jump.
    Parameters
    ----------
    x_1: starting position of first kangaroo
    v_1: rate of meters per jump of first kangaroo
    x_2: starting position of second kangaroo
    v_2: rate of meters per jump of second kangaroo
    Constraints
    -----------
    0 =< x_1 < x_2 =< 10000
    1 =< v_1 =< 10000
    1 =< v_2 =< 10000
    Returns
    -------
    string, "Yes" if possible otherwise 'No'
    """
    if x_2 > x_1 and v_2 >= v_1:
        return "No"
    elif (x_2 - x_1) % (v_1 - v_2) == 0:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    x_1, v_1, x_2, v_2 = 0, 3, 4, 2
    print(meeting_possibility(x_1, v_1, x_2, v_2))
