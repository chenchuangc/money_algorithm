#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个包含n个整数的数组nums,判断nums中是否存在三个元素，其和为target


def three_sum(arr, target):
    s_arr = sorted(arr)
    n = len(arr)
    for i in range(n - 2):
        temp = target - arr[i]
        s = i + 1
        j = n - 1
        while s < j:
            temp_sum = arr[s] + arr[j]
            if temp_sum == temp:
                if arr[i] == arr[s] or arr[s] == arr[j]:
                    continue
                return arr[i], arr[s], arr[j]
            elif temp_sum < temp:
                s += 1
            elif temp_sum > temp:
                j -= 1
    return -1, -1, -1


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(three_sum(a, 23))
