#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个长度为n的整数数组，你的任务是在最多改变一个元素的情况下该数组能否变成一个的非递减数列

def if_in_ordered(arr):
    count = 0
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            count += 1
            if count > 1:
                return False
            if i > 1:
                if arr[i] <= arr[i - 2]:
                    arr[i] = arr[i - 1]
    return True


a = [1, 2, 3, 5, 6, 7, 8, 3, 7, 10]
print(if_in_ordered(a))
