# !/bin/python
# -*- encoding:utf-8 -*-
# 给定一个非负整数组成非空数组，在该数基础上面加一，返回一个新的数组

def addOne(arr_num):
    length = len(arr_num)
    over_add = False
    if arr_num[length - 1] + 1 == 10:
        arr_num[length - 1] = 0
        over_add = True
    else:
        arr_num[length - 1] += 1
        return arr_num
    for i in reversed(range(length - 1)):
        if over_add:
            tSum = arr_num[i] + 1
            if tSum == 10:
                arr_num[i] = 0
            else:
                arr_num[i] += 1
                return arr_num
    if over_add:
        longer_arr = [1]
        longer_arr += arr_num
        # print(arr_num)
        return longer_arr
        # longer_arr.append(arr_num)
        # print(longer_arr)
        # for e in arr_num:
        #     print(e)
        #     longer_arr.append(e)
        #     return longer_arr


src = [9, 9, 9, 9, 9]
print(addOne(src))
