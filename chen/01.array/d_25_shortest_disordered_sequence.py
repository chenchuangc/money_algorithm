#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个数组，找到一个最短的子序列，对这个子数组进行排序后整个数组都会变成升序

# 这个还不好做
# 方法1. 排序，找到最开始对不上的前后两个即可
# 方法2. 找到小于左边最大值的数的下标，找到大于右边最小值的下标，就是子序列的范围


def find_shortest_seq_sorting(arr):
    b = sorted(arr)
    n = len(arr)
    l = 0
    r = 0
    for i in range(n):
        if arr[i] != b[i]:
            l = i
            break
    for j in reversed(range(n)):
        if arr[j] != b[j]:
            r = j
            break
    return l, r


def find_shortest_seq(arr):
    n = len(arr)
    l2 = n - 1
    r = 0
    l_max = arr[0]
    r_min = arr[n - 1]
    for i in range(1, n):
        if arr[i] < l_max:
            r = i
        l_max = max(arr[i], l_max)
        if arr[n - i] > r_min:
            l2 = n - i
        r_min = min(arr[n - i], r_min)
    return l2, r


a = [1, 2, 3, 4, 7, 8, 9, 5, 6]
print(find_shortest_seq_sorting(a))
print(find_shortest_seq(a))
