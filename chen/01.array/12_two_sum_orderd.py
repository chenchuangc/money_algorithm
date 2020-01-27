#!/bin/python
# -*- encoding:utf-8 -*-

def get_target(arr, target):
    length = len(arr)
    l = 0
    r = length - 1
    while r > l:
        if arr[l] + arr[r] == target:
            if arr[l] == arr[r]:
                return -1, -1
            return l, r
        if arr[l] + arr[r] > target:
            r -= 1
        else:
            l += 1
    return -1, -1


a = [1, 2, 3, 5, 6, 8, 12, 15, 20, 23, 32]
print(get_target(a, 50))
