class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        i=1
        if nums[0] != nums[1]:
            return nums[0]

        while i < len(nums) -1:
            if nums[i-1] != nums[i] != nums[i+1]:
                return nums[i]
            i += 1

        return nums[-1]
