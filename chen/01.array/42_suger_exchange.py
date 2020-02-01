#!/bin/python
# -*- encoding:utf-8 -*-

# 爱丽丝和鲍勃各有一组糖果，每个糖果的大小不一样，如何交换，让他们拥有的糖果的数量一样多
# 因为需要查找的次数过多，所以使用hashtable或者是set是最合适的


def suger_exchange(arr01, arr02):
    sum01 = sum(arr01)
    sum02 = sum(arr02)
    diff = sum01 - sum02
    print(diff)

    count = [-1] * 10000
    for i in range(len(arr02)):
        count[arr02[i]] = i
    for j in range(len(arr01)):
        temp = arr01[j] - (diff // 2)
        if count[temp] != -1:
            print(temp)
            return j, count[temp]


a = [2, 3, 4, 5, 6, 7, 8, 2]
b = [2, 3, 4, 5, 6, 7, 8, 6]

print(suger_exchange(a, b))
