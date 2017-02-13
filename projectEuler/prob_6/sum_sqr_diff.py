# Project Euler #6: Sum square difference
# Find the absolute difference between the sum of the squares of the
# first N natural numbers and the square of the sum.


def square_sum(n):
    x = [i*i for i in range(1, n+1)]
    return(sum(x))


def sum_square(n):
    x = [i for i in range(1, n+1)]
    return(sum(x) ** 2)


def diff(n):
    return(sum_square(n) - square_sum(n))


if __name__ == "__main__":
    N = [3, 4, 5, 6, 7, 8, 9, 10]
    diff_list = [diff(n) for n in N]
    print(diff_list)
    pattern = []
    for i in range(len(diff_list)-1):
        pattern.append(diff_list[i+1] - diff_list[i])
    print(pattern)
