class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if num[i] >= nums[j]:
                    continue
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False
