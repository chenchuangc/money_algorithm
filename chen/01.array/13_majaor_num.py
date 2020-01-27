#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个大小为n的数组，找到其中的众数，众数是过半的数字


def find_major(arr):
    # major = -20
    count = 0
    for i in range(0, len(arr)):
        if count == 0:
            major = arr[i]
        if arr[i] == major:
            count += 1
        else:
            count -= 1
    return major


a = [2, 3, 3, 3, 3, 3, 3,3,3, 5, 6, 7, 99]
print(find_major(a))
