#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个数组nums,和一个目标值target,判断nums中是否存在四个元素，a+b+c+d=target,找出所有满足条件且不重复的元组
# 根据分治法推算出来元素的移动


def four_sum(arr_s, target):
    n = len(arr_s)
    arr = sorted(arr_s)
    res = []
    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if arr[j] == arr[j - 1]:
                continue
            k = j + 1
            m = n - 1
            while k < m:

                temp_target = target - arr[i] - arr[j]
                temp_sum = arr[k] + arr[m]
                if temp_sum == temp_target:
                    res.append([arr[i], arr[j], arr[k], arr[m]])
                    while arr[k] == arr[k + 1]:
                        k += 1
                    while arr[m] == arr[m + 1]:
                        m -= 1
                    k += 1
                    m -= 1
                elif temp_sum > temp_target:
                    m -= 1
                else:
                    k += 1
    return res


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 18]
for e in four_sum(a, 22):
    print(e)
