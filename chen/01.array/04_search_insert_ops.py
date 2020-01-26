#!/bin/python
# -*- encoding:UTF-8 -*-
# 给定一个排序数组和一个目标值，在数组中找到目标值返回其索引，如果不存在，返回他按照顺序被插入的索引位置


def get_insert_position(arr, val):
    low = 0
    high = len(arr) - 1
    while high > low:
        mid = low + (high - low) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            high = mid - 1
        else:
            low = mid + 1

    # print(low)
    if arr[low] == val:
        return low
    elif arr[low] < val:
        return low + 1
    else:
        return low


src = [3, 4, 5, 7,  9,12]
print(get_insert_position(src, 8))
