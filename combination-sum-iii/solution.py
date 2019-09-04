class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def f(nums, cur, choice, k, n):

            if cur >= len(nums) or k <= 0:
                return

            if n - nums[cur] == 0 and k==1:
                choice.append(nums[cur])
                result.append(list(choice))
                choice.pop()

            if n - nums[cur] >= 0:
                choice.append(nums[cur])
                f(nums, cur + 1, choice, k - 1, n - nums[cur])
                choice.pop()

            f(nums, cur + 1, choice, k, n)

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = []
        f(nums, 0, [], k, n)
        return result
