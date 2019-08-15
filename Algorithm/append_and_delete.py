"""
Append and Delete
ref: https://www.hackerrank.com/challenges/append-and-delete/problem
"""

import argparse
import difflib


def arguments():
    ap = argparse.ArgumentParser("Check whether text1 can be converted to text2 within k moves")
    ap.add_argument('-s', '--text_1', type=str, required=True,
                    help="first string")
    ap.add_argument('-t', '--text_2', type=str, required=True,
                    help="second string")
    ap.add_argument('-k', '--moves', type=int, required=True,
                    help="Number of moves allowed")
    args = ap.parse_args()
    return args


def common_string_size():
    txt_1 = args.text_1,
    txt_2 = args.text_2
    sq = difflib.SequenceMatcher(None, txt_1, txt_2)
    match = sq.find_longest_match(0, len(txt_1) - 1, 0, len(txt_2) - 1)
    # common_txt = txt_1[match.a:match.size]
    if match.a == 0 and match.b == 0:
        return match.size
    else:
        return 0


def append_and_delete():
    """
    A string can be converted to another string in given moves or not.
    Parameter
    ---------
    s: the initial string
    t: the desired string
    k: an integer that represents the number of operations
    Returns
    -------
    a string, either Yes or No
    """
    s=args.text_1
    t=args.text_2
    k=args.moves
    c_len = common_string_size()
    # Case 1
    # breakpoint()
    op_left = k - (len(s) + len(t) - (2 * c_len))
    if len(s) + len(t) <= k:
        return "Yes"
    # Case 2, operation left is > 0 and even then we can add and delete
    elif (op_left >= 0) and (op_left % 2 == 0):
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    args = arguments()
    # common = common_initial_text()
    # d = to_delete(common)
    # a = to_append(common)
    # if args.moves >= (d + a):
    #     print('Yes')
    # else:
    #     print('No')
    res = append_and_delete()
    print(res)

