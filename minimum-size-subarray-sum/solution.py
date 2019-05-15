class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        length = None
        i = 0
        for j,v in enumerate(nums):
            total += v
            if total >= s:
                while i <= j and total - nums[i] >= s:
                    total -= nums[i]
                    i += 1
                if length is None:
                    length = j - i + 1
                else:
                    length = min(j-i+1, length)
        if length is None:
            return 0
        else:
            return length
