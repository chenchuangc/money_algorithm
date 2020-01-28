from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while(left<=right):
            position = (left + right) // 2

            if nums[position]< target:
                left = position + 1
            else:
                right = position -1

        if nums[position]< target:
            return position + 1
        else:
            return position

if __name__ =="__main__":
    answer = Solution()
    print(answer.searchInsert([1,3,5,7],8))