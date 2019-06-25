class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_s = sorted(nums)
        i = 0
        while i < len(nums) and nums_s[i] == nums[i]:
            i += 1

        j = len(nums) - 1
        while 0 <= j and nums_s[j] == nums[j]:
            j -= 1

        if i < j:
            return j - i + 1
        else:
            return 0
