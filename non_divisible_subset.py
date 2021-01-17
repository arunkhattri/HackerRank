# -*- coding: utf-8 -*-
"""
Created on Wed May 25 00:35:52 2016
@author: nakedgun
Problem:
n, k ----> space-separated integers,
a -------> n space-separated integers.
Constraints:
1 <= n <= 10^5
1 <= k <= 100
a <= a_i <= 10^9
All of the given numbers are distinct.
Print the size of the largest possible subset.
"""

n, k = 4, 3
a = [1, 7, 2, 4]
i = 0
res = []
while i < len(a):
    res.add(i)
    temp = [item for item in a if((i + item) % k != 0) and item not in res]
    res = res + temp
    for j in range(len(res)):
