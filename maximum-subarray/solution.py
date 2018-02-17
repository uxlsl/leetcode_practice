class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        old = None
        record = {}

        for index, num in enumerate(nums):
            for i in range(index+1):
                if i not in record:
                    record[i] = 0
                record[i] += num
                if old is None:
                    old = record[i]
                elif record[i] > old:
                    old = record[i]
        return old

