#!/bin/python
# -*- encoding:UTF-8 -*-

# 一个整数数组nums,找到最大和的连续子数组,返回其最大值的和

# 一个记录当前的最大值的变量max，一个记录当前正在累积的子数组的和cur_sum，这个和与当前遍历到的单个元素进行比较，取其中更大的值
# 然后和cur_sum 和max进行比较以决定是否替换他


def sumA(arr):
    s = 0
    for e in arr:
        s += e
    return s


def find_max_sum(arr):
    if None is arr or len(arr) == 0:
        return -1
    length = len(arr)
    max_s = arr[0]
    cur_sum = 0
    for i in range(length):
        cur_sum = max(arr[i], cur_sum + arr[i])
        max_s = max(cur_sum, max_s)
        print(str(cur_sum) + ":" + str(max_s))
    return max_s


src = [1, -2, 3, 5, -6, 6, 1, -3]
print(find_max_sum(src))
