#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个由0和1组成的二维数组，找到联通的最大区域

# 使用广度或者深度优先搜索就行吧


def deep_find(arr, checked, r, c, count):
    if r < 0 or r >= len(arr) or c < 0 or c >= len(arr[0]) or arr[r][c] == 0 or checked[r][c]:
        return
    checked[r][c] = True
    count[0] += 1
    direct = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    for step in direct:
        new_r = r + step[0]
        new_c = c + step[1]
        deep_find(arr, checked, new_r, new_c, count)


def max_area(arr):
    rows = len(arr)
    cols = len(arr[0])
    max_num = 0
    checked = [[False] * cols for i in range(rows)]

    for r in range(rows):
        for c in range(cols):
            count = [0]
            deep_find(arr, checked, r, c, count)
            max_num = max(max_num, count[0])
    return max_num


a = [
    [1, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 1, 1]
]
print(max_area(a))
