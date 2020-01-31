#!/bin/python
# -*- encoding:utf-8 -*-

# 给一个数组，求与这个数组的度相同的最短子数组，数组的度是数组中出现最多次数的数字出现的次数


def find_shortest_same_degree(arr):
    n = len(arr)
    count = [0] * n * 2
    max_num = 0
    mac_count = 0
    start = 0
    end = 0
    for i in range(n):
        count[arr[i]] += 1
    for j in range(n):
        if count[j] > mac_count:
            max_num = j
            mac_count = count[j]
    for k in range(n):
        if arr[k] == max_num:
            start = k
            break
    for m in reversed(range(n)):
        if arr[m] == max_num:
            end = m
            break
    return start, end


a = [1, 2, 3, 2, 4, 2, 5, 6, 7, 8]
print(find_shortest_same_degree(a))
