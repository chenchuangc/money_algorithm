# !/bin/python
# -*- encoding:utf-8 -*-


# 一个数组中存了股票的价格，最多只能买卖一次，设计一个算法来获得最大利润


def max_money(arr):
    length = len(arr)
    max_m = -1
    buy = arr[0]
    for i in range(1, length):
        sell = arr[i]
        if sell - buy > max_m:
            max_m = (sell - buy)
        if sell < buy:
            buy = sell

    return max_m


a = [5, 4, 8, 20, 40, 3, 80]

print(max_money(a))
