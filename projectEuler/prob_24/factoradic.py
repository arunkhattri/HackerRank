# Project Euler #24: Lexicographic Permutations
# what is the nth lexicographic permutation of the word 'abcdefghijklm'


def fact_num_system(n):
    i = 1
    factoradic_list = []
    while n > 0:
        print("i = {}".format(i))
        new_n = n // i
        print("new_n = {}".format(new_n))
        f = n % i
        print("factoradic = {}".format(f))
        factoradic_list.append(f)
        n = new_n
        i += 1
    factoradic_list.reverse()
    return(factoradic_list)

# def fact_num_system(n):
#     i = 1
#     m = 1
#     factroid = 0
#     while n > 0:
#         new_n = n // i
#         factroid += (n % i) * m
#         n = new_n
#         i += 1
#         m *= 10
#     return(factroid)


def new_string(f, s):
    ''' 
    return new string as per factoradic f
    f ----> factoradic
    s ----> string
    '''
    word = [i for i in s]
    if len(s) > len(f):
        # list of factoradic
        diff = len(s) - len(f)
        prefaced = [i * 0 for i in range(diff + 1)]
        eff_fact = prefaced + f
    else:
        eff_fact = f

    new_string = ""
    for i in eff_fact:
        S = word.pop(i)
        new_string += S
    return(new_string)


def nth_perm(n, s="abcdefghijklm"):
    f = fact_num_system(n-1)  # 1st is s itself
    res = new_string(f, s)
    return(res)


if __name__ == "__main__":
    N = [1, 2, 6227020798]
    for n in N:
        print(nth_perm(n))
