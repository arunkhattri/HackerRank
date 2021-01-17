from __future__ import division


a = int(raw_input("Numbers of Students"))
record = {}
for i in range(a):
    s = raw_input("names & marks_of seperated by space")
    # split names and marks (returns list of strings)
    s_split = s.split(' ',3)
    # seperate key and values
    k = s_split[0]
    val = [float(i) for i in s_split[1:]]
    record[k] = val

marks_of = raw_input("Name: ")
b = record.get(marks_of)
print format(sum(b)/len(b),'.2f')

######################################################################
## Find the median
# import numpy as np
import heapq

a = int(raw_input("array size: "))

s = raw_input("numbers that makes up the array")
# split names and marks (returns list of strings)
s_split = s.split(' ',a)
# print s_split
# list

val = [int(i) for i in s_split]
# print val
# val = np.array(val)
# b = len(val)
# if b % 2 == 0:
#     print (val[b/2] + val[(b + 1)/2])/2
# else:
#     print val[(b/2)+1]

# val_heap = heapify(val)
half_list = heapq.nsmallest((len(val)//2) + 1, val)
print half_list[-1]

######################################################################
# All Domains ---> Algorithms ---> Sorting ---> Intro to Tutorial Challenges

v = int(raw_input("value to be searched "))
a = int(raw_input("array size: "))

s = raw_input("numbers that makes up the array: ")
# split names and marks (returns list of strings)
s_split = s.split(' ',a)
val = [int(i) for i in s_split]
print val.index(v)

m = input()
ar = [int(i) for i in raw_input().strip().split()]

######################################################################

def insertionSort(ar):
    len_arr = len(ar)
    arr_copy = ar[:]
    i = len_arr-1
    

    while i > 0:
        num = arr_copy[i]
        del arr_copy[i]
        if num < arr_copy[i-1]:
            del arr_copy[i]
            arr_copy.insert(i, ar[i-1])
            print arr_copy

        else:
            print arr_copy
        arr_copy.insert(i-1, num)
        del arr_copy[i]
        i -= 1

    return arr_copy

m = input("size of the array:")
ar = [int(i) for i in raw_input("array of integers: ").strip().split()]
# insertionSort(ar)               


len_arr = len(ar)
arr_copy = ar[:]
i = len_arr-1


while i > 0:
    num = arr_copy[i]
    del arr_copy[i]
    if num < arr_copy[i]:
        arr_copy.insert(i, ar[i])
        print arr_copy

    else:
        print arr_copy
    arr_copy.insert(i-1, num)
    del arr_copy[i]
    i -= 1
print arr_copy
