#!/bin/python
# -*- encoding:utf-8 -*-


# 给定一个整数数组a和整数k  在数组中找到不同的k-diff 对，其中i,j都是数组中的数字，且两个数的差是绝对值k


def count_diff_k(a, k):
    dict_nums = {}
    list_r = []
    for e in a:
        dict_nums[e] = 1
    for m in a:
        target01 = m - k
        target02 = m + k
        if dict_nums.get(target01, 2) == 1:
            list_r.append((m, target01))
            dict_nums[target01] = 3
            dict_nums[m]=3
        if dict_nums.get(target02) ==1:
            list_r.append((m,target02))
            dict_nums[target02]=3
            dict_nums[m]=3
    return list_r


a=[1,2,3,4,4,5,6,7,8]
print(count_diff_k(a,6))
