
# Project Euler #1: Multiples of 3 and 5
# Find the sum of all the multiples of 3 or 5 below N

# t ---> no of test cases
# n ---> list of N


def multiple_of_3_and_5(t, n):
    def ar(x):
        return(x * (x + 1))

    ans = []
    for i in range(t):
        num = n[i] - 1
        a = int(num/3)
        b = int(num/5)
        c = int(num/15)
        ans.append(int(int(3 * ar(a) + 5 * ar(b) - 15 * ar(c)) >> 1))

    return ans


if __name__ == "__main__":
    t = 2
    n = [10, 100]
    ans = multiple_of_3_and_5(t, n)
    for i in range(t):
        print("for n = {} answer is {}".format(n[i], ans[i]))
