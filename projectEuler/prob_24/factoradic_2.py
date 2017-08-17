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
