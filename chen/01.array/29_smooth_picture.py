#!/bin/python
# -*- encoding:utf-8 -*-

def get_smooth_res(arr):
    rows = len(arr)
    cols = len(arr[0])
    direct = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]
    new_arr = [[0] * cols for i in range(rows)]

    for row in range(rows):
        for col in range(cols):
            sum = 0
            num = 1
            sum += arr[row][col]
            for step in direct:
                row_t = row + step[0]
                col_t = col + step[1]
                if rows > row_t >= 0 and cols > col_t >= 0:
                    sum += arr[row_t][col_t]
                    num += 1
            new_arr[row][col] = sum / num
    return new_arr


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for e in a:
    print(e)

new_arr = get_smooth_res(a)

for k in new_arr:
    print(k)
