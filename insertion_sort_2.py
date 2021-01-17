#!/bin/python3
def insertionSort(ar):
    len_arr = len(ar)
    arr_copy = ar[:]
    i = len_arr-1
    while i > 0:
        # print("i = ",i)
        num = arr_copy[i]
        del arr_copy[i]
        if num < arr_copy[i-1]:
            arr_copy.insert(i,ar[i-1])
            # print(*arr_copy,sep=' ')
            arr_copy.insert(i-1, num)
            # print("array after insert: ", *arr_copy, sep=' ')
            del arr_copy[i+1]
            if i == 1:
                # print(*arr_copy, sep=' ')
                break
        else:
            arr_copy.insert(i,num)
            # print(*arr_copy, sep=' ')
            break

        i -= 1
    return arr_copy
    # print arr_copy

# m = input("size of the array: ")
# ar = [int(i) for i in input("array of integers: ").strip().split()]
# insertionSort(ar)               

#test case 1
#14
##1 3 5 9 13 22 27 35 46 51 55 83 87 23

def insertionSort1(ar):
    len_arr = len(ar)
    arr_copy = ar[:]
    i = 1


    while i < len(ar):
        # print("i = ",i)
        num = arr_copy[i]
        if num > arr_copy[i-1]:
            print(*arr_copy, sep=' ')
        else:
            arr_slice = arr_copy[:i+1]
            x = insertionSort(arr_slice)
            del arr_copy[:i+1]
            arr_copy = x + arr_copy
            print(*arr_copy, sep=' ')
        i += 1
# print arr_copy


m = input("size of the array: ")
ar = [int(i) for i in input("array of integers: ").strip().split()]
# insertionSort(ar)               

#test case 1
#14
##1 3 5 9 13 22 27 35 46 51 55 83 87 23
