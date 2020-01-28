#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个包含0-n 的n个数的序列（理论上是是n+1个），找出缺失的数字


def find_miss_num(arr, n):
    a = 0
    for i in range(1, n):
        a ^= i
        a ^= arr[i]
    return a ^ n


a = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]
print(find_miss_num(a, 12))
