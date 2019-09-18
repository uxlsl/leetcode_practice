class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def f(nums):
            if not nums:
                return []
            mem = set()
            lst = []
            for i in f(nums[:-1]):
                if i[-1] <= nums[-1]:
                    lst.append(i + [nums[-1]])
                lst.append(i)

            for i in nums[:-1]:
                if i <= nums[-1]:
                    lst.append([i,nums[-1]])
            lst = set([tuple(i) for i in lst])
            return [list(i) for i in lst]

        return f(nums)
