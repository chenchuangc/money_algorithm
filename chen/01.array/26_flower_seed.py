#!/bin/python
# -*- encoding:utf-8 -*-

# 给你一个种过一些花的花坛，花儿不能挨着种，给你n朵花，测试一下能否全部种进去

def can_flower_do(arr, n):
    length = len(arr)
    can = 0
    for i in range(length):
        if i == 0:
            if arr[i] == 0 and arr[i + 1] == 0:
                arr[i] = 1
                can += 1
        elif i == n - 1:
            if arr[i] == 0 and arr[i - 1] == 0:
                arr[i] = 1
                can += 1
        else:
            if arr[i] == 0 and arr[i - 1] == 0 and arr[i + 1] == 0:
                arr[i] = 1
                can += 1
    print(can)

    return can >= n


a = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
print(can_flower_do(a, 4))
