class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:n+m] = nums2
        def mergeSort(alist):
            # print("Splitting ", alist)
            if len(alist) > 1:
                mid = len(alist) // 2
                lefthalf = alist[:mid]
                righthalf = alist[mid:]
                mergeSort(lefthalf)
                mergeSort(righthalf)
                i = 0
                j = 0
                k = 0
                while i < len(lefthalf) and j < len(righthalf):
                    if lefthalf[i] < righthalf[j]:
                        alist[k] = lefthalf[i]
                        i = i + 1
                    else:
                        alist[k] = righthalf[j]
                        j = j + 1
                    k = k + 1

                while i < len(lefthalf):
                    alist[k] = lefthalf[i]
                    i = i + 1
                    k = k + 1

                while j < len(righthalf):
                    alist[k] = righthalf[j]
                    j = j + 1
                    k = k + 1

            # print("Merging ", alist)
            return alist

        return mergeSort(nums1)
