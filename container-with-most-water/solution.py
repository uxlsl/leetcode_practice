class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        for i1 in range(len(height)):
            for i2 in range(i1+1, len(height)):
                ret = max(min(height[i1], height[i2])*(i2-i1),
                        ret)
        return ret
