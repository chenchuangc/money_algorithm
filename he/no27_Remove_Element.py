'''
此题力扣官方答案给两种解法，我是第二种，但写法和官方不同，官方更简洁
'''
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        while(i<=j):
            while( j>=0 and nums[j] == val):
                j = j-1
            while(i<len(nums) and nums[i] != val ):
                i = i+1
            if i<j:
                nums[i],nums[j] = nums[j],nums[i]
        return j+1

if __name__ == "__main__":
    answer = Solution()
    print(answer.removeElement([2],3))