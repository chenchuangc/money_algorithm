#!/bin/python
# -*- encoding:utf-8 -*-


# 一个域名包含多级域名，比如leetcode.com ,com是顶级域名，leetcode是次级域名，
# 给你一个域名和访问次数的组合，计算所有域名的访问次数

def domain_count(arr):
    dict_domian = {}
    for a_domian_count in arr:
        a_d_count_arr = a_domian_count.split(" ")
        a_domin = a_d_count_arr[0]
        a_count = int(a_d_count_arr[1])
        for i in range(len(a_domin)):
            if a_domin[i] == ".":
                dict_domian[a_domin[:i]] = dict_domian.get(a_domin[:i], 0) + a_count
        dict_domian[a_domin] = dict_domian.get(a_domin, 0) + a_count

    return dict_domian


a = ["com.chen.work 3", "com.qi.work 4", "com.le.work 5"]
print(domain_count(a))
