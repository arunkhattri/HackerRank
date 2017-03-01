# Project Euler #17: Number to Words
# Given a word, write it in words.


def num_dict():
    num_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18,
               19, 20, 30, 40, 50, 60, 70, 80, 90]
    num_words = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',
                 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
                 'Eighty', 'Ninety']
    return dict(zip(num_int, num_words))

nd = num_dict()

def tens(n):
    if n not in nd.keys():
        t = n - (n % 10)
        u = n % 10
        return("{} {}".format(nd[t], nd[u]))
    else:
        return("{}".format(nd[n]))


def hundreds(n):
    h = n // 100
    t = n % 100
    return("{} Hundred {}".format(tens(h), tens(t)))


def thousands(n):
    t = n // 10 ** 3
    h = n % 10 ** 3
    return("{} Thousand {}".format(conditions(t), conditions(h)))


def millions(n):
    m = n // 10 ** 6
    t = n % 10 ** 6
    return("{} Million {}".format(conditions(m), conditions(t)))


def billions(n):
    b = n // 10 ** 9
    m = n % 10 ** 9
    return("{} Billion {}".format(conditions(b), conditions(m)))


def conditions(n):
    '''
    n ----> int
    return appropriate condition of the number
    '''
    # billionth_condition = (n >= 10 ** 9)
    # millionth_condition = (n >= 10 ** 6 and n < billionth_condition)
    # thousandth_condition = (n >= 10 ** 3 and n < millionth_condition)
    # hundredth_condition = (n >= 100 and n < thousandth_condition)
    # tenth_condition = n < hundredth_condition
    if n >= 10 ** 9:
        return(billions(n))
    elif n >= 10 ** 6 and n < 10 ** 9:
        return(millions(n))
    elif n >= 10 ** 3 and n < 10 ** 6:
        return(thousands(n))
    elif n >= 100 and n < 10 ** 3:
        return(hundreds(n))
    else:
        return(tens(n))
