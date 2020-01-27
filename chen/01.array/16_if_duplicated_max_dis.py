#!/bin/python
# -*- encoding:utf-8 -*-


# 给定一个整数数组和一个整数k,判断数组中是否存在两个不同的索引i,j,使得nums[i]=nums[j],并且i,j的差的绝对值最大为k

def if_k_duplicated(arr, k):
    n = len(arr)
    for i in range(n - k):
        for j in range(1, k + 1):
            if arr[i] == arr[i + j]:
                return True
    return False


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6]

print(if_k_duplicated(a, 4))
