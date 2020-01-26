class Solution(object):
    def removeDuplicates(self, nums):
        """
        作者：LeetCode
        链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shan-chu-pai-xu-shu-zu-zhong-de-zhong-fu-xiang-by-/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0
        i = 0
        for j in range(1, len(nums)):
            if (nums[j] != nums[i]):
                i=i+1
                nums[i] = nums[j]
        return i + 1