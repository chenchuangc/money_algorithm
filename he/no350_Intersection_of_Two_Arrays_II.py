'''
本题中进阶中的三个问题很有意思
'''
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if (len(nums1)>len(nums2)):
            return self.intersect(nums2,nums1)
        num_count = {}
        for i in nums1:
            if i in num_count.keys():
                num_count[i] = num_count[i]+1
            else:
                num_count[i] = 1
        k = 0
        for j in nums2:
            if j in num_count.keys() and num_count[j]>0:
                nums1[k] = j
                k = k+1
                num_count[j] = num_count[j]-1
        return nums1[0:k]

if __name__ == "__main__":
    n = [0,1,2]
    k = 0
    print(n[0:k])