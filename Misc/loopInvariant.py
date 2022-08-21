def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        print("#" * 35,"\n i = {} and j = {}".format(i,j))
        key = l[i]
        print("key = {}".format(key))
        if l[j] > key:
            x = l.pop(j)
            l[i] = x
        else:
            
            while (j > 0) and (l[j] > key):
               l[j+1] = l[j]
               j -= 1
        l[j+1] = key
        print("array = ", l)
        

m = int(input("m: ").strip())
ar = [int(i) for i in input("ar: ").strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
