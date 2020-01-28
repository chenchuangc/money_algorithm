#!/bin/python
# -*- encoding:utf-8 -*-


# 给定一个数组，返回第三大的数字(重复的算作同一个)，如果不存在，返回最大的数字，要求T O(n)

def find_third_max(arr):
    temp = [-200, -200, -200]
    n = len(arr)
    for i in range(n):
        if arr[i] <= temp[2]:
            continue
        elif temp[2] < arr[i] < temp[1]:
            temp[2] = arr[i]
        elif temp[1] < arr[i] < temp[0]:
            temp[2] = temp[1]
            temp[1] = arr[i]
        elif arr[i] > temp[0]:
            temp[2] = temp[1]
            temp[1] = temp[0]
            temp[0] = arr[i]
    if temp[2] == -200:
        return temp[0]
    return temp[2]


a = [18, 22, 3, 4, 5, 6, 7, 8, 9, 12, 13]
print(find_third_max(a))
