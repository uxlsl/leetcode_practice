class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        max_num = max(nums)
        try:
            return (set(i for i in range(max_num+1)) - set(nums)).pop()
        except KeyError:
            return max_num + 1
