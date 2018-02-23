class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xs = nums[:3]
        for v in nums[3:]:
            for i,x in enumerate(xs):
                if x < v:
                    xs[i] = v
                    break
        return xs[0] * xs[1] * xs[2]


