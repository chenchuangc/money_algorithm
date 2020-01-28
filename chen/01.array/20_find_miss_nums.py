#!/bin/python
# -*- encoding:utf-8 -*-


# 给定一个范围在 1<= a[i] <=n的整形数组，数组中的一些元素出现了2次，一些出现了一次，找到没有出现的数据


def find_miss_nums_in_n(arr):
    n = len(arr)
    new_arr = [0] * n
    for i in range(n):
        new_arr[arr[i] - 1] = 1

    list = []
    for i in range(n):
        if new_arr[i] != 1:
            list.append(i + 1)
    return list


# # 空间复杂度o(1)复杂度太高了
# def find_miss_nums_in_n01(arr):
#     n = len(arr)
#     for i in range(n):
#         e = a[i]
#         t = a[e - 1]
#         if t != 0:
#             a[i] = t
#         a[e - 1] = 0


a = [1, 1, 3, 3, 4, 6]
print(find_miss_nums_in_n(a))
