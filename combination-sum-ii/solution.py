class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def f(candidates, cur, choice, target):
            if cur >= len(candidates):
                return

            if target - candidates[cur] > 0:
                choice.append(candidates[cur])
                f(candidates, cur+1, choice, target-candidates[cur])
                choice.pop()

            if target - candidates[cur] == 0:
                choice.append(candidates[cur])
                result.append(list(choice))
                choice.pop()

            # 跳过相同的值
            while cur<len(candidates)-1 and candidates[cur] == candidates[cur+1]:
                cur += 1
            f(candidates, cur+1, choice, target)

        result = []
        candidates.sort()
        f(candidates, 0, [], target)
        return result
