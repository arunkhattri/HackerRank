from itertools import product

with open("./inputs.txt", 'r') as f:
    data = f.readlines()
    K, M = list(map(int, data[0].split()))
    l_of_lists = []
    for i in range(1, K):
        N = list(map(int, data[i].split()))[1:]
        sq_N = [i**2 for i in N]
        l_of_lists.append(sq_N)

    print(l_of_lists)

cartesian_product = list(product(*l_of_lists))
sum_cart_prod = [sum(i) % M for i in cartesian_product]
print(max(sum_cart_prod))