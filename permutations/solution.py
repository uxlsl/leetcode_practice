class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def f(l, nums, results):
            if len(nums) > 0:
                for i in range(len(nums)):
                    v = nums.pop(i)
                    l.append(v)
                    f(l, nums, results)
                    nums.insert(i, v)
                    l.pop()
            else:
                results.append(list(l))

        results = []
        f([], nums, results)
        return results
