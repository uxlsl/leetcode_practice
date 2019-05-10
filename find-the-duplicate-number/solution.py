class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 2**(len(nums)-1)
        for i in nums:
            if (1<<(i-1)) & m:
                return i
            else:
                m = m | (1<<(i-1))
