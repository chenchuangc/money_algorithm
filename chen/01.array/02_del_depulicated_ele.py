#!/bin/python
# -*- encoding:UTF-8 -*-

# 给定一个排序数组，使用原地算法删除重复出现的元素，返回溢出后数组的新的长度


def unique_length(arr):
    if None is arr:
        return -1
    slow = 0
    length = len(arr)
    for fast in range(1, length):
        if arr[slow] == arr[fast]:
            continue
            # fast += 1
        else:
            slow += 1
            arr[slow] = arr[fast]
            # fast += 1
    return slow + 1


src = [2, 3, 4, 5, 5, 6, 7, 9, 9, 10, 10, 11, 11, 11, 11]
print(unique_length(src))
