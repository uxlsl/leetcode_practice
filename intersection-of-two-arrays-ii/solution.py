class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tmp = []
        nums2_1 = list(nums2)
        for i in nums1:
            try:
                nums2_1.remove(i)
                tmp.append(i)
            except ValueError:
                pass
        return tmp
