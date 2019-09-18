class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 使用所有的火柴拼成正方形
        # 可以求出边长
        import functools

        @functools.lru_cache(None)
        def f(i,h):
            a,b,c,d = h
            if i == -1:
                if a == b == c == d == 0:
                    return True
                else:
                    return False
            if a < 0 or b < 0 or c < 0 or d < 0:
                return False
            v = nums[i]
            return (
                    f(i-1, tuple(sorted([a-v, b, c, d])))
                    or f(i-1, tuple(sorted([a, b-v, c, d])))
                    or f(i-1, tuple(sorted([a, b, c-v, d])))
                    or f(i-1, tuple(sorted([a, b, c, d-v]))))

        total = sum(nums)
        if len(nums) == 0 or total % 4 != 0:
            return False
        avg = total / 4
        return f(len(nums)-1, (avg, avg, avg, avg))
