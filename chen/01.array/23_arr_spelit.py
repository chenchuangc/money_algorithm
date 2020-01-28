#!/bin/python
# -*- encoding:utf-8 -*-


# 长度为2n的数组，拆成n，对，如（a1,b1）,(a2,b2)..(an,bn),使得，从1->n 的min(ai,bi)总和最大

def find_max_min(arr):
    sorted(arr)
    n2 = len(arr)
    list_r = []
    for i in range(n2 // 2):
        list_r.append((arr[i], arr[i + 1]))
    return list_r


a = [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 15, 16, 18, 20]
print(find_max_min(a))
