#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个包含n个整数的数组nums,判断nums中是否存在三个元素，其和为target


def three_sum(arr_s, target):
    arr = sorted(arr_s)
    n = len(arr)
    print(arr)
    res = []
    for i in range(n - 2):
        temp = target - arr[i]
        s = i + 1
        j = n - 1
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        while s < j:
            temp_sum = arr[s] + arr[j]
            if temp_sum == temp:
                res.append([arr[i], arr[s], arr[j]])
                while s < j and arr[s] == arr[s + 1]:
                    s += 1
                while s < j and arr[j] == arr[j - 1]:
                    j -= 1
                s += 1
                j -= 1
            elif temp_sum <= temp:
                s += 1
            elif temp_sum > temp:
                j -= 1
    return res


a = [5, 5, 6, 7, 8, 9]
print(three_sum(a, 19))
