#!/bin/python
# -*- encoding:utf-8 -*-


# 一排座位，0标识没人，1标识有人，选择一个你可以距离最远的座位


def max_distance(arr):
    n = len(arr)
    i = 0
    max_dis = 0
    for j in range(n):
        if arr[j] == 0:
            j += 1
            continue
        else:
            if i == 0 or j == n - 1:
                max_dis = max(max_dis, j - i)
            else:
                max_dis = max(max_dis, (j - i) // 2)
            i = j + 1
    return max_dis


arr = [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1]
print(max_distance(arr))
