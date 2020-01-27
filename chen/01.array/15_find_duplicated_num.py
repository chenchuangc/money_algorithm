#!/bin/python
# -*- encoding:utf-8 -*-

# 给定一个数组，判断是否存在重复元素

def if_duplicated(arr):
    if None is arr or len(arr)<=1:
        return False
    sorted(arr)
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            return True
    return False




a=[1,2,3,4,5,6,8,9,1]
print(if_duplicated(a))



