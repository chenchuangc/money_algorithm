#!/bin/python
# -*- encoding:UTF-8 -*-

# 给定一个特定数组nums和值val,使用原地算法删除所有值为val的元素，返回新的数组的长度


def rm_val_in_arr(arr, val):
    slow = 0
    length = len(arr)
    for fast in range(length):
        if arr[fast] != val:
            arr[slow] = arr[fast]
            slow += 1
    return slow + 1


src = [1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9]
print(rm_val_in_arr(src,3))
print(src)
