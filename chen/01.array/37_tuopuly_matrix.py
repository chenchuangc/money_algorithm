#!/bin/python
# -*- encoding:utf-8 -*-

# 托普利矩阵是一个所有对角线元素都是一样的矩阵，给定一个矩阵，判断是否为托普利矩阵


def is_tuopuli(arr):
    rows = len(arr)
    cols = len(arr[0])

    for c in range(1, cols - 1):
        num = arr[0][c]
        c_s = c + 1
        r_s = 1
        while c_s < cols and r_s < rows:
            if arr[r_s][c_s] != num:
                return False
            c_s += 1
            r_s += 1
    for r in range(1, rows - 1):
        num = arr[r][0]
        c_s = 1
        r_s = r + 1
        while c_s < cols and r_s < rows:
            if arr[r_s][c_s] != num:
                return False
            c_s += 1
            r_s += 1

    return True


a = [
    [1, 2, 3, 4],
    [2, 1, 2, 3],
    [5, 2, 1, 2]
]

print(is_tuopuli(a))
