class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2 = sorted(nums2)
        m = {}

        for i in range(len(nums2)-1):
            m[nums2[i]] = nums2[i+1]

        ret = []

        for i in nums1:
            if i in m:
                ret.append(m[i])
            else:
                ret.append(-1)

        return ret
