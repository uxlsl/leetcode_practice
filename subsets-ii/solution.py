# leetcode
# https://leetcode-cn.com/problems/subsets-ii/


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def f(nums, cur, choice, result):
            if cur >= len(nums):
                return
            choice.append(nums[cur])
            result.append(list(choice))
            f(nums, cur+1, choice, result)
            choice.pop()

            while cur<len(nums)-1 and nums[cur] == nums[cur+1]:
                cur += 1

            f(nums, cur+1, choice, result)

        result = [[]]
        nums.sort()
        f(nums, 0, [], result)
        return result
