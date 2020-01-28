#!/bin/python
# -*- encoding:utf-8 -*-

# 模仿matlab中的reshap函数，重构后要有相同的行便利顺序

def reshape(arr, r, c):
    row_n = len(arr)
    col_n = len(arr[0])
    total = row_n * col_n
    if row_n * col_n != r * c:
        return arr

    new_arr = [[0] * c for i in range(r)]
    for i in range(total):
        old_r = i // col_n
        old_col = i % col_n
        new_r = i // c
        new_col = i % c
        new_arr[new_r][new_col] = arr[old_r][old_col]
    return new_arr


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print(a)
res = reshape(a, 2, 6)
for e in res:
    print(e)
