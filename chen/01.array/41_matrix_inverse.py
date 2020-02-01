#!/bin/python
# -*- encoding:utf-8 -*-

# 矩阵转置


def matrix_reverse(arr):
    rows = len(arr)
    cols = len(arr[0])
    new_matrix = [[0] * rows for i in range(cols)]
    for r in range(rows):
        for c in range(cols):
            new_matrix[c][r] = arr[r][c]
    return new_matrix


a = [
    [1, 2, 3],
    [4, 5, 6]
]
res = matrix_reverse(a)
for e in res:
    print(e)
