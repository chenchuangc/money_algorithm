#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个包含n个整数的数组和一个target,找出nums中的三个整数，使得他们的和与target最接近，返回这三个数的和，假定每组输入只有唯一解


def three_sum_closet(arr_s, target):
    n = len(arr_s)
    arr = sorted(arr_s)
    print(arr)
    diff_val = 20000
    pre_res = -1, -1, -1

    for i in range(n - 2):
        temp_target = target - arr[i]
        left = i + 1
        right = n - 1
        pre_diff = 20000
        temp_i = i
        temp_left = left
        temp_right = right
        while left < right:
            temp_sum = arr[left] + arr[right]
            if temp_sum == temp_target:
                if arr[i] != arr[left] and arr[left] != arr[right]:
                    return i, left, right
                else:
                    left += 1
            else:
                temp_diff = abs(temp_target - temp_sum)
                if temp_diff > pre_diff:
                    break
                pre_diff = temp_diff
                temp_i = i
                temp_left = left
                temp_right = right
                if temp_sum > temp_target:
                    right -= 1
                elif temp_sum < temp_target:
                    left += 1
        if pre_diff < diff_val:
            pre_res = temp_i, temp_left, temp_right
    return pre_res


a = [11, 8, 7, 4, 5, 6, 7, 8, 9]
print(three_sum_closet(a, 29))
