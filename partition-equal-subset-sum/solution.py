class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        record = [False] * (total + 1)
        record[total] = True

        for i in nums:
            for j, v in enumerate(record):
                if v:
                    record[j-i] = True
                if record[total//2]:
                    return True
        return False

