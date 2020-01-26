# !/bin/python
# -*- encoding:UTF-8 -*-

# 给定两个有序数组nums01,nums02,将nums02合并到nums01当中，使得nums01称为一个有序数组
# 假设nums01有足够的空间来存储

# 归并排序的一部分，其实是，从后面往前就可以了


def merge_arr(nums01,len01, nums02):
    # len01 = len(nums01)
    len02 = len(nums02)
    right = len01 + len02 - 1
    len01-=1
    len02-=1

    while len01 >= 0 and len02 >= 0:
        # print(len02)
        print(right)
        if nums01[len01] > nums02[len02]:
            nums01[right] = nums01[len01]
            len01 -= 1
        else:
            nums01[right] = nums02[len02]
            len02 -= 1
        right -= 1
    while len02 >= 0:
        nums01[right] = nums02[len02]
        right -= 1
        len02 -= 1

src01=[1,3,5,6,0,0,0,0,0,0,0]
src02=[2,4,6,8]

merge_arr(src01,4,src02)
print(src01)
