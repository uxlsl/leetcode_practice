ass Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xs = sorted(nums)
        # 也可使用heaq
        return max(xs[-1]*xs[-2]*xs[-3], xs[-1]*xs[0]*xs[1])
