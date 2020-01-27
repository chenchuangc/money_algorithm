#!/bin/python
# -*- encoding:utf-8 -*-

# 旋转数组，将数组中的元素右移k个位置

def roated_arr(arr, k):
    if None is arr or len(arr) == 1:
        return arr
    n = len(arr)
    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - 1 - i]
        arr[n - 1 - i] = temp
    for j in range(k // 2):
        temp = arr[j]
        arr[j] = arr[k - 1 - j]
        arr[k - 1 - j] = temp
    for m in range((n - k) // 2):
        temp = arr[k + m]
        arr[k + m] = arr[n - 1 - m]
        arr[n - 1 - m] = temp


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
roated_arr(a, 3)
print(a)
