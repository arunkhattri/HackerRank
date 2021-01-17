# -*- coding: utf-8 -*-
"""
Created on Wed May 25 00:03:44 2016

@author: nakedgun
"""

#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
l = len(a)
diag_1 = sum([a[i][i] for i in range(l)])
diag_2 = sum([a[i][l-1-i] for i in range(l)])
print(abs(diag_1 - diag_2))