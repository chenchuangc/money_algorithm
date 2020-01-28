'''
本题考查字典数据结构的使用
'''
from typing import List
class Solution(object):
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):   # x是元素，i是索引
            if x not in left: left[x] = i  # 第一次出现的位置
            right[x] = i    # 最后一次出现的位置，之前的会被最后一次的覆盖
            count[x] = count.get(x, 0) + 1   # 每个元素出现多少次

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/degree-of-an-array/solution/shu-zu-de-du-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ =="__main__":
    answer = Solution()
    answer.findShortestSubArray([1, 2, 2, 3, 1])