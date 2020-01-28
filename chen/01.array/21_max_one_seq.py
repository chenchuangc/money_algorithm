#!/bin/python
# -*- encoding:utf-8 -*-

# 二进制数组，由0，1组成的数组，计算其中最大连续1的个数

def max_seq_one(arr):
    slow = 0
    n = len(arr)
    max_n = 0
    for fast in range(n):
        if arr[fast] == 1:
            max_n = max(max_n, (fast - slow + 1))

        else:
            slow = fast + 1
    return max_n


a = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
print(max_seq_one(a))
