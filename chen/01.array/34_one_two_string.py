#!/bin/python
# -*- encoding:utf-8 -*-

# 有两种字符串，一种用一比特0标识，第二种用两比特（10，11）标识
# 给定一个字符串，判读最后一个字符是否必定为一个一比特字符，给定的字符串总是由0结束

# 这个题最开始想的有点复杂总是想用分治或者递归的方式来解决问题
# 实际上从头开始遍历就行了


def weather_be_single(str):
    n = len(str)
    index = 0
    while index < n:
        if index == n - 1:
            return True
        if str[index] == '1':
            index += 2
        else:
            index += 1
    return False


str = "101100100"
print(weather_be_single(str))
