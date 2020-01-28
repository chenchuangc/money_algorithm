from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        result = set1.intersection(set2)
        return list(result)

    '''
    class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)

        作者：LeetCode
        链接：https://leetcode-cn.com/problems/intersection-of-two-arrays/solution/liang-ge-shu-zu-de-jiao-ji-by-leetcode/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''

if __name__ == "__main__":
    answer = Solution()
    print(answer.intersection([1,2,3],[2,2,4]))