#!/bin/python
# -*- encoding:utf-8 -*-

# 杨辉三角，返回杨辉三角第k行


def get_k_trangle(k):
    arr = [1] * k
    if k == 1:
        return arr
    for i in range(2, k + 1):
        for j in reversed(range(1, i - 1)):
            arr[j] += arr[j - 1]
    return arr


print(get_k_trangle(5))
