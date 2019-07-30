# leetcode
# https://leetcode-cn.com/problems/combination-sum/
# 解法: 选择 or 重新选择

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def f(candidates, target, result, choice):
            if len(candidates) == 0:
                return
            a = candidates[-1]
            if a > target:
                del candidates[-1]
                f(candidates, target, result, choice)
                return
            choice.append(a)
            if target - a == 0:
                result.append(list(choice))
            else:
                f(list(candidates), target-a, result, choice)
            choice.pop()
            f(candidates[:-1], target, result, choice)

        result = []
        candidates = sorted(candidates)
        f(candidates, target, result, [])
        return result
