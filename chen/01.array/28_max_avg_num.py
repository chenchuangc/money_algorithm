#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个数组，找出长度为k的子序列中平均值最大的子序列的平均值


def find_max_avg_sub(arr, k):
    n = len(arr)
    avg = 0
    sum = 0
    for i in range(k):
        sum += arr[i]
    avg = sum / k

    for j in range(k, n):
        sum = (sum + arr[j] - arr[j - k])
        temp_avg = sum / k
        avg = max(avg, temp_avg)

    return avg


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find_max_avg_sub(a, 4))
