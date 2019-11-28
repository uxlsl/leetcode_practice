class Solution(object):
    def makesquare1(self, nums):
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

    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)

    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        return self.canPartitionKSubsets(nums, 4)
