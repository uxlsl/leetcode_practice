# leetcode
# 双指针


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


    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        l = 0
        r = len(height)
        while l < r:
            maxarea = max(
                    maxarea, Math.min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxarea
