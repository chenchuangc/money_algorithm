#!/bin/python
# -*- encoding:utf-8 -*-

# 在一个给定数组中nums中，总是存在一个最大元素，查看最大元素是否最少是其他元素的2倍
# 如果是，返回最大元素的索引，否则，返回-1


def max_is_dubble(arr):
    n = len(arr)
    max_num_index = -1
    max_num = 0
    sec_num = 0
    for i in range(1, n):
        if sec_num < arr[i] < max_num:
            sec_num = arr[i]
        elif arr[i] > max_num:
            sec_num = max_num
            max_num = arr[i]
            max_num_index = i

    if max_num // sec_num >= 2:
        return max_num_index
    else:
        return -1


a = [1, 2, 3, 5, 7, 8, 9, 18]
print(max_is_dubble(a))
