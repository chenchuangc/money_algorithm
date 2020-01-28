#!/bin/python
# -*- encoding:utf-8 -*-


# 给定一个数组，将所有的零移动到数组的末尾，并保持相对顺序


def mv_zeros(arr):
    n = len(arr)
    j = 0
    for i in range(n):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    print(j)
    for k in range(j, n):
        arr[k] = 0


a = [0, 1, 0, 0, 0, 2, 3, 4, 0, 0, 5, 6, 7]
mv_zeros(a)
print(a)
