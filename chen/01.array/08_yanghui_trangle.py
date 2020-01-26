#!/bin/python
# -*- encoding:UTF-8 -*-

# 生成杨辉三角的前num行


def get_yang_hui(num):
    res = []
    pre = []
    for i in range(num):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(pre[j - 1] + pre[j])
        pre = temp
        print(temp)
        res.append(temp)


get_yang_hui(9)
