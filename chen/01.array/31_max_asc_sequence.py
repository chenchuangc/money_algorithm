#!/bin/python
# -*- encoding:utf-8 _-*-


# 一个未经排序的数组，找到最长连续递增子序列

def find_max_asc_seq(arr):
    n = len(arr)
    slow = 0
    start = 0
    end = 0
    for fast in range(1, n):
        if arr[fast] > arr[fast - 1]:
            if fast == n - 1:
                if fast - slow > end - start:
                    start = slow
                    end = fast
            continue
        else:
            if fast - slow > end - start:
                start = slow
                end = fast - 1
            slow = fast
    return start, end


a = [1, 2, 3, 4, 6, 8, 5, 6, 7, 9, 10]
print(find_max_asc_seq(a))
