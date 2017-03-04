# Counting Sundays through Zellar's congruence


def yr_mth_day(dt):
    '''
    input ---->date in (yyyy mm dd) format
    return tuple (y, m, d)
    '''
    (y, m, d) = [int(i) for i in dt.split()]
    return(y, m, d)


def start_date(y, m, d):
    ''' Returns start date from 1st of next month if not
    already date is 1st'''
    y, m, d = y, m, d
    if d != 1 and m == 12:
        y, m, d = y + 1, 1, 1
    if d != 1:
        y, m, d = y, m + 1, 1
    return(y, m, d)


def end_date(y, m, d):
    if d != 1:
        d = 1
    return(y, m, d)


def zellars(y, m, d):
    '''
    q ----> month of the day, int
    m ----> int, month (march = 3, april=4, ..., jan=13, feb=14)
    y ----> int, year, int
    return j ---> week of the day (0 - Sat, 1 - Sun, ...)
    '''
    if m == 1:
        m, y = 13, y - 1
    if m == 2:
        m, y = 14, y - 1
    h = (d + (13 * (m + 1) // 5) + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return(h)


def count_sundays(d1, d2):
    y1, m1, d1 = yr_mth_day(d1)
    y, m, d = start_date(y1, m1, d1)
    y2, m2, d2 = yr_mth_day(d2)
    y2, m2, d2 = end_date(y2, m2, d2)
    count = 0
    sundays = []
    while (y, m, d) <= (y2, m2, d2):
        for month in range(m, 13):
            if zellars(y, month, d) == 1:
                count += 1
                sundays.append((y, month, d))
            if (y, month, d) >= (y2, m2, d2):
                break
        y, m = y+1, 1
    return(count, sundays)
