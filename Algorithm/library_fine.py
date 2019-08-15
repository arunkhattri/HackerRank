"""
Library Fine
ref: https://www.hackerrank.com/challenges/library-fine/problem
"""

import datetime

def library_fine(d1, m1, y1, d2, m2, y2):
    """
    Calculates the fine (if any).
    Parameters
    ----------
    d1: an integer, returned date
    m1: an integer, returned month
    y1: an integer, returned year
    d2 an integer, due date
    m2: an integer, due month
    y2: an integer, due year
    Returns
    -------
    an integer, fine due
    """
    # if the  book is returned on or before the expected return date,
    # no fine will be charged
    return_date = datetime.date(y1, m1, d1)
    due_date = datetime.date(y2, m2, d2)
    fine = 0

    if return_date <= due_date:
        fine = 0
    # if the book is returned after the expected return day but
    # still within the same calender month and year as the expected
    # return_date, fine = 15 Hackos * number of days late
    elif return_date > due_date and \
         return_date.month == due_date.month and \
         return_date.year == due_date.year:
        fine = 15 * (return_date.day - due_date.day)
    # If the book is returned after the expected return month but
    # still within the same calendar year as the expected return date,
    # fine = 500 Hackos * number of months late
    elif return_date > due_date and return_date.year == due_date.year:
        fine = 500 * (return_date.month - due_date.month)
    # If the book is returned after the calendar year in which it
    # was expected, fine = 10,000 Hackos (fixed)
    else:
        fine = 10000

    return fine


if __name__ == '__main__':
    d1, m1, y1 = 9, 6, 2015
    d2, m2, y2 = 6, 6, 2015
    fine = library_fine(d1, m1, y1, d2, m2, y2)
    print(f"Fine: {fine} Hackos")
