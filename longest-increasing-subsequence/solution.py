class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        max_length = 1
        for i in range(len(nums)):
            count = 1
            cur = nums[i]
            pre = None
            for j in range(i + 1, len(nums)):
                if cur < nums[j]:
                    count += 1
                    pre = cur
                    cur = nums[j]
                elif cur > nums[j]:
                    if pre is not None:
                        if pre < nums[j]:
                            cur = nums[j]

            max_length = max(max_length, count)

        return max_length

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        dp = {}
        dp[0] = 1
        ret = 1
        for i in range(1, len(nums)):
            val = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    val = max(val, dp[j])

            dp[i] = val + 1
            ret = max(dp[i], ret)

        return ret
