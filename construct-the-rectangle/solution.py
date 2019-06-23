class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math

        idea = int(math.sqrt(area))

        for i in range(idea+1,0,-1):
            if area % i == 0:
                return [area//i, i] if i < area//i else [i, area//i]
