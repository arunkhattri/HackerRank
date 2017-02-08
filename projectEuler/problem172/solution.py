# Project Euler #172: Investigating numbers with few repeated digits. 
# Problem: How many k digit numbers n (without leading zeroes) are there
# such that no digit occurs more than m times in n? Output the answer
# modulo 10^9 + 7.


def numbers_with_repeated_digit(m=3, t=2, k=[3, 4], modulo=10 ** 9 + 7):
    start = []
    end = []
    for i in range(len(k)):
        start.append(int("1" + ("0" * (k[i]-1))))
        end.append(int("9" * k[i]))

    ans = []

    def count_num(n, c):
        n = str(n)
        counter = []
        for i in range(len(n)):
            m = n.count(n[i])
            counter.append(m)
        return(c in counter)

    for i in range(len(start)):
        num = []
        for j in range(start[i], end[i] + 1):
            if count_num(j, m+1):
                continue
            else:
                num.append(j)
        ans.append(len(num))

    return(ans)
