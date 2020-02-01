#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一副牌，找到一个数字x,将牌分成一组或者多组，每组都有x张牌，每组内都写着相同的数字


def find_x_in_group(arr):
    max_one = max(arr)
    count = [0] * (max_one + 1)
    for e in arr:
        count[e] += 1
    min_count = 10000
    for i in count:
        if i > 0:
            min_count = min(i, min_count)

    # find = False

    for step in range(2, min_count + 1):
        mark = 0
        for index in range(len(count)):
            if count[index] % step != 0:
                break
            else:
                mark = index
        if mark == max_one:
            return True
    return False


a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
print(find_x_in_group(a))
