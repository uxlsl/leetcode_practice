import bisect

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        pos = 0
        i = 0
        while i < n:
            pos = bisect.bisect(nums1, nums2[i], pos, m)
            if pos == m:
                break
            nums1.insert(pos, nums2[i])
            m += 1
            i += 1
        nums1[m:] = nums2[i:n]
