#!/bin/python
# -*- encoding:utf-8 -*-


def is_single_order(arr):
    init = False
    diff = 0
    for i in range(1, len(arr)):
        if not init or init == 0:
            diff = arr[i] - arr[i - 1]
            init = True
            continue
        if (arr[i] - arr[i - 1]) * diff < 0:
            return False
    return True


a = [1, 1, 2, 3, 4, 5, 6, 6]
print(is_single_order(a))
