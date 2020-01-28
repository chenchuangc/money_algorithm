'''
分治法，本题可用动态规划和贪心
'''
from typing import List
class Solution:
    def cross_sum(self, nums, left, right, p):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]

        p = (left + right) // 2

        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)

        return max(left_sum, right_sum, cross_sum)

    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)


# 作者：LeetCode
# 链接：https: // leetcode - cn.com / problems / maximum - subarray / solution / zui - da - zi - xu - he - by - leetcode /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。