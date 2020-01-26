#!/bin/python

# -*- encoding:UTF-8 -*-

# 给定一个整数数组和一个目标值，找出数组中和为target的两个数，元素不能被重复利用，只有一种答案


def find_sum_index(arr, target):
    sort_arr = sorted(arr)
    print(arr)
    length = len(arr)
    # for i in range(length):
    left = 0
    right = length - 1
    while right > left:
        sum = sort_arr[left] + sort_arr[right]
        if sum == target:
            if sort_arr[left] == sort_arr[right]:
                return -1, -1
            return sort_arr[left], sort_arr[right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return -1, -1


src = [6, 1, 3, 4, 4, 5, 6, 7, 8, 9]
print(find_sum_index(src, 15))
