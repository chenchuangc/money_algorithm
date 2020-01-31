#!/bin/python
# -*- encoding:utf-8 -*-

# 幻方，每一行每一列的和都是相等的


def is_magic(r, c, arr):
    init = False
    line = 0
    # 求行
    for tr in range(r, r + 3):
        sum_t = 0
        for tc in range(c, c + 3):
            sum_t += arr[tr][tc]
        if not init:
            line = sum_t
            init = True
        elif sum_t != line:
            return False

    # 求列
    for tc02 in range(c, c + 3):
        sum_c = 0
        for tr02 in range(r, r + 3):
            sum_c += arr[tr02][tc02]
        if sum_c != line:
            return False

    # 对角线1
    left_sum = 0
    for i in range(3):
        left_sum += arr[r + i][c + i]
    if left_sum != line:
        return False

    # 对角线2
    right_sum = 0
    for j in range(3):
        right_sum += arr[r + j][c + 2 - j]
    if right_sum != line:
        return False

    return True


def magic_matrix_num(arr):
    rows = len(arr)
    cols = len(arr[0])
    count = 0
    for r in range(rows - 2):
        for c in range(cols - 2):
            if is_magic(r, c, arr):
                count += 1
    return count


a = [
    [4, 3, 8, 4],
    [9, 5, 1, 9],
    [2, 7, 6, 2]
]

print(magic_matrix_num(a))
