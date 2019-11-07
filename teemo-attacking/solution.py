class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        out = -1
        for i in timeSeries:
            if out < i:
                total += duration
                out = i + duration
            elif out < i + duration:
                total += i + duration - out
                out = i + duration

        return total
