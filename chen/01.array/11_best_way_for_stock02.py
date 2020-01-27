#!/bin/python
# -*- encoding:utf-8 -*-

# 一个数组中存了股票的价格，能买卖多次，设计一个算法来获得最大利润


def max_money(arr):
    earn_money = 0
    s = 0
    length = len(arr)
    while s < length - 1:
        while (s < length - 1) and (arr[s] > arr[s + 1]):
            s += 1
        buy_index = s
        while (s < length - 1) and arr[s] < arr[s + 1]:
            s += 1
        earn_money += (arr[s] - arr[buy_index])
    return earn_money


a = [2, 3, 4, 9, 8, 2, 6]
print(max_money(a))
