#!/bin/python
# -*- encoding:utf-8 -*-
#
# 有n个点，(i，ai)...(n,an) 沿着


def max_area(points):
    n = len(points)
    m_area = 0
    line01 = 0
    line02 = 0
    for i in range(n):
        for j in range(i + 1, n):
            width = abs(points[i][0] - points[j][0])
            height = min(points[i][1], points[j][1])
            area = width * height
            if area > m_area:
                m_area = area
                line01 = i
                line02 = j

    return line01, line02


points = [(1, 6), (2, 8), (3, 5), (4, 4), (5, 5)]

print(max_area(points))
