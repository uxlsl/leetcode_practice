class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(2, len(height)):
            if height[i] < height[i - 1]:
                continue
            for j in range(i - 2, -1, -1):
                if height[j] <= height[i] and height[j] > height[j + 1]:
                    ret += i - j - 1
        return ret
