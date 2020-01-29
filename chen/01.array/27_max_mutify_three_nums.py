#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个整形数组，求三个数输出的最大乘积


def three_multiply_max(arr):
    n = len(arr)

    for i in range(3):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    for m in range(2):
        for l in reversed(range(1, n - m)):
            if arr[l] < arr[l - 1]:
                temp = arr[l]
                arr[l] = arr[l - 1]
                arr[l - 1] = temp
    print(arr)
    if arr[n - 1] > 0:
        if arr[n - 2] * arr[n - 3] > arr[0] * arr[1]:
            return arr[n - 2] * arr[n - 3] * arr[n - 1]
        else:
            return arr[n - 1] * arr[0] * arr[1]
    else:
        return arr[0] * arr[1] * arr[2]


a = [-8, -5, -1, 2, 3, 6, 7]
print(three_multiply_max(a))
