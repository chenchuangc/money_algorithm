#!/bin/python
# -*- enconding:utf-8 -*-

# 把一个数组按照偶数在前，奇数在后的方式进行排列

def odd_even_group(arr):
    n = len(arr)
    start = 0
    end = n - 1

    while end > start:
        while end > start and arr[end] % 2 == 1:
            end -= 1
        while start < end and arr[start] % 2 == 0:
            start += 1
        if end > start:
            temp = arr[end]
            arr[end] = arr[start]
            arr[start] = temp


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
odd_even_group(arr)
print(arr)
