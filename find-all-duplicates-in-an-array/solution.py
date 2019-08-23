class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        nums.sort()
        i,j = 0, 1
        while i < len(nums)-1:
            if nums[i] == nums[j]:
                ret.append(nums[i])
            i,j = j,j+1
        return ret
