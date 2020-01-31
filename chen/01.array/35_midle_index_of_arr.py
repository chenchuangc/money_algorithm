#!/bin/python
# -*- encoding:utf-8 -*-
# 找到数组的中心索引，中心索引元素满足，索引左边所有元素的和等于索引元素右边所有元素的和

# 如果不存在返回-1，存在多个的话返回最左边的索引元素的下标
# 可以先进行一次求和，得到总和，这样计算起来就更加简单了


def middle_index(arr):
    n = len(arr)
    s = sum(arr)
    sum_sub = 0
    for i in range(n):
        if sum_sub == (s - arr[i] - sum_sub):
            return i
        sum_sub += arr[i]
    return -1


a = [0, 3, 4, 5, 0, 0, 6, 3, 3]
print(middle_index(a))
